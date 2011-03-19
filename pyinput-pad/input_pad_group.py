# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_input_pad_group', [dirname(__file__)])
        except ImportError:
            import _input_pad_group
            return _input_pad_group
        if fp is not None:
            try:
                _mod = imp.load_module('_input_pad_group', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _input_pad_group = swig_import_helper()
    del swig_import_helper
else:
    import _input_pad_group
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


INPUT_PAD_TABLE_TYPE_NONE = _input_pad_group.INPUT_PAD_TABLE_TYPE_NONE
INPUT_PAD_TABLE_TYPE_CHARS = _input_pad_group.INPUT_PAD_TABLE_TYPE_CHARS
INPUT_PAD_TABLE_TYPE_KEYSYMS = _input_pad_group.INPUT_PAD_TABLE_TYPE_KEYSYMS
INPUT_PAD_TABLE_TYPE_STRINGS = _input_pad_group.INPUT_PAD_TABLE_TYPE_STRINGS
INPUT_PAD_TABLE_TYPE_COMMANDS = _input_pad_group.INPUT_PAD_TABLE_TYPE_COMMANDS
class _InputPadGroup(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, _InputPadGroup, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, _InputPadGroup, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _input_pad_group._InputPadGroup_name_set
    __swig_getmethods__["name"] = _input_pad_group._InputPadGroup_name_get
    if _newclass:name = _swig_property(_input_pad_group._InputPadGroup_name_get, _input_pad_group._InputPadGroup_name_set)
    __swig_setmethods__["table"] = _input_pad_group._InputPadGroup_table_set
    __swig_getmethods__["table"] = _input_pad_group._InputPadGroup_table_get
    if _newclass:table = _swig_property(_input_pad_group._InputPadGroup_table_get, _input_pad_group._InputPadGroup_table_set)
    __swig_setmethods__["next"] = _input_pad_group._InputPadGroup_next_set
    __swig_getmethods__["next"] = _input_pad_group._InputPadGroup_next_get
    if _newclass:next = _swig_property(_input_pad_group._InputPadGroup_next_get, _input_pad_group._InputPadGroup_next_set)
    __swig_setmethods__["priv"] = _input_pad_group._InputPadGroup_priv_set
    __swig_getmethods__["priv"] = _input_pad_group._InputPadGroup_priv_get
    if _newclass:priv = _swig_property(_input_pad_group._InputPadGroup_priv_get, _input_pad_group._InputPadGroup_priv_set)
    def __init__(self): 
        this = _input_pad_group.new__InputPadGroup()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _input_pad_group.delete__InputPadGroup
    __del__ = lambda self : None;
_InputPadGroup_swigregister = _input_pad_group._InputPadGroup_swigregister
_InputPadGroup_swigregister(_InputPadGroup)

class _InputPadTable(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, _InputPadTable, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, _InputPadTable, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _input_pad_group._InputPadTable_name_set
    __swig_getmethods__["name"] = _input_pad_group._InputPadTable_name_get
    if _newclass:name = _swig_property(_input_pad_group._InputPadTable_name_get, _input_pad_group._InputPadTable_name_set)
    __swig_setmethods__["column"] = _input_pad_group._InputPadTable_column_set
    __swig_getmethods__["column"] = _input_pad_group._InputPadTable_column_get
    if _newclass:column = _swig_property(_input_pad_group._InputPadTable_column_get, _input_pad_group._InputPadTable_column_set)
    __swig_setmethods__["type"] = _input_pad_group._InputPadTable_type_set
    __swig_getmethods__["type"] = _input_pad_group._InputPadTable_type_get
    if _newclass:type = _swig_property(_input_pad_group._InputPadTable_type_get, _input_pad_group._InputPadTable_type_set)
    __swig_setmethods__["next"] = _input_pad_group._InputPadTable_next_set
    __swig_getmethods__["next"] = _input_pad_group._InputPadTable_next_get
    if _newclass:next = _swig_property(_input_pad_group._InputPadTable_next_get, _input_pad_group._InputPadTable_next_set)
    __swig_setmethods__["priv"] = _input_pad_group._InputPadTable_priv_set
    __swig_getmethods__["priv"] = _input_pad_group._InputPadTable_priv_get
    if _newclass:priv = _swig_property(_input_pad_group._InputPadTable_priv_get, _input_pad_group._InputPadTable_priv_set)
    __swig_getmethods__["data"] = _input_pad_group._InputPadTable_data_get
    if _newclass:data = _swig_property(_input_pad_group._InputPadTable_data_get)
    def __init__(self): 
        this = _input_pad_group.new__InputPadTable()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _input_pad_group.delete__InputPadTable
    __del__ = lambda self : None;
_InputPadTable_swigregister = _input_pad_group._InputPadTable_swigregister
_InputPadTable_swigregister(_InputPadTable)

class _InputPadTable_data(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, _InputPadTable_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, _InputPadTable_data, name)
    __repr__ = _swig_repr
    __swig_setmethods__["chars"] = _input_pad_group._InputPadTable_data_chars_set
    __swig_getmethods__["chars"] = _input_pad_group._InputPadTable_data_chars_get
    if _newclass:chars = _swig_property(_input_pad_group._InputPadTable_data_chars_get, _input_pad_group._InputPadTable_data_chars_set)
    __swig_setmethods__["keysyms"] = _input_pad_group._InputPadTable_data_keysyms_set
    __swig_getmethods__["keysyms"] = _input_pad_group._InputPadTable_data_keysyms_get
    if _newclass:keysyms = _swig_property(_input_pad_group._InputPadTable_data_keysyms_get, _input_pad_group._InputPadTable_data_keysyms_set)
    __swig_setmethods__["strs"] = _input_pad_group._InputPadTable_data_strs_set
    __swig_getmethods__["strs"] = _input_pad_group._InputPadTable_data_strs_get
    if _newclass:strs = _swig_property(_input_pad_group._InputPadTable_data_strs_get, _input_pad_group._InputPadTable_data_strs_set)
    __swig_setmethods__["cmds"] = _input_pad_group._InputPadTable_data_cmds_set
    __swig_getmethods__["cmds"] = _input_pad_group._InputPadTable_data_cmds_get
    if _newclass:cmds = _swig_property(_input_pad_group._InputPadTable_data_cmds_get, _input_pad_group._InputPadTable_data_cmds_set)
    __swig_setmethods__["_future"] = _input_pad_group._InputPadTable_data__future_set
    __swig_getmethods__["_future"] = _input_pad_group._InputPadTable_data__future_get
    if _newclass:_future = _swig_property(_input_pad_group._InputPadTable_data__future_get, _input_pad_group._InputPadTable_data__future_set)
    def __init__(self): 
        this = _input_pad_group.new__InputPadTable_data()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _input_pad_group.delete__InputPadTable_data
    __del__ = lambda self : None;
_InputPadTable_data_swigregister = _input_pad_group._InputPadTable_data_swigregister
_InputPadTable_data_swigregister(_InputPadTable_data)

class _InputPadTableStr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, _InputPadTableStr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, _InputPadTableStr, name)
    __repr__ = _swig_repr
    __swig_setmethods__["label"] = _input_pad_group._InputPadTableStr_label_set
    __swig_getmethods__["label"] = _input_pad_group._InputPadTableStr_label_get
    if _newclass:label = _swig_property(_input_pad_group._InputPadTableStr_label_get, _input_pad_group._InputPadTableStr_label_set)
    __swig_setmethods__["comment"] = _input_pad_group._InputPadTableStr_comment_set
    __swig_getmethods__["comment"] = _input_pad_group._InputPadTableStr_comment_get
    if _newclass:comment = _swig_property(_input_pad_group._InputPadTableStr_comment_get, _input_pad_group._InputPadTableStr_comment_set)
    __swig_setmethods__["rawtext"] = _input_pad_group._InputPadTableStr_rawtext_set
    __swig_getmethods__["rawtext"] = _input_pad_group._InputPadTableStr_rawtext_get
    if _newclass:rawtext = _swig_property(_input_pad_group._InputPadTableStr_rawtext_get, _input_pad_group._InputPadTableStr_rawtext_set)
    def __init__(self): 
        this = _input_pad_group.new__InputPadTableStr()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _input_pad_group.delete__InputPadTableStr
    __del__ = lambda self : None;
_InputPadTableStr_swigregister = _input_pad_group._InputPadTableStr_swigregister
_InputPadTableStr_swigregister(_InputPadTableStr)

class _InputPadTableCmd(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, _InputPadTableCmd, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, _InputPadTableCmd, name)
    __repr__ = _swig_repr
    __swig_setmethods__["label"] = _input_pad_group._InputPadTableCmd_label_set
    __swig_getmethods__["label"] = _input_pad_group._InputPadTableCmd_label_get
    if _newclass:label = _swig_property(_input_pad_group._InputPadTableCmd_label_get, _input_pad_group._InputPadTableCmd_label_set)
    __swig_setmethods__["execl"] = _input_pad_group._InputPadTableCmd_execl_set
    __swig_getmethods__["execl"] = _input_pad_group._InputPadTableCmd_execl_get
    if _newclass:execl = _swig_property(_input_pad_group._InputPadTableCmd_execl_get, _input_pad_group._InputPadTableCmd_execl_set)
    def __init__(self): 
        this = _input_pad_group.new__InputPadTableCmd()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _input_pad_group.delete__InputPadTableCmd
    __del__ = lambda self : None;
_InputPadTableCmd_swigregister = _input_pad_group._InputPadTableCmd_swigregister
_InputPadTableCmd_swigregister(_InputPadTableCmd)

class _InputPadTableXXX(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, _InputPadTableXXX, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, _InputPadTableXXX, name)
    __repr__ = _swig_repr
    __swig_setmethods__["reserved1"] = _input_pad_group._InputPadTableXXX_reserved1_set
    __swig_getmethods__["reserved1"] = _input_pad_group._InputPadTableXXX_reserved1_get
    if _newclass:reserved1 = _swig_property(_input_pad_group._InputPadTableXXX_reserved1_get, _input_pad_group._InputPadTableXXX_reserved1_set)
    __swig_setmethods__["reserved2"] = _input_pad_group._InputPadTableXXX_reserved2_set
    __swig_getmethods__["reserved2"] = _input_pad_group._InputPadTableXXX_reserved2_get
    if _newclass:reserved2 = _swig_property(_input_pad_group._InputPadTableXXX_reserved2_get, _input_pad_group._InputPadTableXXX_reserved2_set)
    __swig_setmethods__["reserved3"] = _input_pad_group._InputPadTableXXX_reserved3_set
    __swig_getmethods__["reserved3"] = _input_pad_group._InputPadTableXXX_reserved3_get
    if _newclass:reserved3 = _swig_property(_input_pad_group._InputPadTableXXX_reserved3_get, _input_pad_group._InputPadTableXXX_reserved3_set)
    __swig_setmethods__["reserved4"] = _input_pad_group._InputPadTableXXX_reserved4_set
    __swig_getmethods__["reserved4"] = _input_pad_group._InputPadTableXXX_reserved4_get
    if _newclass:reserved4 = _swig_property(_input_pad_group._InputPadTableXXX_reserved4_get, _input_pad_group._InputPadTableXXX_reserved4_set)
    __swig_setmethods__["reserved5"] = _input_pad_group._InputPadTableXXX_reserved5_set
    __swig_getmethods__["reserved5"] = _input_pad_group._InputPadTableXXX_reserved5_get
    if _newclass:reserved5 = _swig_property(_input_pad_group._InputPadTableXXX_reserved5_get, _input_pad_group._InputPadTableXXX_reserved5_set)
    def __init__(self): 
        this = _input_pad_group.new__InputPadTableXXX()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _input_pad_group.delete__InputPadTableXXX
    __del__ = lambda self : None;
_InputPadTableXXX_swigregister = _input_pad_group._InputPadTableXXX_swigregister
_InputPadTableXXX_swigregister(_InputPadTableXXX)


def input_pad_group_append_from_file(*args):
  return _input_pad_group.input_pad_group_append_from_file(*args)
input_pad_group_append_from_file = _input_pad_group.input_pad_group_append_from_file

def input_pad_group_parse_all_files(*args):
  return _input_pad_group.input_pad_group_parse_all_files(*args)
input_pad_group_parse_all_files = _input_pad_group.input_pad_group_parse_all_files

def input_pad_group_destroy(*args):
  return _input_pad_group.input_pad_group_destroy(*args)
input_pad_group_destroy = _input_pad_group.input_pad_group_destroy
def parse_all_files(custom_dirname=None, domain=None):
    return input_pad_group_parse_all_files (custom_dirname, domain)



