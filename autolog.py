"""Automated logging.

This module enables to log function and method calls automatically.

Here are some of the useful functions provided by this module:

    Autolog(list_of_modules, recursion_depth=1)
    run()

No warranties for this module.
"""
__author__ = ('englerfa', 'karel.kubicek@inf.ethz.ch')

# TODO: document the methods

import inspect                  # module used to retrieve information about functions (such as arguments, return value)


class Autolog:
    def __init__(self, list_of_modules, recursion_depth=1):
        """
        :param list_of_modules:
        :param recursion_depth:
        :patch_id: counts the patched and assigns the unique ID to prevent redefinition
        """
        self.modules_to_log = list_of_modules
        self.recursion_depth = recursion_depth
        self.patch_id = 0

    def run(self):
        """
        Starts the execution
        :return: None
        """
        self._traverse_modules()
        print("Monkey patching done, executing the program")

    def _traverse(self, module, depth):
        """

        :param module:
        :param depth:
        :return:
        """
        if depth < 0:  # stop recursion
            return

        self.module_import(module)
        for elem in inspect.getmembers(module):
            if type(elem[1]).__name__ == "function":  # get global functions
                if elem[1].__qualname__ == 'f_monkey':
                    continue  # checks for already processed functions to prevent re-inspection
                functions_mod = inspect.getmodule(elem[1])
                self.module_import(functions_mod)
                tup = (elem[1], functions_mod.__name__)
                if '<' in tup[0].__name__ or '<' in tup[1]:
                    continue  # prevent inspecting invalid paths
                self._execute_monkey_patching(tup)
            # Need to exclude tup '__class__', since they are also of type 'class'
            elif type(elem[1]) == type.__class__ and elem[0] != "__class__":
                self._traverse(elem[1], depth-1)  # recursion to get nested classes
            elif type(elem[1]).__name__ == "module":
                print(f'found module elem[1].__name__')
                self._traverse(elem[1], depth-1)  # recursion to the module

    def _traverse_modules(self):
        """
        Traverses all the modules provided to constructor
        """
        for mod in self.modules_to_log:
            self._traverse(mod, self.recursion_depth)

    @staticmethod
    def module_import(mod):
        """
        Imports necessary submodules of given path
        :param mod: module to inspect. It will be imported globally from this scope
        """
        if type(mod).__name__ != "module":
            return

        # for module a.b.c it 1. `import c from a.b`, 2. `import b from a`, 3. `import a`
        mod_path = mod.__name__.split('.')
        while len(mod_path) > 1:
            command = f'global {mod_path[-1]}\nfrom {".".join(mod_path[:-1])} import {mod_path[-1]}'
            print(command)
            exec(command)
            mod_path.pop()
        command = f'global {mod_path[-1]}\nimport {mod_path[-1]}'
        print(command)
        exec(command)

    @staticmethod
    def _format_signature(signature, value=True):
        """

        :param signature:
        :param value:
        :return: signature in case the function is patchable, False else
        """
        res = '('
        comma = False  # solution for post fence problem

        param_count = 0
        for sig in signature.parameters:
            param_count += 1

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
                if '<' in default:  # skip invalid characters (e.g., np._NoValueType resolves to '<no value>'
                    continue

            print('signature attri: ' + signature.parameters[sig].name)
            print('signature value: ' + default)
            if comma:
                res += ', '
            if '**' in str(signature.parameters[sig]):
                res += '**'
            elif '*' in str(signature.parameters[sig]):
                res += '*'
            res += signature.parameters[sig].name
            if value and not empty:
                res += '=' + default
            comma = True

        if param_count != len(str(signature).split(',')):
            # example: https://matplotlib.org/3.1.0/_modules/matplotlib/pyplot.html#imshow
            # function is not patchable, invalid argument
            return ''

        res += ')'
        #print('resulting signature: ' + res)
        return res

    def _execute_monkey_patching(self, f):
        """

        :param f:
        :return:
        """
        s_name = f[1] + "." + f[0].__qualname__

        s_global = f"global f_original{self.patch_id}"
        s_original = f"f_original{self.patch_id}={s_name}"  # patch_id is needed to create for every function an individual name, otherwise it gets overwritten (point to same reference)

        s_signature = self._format_signature(inspect.signature(f[0]), value=False)
        s_signature_values = self._format_signature(inspect.signature(f[0]))
        s_signature_values = s_signature_values.replace('\n', '\\n')  # escape backslashes before execution

        if s_signature_values == '':
            return  # skip function with invalid signatures

        s_f_def = f"def f_monkey{s_signature_values}:"
        s_f_log = f"  print(f\"autolog fun called: {s_name}{s_signature_values}\")"
        s_f_call= f"  result = f_original{self.patch_id}{s_signature}"
        s_f_res = f"  print(result, type(result))"
        s_f_ret = f"  return result"

        s_replace = s_name + ' = f_monkey'

        s_execute = '\n'.join([s_global, s_original, s_f_def, s_f_log, s_f_call, s_f_res, s_f_ret, s_replace])
        print(s_execute)
        exec(s_execute)

        self.patch_id += 1
