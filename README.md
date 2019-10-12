# Logging_Python
This repository provides a method to log all method calls automatically. A log statement contains a timestamp, method name, argument names, types, and values, and return type and value.
We implement automated logging using monkey patching, which replaces existing functions at runtime adding logging statements to it. 


## Limitations
* We do not log monkey functions to prevent re-inspection.
* We do not log inner functions, also called nested functions since module `inspect` does not retrieve them.
* We do not log lambda functions since since module `inspect` does not retrieve them.
* We skip methods that have a non-executable signature, e.g., that contain an invalid path. More formally, when an object's built-in method `repr()`, which should return an executable string of the object, returns something with an invalid syntax (e.g., string containing `<, >, ', ", /, \`, ...), we want to skip it.
* We skip functions that contain the following strings in the signature `<locals>`, `_get_kwargs`, `_\repr__`, and `argparse._ActionsContainer._get_handler`.
