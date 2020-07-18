# This file states for getting the suggested answers for the exect 
# question of http://www.humansnotinvited.com/.

# As for me, the ``action`` requires Internet connection. Is getting
# the file's hash there possible without it?

# Should earlier versions be removed?
# Are all slashes essential here?


__all__ = ['table', 'action', 'main']


from file import get_info
import os
from libs.hasht import save_file, get_hash

from names import HASHING_TYPE, LOCAL_ANSWERS, STOP_WORD
from get_answers import folder


try:
    os.makedirs(LOCAL_ANSWERS)
except:
    None


def table_v0():  # It was earlier
    table0 = """\
—————————————
| 1 | 2 | 3 |
|———————————|
| 4 | 5 | 6 |
|———————————|
| 7 | 8 | 9 |
—————————————"""
    for i in table0.split('\n'):
        assert len(i) == len(table0.split('\n')[0])

    return table0


def table(a):
    """Create a local table.

    Usage example:
    >>> print(table(3).format(*list(range(9))))
    ╔═══╤═══╤═══╗
    ║ 0 │ 1 │ 2 ║
    ╟───┼───┼───╢
    ║ 3 │ 4 │ 5 ║
    ╟───┼───┼───╢
    ║ 6 │ 7 │ 8 ║
    ╚═══╧═══╧═══╝

    Note: a ``table(a, b)`` could be done in the same way; even for
    any input (i.e. with possibly length-different symbols in `format`).
    """
    def _align(line, n_times, *, by_symbol=" "):
        # If trying `"{:=...}".format(str(...))`
        # (with exect values intead of '...'): 
        # ``ValueError: '=' alignment not allowed in string format specifier``
        return by_symbol * ((n_times - 1) // 2) + line \
             + by_symbol * ((n_times) // 2)

    columns = 3  # Number of columns.
    line = "╟" + "┼".join([
                           "─"*a for i in range(columns)  
                           ]) + "╢"
    input_line = "║" + "│".join([
                                 _align("{}", a) for i in range(columns)
                                 ]) +"║"

    # These `return` difference is a readibility, not a result.

    """return f'╔{"═"*a}╤{"═"*a}╤{"═"*a}╗\n' \
+ (line + '\n').join(input_line + '\n' for i in range(3)) 
+ f'╚{"═"*a}╧{"═"*a}╧{"═"*a}╝'"""
    
    return f'╔{"═"*a}╤{"═"*a}╤{"═"*a}╗\n' \
+ input_line + '\n' \
+ line + '\n' \
+ input_line + '\n' \
+ line + '\n' \
+ input_line + '\n' \
+ f'╚{"═"*a}╧{"═"*a}╧{"═"*a}╝'


def table_of_answers(_answers):
    return table(3).format(*["•" if n in _answers else " " \
                                        for n in range(1, 10)])


def action(text):

    # Removing the previous results:
    for filename in os.listdir(LOCAL_ANSWERS):
        os.remove(LOCAL_ANSWERS + filename)

    topic, links = get_info(text); del text
    source = folder + topic + '\\'

    possible_answers = os.listdir(source)

    # Making a list of requested hashes (i.e. all questions):
    hashes = dict()
    for link in links:
        _hash_ = get_hash(link, hashing_type=HASHING_TYPE)
        hashes.update({_hash_: link})

    answers_h = tuple(filter(lambda hash_: hash_ + '.png' \
                               in list(map(lambda obj: obj.split('_')[-1], possible_answers)),
                           hashes.keys()))
    
    for h in answers_h:
        save_file(hashes[h], LOCAL_ANSWERS + h + '.png')
        """ # Or so:
        with open('data/pictures/' + i + '.png', 'rb') as f, \
             open(FOLDER + i + '.png', 'wb') as g:
            g.write(f.read())"""

        # Which is faster: doing ``requests.get(link).content``
        # or doing the ``g.write(f.read())`` (with open(...) ... )?

    L = [h for h in hashes if h in answers_h]
    keys = list(hashes.keys())
    answers = [keys.index(h) + 1 for h in L]

    with open(LOCAL_ANSWERS + "README.txt", 'w', encoding='utf-8') as f:
        # V0:
        # f.write('1. These are numbers of pictures, which are suggested to be answers: '
        #     + ', '.join(map(str, answers))
        #     + '.\n2. The table, according to which they are numarated:\n' + TABLE
        #     + '\n\n3. All pictures of those were placed to this folder.')  #?
        
        # V1:
        f.write('The table of suggested answers:\n'
                + table_of_answers(answers)
                + '\n\nAll those pictures (and only those) were placed to this folder.')

    return answers


def _get_text(*, with_stop=True):
    if with_stop:
        def lines():
            while True:
                i = input()
                if i != STOP_WORD:
                    yield i
                else:
                    break

        return '\n'.join(lines())

    else:
        # Alternatively, it could be done by adding a hotkey,
        # which interrupts the input.
        pass

    '''# Alternatively, it can be done like this:
    all_text = ''
    def one_line():
        i = input()
        if i != STOP_WORD:
            return i

    while True:
        line = one_line()

        if line is not None:
            all_text += '\n' + line
        else:
            break
    
    return all_text
    '''


def _main():

    # In case of adding an option "act without stop-word", to change:
    print(f'Enter the text here:\n(Print "{STOP_WORD}" to stop)\n')
    text = _get_text()

    print("\nTrying to get the result...", end="")
    answers = action(text)

    print("""
Here are suggested answers:
{}

This and some more were written to the folder "{}".""".format(
        table_of_answers(answers), LOCAL_ANSWERS))


def main():
    try:
        _main()
    except Exception as e:
        print(e)

    input()  # Is `finally` needed here?


if __name__ == '__main__':
    main()
