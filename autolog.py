"""Automated logging.

This module enables to log function and method calls automatically.

Here are some of the useful functions provided by this module:

    add_modules(list_of_modules)        Define modules that we want to log
    exclude_modules(list_of_modules)    Define modules that we do not want to log
    run()                               Activate logging

No warranties for this module.
"""
__author__ = ('englerfa')

import inspect                  # module used to retrieve information about functions (such as arguments, return value)
import datetime                 # module used with 'exec' command. Do not delete even though it seems unused.

import basic
import basic2
import inheritance
import nested
import new

functions = []
modules_to_log = []
modules_not_to_log = []

def add_modules(list_of_modules):
    global  modules_to_log
    modules_to_log = list_of_modules

def exclude_modules(list_of_modules):
    global modules_not_to_log
    modules_not_to_log = list_of_modules

def run():
    _traverse_modules(list(set(modules_to_log) - set(modules_not_to_log)))
    _execute_monkey_patching()

def _traverse(nodes):
    for elem in inspect.getmembers(nodes):
        if type(elem[1]).__name__ == "function":                            # get global functions
            tup = (elem[1], mod.__name__)
            functions.append(tup)
        if type(elem[1]) == type.__class__ and elem[0] != "__class__":      # Need to exclude tup '__class__', since they are also of type 'class'
            _traverse(elem[1])   # recursion to get nested classes

def _traverse_modules(mods):
    global mod
    for mod in mods:
        _traverse(mod)

def _format_signature(signature):
    res = '('
    first = True        # solution for post fence problem
    for sig in signature.parameters:
        if first:
            res += str(sig) + '=' + '{' + str(sig) + '}'
            first = False
        else:
            res += ',' + str(sig) + '=' + '{' + str(sig) + '}'
    res += ')'
    return res

def _execute_monkey_patching():
    i = 0
    for f in functions:
        qualified_name = f[1] + "." + f[0].__qualname__
        signature = str(inspect.signature(f[0]))
        signature_values = _format_signature(inspect.signature(f[0]))

        s_global        = f"global f_original{str(i)}\n"
        s_original      = f"f_original{str(i)}={qualified_name}\n"         # str(i) is needed to create for every function an individual name, otherwise it gets overwritten (point to same reference)
        s_def           = f"def f_monkey {signature}:\n"
        s_try           = f"    try:\n"
        s_result        = f"        result = f_original{str(i)}{signature}\n"
        s_extend        = f"        print(f'{datetime.datetime.now()} {qualified_name}{signature_values} =',result, type(result))\n"
        s_except        = f"    except Exception as e:\n"
        s_except_text   = f"        print(f'{datetime.datetime.now()} Caught an exception',e, f'in function {qualified_name}')\n"
        s_raise         = f"        raise e  # raise it again, so the code behavior is not modified\n"
        s_replace       = f"{qualified_name}=f_monkey\n"

        s_execute = s_global + s_original + s_def + s_try + s_result + s_extend + s_except + s_except_text + s_raise + s_replace
        #print(s_execute)
        exec(s_execute)

        i = i + 1