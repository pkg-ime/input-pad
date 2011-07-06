# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.3
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
            fp, pathname, description = imp.find_module('_input_pad_window_gtk', [dirname(__file__)])
        except ImportError:
            import _input_pad_window_gtk
            return _input_pad_window_gtk
        if fp is not None:
            try:
                _mod = imp.load_module('_input_pad_window_gtk', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _input_pad_window_gtk = swig_import_helper()
    del swig_import_helper
else:
    import _input_pad_window_gtk
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


class _InputPadGtkWindow(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, _InputPadGtkWindow, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, _InputPadGtkWindow, name)
    __repr__ = _swig_repr
    __swig_setmethods__["parent"] = _input_pad_window_gtk._InputPadGtkWindow_parent_set
    __swig_getmethods__["parent"] = _input_pad_window_gtk._InputPadGtkWindow_parent_get
    if _newclass:parent = _swig_property(_input_pad_window_gtk._InputPadGtkWindow_parent_get, _input_pad_window_gtk._InputPadGtkWindow_parent_set)
    __swig_setmethods__["child"] = _input_pad_window_gtk._InputPadGtkWindow_child_set
    __swig_getmethods__["child"] = _input_pad_window_gtk._InputPadGtkWindow_child_get
    if _newclass:child = _swig_property(_input_pad_window_gtk._InputPadGtkWindow_child_get, _input_pad_window_gtk._InputPadGtkWindow_child_set)
    __swig_setmethods__["priv"] = _input_pad_window_gtk._InputPadGtkWindow_priv_set
    __swig_getmethods__["priv"] = _input_pad_window_gtk._InputPadGtkWindow_priv_get
    if _newclass:priv = _swig_property(_input_pad_window_gtk._InputPadGtkWindow_priv_get, _input_pad_window_gtk._InputPadGtkWindow_priv_set)
    def __init__(self, *args): 
        this = _input_pad_window_gtk.new__InputPadGtkWindow(*args)
        try: self.this.append(this)
        except: self.this = this
    def hide(self): return _input_pad_window_gtk._InputPadGtkWindow_hide(self)
    def show(self): return _input_pad_window_gtk._InputPadGtkWindow_show(self)
    def get_visible(self): return _input_pad_window_gtk._InputPadGtkWindow_get_visible(self)
    def set_paddir(self, *args): return _input_pad_window_gtk._InputPadGtkWindow_set_paddir(self, *args)
    def append_padfile(self, *args): return _input_pad_window_gtk._InputPadGtkWindow_append_padfile(self, *args)
    def set_char_button_sensitive(self, *args): return _input_pad_window_gtk._InputPadGtkWindow_set_char_button_sensitive(self, *args)
    def reorder_button_pressed(self): return _input_pad_window_gtk._InputPadGtkWindow_reorder_button_pressed(self)
    def get_keyboard_state(self): return _input_pad_window_gtk._InputPadGtkWindow_get_keyboard_state(self)
    def set_keyboard_state(self, *args): return _input_pad_window_gtk._InputPadGtkWindow_set_keyboard_state(self, *args)
    def set_keyboard_state_with_keysym(self, *args): return _input_pad_window_gtk._InputPadGtkWindow_set_keyboard_state_with_keysym(self, *args)
    def set_kbdui_name(self, *args): return _input_pad_window_gtk._InputPadGtkWindow_set_kbdui_name(self, *args)
    def set_show_table(self, *args): return _input_pad_window_gtk._InputPadGtkWindow_set_show_table(self, *args)
    def set_show_layout(self, *args): return _input_pad_window_gtk._InputPadGtkWindow_set_show_layout(self, *args)
    def show_all(self): return _input_pad_window_gtk._InputPadGtkWindow_show_all(self)
    def connect(self, *args): return _input_pad_window_gtk._InputPadGtkWindow_connect(self, *args)
    __swig_destroy__ = _input_pad_window_gtk.delete__InputPadGtkWindow
    __del__ = lambda self : None;
_InputPadGtkWindow_swigregister = _input_pad_window_gtk._InputPadGtkWindow_swigregister
_InputPadGtkWindow_swigregister(_InputPadGtkWindow)

class _InputPadGtkWindowClass(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, _InputPadGtkWindowClass, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, _InputPadGtkWindowClass, name)
    __repr__ = _swig_repr
    __swig_setmethods__["parent_class"] = _input_pad_window_gtk._InputPadGtkWindowClass_parent_class_set
    __swig_getmethods__["parent_class"] = _input_pad_window_gtk._InputPadGtkWindowClass_parent_class_get
    if _newclass:parent_class = _swig_property(_input_pad_window_gtk._InputPadGtkWindowClass_parent_class_get, _input_pad_window_gtk._InputPadGtkWindowClass_parent_class_set)
    __swig_setmethods__["button_pressed"] = _input_pad_window_gtk._InputPadGtkWindowClass_button_pressed_set
    __swig_getmethods__["button_pressed"] = _input_pad_window_gtk._InputPadGtkWindowClass_button_pressed_get
    if _newclass:button_pressed = _swig_property(_input_pad_window_gtk._InputPadGtkWindowClass_button_pressed_get, _input_pad_window_gtk._InputPadGtkWindowClass_button_pressed_set)
    __swig_setmethods__["keyboard_changed"] = _input_pad_window_gtk._InputPadGtkWindowClass_keyboard_changed_set
    __swig_getmethods__["keyboard_changed"] = _input_pad_window_gtk._InputPadGtkWindowClass_keyboard_changed_get
    if _newclass:keyboard_changed = _swig_property(_input_pad_window_gtk._InputPadGtkWindowClass_keyboard_changed_get, _input_pad_window_gtk._InputPadGtkWindowClass_keyboard_changed_set)
    __swig_setmethods__["group_changed"] = _input_pad_window_gtk._InputPadGtkWindowClass_group_changed_set
    __swig_getmethods__["group_changed"] = _input_pad_window_gtk._InputPadGtkWindowClass_group_changed_get
    if _newclass:group_changed = _swig_property(_input_pad_window_gtk._InputPadGtkWindowClass_group_changed_get, _input_pad_window_gtk._InputPadGtkWindowClass_group_changed_set)
    __swig_setmethods__["group_appended"] = _input_pad_window_gtk._InputPadGtkWindowClass_group_appended_set
    __swig_getmethods__["group_appended"] = _input_pad_window_gtk._InputPadGtkWindowClass_group_appended_get
    if _newclass:group_appended = _swig_property(_input_pad_window_gtk._InputPadGtkWindowClass_group_appended_get, _input_pad_window_gtk._InputPadGtkWindowClass_group_appended_set)
    __swig_setmethods__["char_button_sensitive"] = _input_pad_window_gtk._InputPadGtkWindowClass_char_button_sensitive_set
    __swig_getmethods__["char_button_sensitive"] = _input_pad_window_gtk._InputPadGtkWindowClass_char_button_sensitive_get
    if _newclass:char_button_sensitive = _swig_property(_input_pad_window_gtk._InputPadGtkWindowClass_char_button_sensitive_get, _input_pad_window_gtk._InputPadGtkWindowClass_char_button_sensitive_set)
    __swig_setmethods__["reorder_button_pressed"] = _input_pad_window_gtk._InputPadGtkWindowClass_reorder_button_pressed_set
    __swig_getmethods__["reorder_button_pressed"] = _input_pad_window_gtk._InputPadGtkWindowClass_reorder_button_pressed_get
    if _newclass:reorder_button_pressed = _swig_property(_input_pad_window_gtk._InputPadGtkWindowClass_reorder_button_pressed_get, _input_pad_window_gtk._InputPadGtkWindowClass_reorder_button_pressed_set)
    __swig_setmethods__["_window_reserved1"] = _input_pad_window_gtk._InputPadGtkWindowClass__window_reserved1_set
    __swig_getmethods__["_window_reserved1"] = _input_pad_window_gtk._InputPadGtkWindowClass__window_reserved1_get
    if _newclass:_window_reserved1 = _swig_property(_input_pad_window_gtk._InputPadGtkWindowClass__window_reserved1_get, _input_pad_window_gtk._InputPadGtkWindowClass__window_reserved1_set)
    __swig_setmethods__["_window_reserved2"] = _input_pad_window_gtk._InputPadGtkWindowClass__window_reserved2_set
    __swig_getmethods__["_window_reserved2"] = _input_pad_window_gtk._InputPadGtkWindowClass__window_reserved2_get
    if _newclass:_window_reserved2 = _swig_property(_input_pad_window_gtk._InputPadGtkWindowClass__window_reserved2_get, _input_pad_window_gtk._InputPadGtkWindowClass__window_reserved2_set)
    __swig_setmethods__["_window_reserved3"] = _input_pad_window_gtk._InputPadGtkWindowClass__window_reserved3_set
    __swig_getmethods__["_window_reserved3"] = _input_pad_window_gtk._InputPadGtkWindowClass__window_reserved3_get
    if _newclass:_window_reserved3 = _swig_property(_input_pad_window_gtk._InputPadGtkWindowClass__window_reserved3_get, _input_pad_window_gtk._InputPadGtkWindowClass__window_reserved3_set)
    __swig_setmethods__["_window_reserved4"] = _input_pad_window_gtk._InputPadGtkWindowClass__window_reserved4_set
    __swig_getmethods__["_window_reserved4"] = _input_pad_window_gtk._InputPadGtkWindowClass__window_reserved4_get
    if _newclass:_window_reserved4 = _swig_property(_input_pad_window_gtk._InputPadGtkWindowClass__window_reserved4_get, _input_pad_window_gtk._InputPadGtkWindowClass__window_reserved4_set)
    def __init__(self): 
        this = _input_pad_window_gtk.new__InputPadGtkWindowClass()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _input_pad_window_gtk.delete__InputPadGtkWindowClass
    __del__ = lambda self : None;
_InputPadGtkWindowClass_swigregister = _input_pad_window_gtk._InputPadGtkWindowClass_swigregister
_InputPadGtkWindowClass_swigregister(_InputPadGtkWindowClass)


def input_pad_gtk_window_get_type():
  return _input_pad_window_gtk.input_pad_gtk_window_get_type()
input_pad_gtk_window_get_type = _input_pad_window_gtk.input_pad_gtk_window_get_type

def input_pad_gtk_window_new(*args):
  return _input_pad_window_gtk.input_pad_gtk_window_new(*args)
input_pad_gtk_window_new = _input_pad_window_gtk.input_pad_gtk_window_new

def input_pad_gtk_window_set_paddir(*args):
  return _input_pad_window_gtk.input_pad_gtk_window_set_paddir(*args)
input_pad_gtk_window_set_paddir = _input_pad_window_gtk.input_pad_gtk_window_set_paddir

def input_pad_gtk_window_append_padfile(*args):
  return _input_pad_window_gtk.input_pad_gtk_window_append_padfile(*args)
input_pad_gtk_window_append_padfile = _input_pad_window_gtk.input_pad_gtk_window_append_padfile

def input_pad_gtk_window_set_char_button_sensitive(*args):
  return _input_pad_window_gtk.input_pad_gtk_window_set_char_button_sensitive(*args)
input_pad_gtk_window_set_char_button_sensitive = _input_pad_window_gtk.input_pad_gtk_window_set_char_button_sensitive

def input_pad_gtk_window_reorder_button_pressed(*args):
  return _input_pad_window_gtk.input_pad_gtk_window_reorder_button_pressed(*args)
input_pad_gtk_window_reorder_button_pressed = _input_pad_window_gtk.input_pad_gtk_window_reorder_button_pressed

def input_pad_gtk_window_get_keyboard_state(*args):
  return _input_pad_window_gtk.input_pad_gtk_window_get_keyboard_state(*args)
input_pad_gtk_window_get_keyboard_state = _input_pad_window_gtk.input_pad_gtk_window_get_keyboard_state

def input_pad_gtk_window_set_keyboard_state(*args):
  return _input_pad_window_gtk.input_pad_gtk_window_set_keyboard_state(*args)
input_pad_gtk_window_set_keyboard_state = _input_pad_window_gtk.input_pad_gtk_window_set_keyboard_state

def input_pad_gtk_window_set_keyboard_state_with_keysym(*args):
  return _input_pad_window_gtk.input_pad_gtk_window_set_keyboard_state_with_keysym(*args)
input_pad_gtk_window_set_keyboard_state_with_keysym = _input_pad_window_gtk.input_pad_gtk_window_set_keyboard_state_with_keysym

def input_pad_gtk_window_get_kbdui_name_list():
  return _input_pad_window_gtk.input_pad_gtk_window_get_kbdui_name_list()
input_pad_gtk_window_get_kbdui_name_list = _input_pad_window_gtk.input_pad_gtk_window_get_kbdui_name_list

def input_pad_gtk_window_set_kbdui_name(*args):
  return _input_pad_window_gtk.input_pad_gtk_window_set_kbdui_name(*args)
input_pad_gtk_window_set_kbdui_name = _input_pad_window_gtk.input_pad_gtk_window_set_kbdui_name

def input_pad_gtk_window_set_show_table(*args):
  return _input_pad_window_gtk.input_pad_gtk_window_set_show_table(*args)
input_pad_gtk_window_set_show_table = _input_pad_window_gtk.input_pad_gtk_window_set_show_table

def input_pad_gtk_window_set_show_layout(*args):
  return _input_pad_window_gtk.input_pad_gtk_window_set_show_layout(*args)
input_pad_gtk_window_set_show_layout = _input_pad_window_gtk.input_pad_gtk_window_set_show_layout
class InputPadGtkWindow(_InputPadGtkWindow):
    def __init__(self, pytype, child=0):
        _InputPadGtkWindow.__init__(self, pytype, child)
    def set_paddir(self, paddir, domain=None):
        _InputPadGtkWindow.set_paddir(self, paddir, domain)
    def append_padfile(self, padfile, domain=None):
        _InputPadGtkWindow.append_padfile(self, padfile, domain)

def get_kbdui_name_list():
    return _input_pad_gtk_window_get_kbdui_name_list_wrapper()


def _input_pad_gtk_window_new_with_gtype(*args):
  return _input_pad_window_gtk._input_pad_gtk_window_new_with_gtype(*args)
_input_pad_gtk_window_new_with_gtype = _input_pad_window_gtk._input_pad_gtk_window_new_with_gtype

def _input_pad_gtk_window_get_kbdui_name_list_wrapper():
  return _input_pad_window_gtk._input_pad_gtk_window_get_kbdui_name_list_wrapper()
_input_pad_gtk_window_get_kbdui_name_list_wrapper = _input_pad_window_gtk._input_pad_gtk_window_get_kbdui_name_list_wrapper

def _input_pad_gtk_window_new_wrapper(*args):
  return _input_pad_window_gtk._input_pad_gtk_window_new_wrapper(*args)
_input_pad_gtk_window_new_wrapper = _input_pad_window_gtk._input_pad_gtk_window_new_wrapper
class python_callback_data(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, python_callback_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, python_callback_data, name)
    __repr__ = _swig_repr
    __swig_setmethods__["pysignal_cb"] = _input_pad_window_gtk.python_callback_data_pysignal_cb_set
    __swig_getmethods__["pysignal_cb"] = _input_pad_window_gtk.python_callback_data_pysignal_cb_get
    if _newclass:pysignal_cb = _swig_property(_input_pad_window_gtk.python_callback_data_pysignal_cb_get, _input_pad_window_gtk.python_callback_data_pysignal_cb_set)
    __swig_setmethods__["pydata"] = _input_pad_window_gtk.python_callback_data_pydata_set
    __swig_getmethods__["pydata"] = _input_pad_window_gtk.python_callback_data_pydata_get
    if _newclass:pydata = _swig_property(_input_pad_window_gtk.python_callback_data_pydata_get, _input_pad_window_gtk.python_callback_data_pydata_set)
    def __init__(self): 
        this = _input_pad_window_gtk.new_python_callback_data()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _input_pad_window_gtk.delete_python_callback_data
    __del__ = lambda self : None;
python_callback_data_swigregister = _input_pad_window_gtk.python_callback_data_swigregister
python_callback_data_swigregister(python_callback_data)


def button_pressed_cb(*args):
  return _input_pad_window_gtk.button_pressed_cb(*args)
button_pressed_cb = _input_pad_window_gtk.button_pressed_cb

def _input_pad_gtk_window_connect_wrapper(*args):
  return _input_pad_window_gtk._input_pad_gtk_window_connect_wrapper(*args)
_input_pad_gtk_window_connect_wrapper = _input_pad_window_gtk._input_pad_gtk_window_connect_wrapper


