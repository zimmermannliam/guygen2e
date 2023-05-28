"""Basic unit test functionality for guygen"""

import unittest


import cmd
import char
from state import State

class testCmd(unittest.TestCase):
    """Test cmd.py"""


    def test_alt_names(self):
        """Test if the alternative name key is not in cmds, and test if the value is in
           cmds"""
        for alt_name in cmd.cmd_alt_names:
            self.assertNotIn(alt_name, cmd.cmds)

        for alt_val in cmd.cmd_alt_names.values():
            self.assertIn(alt_val, cmd.cmds)


class testChar(unittest.TestCase):
    """ Test char.py """

    
    def setUp(self):
        """ Set up the state """
        self.state = State([])

    
    def test_random_char(self):
        """ Sniff-tests the random character generator """
        self.assertEqual(self.state.cid, 0)
        cmd.mon_newcharacter(["nc", "100"], self.state)
        self.assertEqual(self.state.cid, 100)
        for char in self.state.chars:
            for stat in char.stats:
                self.assertGreaterEqual(stat, 3)
                self.assertLessEqual(stat, 18)




if __name__ == "__main__":
    unittest.main()
