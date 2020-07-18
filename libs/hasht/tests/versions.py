from __init__ import _FOLDER, save_file, deprecated, BASIC_FILENAME
from __init__ import *
from __init__ import _tlink as url # Mind name.
import hashlib, requests

# To see the time better
from time import time

BASIC = 100
def timer(f, times = BASIC):
    def wrapper(*args, **kwargs):
        t0 = time()
        for i in range(times):
            f(*args, **kwargs)
        return time() - t0
    return wrapper

@timer
def get_hash_v0(link, filename = BASIC_FILENAME):
    """Get a hash (md5) from link."""
    filename = save_file(link, filename)
    return file_hash(filename)

@timer
def get_hash_v1(link, *, hash_type = 'md5'):
    data = requests.get(link).content
    m = eval('hashlib.{}(data)'.format(hash_type))
    return m.hexdigest()

@timer
def get_hash_v2(link):
    data = requests.get(link).content
    m = hashlib.md5()
    m.update(data)
    return m.hexdigest()

@timer
def get_hash_v3(link):
    data = requests.get(link).content
    m = hashlib.md5(data)
    return m.hexdigest()

__all__ = [i for i in globals() if i.startswith('get_hash')]

def do(link = url, *, function = get_hash, version = 1, **kwargs):
    f = eval(f'get_hash_v{version}')
    return f(link, **kwargs)
