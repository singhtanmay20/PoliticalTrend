#!/usr/bin/env python

"""mapper.py"""

import sys
mywords = ["music","movie","entertainment","dance","book","television","love","time","show","like"]
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for i in range(len(words)-1):
        if(words[i] in mywords or words[i+1] in mywords):
	    l=" "
            print('%s%s%s\t%s' % (words[i],l,words[i+1],1))
