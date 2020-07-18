Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=== RESTART: C:\Users\hp\Desktop\Python\Captcha Tests\libs\hasht\versions.py ===
>>> do(function = get_hash)
9.675019264221191
>>> do(function = get_hash_vprev)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    do(function = get_hash_vprev)
  File "C:\Users\hp\Desktop\Python\Captcha Tests\libs\hasht\versions.py", line 37, in do
    return function(link, **kwargs)
  File "C:\Users\hp\Desktop\Python\Captcha Tests\libs\hasht\versions.py", line 13, in wrapper
    f(*args, **kwargs)
  File "C:\Users\hp\Desktop\Python\Captcha Tests\libs\hasht\versions.py", line 21, in get_hash_vprev
    return file_hash(filename)
NameError: name 'file_hash' is not defined
>>> 
=== RESTART: C:\Users\hp\Desktop\Python\Captcha Tests\libs\hasht\versions.py ===
>>> do(function = get_hash_vprev)
10.549477100372314
>>> do(function = get_hash_vprev)
9.925863027572632
>>> do(function = get_hash_vprev)
10.432549953460693
>>> do(function = get_hash)
12.227441310882568
>>> do(function = get_hash)
10.54847764968872
>>> do(function = get_hash)
9.567085266113281
>>> do(function = get_hash_v2)
10.161717653274536
>>> do(function = get_hash_v2)
9.652032375335693
>>> 
=== RESTART: C:\Users\hp\Desktop\Python\Captcha Tests\libs\hasht\versions.py ===
>>> do(function = get_hash_vprev); do(function = get_hash); do(function = get_hash_v2)
18.33766269683838
18.41261601448059
24.319963932037354
>>> do(function = get_hash_v2); do(function = get_hash_vprev); do(function = get_hash)
28.97708511352539
24.84963631629944
25.557199478149414
>>> 
=== RESTART: C:\Users\hp\Desktop\Python\Captcha Tests\libs\hasht\versions.py ===
>>> do(function = get_hash_v2); do(function = get_hash_vprev); do(function = get_hash)
24.40491032600403
20.036611557006836
20.374388456344604
>>> do(function = get_hash_v0)
31.59646463394165
>>> do(function = get_hash_v2); do(function = get_hash_vprev); do(function = get_hash)
19.95566153526306
18.52153491973877
18.632480144500732
>>> for i in hash
SyntaxError: invalid syntax
>>> 
=== RESTART: C:\Users\hp\Desktop\Python\Captcha Tests\libs\hasht\versions.py ===
>>> for i in hashlib.algorithms_available:
	do(function = get_hash, hash_type = i)

	
12.580220222473145

>>> for i in hashlib.algorithms_available:
	print(f'With {i}:', do(function = get_hash, hash_type = i))

	
With sha384: 10.067775964736938
With sha224: 12.106503009796143
Traceback (most recent call last):
  File "<pyshell#22>", line 2, in <module>
    print(f'With {i}:', do(function = get_hash, hash_type = i))
  File "C:\Users\hp\Desktop\Python\Captcha Tests\libs\hasht\versions.py", line 45, in do
    return function(link, **kwargs)
  File "C:\Users\hp\Desktop\Python\Captcha Tests\libs\hasht\versions.py", line 14, in wrapper
    f(*args, **kwargs)
  File "C:\Users\hp\Desktop\Python\Captcha Tests\libs\hasht\versions.py", line 28, in get_hash
    return m.hexdigest()
