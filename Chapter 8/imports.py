# import module_name

import show_magicians_function

magicians = ['David', 'melo', 'james']
show_magicians_function.show_magicians(magicians)

# from module_name import function_name

from show_magicians_function import show_magicians

magicians = ['David', 'melo', 'james']
show_magicians(magicians)

# from module_name import function_name as fn

from show_magicians_function import show_magicians as sm

magicians = ['David', 'melo', 'james']
sm(magicians)

# import module_name as mn

import show_magicians_function as smf

magicians = ['David', 'melo', 'james']
smf.show_magicians(magicians)

# from module_name import *

from show_magicians_function import *

magicians = ['David', 'melo', 'james']
show_magicians(magicians)
