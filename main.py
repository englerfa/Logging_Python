import basic
import basic2
import nested
import inheritance
import complex_types
import libuse

from autolog import Autolog

autolog = Autolog([basic, basic2, nested, inheritance, complex_types, libuse])
autolog.run()  # by running this function, logging is activated

complex_types.run()
libuse.run()
basic.run()
basic2.run()
nested.run()
inheritance.run()