<a id="page_top"></a>

# Table of contents #

+ [Notes](#notes)
+ [Some ideas](#ideas)
    * [Viewing](#viewing)
        * [Return's examples](#returns)
    * [Detecting active processes](#detecting)

# Notes #

**Question**:
> "Is the process running?"

Possible stage of getting an answer to this question:
* Detecting this process (at least *having a criterion to say, whether the given process is a part of processes, searched for*).

Maybe on OS Linux the answer to it could be received using `os.kill(pid, 0)` (on Windows in seems just to kill the process, but in some Internet discussions I saw such a version for Linux).

# Some ideas #
<a id="ideas"></a>

## Ideas for viewing a list of active processes ##
<a id="viewing"></a>

> Return's examples: [examples for 1 and 2](#returns).

1. Via `psutil`.
```Python
import psutil


def func():
    # Each item of a such iterable is of type `psutil.Process`
    active_processes = psutil.process_iter()  # Maybe with extra args
    active_processes = list(active_processes)  # Optional

    return active_processes
```
<!-- Example of return: `func()[0]` -> `psutil.Process(pid=0, name='System Idle Process')` -->

2. Via `subprocess`.
```Python
import subprocess


def func():
    # This command works in Windows.
    obj = subprocess.Popen('tasklist /FO CSV /V /NH /FI "PID ge 100000"',
                           stdout=subprocess.PIPE)
    # P.S. Here args of `tasklist` are as an example.
    # (See ``tasklist --help'' for the help to it.)

    data = obj.communicate()[0]  # `data` is of type `bytes`
    result = data.decode("oem").replace("\r", "").split("\n")
    # Each item of `result` is a string

    # MAYBE more effective is to do so:
    result = [eval(line) for line in result if line]  # Each item is a tuple.

    # NOTE: Once I saw a mistake with doing `eval(line)` here. I don't know,
    # why did it happen.

    return result
```

3. Other.
```Python
import psutil

pid = ...
psutil.pid_exists(pid)  # Boolean
```

### Return's examples for `func()[0]`: ###
<a id="returns"></a>

1. `psutil.Process(pid=0, name='System Idle Process')`
2. `('dllhost.exe', '105520', 'Console', '1', '10\xa0556 КБ', 'Running', 'DESKTOP-EIFNPVD\\hp', '0:00:00', 'OleMainThreadWndName')`

## Ideas for detecting running processes ##
<a id="detecting"></a>

* Via `__file__ in ps.cmdline()` (or, more generally, `abs_filename` instead of `__file__`; package `psutil`, `ps` marks a process).
* Remembering the ID of last lauched process and then checking if it is running.

For some implementations the code of `__init__.py` could be viewed.


[Up to the page's top](#page_top)