#!/usr/bin/env python3
import sys
import re
if len(sys.argv) < 3 :
    print("none")
else:
    word = sys.argv[1]
    sentence = sys.argv[2]

    matches = re.findall(re.escape(word), sentence)

    if len(matches) == 0:
            print("none")
    else:
         print(len(matches))
         
