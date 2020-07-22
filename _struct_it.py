# QUESTION: (1)

import json
import os  # It's needed only with ``getpid`` and in 2 ``try-except``.
from os.path import abspath

from names import JSON, STRUCTIONS_STORAGE


BASIC_FILENAME = f"structed_{os.getpid()}.json"
IS_TEST = False


try:
    os.makedirs(STRUCTIONS_STORAGE)
except FileExistsError:
    None
except Exception as e:
    raise e


# NOTE: It's done to ensure that the file with name `BASIC_FILENAME`
# do not already exists.  Of course, it could be done by generating that
# name in a more clever way or by letting file's rewriting here.
try:
    assert not STRUCTIONS_STORAGE + BASIC_FILENAME in \
        os.listdir(STRUCTIONS_STORAGE)
except:
    input('Woops: a rare error occurred! Try to reload the program.')
    os.kill(os.getpid(), 0)


del os


def struct_v1(to_file=BASIC_FILENAME, percentage=(0, 1)):
    with open(JSON, encoding='utf-8') as f:
        data = json.load(f)

    d = {}
    for i in data:
        topic = i['topic']

        hashes = i['hashes']
        topic_counts = len(tuple(
                                 filter(lambda dict_: \
                                            dict_['topic'] == topic,
                                        data)
                           ))

        # Forming the dictionary of hashes [for this topic] (``d0``):
        try:
            d0 = d[topic]['hashes']
        except:
            d0 = {}

        for h in hashes:
            try:
                counts = d[topic]['hashes'][h]  #? (1) Could it be replaced
                                                #      with a ``d0[h]``?
                d0[h] = counts + 1
            except:
                d0[h] = 1

        d.update({topic: {'counts': topic_counts, 'hashes': d0}})

    total_requests = len(data)  # Does it helps to work [a bit] faster?

    # Now ``data`` is already used.
    del data

    try:
        _min, _max = percentage
    except:
        _min, _max = percentage, 1

    # Filtering the got results according to the requested percentage:
    for topic in d:
        hashesd = d[topic]['hashes']
        topic_counts = d[topic]['counts']

        hashesd = {key: hashesd[key] for key in hashesd
                       if _min <= hashesd[key] / topic_counts <= _max}

        d.update({topic: {'counts': topic_counts, 'hashes': hashesd}})

    # Dumping the resulting data:
    with open(STRUCTIONS_STORAGE + to_file, 'w', encoding='utf-8') as f:
        json.dump({
                   'total_requests': total_requests,
                   'percentage': f'from {_min} to {_max}',
                   'data': d
                   },
                  f, indent=4)


def struct_v2(to_file=BASIC_FILENAME, percentage=(0, 1)):
    with open(JSON, encoding='utf-8') as f:
        data = json.load(f)

    total_requests = len(data)

    def unite(*dicts) -> dict:  ## ``dicts`` should be of a positive length.
        """Special uniting of ``dict`` objects. Example:
        ``unite({'a': 1, 'b': 2}, {'a': 100})'' ->
                       -> ``{'a': 101, 'b': 2}''. (101 = 100 + 1)
        """
        if len(dicts) == 1:
            return dicts[0]

        keys = []
        for d in dicts:
            for key in d:
                if key not in keys:
                    keys.append(key)

        def value(key):
            return sum(d[key] for d in dicts if key in d.keys())

        return {key: value(key) for key in keys}

    topics = []
    for d in data:
        topic = d['topic']
        if topic not in topics:
            topics.append(topic)

    d = {}
    for topic in topics:
        dicts = tuple(filter(lambda dd: dd['topic'] == topic, data))
        d.update({topic: {
                          'counts': len(dicts),
                          'hashes': unite(*[{h: 1 for h in list_} for list_ in \
                                                map(lambda dd: dd['hashes'], dicts)
                                            ]
                                          )
                          }})

    # Now ``data`` is already used.
    del data

    try:
        _min, _max = percentage
    except:
        _min, _max = percentage, 1

    # Filtering the got results according to the requested percentage:
    for topic in d:
        hashesd = d[topic]['hashes']
        topic_counts = d[topic]['counts']

        hashesd = {key: hashesd[key] for key in hashesd \
                       if _min <= hashesd[key] / topic_counts <= _max}

        d.update({topic: {'counts': topic_counts, 'hashes': hashesd}})

    # Dumping the resulting data:
    with open(STRUCTIONS_STORAGE + to_file, 'w', encoding='utf-8') as f:
        json.dump({
                   'total_requests': total_requests,
                   'percentage': f'from {_min} to {_max}',
                   'data': d
                   },
                  f, indent=4)


if IS_TEST:
    from time import time as t

    def main(func):
        exec("{0}('TESTFILE-{0}.tmp.json', 0.1)".format(func), globals())

    def measure_time(func):
        t0 = t()
        main(func)
        print(t() - t0)

    measure_time('struct_v1')
    measure_time('struct_v2')

    __import__("sys").exit("End of test.")


# According to the tests' results, which I saw, the ``struct_v2`` function
# seems to be much faster (nearly twice) than ``struct_v1``.
struct = struct_v2


def main():
    if input('Struct it? ("yes" or "no") ').lower() == 'yes':
        maybename = input(f'\nTo which file? (An empty input means structing to the file {BASIC_FILENAME!r}.) ')
        percentage = input('Percentage (empty input means from 0 to 1, N means from N to 1): ')
        print('Trying to perform it...')

        try:
            d = {}
            if maybename:
                d['to_file'] = maybename
            if percentage:
                # ``percentage`` can be a not counted number, for example a
                # ``1 / __import__("math").pi``.  (*)
                d['percentage'] = eval(percentage)

            del maybename, percentage

            struct(**d)
            input('Done!')
        except Exception as e:
            input(f'Error! Some details:\n{e}')


if __name__ == '__main__':
    main()
