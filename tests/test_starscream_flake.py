# flake8: noqa

from starscream_flake8 import check_no_json_import, detect_u_literal, detect_range_instead_of_xrange

def test_check_no_json_import():
    physical_line = 'import json'
    assert check_no_json_import(physical_line.strip(), physical_line, 1, 'test_starscream_flake.py') == (0, 'SC01 import json found, use import simplejson instead.')

    physical_line = 'import jsonschema'
    assert check_no_json_import(physical_line.strip(), physical_line, 1, 'test_starscream_flake.py') == None

    physical_line = 'from json import dumps'
    assert check_no_json_import(physical_line.strip(), physical_line, 1, 'test_starscream_flake.py') == (0, 'SC01 import json found, use import simplejson instead.')


def test_detect_u_literal():
    physical_line = "u'str'"
    assert detect_u_literal(physical_line.strip(), physical_line, 1, 'test_starscream_flake.py') == (0, "SC02 found u'str', please use __future__ import unicode_literals instead.")

    physical_line = 'u"str"'
    assert detect_u_literal(physical_line.strip(), physical_line, 1, 'test_starscream_flake.py') == (0, "SC02 found u'str', please use __future__ import unicode_literals instead.")


def test_detect_u_literaldetect_u_literal():
    physical_line = 'for x in range(5)'
    assert detect_range_instead_of_xrange(physical_line.strip(), physical_line, 1, 'test_starscream_flake.py') == (8, 'SC03 found range method, use xrange instead as xrange is an iterator.')

