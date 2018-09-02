import colored
from colored import fg, bg, attr, stylize

bad = bg('dark_red_1')  + colored.attr("bold")
meh = bg('green_yellow') + fg("black") + colored.attr("bold")
good = bg('green_4') + fg("white") + colored.attr("bold")
