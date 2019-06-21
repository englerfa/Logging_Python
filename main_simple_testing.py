import main_simple
import logging

modules_to_log = [main_simple]

logging.add_module(main_simple)
logging.traverse_modules(modules_to_log)
logging.execute_monkey_patching()


main_simple.print_text()









