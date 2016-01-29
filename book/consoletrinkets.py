#!/usr/bin/python
from __future__ import print_function
import re
import sys
import os

"""Wraps trinket javascript around all `~~~~ {.python trinket}` blocks via stdin/stdout"""

in_trinket = False

while True:
    try:
        line = raw_input()
    except:
        break
    
    x = re.findall(r'~~~~ {(.*)}', line)
    
    add_trinket = False
    
    if len(x):
        add_trinket = (".python" in x[0]) and ("trinket" in x[0])
    
    if add_trinket:
        # Add trinket javascript with open HTML comment
        with open('trinket/trinket-script') as ts:
            print(ts.read())
        in_trinket = True
        continue
    elif in_trinket and (line.strip() == r"~~~~"):
        # End HTML comment
        print('-->')
        in_trinket = False
        continue
    else:
        print(line)
        continue