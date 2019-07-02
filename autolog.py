"""Automated logging.

This module enables to log function and method calls automatically.

Here are some of the useful functions provided by this module:

    add_modules()
    run()

No warranties for this module.
"""
__author__ = ('englerfa')

import inspect                  # module used to retrieve information about functions (such as arguments, return value)
import datetime                 # module used with 'exec' command. Do not delete even though it seems unused.

import basic
import basic2
import inheritance
import nested

functions = []
modules_to_log = []
modules_not_to_log = []

def exclude_modules(list_of_modules):
    global modules_not_to_log
    modules_not_to_log = list_of_modules

def add_modules(list_of_modules):
    global  modules_to_log
    modules_to_log = list_of_modules

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
        s_name = f[1] + "." + f[0].__qualname__

        s_global = f"global f_original{str(i)}"
        s_original = f"f_original{str(i)}={s_name}"         # str(i) is needed to create for every function an individual name, otherwise it gets overwritten (point to same reference)

        s_signature = str(inspect.signature(f[0]))
        s_signature_values = _format_signature(inspect.signature(f[0]))

        s_f_original = f"def f_monkey {s_signature}: \n    result = f_original{str(i)}{s_signature}"

        s_extend_try = f"    try:\n        print(f'{datetime.datetime.now()} {s_name}{s_signature_values} =',result, type(result))"
        s_extend_exception = '    except Exception as e:\n        print(datetime.datetime.now(),"exception raised while logging", str(e))'
        s_extend = s_extend_try + '\n' + s_extend_exception

        s_replace = s_name + ' = f_monkey'

        s_execute = s_global + '\n' + s_original + '\n' + s_f_original + '\n' + s_extend+ '\n' + s_replace
        #print(s_execute)
        exec(s_execute)

        i = i + 1