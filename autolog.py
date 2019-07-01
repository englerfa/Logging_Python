"""Automated logging.

This module enables to log function and method calls automatically.

Here are some of the useful functions provided by this module:

    add_modules()
    run()

No warranties for this module.
"""
__author__ = ('englerfa')

import inspect                  # module used to retrieve information about functions (such as arguments, return value)

import basic
import basic2
import inheritance
import nested

functions = []
modules_to_log = [basic, basic2, inheritance, nested]

def add_modules(list_of_modules):
    global  modules_to_log
    modules_to_log = list_of_modules

def run():
    _traverse_modules(modules_to_log)
    _execute_monkey_patching()
    print("Monkey patching done, executing the program")

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
        mod_path = mod.__name__.split('.')
        if len(mod_path) > 1:
            command = f'global {mod_path[-1]}\nfrom {".".join(mod_path[:-1])} import {mod_path[-1]}'
        else:
            command = f'global {mod_path[-1]}\nimport {mod_path[-1]}'
        #print(command)
        exec(command)
        _traverse(mod)

def _format_signature(signature):
    res = '('
    comma = False        # solution for post fence problem
    for sig in signature.parameters:
        default = signature.parameters[sig].default
        empty = False
        if type(default) == str:
            default = "'" + str(default) + "'"
        elif default == inspect._empty:
            empty = True
            default = ''
        elif type(default) == type:
            # import type from the module to assure its existence
            command = f'global {default.__name__}\nfrom {default.__module__} import {default.__name__}'
            #print(command)
            exec(command)
            default = str(default.__name__)
        else:
            default = str(default)

        print('signature attri: ' + signature.parameters[sig].name)
        print('signature value: ' + default)
        if comma:
            res += ', '
        if '**' in str(signature.parameters[sig]):
            res += '**'
        res += signature.parameters[sig].name
        if not empty:
             res += '=' + default
        comma = True
    res += ')'
    #print('resulting signature: ' + res)
    return res

def _execute_monkey_patching():
    i = 0
    for f in functions:
        s_name = f[1] + "." + f[0].__qualname__

        s_global = f"global f_original{str(i)}"
        s_original = f"f_original{str(i)}={s_name}"         # str(i) is needed to create for every function an individual name, otherwise it gets overwritten (point to same reference)

        s_signature = str(inspect.signature(f[0]))
        s_signature_values = _format_signature(inspect.signature(f[0]))

        s_f_def = f"def f_monkey{s_signature_values}:"

        s_f_log = f"  print(f\"autolog fun called: {s_name}{s_signature_values}\")"

        s_f_call = f"  result = f_original{str(i)}{s_signature_values}"
        
        s_f_ret = "  print(result, type(result))"

        s_replace = s_name + ' = f_monkey'

        s_execute = '\n'.join([s_global, s_original, s_f_def, s_f_log, s_f_call, s_f_ret, s_replace])
        print(s_execute)
        exec(s_execute)

        i = i + 1