TypeError: hexdigest() takes exactly one argument (0 given)
>>> data = requests.get(link).content
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    data = requests.get(link).content
NameError: name 'link' is not defined
>>> #
>>> data = requests.get(url).content
>>> print(hashlib.algorithms_available)
{'sha384', 'sha224', 'shake_256', 'sha512', 'ripemd160', 'whirlpool', 'sm3', 'md5-sha1', 'sha3_256', 'blake2b', 'blake2s', 'mdc2', 'sha256', 'sha3_512', 'shake_128', 'sha512_224', 'md4', 'sha512_256', 'md5', 'sha1', 'sha3_224', 'sha3_384'}
>>> obj = hashlib.shake_256()
>>> obj
<_sha3.shake_256 object at 0x000002A48A63D330>
>>> obj.hexdigest()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    obj.hexdigest()
TypeError: hexdigest() takes exactly one argument (0 given)
>>> o = hashlib.sha256()
>>> o.hexdigest()
'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
>>> hashlib.algorithms_guaranteed
{'sha384', 'md5', 'sha1', 'sha3_224', 'sha224', 'shake_256', 'sha256', 'sha512', 'sha3_256', 'sha3_384', 'sha3_512', 'blake2b', 'blake2s', 'shake_128'}
>>> hashlib.algorithms_guaranteed.__doc__
'set() -> new empty set object\nset(iterable) -> new set object\n\nBuild an unordered collection of unique elements.'
>>> for i in hashlib.algorithms_guaranteed:
	print(f'With {i}:', do(function = get_hash, hash_type = i))

	
With sha384: 9.518114566802979

>>> for i in hashlib.algorithms_guaranteed:
	print(f'With {i}:', do(function = get_hash, hash_type = i))

	


>>> for i in hashlib.algorithms_guaranteed:
	try:print(f'With {i}:', do(function = get_hash, hash_type = i))
	except Exception as e: print(e)

	
