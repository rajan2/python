#!/usr/bin/python

import sys

from functools import wraps

from fabric.api import env
from fabric.api import run
from fabric.api import settings

import logging
FORMAT = "%(levelname)-8s %(message)s"
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        with settings(warn_only=True):
            try:
                retval = f(*args, **kwds)
                print retval.failed
                if retval.failed:
                    return logger.error("%s command:%s" %(env.host_string, retval.command))
                else:
                    return logger.info("%s %s" %(env.host_string, retval))
            except Exception as e:
                logger.debug(e)
                sys.exit(1)
    return wrapper

run = my_decorator(run)
if __name__ == "__main__":
    with settings(host_string=sys.argv[1]):
        run(sys.argv[2])

