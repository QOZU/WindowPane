# test_windowpane.py
"""
Tests for WindowPane module.
"""

import unittest
from windowpane import WindowPane

class TestWindowPane(unittest.TestCase):
    """Test cases for WindowPane class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WindowPane()
        self.assertIsInstance(instance, WindowPane)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WindowPane()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
