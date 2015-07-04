"""
A table printer lifted from ActiveState and slightly modified
to be PEP8 compliant. It's ain't pretty, but it does work.

Source: http://code.activestate.com/recipes/267662/
"""
from __future__ import print_function

import re
import math
import operator
from functools import reduce
try:
    import cStringIO as io
except:
    import io


def indent(rows, hasHeader=False, headerChar='-', delim=' | ', justify='left',
           separateRows=False, prefix='', postfix='', wrapfunc=lambda x: x):
    """Indents a table by column.
       - rows: A sequence of sequences of items, one sequence per row.
       - hasHeader: True if the first row consists of the columns' names.
       - headerChar: Character to be used for the row separator line
         (if hasHeader==True or separateRows==True).
       - delim: The column delimiter.
       - justify: Determines how are data justified in their column.
         Valid values are 'left','right' and 'center'.
       - separateRows: True if rows are to be separated by a line
         of 'headerChar's.
       - prefix: A string prepended to each printed row.
       - postfix: A string appended to each printed row.
       - wrapfunc: A function f(text) for wrapping text; each element in
         the table is first wrapped by this function."""
    # closure for breaking logical rows to physical, using wrapfunc
    def rowWrapper(row):
        newRows = [wrapfunc(item).split('\n') for item in row]
        return [
            [substr or '' for substr in item]
            for item in list(map(lambda *a: a, *newRows))
        ]
    # break each logical row into one or more physical ones
    logicalRows = [rowWrapper(row) for row in rows]
    # columns of physical rows
    columns = list(map(lambda *a: a, *reduce(operator.add, logicalRows)))
    # get the maximum of each column by the string length of its items
    maxWidths = [
        max([len(str(item)) for item in column]) for column in columns
    ]
    rowSeparator = headerChar * (len(prefix) + len(postfix) + sum(maxWidths) +
                                 len(delim) * (len(maxWidths) - 1))
    # select the appropriate justify method
    justify = {
        'center': str.center,
        'right': str.rjust,
        'left': str.ljust
    }[justify.lower()]
    output = io.StringIO()
    if separateRows:
        print >> output, rowSeparator
    for physicalRows in logicalRows:
        for row in physicalRows:
            print(
                prefix +
                delim.join([
                    justify(str(item), width)
                    for (item, width) in zip(row, maxWidths)
                ]) + postfix, file=output
            )
        if separateRows or hasHeader:
            print(rowSeparator, file=output)
            hasHeader = False
    return output.getvalue()


def wrap_onspace(text, width):
    """
    A word-wrap function that preserves existing line breaks
    and most spaces in the text. Expects that existing line
    breaks are posix newlines (\n).

    By Mike Brown
    http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/148061
    """
    return reduce(
        lambda line, word, width=width: '%s%s%s' %
        (
            line,
            ' \n'
            [
                (
                    len(line[line.rfind('\n') + 1:]) +
                    len(word.split('\n', 1)[0]) >= width
                )
            ],
            word
        ),
        text.split(' ')
    )


def wrap_onspace_strict(text, width):
    """
    Similar to wrap_onspace, but enforces the width constraint:
    words longer than width are split.
    """
    wordRegex = re.compile(r'\S{' + str(width) + r',}')
    return wrap_onspace(
        wordRegex.sub(lambda m: wrap_always(m.group(), width), text),
        width
    )


def wrap_always(text, width):
    """
    A simple word-wrap function that wraps text on exactly width characters.

    It doesn't split the text in words.
    """
    return '\n'.join([
        text[width * i:width * (i + 1)]
        for i in range(
            int(math.ceil(1.0 * len(text) / width))
        )
    ])
