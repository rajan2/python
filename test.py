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