With sha384: 9.35021162033081
With md5: 9.415173292160034
With sha1: 11.94660210609436
With sha3_224: 10.595442295074463
With sha224: 9.699991703033447
hexdigest() takes exactly one argument (0 given)
With sha256: 9.803933143615723
With sha512: 9.762959480285645
With sha3_256: 9.35920763015747
With sha3_384: 10.347596168518066
With sha3_512: 14.789851665496826
With blake2b: 8.877501964569092
With blake2s: 9.544099569320679
hexdigest() takes exactly one argument (0 given)
>>> obj = hashlib.shake_128(data)
>>> obj.hexdigest(10)
'6d64a0474f04af26d755'
>>> obj.hexdigest(100)
'6d64a0474f04af26d755da2ba90037da3689dcd2e813102ba49cf802a9456dff4a6db752805b94df9e4689f52acef6ed13396bcf076390dc12f06fa69f8426559e702722437f07645d75f0ce4647d2d2d7caaac811c68471045f640ccbee8a9036db1d51'
>>> obj.hexdigest(1000)
'6d64a0474f04af26d755da2ba90037da3689dcd2e813102ba49cf802a9456dff4a6db752805b94df9e4689f52acef6ed13396bcf076390dc12f06fa69f8426559e702722437f07645d75f0ce4647d2d2d7caaac811c68471045f640ccbee8a9036db1d51d30f1c86b30d1bacb1ff2a95e6be92097c8f3bbb4b08ba2085ec0a0df621e9906eae68f6a978ce9b5fd91d90d9860189a95c2f3cc07964497de762f3a8842c249a3af5e0006cb8eacb40c47598df6237a1b537d0efd07881601ff3b71e02efcafac0f2a4692b3c43795685c33ffa95cfdf8ee16f4383ff518a7e1cdf6c389dc91f51057578e6cc00a509d56be1e4eacf32460b81efde83e4b6d2ec125b00548eda5b88a06b78e5a9dcfd2c0ee589cf943d3b5619c29db1b3e94c642df9896a378b3869f810ca9077baccdee1541f56ae30ea86d74b70b6c4e645c0adaa6350794dc1a1fd72d348f0e2cdbcb2392809f1407c83826dfda2f6fecdd2cdfb1a97d319581a73fba7fb5e5235095af1ad617d9473428689d643eac70e1ff59b4b334bef43b2de486a4f9dca9eb6cf5caac441edda2fe9987d2e8e245f2effec43c9419260aea8220058471f7823d14b8978366f8ce27338bdfc4584982daddac5693ab32c9af288c32b00a8be064fba03ac7e6dc18f7517ed6e8593cc8ff0bb7bd99668e203e4c1179ed80986a0186603f2599a9413c96022a513e44159f80f9e0ad5a82a696da5a63e123bc96f681a6967c326e74d20efa42d9a9d762d306178f55a653b36d7f873c89e0edf8b5968ca35fa3c8c453574c70155bb6eb6be5f47f1307684e59a9265450749911cbec17acdd1338f490cd802ef6872a8c678725aa28d15aadcb18b809ba963c5ae8606ca49e5290b7c6dc745713ad458b7032b893a6a50f86a51fea61867dc29c69707ab690614138c9bd36f446dc99a4fab8a57a09c2d6ea5c220d01ce9903e54cb02fa847ec3d53e7af0afb3dbb2cdd657fda5934af43cd18323995370cdc5f89b87dd85ce602636860693206a0c2efe2ed7e726657686f2f65c0bbb685e28d1ad521d32537784a10578dacd032e597f6ccd29a5559f18bd30e7521eabdd5d9f9c73df2b5c2804d012f0b764d336a6c067924228a19bbd871470897c11d371d44b00a6cd0d2164022957e1fe1415a816734b9dbc89ce506a0cc805b4a87f8d4cbc2724d531e9e6a4a5ea378a11e8fc7fc5eea479c7e04ffd504c59ecabc70b0ad2fd0ec9bdfa1f0f755b7bbb412145c2e956f449430d6811f12be3c84120e86b965814bd337937358a1309357cf7abbcdcbb5b3d948c3242c7699366b9248b0cb0b10fbc2d12d11a2c482ca26adb86573a3f0f6c36a1e371c64b4f2734c29b5de50814f772a7c89a65396129b5e925597c9b76ce03bde58250'
>>> hashlib.shake_128().hexdigest(100)
'7f9c2ba4e88f827d616045507605853ed73b8093f6efbc88eb1a6eacfa66ef263cb1eea988004b93103cfb0aeefd2a686e01fa4a58e8a3639ca8a1e3f9ae57e235b8cc873c23dc62b8d260169afa2f75ab916a58d974918835d25e6a435085b2badfd6df'
>>> 
=============================================== RESTART: C:\Users\hp\Desktop\Python\Captcha Tests\libs\hasht\versions.py ==============================================
>>> print(__all__)
<generator object __all_ at 0x0000016B337EF270>
>>> print(list(__all__))
[]
>>> 
=============================================== RESTART: C:\Users\hp\Desktop\Python\Captcha Tests\libs\hasht\versions.py ==============================================
>>> print(list(__all__))
['get_hash_vprev', 'get_hash', 'get_hash_v0', 'get_hash_v1', 'get_hash_v2', 'get_hash_v3']
>>> print(list(__all__))
[]
>>> 
=============================================== RESTART: C:\Users\hp\Desktop\Python\Captcha Tests\libs\hasht\versions.py ==============================================
>>> list(__all__)
['get_hash_vprev', 'get_hash', 'get_hash_v0', 'get_hash_v1', 'get_hash_v2', 'get_hash_v3']
>>> list(__all__)
[]
>>> 
=============================================== RESTART: C:\Users\hp\Desktop\Python\Captcha Tests\libs\hasht\versions.py ==============================================
>>> __all__ = list(__all__)
>>> list(__all__)
['get_hash_vprev', 'get_hash', 'get_hash_v0', 'get_hash_v1', 'get_hash_v2', 'get_hash_v3']
>>> ['get_hash_vprev', 'get_hash', 'get_hash_v0', 'get_hash_v1', 'get_hash_v2', 'get_hash_v3']
['get_hash_vprev', 'get_hash', 'get_hash_v0', 'get_hash_v1', 'get_hash_v2', 'get_hash_v3']
>>> list(__all__)
['get_hash_vprev', 'get_hash', 'get_hash_v0', 'get_hash_v1', 'get_hash_v2', 'get_hash_v3']
>>> 
=============================================== RESTART: C:\Users\hp\Desktop\Python\Captcha Tests\libs\hasht\versions.py ==============================================
>>> 
=============================================== RESTART: C:\Users\hp\Desktop\Python\Captcha Tests\libs\hasht\versions.py ==============================================
>>> __all__
['get_hash_vprev', 'get_hash', 'get_hash_v0', 'get_hash_v1', 'get_hash_v2', 'get_hash_v3']
>>> __all__
['get_hash_vprev', 'get_hash', 'get_hash_v0', 'get_hash_v1', 'get_hash_v2', 'get_hash_v3']
>>> 
=============================================== RESTART: C:\Users\hp\Desktop\Python\Captcha Tests\libs\hasht\versions.py ==============================================
>>> 
=============================================== RESTART: C:\Users\hp\Desktop\Python\Captcha Tests\libs\hasht\versions.py ==============================================
>>> for i in [0, 1, 2, 3]: do(version = i)

Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    for i in [0, 1, 2, 3]: do(version = i)
  File "C:\Users\hp\Desktop\Python\Captcha Tests\libs\hasht\versions.py", line 52, in do
    return eval(function(link, **kwargs))
  File "<string>", line 1
    389975d8d57ca94e672162998e06c017
          ^
