# test_futurepulse.py
"""
Tests for FuturePulse module.
"""

import unittest
from futurepulse import FuturePulse

class TestFuturePulse(unittest.TestCase):
    """Test cases for FuturePulse class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FuturePulse()
        self.assertIsInstance(instance, FuturePulse)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FuturePulse()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
