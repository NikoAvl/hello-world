import time
import os

colors = [
    "\033[1;31;40m", "\033[1;32;40m", "\033[1;33;40m", "\033[1;34;40m",
    "\033[1;35;40m", "\033[1;36;40m", "\033[1;37;40m",
    "\033[1;91;40m", "\033[1;92;40m", "\033[1;93;40m", "\033[1;94;40m",
    "\033[1;95;40m", "\033[1;96;40m", "\033[1;97;40m",
    "\033[1;101;97m", "\033[1;102;97m", "\033[1;103;97m", "\033[1;104;97m",
    "\033[1;105;97m", "\033[1;106;97m", "\033[1;107;97m"
]

for color in colors:
    os.system('cls')
    print(color +
           """
#   #        #  #          #   #   #          #     #  #
#   #        #  #          #  # #  #          #     #  #
#   #   ##   #  #   ##      # # # #   ##   ## #   ###  #
#####  #  #  #  #  #  #     # # # #  #  #  #  #  #  #  #
#   #  ####  #  #  #  #     # # # #  #  #  #  #  #  #  #
#   #  #     #  #  #  #     # # # #  #  #  #  #  #  #   
#   #   ###  #  #   ##       #   #    ##   #  #   ###  #

""" + "\033[0m")
    time.sleep(1) 
    
