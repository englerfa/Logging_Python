import basic
import basic2
import inheritance
import nested

import inspect                  # module used to retrieve information about functions (such as arguments, return value)
import datetime                 # module used with 'exec' command. Do not delete even though it seems unused.


functions = []
modules_to_log = []


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

def _format_arguments(args):
    arg_names = args.args
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
def _assemble_arguments_default(args_specification):
    defs = []
    k=0
    for arg in args_specification.args:
        if args_specification != None and args_specification.defaults != None and k < len(args_specification.defaults):
            defs.insert(0,args_specification.defaults[k])
        else:
            defs.insert(0,'')
        k=k+1

    res = ""
    i = 0
    first = True
    for arg in args_specification.args:
        if first:
            if defs[i] == '':
                res += f'{args_specification.args[i]}'
                i = i+1
                first = False
            else:
                res += f'{args_specification.args[i]}={defs[i]}'
                i = i+1
                first = False
        else:
            if defs[i] == '':
                res += f',{args_specification.args[i]}'
                i = i+1
            else:
                res += f',{args_specification.args[i]}={defs[i]}'
                i = i+1
    return res

def _execute_monkey_patching():
    i = 0
    for f in functions:
        args_specification = inspect.getfullargspec(f[0])
        qualname = f[1] + "." + f[0].__qualname__

        s_global = 'global f_original' + str(i) + ';'
        s_original = 'f_original' + str(i) + '=' + qualname + ';'  # str(i) is needed to create for every function an individual name, otherwise it gets overwritten (point to same reference)

        s_arg_defaults = '(' + _assemble_arguments_default(args_specification) + ')'
        s_args = _format_arguments(args_specification)

        s_signature = '"' + qualname + '(" ' + s_args + ',"' + ") = " + '"'
        s_result = ", result," + '"' + "[" + '"' + ", type(result)," + '"' + "]" + '"'

        s_f_original = 'def f_monkey' + s_arg_defaults + ':\n' + '    result = f_original' + str(i) + s_arg_defaults
        s_f_extend = '    try:\n        print("     ",   datetime.datetime.now(),' + s_signature + s_result + ')' + '\n    except Exception as e:\n        print(datetime.datetime.now(),"exception raised while logging", str(e))'

        s_replace = qualname + ' = f_monkey'

        s_execute = s_global + '\n' + s_original + '\n' + s_f_original + '\n' + s_f_extend+ '\n' + s_replace
        #print(s_execute)
        exec(s_execute)

        i = i + 1

















