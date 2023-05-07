"""Basic unit test functionality for guygen"""

import unittest
import cmd

class testCmd(unittest.TestCase):
    """Test cmd.py"""
    def test_alt_names(self):
        """Test if the alternative name key is not in cmds, and test if the value is in
           cmds"""
        for alt_name in cmd.cmd_alt_names:
            self.assertNotIn(alt_name, cmd.cmds)

        for alt_val in cmd.cmd_alt_names.values():
            self.assertIn(alt_val, cmd.cmds)

if __name__ == "__main__":
    unittest.main()
