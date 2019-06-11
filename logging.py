import main                     # module that we want to extend with logging
import main_basic_nested               # module that we want to extend with logging
import main_basic

import inspect                  # module with information about about objects such as functions
import datetime                 # do not delete this module even though it seems unused. It is used with the 'exec' command.

# Choose module that contains functions to log
module = main_basic


# Retrieve functions
functions = []
def traverse(nodes):
    for elem in inspect.getmembers(nodes):
        if type(elem[1]).__name__ == "function":                            # get global functions
            functions.append(elem[1])
        if type(elem[1]) == type.__class__ and elem[0] != "__class__":      # Need to exclude tuple '__class__', since they are also of type 'class'
            traverse(elem[1])   # recursion to get nested classes

traverse(module)
print(functions)



# Execute monkey patching
print()

i = 0
for f in functions:
    args = inspect.getfullargspec(f).args

    s_original = 'f_original' + str(i) + '=' + module.__name__ + "." + f.__qualname__       # str(i) is needed to create for every function an own original, otherwise it gets overwritten
    exec(s_original)

    s_args = '(' + ','.join(args) + ')'
    s_arg_names = '"(' + ','.join(args) + ') ="'

    s_f_original = 'def f_monkey' + s_args + ':' + 'result = f_original' + str(i) + s_args + ';'
    s_f_extend = 'print(' + "datetime.datetime.now()," + s_arg_names + "," + s_args + "," + '"' + "return =" + '"' + "," + "result" + "," + "type(result)" + ')'
    s_f = s_f_original + s_f_extend

    exec(s_f)
    s_replace = module.__name__ + "." + f.__qualname__ + ' = f_monkey'
    exec(s_replace)

    i = i+1



# Test function calls
module.print_example()
module.A.add_numbers(0,3,5)





