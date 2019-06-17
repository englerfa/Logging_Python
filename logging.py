import main                     # module that we want to extend with logging
import main_basic_nested               # module that we want to extend with logging
import main_basic

import inspect                  # module with information about about objects such as functions
import datetime                 # do not delete this module even though it seems unused. It is used with the 'exec' command.

# Define modules to log (modules must be imported above)
modules = [main_basic, main, main_basic_nested]


# Retrieve functions
functions = []
def traverse(nodes):
    for elem in inspect.getmembers(nodes):
        if type(elem[1]).__name__ == "function":                            # get global functions
            tuple = (elem[1], mod.__name__)
            functions.append(tuple)
        if type(elem[1]) == type.__class__ and elem[0] != "__class__":      # Need to exclude tuple '__class__', since they are also of type 'class'
            traverse(elem[1])   # recursion to get nested classes



for mod in modules:
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


# Execute monkey patching
i = 0
for f in functions:
    args = inspect.getfullargspec(f[0]).args
    qualname = f[1] + "." + f[0].__qualname__

    s_original = 'f_original' + str(i) + '=' + qualname      # str(i) is needed to create for every function an individual name, otherwise it gets overwritten (point to same reference)
    exec(s_original)

    s_arg_values = '(' + ','.join(args) + ')'
    s_arg_names = '"(' + ','.join(args) + ') ="'
    s_args = format_arguments(args)

    s_signature = '"' + qualname + '(" ' + s_args + ',"' + ") = " + '"'
    s_result = ", result," + '"' + "[" + '"' + ", type(result)," + '"' + "]" + '"'

    s_f_original = 'def f_monkey' + s_arg_values + ':' + 'result = f_original' + str(i) + s_arg_values + ';'
    s_f_extend = 'print(datetime.datetime.now(),' + s_signature + s_result + ')'
    s_f = s_f_original + s_f_extend

    exec(s_f)
    s_replace = qualname + ' = f_monkey'
    exec(s_replace)

    i = i+1


