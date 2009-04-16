#!/usr/bin/env python
"""
Automatically load modules and run tests in those modules.
test.py mypackage.test yourpackage.test
test.py mypackage.test.TestXYZ.testRun
"""

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
