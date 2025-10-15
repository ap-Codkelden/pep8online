#-*- encoding: utf8 -*-

import pycodestyle
import re
import sys
import tempfile

from io import StringIO
from pathlib import Path

def parse_error_text(errdesc, saved=False):
    ERR_REGEX = re.compile(r"^(?P<errtype>[A-Z]+?)(?P<code>[0-9]+?)\s(?P<text>.+)$", re.I)
    ERR_CODE_RE = re.compile("^(?P<type>[A-Z]+?)(?P<code>[0-9]+?)$")
    if not saved:
        line, col, message = errdesc
        m = ERR_REGEX.match(message)
        if not m:
            raise ValueError("Too few arguments")
        else:
            errtype, code, text = m.group('errtype'), m.group('code'), m.group('text')
    else:
        err_code, line, col, text = errdesc
        m = ERR_CODE_RE.match(err_code)
        errtype, code = m.group('type'), m.group('code')
    return {'type': errtype, 'code': code, 'line': int(line), 'place': int(col), 'text': text}


def pep8parser(strings, saved=False):
    """
    Convert strings from pep8 results to list of dictionaries
    Parameter saved determines the source of the input:

        True : parse previously saved results
        False: parse newly checked code
    """
    result_list = []
    for s in strings:
        temp = list(x.strip() for x in s.rsplit(":", 3))
        print(temp)
        if not saved:
            temp = temp[-3:]
        result_list.append(parse_error_text(temp, saved=saved))
    return result_list


def check_text(text, logger=None):
    """
    Check text for PEP8/pycodestyle requirements
    """
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.py') as code_file:
        code_filename = code_file.name
        code_file.write(text)

    buffer = StringIO()
    saved_stdout = sys.stdout
    sys.stdout = buffer

    sg = pycodestyle.StyleGuide(quiet=False)
    checker = pycodestyle.Checker(code_filename, options=sg.options)
    checker.check_all()

    sys.stdout = saved_stdout
    result = buffer.getvalue()

    buffer.close()
    Path(code_filename).unlink(missing_ok=True)

    if logger:
        logger.debug(result)

    fullResultList = pep8parser(result.splitlines())
    fullResultList.sort(key=lambda x: (int(x['line']), int(x['place'])))

    return fullResultList


def is_py_extension(filename):
    filename = Path(filename)
    return filename.suffixes[-1] == '.py'

if __name__ == '__main__':
    pass
