import platform
from types import MethodType

IS_PY3 = (platform.python_version() >= '3')

if IS_PY3:
    iteritems = dict.items
    create_instance_method = MethodType
    basestring = str
    string_types = (basestring,)
    from functools import reduce
else:
    iteritems = dict.iteritems
    from __builtin__ import basestring
    string_types = (str,)
    from __builtin__ import reduce


def items_list(dictionary):
    return list(iteritems(dictionary))
