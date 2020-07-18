# Local mark to this file
# =======================
# What is a quite important part here, this program should be better run
# in a single thread, with no 2 processes of ``single`` at one time.
# Otherwise, due to possible multiple performings of ``single`` at the
# same time, a correct value of `N` is not guaranteed.  So here is a
# group of action, with the implementation of which the condition of
# running <= 1 programs at once seems to be fulfilled.  To view possible
# exit codes, see source of that lib or the checker's __doc__.
#
# Other modules are not needed in this part, so I decided to put them
# after it.


from libs.track_processes import local_action as checker


INI = 'data/configs.ini'
SAVE_TO = 'data/pictures_savings'

TEST_MODE = None


code = checker(ini_filename=INI)
if code != 0:
    import sys
    input('Error! Exit code: {}.'.format(code))
    sys.exit(0)

del checker, code


import requests
from libs.read_html import Reader
from libs.hasht import save_file, get_hash

import json
from time import time, sleep

from names import URL, c, JSON, HASHING_TYPE


def get_info(text=None):
    # Return is a pair "(topic, links)", where ``links`` is a list
    # of the abs. links to the I-net-stored files of the following.

    if text is None:
        text = requests.get(URL).text
    
    body = Reader(text).reader('body')
    info = body[body.index('content'):]

    topic = Reader(text).reader('strong')[1:-1]
    
    def link(n):
        info1 = Reader(info).between('div', n)
        info2 = info1[info1.index('src'):]
        info3 = info2[info2.index('"') + 1 :]
        return info3[: info3.index('"')]

    return topic, [URL + link(i) for i in range(1, 10)]


def single(save_it=False):
    c.read(INI)
    N = c.getint('main', 'n')

    topic, links = get_info()

    # Making the list of all got hashes:
    hashes = []
    for link in links:
        hash_of_it = get_hash(link, hashing_type=HASHING_TYPE)
        if save_it:
            save_file(link, "{}/{}.png".format(SAVE_TO, hash_of_it))

        hashes.append(hash_of_it)

    # Forming the ``dict`` for an appended info:
    added_info = {'N': N, 'topic': topic, 'hashes': hashes}

    # Appending the received info to the already stored:
    with open(JSON, encoding='utf-8') as f:
        data = json.load(f)
    
    data.append(added_info)

    with open(JSON, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

    c.set('main', 'n', str(N + 1))
    with open(INI, 'w') as f:
        c.write(f)


def main(*args, **kwargs):
    t00 = time()
    mode = ""

    while True:
        try:
            if mode == "waiting":
                sleep(60)
                mode = ""

            t0 = time()
            single(*args, **kwargs)

            print(str(time() - t0).ljust(18), end='; ')
        except KeyboardInterrupt:
            input('\n'
                  + str(time() - t00)
                  + '\nStopped!')

            __import__("sys").exit(0)
        except Exception as e:
            print(e)
            mode = "waiting"  # Being of a `sleep` action here can cause
                              # a real `KeyboardInterrupt` in case of it.


if TEST_MODE == 1:
    print(*get_info(), sep='\n', end='\n\n')  #; 111/0

if TEST_MODE == 2:
    t0 = time()
    single(False); print(time() - t0)
    single(True); print(time() - t0)

if TEST_MODE:
    __import__("sys").exit(None)


if __name__ == '__main__':
    print(f"Action starts. Current time: \
{__import__('datetime').datetime.now()}\n")

    # Saving pictures could be easily enabled or disabled here.
    # Without savings the process is faster.
    main(save_it=False)  # Earlier this saving was enabled. Now, seems to be,
                         # all pictures are already collected.
