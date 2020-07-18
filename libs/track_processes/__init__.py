# An action, with the implementation of which the condition of running <= 1
# programs at once seems to be fulfilled. This action's performing requires an
# additional library `psutil`. See IDEAS.md for some more info.


__all__ = ['local_action']


# As I saw, using ``..._v1(version=2)`` here is not effective.
# Also, as I understand, ``..._v1(version=1)`` could be useful here,
# but I wasn't sure in it.
def local_action_v1(version=1):  # Form of it - ?
    # WARNING: This function is implemented badly and states here only
    # as a source for possible idea.
    import psutil
    
    print("Asserting in local thing...")
    try:
        pss = []
        for ps in psutil.process_iter():
            try:
                if not __file__ in ps.cmdline():
                    continue
            except psutil.AccessDenied:
                continue
            pss.append(ps)

        print(*pss, sep='\n')  # Test

        if version == 1:
            print("Performing `version 1`.")  #t
            nodes = set(pss)
            assert any(
                       len(
                           nodes - set(node.children(recursive=True))
                           ) == 1
                           for node in pss  # Or `node in nodes`
                       )

        elif version == 2:
            print("Performing `version 2`.")  #t
            n = len(pss) - 1
            print({ps: ps.children(recursive=True) for ps in pss})
            assert any(len(ps.children(recursive=True)) == n for ps in pss)

        print('The `try` statement was successfully completed.')  #t
        exit_code = 0
    except AssertionError:
        print("Error: 2 programs were found running at one time.")
        exit_code = 1
    except Exception as e:  #?
        print("""\
An another exception occured:
Type: {}
Exception: {}""".format(type(e), e))
        exit_code = 10

    return exit_code


# NOTE: if 2 processes are launched in one time, could it help?
# However this function is quite fast.
def local_action_v2(ini_filename):
    import psutil
    from os import getpid
    import configparser

    c = configparser.ConfigParser()
    c.read(ini_filename)

    def get_code():
    	if 'last_running_pid' not in c.options('main'):
    		return 0
    	else:
    	    last_pid = c.getint('main', 'last_running_pid')

    	    try:
    	        assert not psutil.pid_exists(last_pid)
    	        exit_code = 0
    	    except AssertionError:
    	    	exit_code = 1

    	    return exit_code
    
    exit_code = get_code()

    if exit_code != 0:
    	return exit_code

    pid = getpid()
    c.set('main', 'last_running_pid', str(pid))

    with open(ini_filename, 'w') as f:
        c.write(f)

    return exit_code


def local_action(*args, **kwargs):
	"""Assert that last launched process is not running.

	Return
	------
	Positive answer -> 0.
	Negative (assertion error) -> 1.
	Another error -> 10.
	"""
	code = local_action_v2(*args, **kwargs)

	return code