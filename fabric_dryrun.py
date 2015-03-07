
dryrun = 1
def my_decorator(f):
    """
    wrapper for run command 
    """
    @wraps(f)
    def wrapper(*args, **kwds):
        with settings(warn_only=True):
            try:
                if dryrun:
                    print "DRY RUN: [%s]\t%s(%s)" % (env.host_string, f.__name__,','.join(list(args) + ["%s=%s" % (k, v) for (k, v) in kwds.iteritems()]))
                else:
                    retval = f(*args, **kwds)
                    if retval.failed:
                        return("%s Command Failed [%s] " % (env.host_string, retval.command))
            except Exception as e:
                print e
    return wrapper

run = my_decorator(run)

def Foo():
    """
    with dryrun
    """
    with settings(host_string=myhost):
        run("hostname")

def Bar():
    """
    without dryrun
    """
    with settings(host_string=myhost):
        run("hostname")
