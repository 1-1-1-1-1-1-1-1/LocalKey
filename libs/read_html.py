"""See the __doc__ of this module's functions, see code for more info."""


# 1. Should the ``DEFAULT`` for text be here? It's stated in some
# parts of this file, but I see no real sense in it.

# 2. Does this text derives PEP 8?


__all__ = ['spec', '_in_tag', 'in_tag', 'Reader']


DEFAULT = ""


def spec(t : str) -> str:  # Should it be?
    """A special text beautifying.

    Returns ``t.lstrip('>').rstrip('<').strip()''. Example:
    ``spec(">italic<")'' -> "italic".
    Such a situation could happen at using this module's functions.
    ``Reader(<i>Text in tags 'i'</i>).between("i")'' gives a ``>...<'',
    while a ``spec'' of it is just a text, marked with that dots.
    """
    return t.lstrip('>').rstrip('<').strip()


def _in_tag(str0, text=DEFAULT, *, optional='/'):
    """Pre-function for the function ``in_tag``."""
    if type(str0) is tuple:
        opened, closed = str0
    else:
        opened = f'<{str0}'
        closed = f'{optional}{str0}>'
    
    _start_ = text.index(opened) + len(opened)
    
    i = text.index(closed)
    text_ = text[:i]
    counts = text_.count(opened)
    
    def f(x, time=1, sep=closed):
        assert type(time) is int and time > 0
        if time == 1:
            return x.index(sep)
        
        return f(x[len(sep):], time=time - 1, sep=sep)
    
    _end_ = f(text[i:], time=counts) + len(text_)
    
    return _start_, text[_start_ : _end_], len(closed)

def in_tag(str0, n=1, text=DEFAULT, *, optional='/'):
    """This function is used in the class `Reader`.
Returns a text "between" (not really) tags.
See the code of ``_in_tag`` for more info.
"""
    assert type(n) is int and n > 0
    
    if n == 1:
        pre_res = _in_tag(str0, text=text, optional=optional)[1]
        return pre_res.strip()  # Mind it.
    else:
        pre_res = _in_tag(str0, text=text, optional=optional)
        startpoint = pre_res[0] + len(pre_res[1]) + pre_res[2]
        res = in_tag(str0, n=n - 1, text=text[startpoint:], optional=optional)
        return res


class Reader:
    """In my theory, it should be an utility for working with HTML text.

    All: between, text, reader.
    """

    __all__ = ['between', 'reader']

    def __init__(self, text):
        self.text = text

    def between(self, tag, n=1, optional='/'):
        """See the `in_tag` structure for more info."""
        return in_tag(tag, n=n, text=self.text, optional=optional)

    def reader(self, *from_list):
        """To my thoughts, it's a reader of HTML text.

Notes:
1. Here the ``spec`` function could be useful, but I am not sure
if it should be here.
2. A ``Reader(text).reader()'' (with no arg-s) returns ``text''.

    Usage example:
    >>> text = "Some text: <i>1-st italic</i>, <strong><i>2-nd italic</i>, <i>3</i></strong>."
    >>> obj = Reader(text)
    >>> print(obj.between('i'))  # Here `'i'` means `'i', 1` (same for other tags)
    >1-st italic<
    >>> print(obj.reader(('i', 2)))
    >2-nd italic<
    >>> print(obj.reader('strong', ['i', 2]))
    >3<
    >>> print(spec(obj.between('strong')))
    <i>2-nd italic</i>, <i>3</i>
"""
        if len(from_list) == 0:
            return self.text
        else:
            e = from_list[0]
            if type(e) is str:
                e = e, 1
            text_ = Reader(self.text).between(*e)
            return Reader(text_).reader(*from_list[1:])


########################################################################################
### Tests ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IS_TEST = False
if __name__ == '__main__' and IS_TEST:
    # Earlier:  # Big letters — to make this variables visible...
    TEXT = 'Example of <i> part 1</i> here was a wspace<i> \
<b>&lt;Some text in the bold tags (b)&gt</b>the second time     </i>Sooooo...'

    print(Reader(TEXT).reader('i', 2))

    Test = Reader(DEFAULT)
    print(Test, Test.reader.__doc__, sep='\n')

    # Later:
    text = 'Some text: <i>1-st italic</i>, <strong><i>2-nd italic</i>,\
<i>3</i></strong>.'
    obj = Reader(text)
    print(spec(obj.between('strong')))
    print(obj.reader(['i', 2]))

    __import__("sys").exit(print(spec.__doc__))
