from sidequest01_1 import *
from runes import *

clear_all()
show(anaglyph(repeat_pattern(2,lambda p: egyptian(p,10),rcross_bb)))

show((lambda p: egyptian(p,5))(rcross_bb))
