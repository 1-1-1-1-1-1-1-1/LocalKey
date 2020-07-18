__all__ = [
           # 'hashlib', 'requests', 'getpid',  # Internal.
           # 'BASIC_FILENAME',  # Quite local.
           'save_file', 'get_hash'
           ]


import hashlib
import requests

from os import getpid


BASIC_FILENAME = "temporary_{}".format(getpid())


def save_file(link, filename=BASIC_FILENAME):
    """Save file from link."""
    # Actually this module works both with this function
    # and without it... But some historical happenings
    # went so, that I decided to let this function be here.
    
    with open(filename, 'wb') as f:
        data = requests.get(link).content
        f.write(data)

    return filename


def get_hash(link, *, hashing_type='md5'):
    """Get a file's content hash from link."""
    data = requests.get(link).content
    h = eval('hashlib.{}()'.format(hashing_type))
    h.update(data)
    return h.hexdigest()


# Tests
if __name__ == '__main__':
    tlink = 'http://www.humansnotinvited.com/favicon.png'

    print(get_hash(tlink))
