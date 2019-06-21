import basic
import nested

import inspect                  # module used to retrieve information about functions (such as arguments, return value)
import datetime                 # module used with 'exec' command. Do not delete even though it seems unused.


functions = []
modules_to_log = []

def add_module(module):
    modules_to_log.append(module)

def traverse(nodes):
    for elem in inspect.getmembers(nodes):
        if type(elem[1]).__name__ == "function":                            # get global functions
            tup = (elem[1], mod.__name__)
            functions.append(tup)
        if type(elem[1]) == type.__class__ and elem[0] != "__class__":      # Need to exclude tup '__class__', since they are also of type 'class'
            traverse(elem[1])   # recursion to get nested classes

def traverse_modules(mods):
    global mod
    for mod in mods:
        traverse(mod)

def format_arguments(args):
    res = ""
    first = True
    for arg in args:
        if first:
            res += '"' + arg + ' =",' + arg
            first = False
        else:
            res += "," + '","' + "," + '"' + arg + ' ="' + "," + arg
    return res

def execute_monkey_patching():
    i = 0
    for f in functions:
        args = inspect.getfullargspec(f[0]).args
        qualname = f[1] + "." + f[0].__qualname__

        s_original = 'f_original' + str(i) + '=' + qualname + ';'  # str(i) is needed to create for every function an individual name, otherwise it gets overwritten (point to same reference)
        s_global = 'global f_original' + str(i) + ';'
        #print(s_global + s_original)
        exec(s_global + s_original)


        s_arg_values = '(' + ','.join(args) + ')'
        s_arg_names = '"(' + ','.join(args) + ') ="'
        s_args = format_arguments(args)

        s_signature = '"' + qualname + '(" ' + s_args + ',"' + ") = " + '"'
        s_result = ", result," + '"' + "[" + '"' + ", type(result)," + '"' + "]" + '"'

        s_f_original = 'def f_monkey' + s_arg_values + ':' + 'result = f_original' + str(i) + s_arg_values + ';'
        s_f_extend = 'print("     ",   datetime.datetime.now(),' + s_signature + s_result + ')'
        s_f = s_f_original + s_f_extend
        #print(s_f)
        exec(s_f)

        s_replace = qualname + ' = f_monkey'
        #print(s_replace)
        exec(s_replace)

        i = i + 1