SyntaxError: unexpected EOF while parsing
>>> 
=============================================== RESTART: C:\Users\hp\Desktop\Python\Captcha Tests\libs\hasht\versions.py ==============================================
>>> 
=============================================== RESTART: C:\Users\hp\Desktop\Python\Captcha Tests\libs\hasht\versions.py ==============================================
>>> for i in [0, 1, 2, 3]: do(version = i)

17.749011278152466
9.212304592132568
9.336227178573608
9.57508134841919
>>> 
=============================================== RESTART: C:\Users\hp\Desktop\Python\Captcha Tests\libs\hasht\versions.py ==============================================
>>> for i in [0, 1, 2, 3]: do(version = i)

11.947594165802002
9.609058618545532
9.6440269947052
11.80168628692627
>>> for i in [0, 1, 2, 3]: do(version = i)

9.808924436569214
9.76196551322937
9.278263330459595
10.208688020706177
>>> for i in [0, 1, 2, 3]: do(version = i)

9.985817909240723
12.60519528388977
9.60805606842041
10.141730070114136
>>> for i in [0, 1, 2, 3]: do(version = i)

15.26155710220337
10.238665103912354
12.386330604553223
10.22467851638794
>>> for i in [0, 1, 2, 3]: do(version = i)

9.918855667114258
54.518293142318726
72.64408230781555
18.88032627105713
>>> for i in [0, 1, 2, 3]: do(version = i)

10.083765029907227
9.224296569824219
10.353594064712524
9.864898681640625
>>> for i in [0, 1, 2, 3]: do(version = i)

13.612582445144653
9.020411968231201
9.480136156082153
10.589449644088745
>>> for i in [0, 1, 2, 3]: do(version = i)

10.350600242614746
8.950466394424438
8.982447147369385
17.478188037872314
>>> for i in [0, 1, 2, 3]: do(version = i)

12.160476684570312
13.699530363082886
18.9882595539093
10.352585077285767
>>> for i in [0, 1, 2, 3]: do(version = i)

10.842281818389893
10.024792671203613
9.641039609909058
11.30700945854187
>>> for i in [0, 1, 2, 3]: do(version = i)

8.961458683013916
8.91448426246643
9.499121904373169
9.74497103691101
>>> for i in [0, 1, 2, 3]: do(version = i)

10.776334285736084
10.086764335632324
20.791145086288452
11.401945114135742
>>> for i in [0, 1, 2, 3]: do(version = i)

10.549470663070679
9.251268148422241
9.63904070854187
9.527105808258057
>>> for i in [0, 1, 2, 3]: do(version = i)

11.025182962417603
10.003813743591309
14.564994812011719
13.840439081192017
>>> for i in [0, 1, 2, 3]: do(version = i)

10.376580715179443
9.07738184928894
12.725126504898071
10.735363006591797
>>> for i in [0, 1, 2, 3]: do(version = i)

12.029556512832642
9.047405481338501
9.622048139572144
10.041789531707764
>>> for i in [0, 1, 2, 3]: do(version = i)

10.134735107421875
9.107369422912598
12.401326656341553
9.116366863250732
>>> 
