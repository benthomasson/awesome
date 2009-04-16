#!/usr/bin/env python

import unittest
import sys

for module in sys.argv[1:]:
    done = False
    while not done and module != "": 
        try:
            exec('import ' + module)
            done = True
        except Exception:
            module = module.rpartition('.')[0]
        
if __name__ == '__main__':
    unittest.main()
