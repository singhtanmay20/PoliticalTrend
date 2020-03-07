#!/usr/bin/env python

"""mapper.py"""

import sys
mywords = ["read","show","best","movie","film","time","viewer","director","like","tv"]
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for i in range(len(words)-1):
        if(words[i] in mywords or words[i+1] in mywords):
	    l=" "
            print('%s%s%s\t%s' % (words[i],l,words[i+1],1))
