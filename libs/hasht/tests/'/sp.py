obj = __import__('requests').get('http://www.humansnotinvited.com/favicon.png').content

import configparser; c = configparser.ConfigParser(); c.read('configs.ini', encoding = 'utf-8')
name = __file__.rsplit('\\', maxsplit = 1)[1]
if c.get(name, 'Do').lower() == 'true':
	with open('example.no_Nextension2', 'wb') as f:
		f.write(obj)

	c.set(name, 'Do', 'False')
	with open('configs.ini', 'wt', encoding = 'utf-8') as g:
		c.write(g)

# Other
import hashlib

def file_hash(filename, *, _n = 8192):
    with open(filename, 'rb') as f:
        m = hashlib.md5()
        while True:
            data = f.read(_n)
            if not data:
                break
            m.update(data)
        return m.hexdigest()

print(file_hash('example.png'), file_hash('example2.png'), file_hash('example.no_Nextension'), file_hash('example.no_Nextension2'), sep = '\n')
# The test result: as I now understand, file's content do not depend on the filename
# (meaning the according extension also), even while writing data there just the first time.