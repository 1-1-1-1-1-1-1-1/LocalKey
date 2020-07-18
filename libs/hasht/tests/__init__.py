import hashlib
import requests

# Tests
import os

_FOLDER = __file__.rsplit('\\', maxsplit = 1)[0] + '\\' # os.path.abspath('') + '\\'
_tlink = 'http://www.humansnotinvited.com/favicon.png'
# print(__import__('os').__dir__())

BASIC_FILENAME = "temporary_{}".format(__import__('os').getpid())


def save_file(link, filename = BASIC_FILENAME):
    with open(filename, 'wb') as f:
        f.write(requests.get(link).content)

    return filename

def deprecated(f):
    def wrapper(*args, **kwargs):
        raise DeprecationWarning

    return wrapper

# Is it needed?
def file_hash(filename, *, _n = 8192):
    "Current hashing algorithm: md5."
    with open(filename, 'rb') as f:
        m = hashlib.md5()
        while True:
            data = f.read(_n)
            if not data:
                break
            m.update(data)
        return m.hexdigest()

@deprecated
def get_hash_vprev(link, filename = BASIC_FILENAME):
    """Get an md5 hash from link."""
    filename = save_file(link, filename)
    return file_hash(filename)


def get_hash(link, *, hash_type = 'md5'):
    """Get a hash from link."""
    data = requests.get(link).content
    m = eval('hashlib.{}(data)'.format(hash_type))
    return m.hexdigest()


# Tests
if __name__ == '__main__':
    print(_FOLDER)
    print(get_hash(_tlink))



if not __name__ in ['__main__', '__init__']:
    # print(__name__)
