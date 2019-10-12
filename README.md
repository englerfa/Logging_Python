# Logging_Python
This repository provides a method to log all method calls automatically. A log statement contains a timestamp, method name, argument names, types, and values, and return type and value.
We implement automated logging using monkey patching, which replaces existing functions at runtime adding logging statements to it. 


## Limitations:
* We do not log monkey functions to prevent re-inspection. With monkey functions we mean the functions that we introduced in this method.
* We do not log inner functions also called nested functions. Inner functions are functions defined within other functions. We show a simple example in Figure~\ref{fig:innerfunction}. The reason is that module \texttt{inspect} does not retrieve inner functions since they are invisible outside of its immediately enclosing function. However, if we want to log also inner functions, we show a possible approach to capture inner functions. module \texttt{inspect} offers a method \texttt{getsource()} to retrieve source code. With module \texttt{ast} we can traverse function definitions recursively and retrieve inner functions.
* Similar to the previous limitation, we do not log lambda functions since \texttt{inspect} does not retrieve them. If we want to retrieve lambda functions, we can also use method \texttt{getsource()} from module \texttt{inspect}.
* We skip methods that have a non-executable signature, e.g., that contain an invalid path. More formally, when an object's built-in method \texttt{repr()}, which should return an executable string of the object, returns something with an invalid syntax (e.g., string containing \texttt{<, >, ', ", /, \textbackslash}, ...), we want to skip it.
* We skip functions that contain the following strings in the signature \texttt{<locals>}, \texttt{\_get\_kwargs}, \texttt{\_\_repr\_\_}, and \texttt{argparse.\_ActionsContainer.\_get\_handler}.
