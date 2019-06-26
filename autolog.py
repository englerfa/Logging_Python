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
modules_to_log = [basic, basic2, inheritance, nested]

def add_modules(list_of_modules):
    global  modules_to_log
    modules_to_log = list_of_modules

def run():
    _traverse_modules(modules_to_log)
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

def _format_arguments(fullargsspec):
    arg_names = fullargsspec.args
    res = ""
    first = True
    for arg in arg_names:
        if first:
            res += '"' + arg + ' =",' + arg
            first = False
        else:
            res += "," + '","' + "," + '"' + arg + ' ="' + "," + arg
    return res

# This function is needed to handle default parameters.
def _assemble_variable_arguments(fullargsspec):
    print(fullargsspec)

    # Preparation: transform default values into array of same length as other arguments
    k=0
    defaults = []
    for arg in fullargsspec.args:
        if fullargsspec is not None and fullargsspec.defaults is not None and k < len(fullargsspec.defaults):
            defaults.insert(0,fullargsspec.defaults[k])
        else:
            defaults.insert(0,'')
        k=k+1

        # Handle arguments with different lengths
    res = ""
    i = 0
    first = True
    for arg in fullargsspec.args:
        if first:               # postfence problem
            if defaults[i] == '':
                res += f'{fullargsspec.args[i]}'
                i = i+1
                first = False
            else:
                res += f'{fullargsspec.args[i]}={defaults[i]}'
                i = i+1
                first = False
        else:
            if defaults[i] == '':
                res += f',{fullargsspec.args[i]}'
                i = i+1
            else:
                res += f',{fullargsspec.args[i]}={defaults[i]}'
                i = i+1
    return res

def _execute_monkey_patching():
    i = 0
    for f in functions:
        fullargsspec = inspect.getfullargspec(f[0])
        s_function_name = f[1] + "." + f[0].__qualname__

        s_global = 'global f_original' + str(i) + ';'
        s_original = 'f_original' + str(i) + '=' + s_function_name + ';'  # str(i) is needed to create for every function an individual name, otherwise it gets overwritten (point to same reference)

        s_signature= '(' + _assemble_variable_arguments(fullargsspec) + ')'
        print("NAME="+s_function_name)
        print(inspect.signature(f[0]))
        s_args = _format_arguments(fullargsspec)

        s_definition = '"' + s_function_name + '(" ' + s_args + ',"' + ") = " + '"'
        s_result = ", result," + '"' + "[" + '"' + ", type(result)," + '"' + "]" + '"'

        s_f_original = 'def f_monkey' + s_signature + ':\n' + '    result = f_original' + str(i) + s_signature
        s_f_extend = '    try:\n        print("     ",   datetime.datetime.now(),' + s_definition + s_result + ')' + '\n    except Exception as e:\n        print(datetime.datetime.now(),"exception raised while logging", str(e))'

        s_replace = s_function_name + ' = f_monkey'

        s_execute = s_global + '\n' + s_original + '\n' + s_f_original + '\n' + s_f_extend+ '\n' + s_replace
        print(s_execute)
        exec(s_execute)

        i = i + 1

















