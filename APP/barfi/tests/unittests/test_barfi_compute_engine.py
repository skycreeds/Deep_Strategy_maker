import sys
sys.path.append('../../')
from APP.barfi.barfi1.berfi import Block
import unittest

# TODO
# Make a feed with one output and result with one input and a process block with 2 inputs
# 2 outputs and all the options and a compute function that uses all the options, inputs 
# and sets the outputs. Test the result from this. 

class TestBarfiBlock(unittest.TestCase):

    def setUp(self):
        pass

    def test_compute_engine(self):
        pass

        
if __name__ == '__main__':
    unittest.main()
