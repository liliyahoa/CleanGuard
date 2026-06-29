# test_cleanguard.py
"""
Tests for CleanGuard module.
"""

import unittest
from cleanguard import CleanGuard

class TestCleanGuard(unittest.TestCase):
    """Test cases for CleanGuard class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CleanGuard()
        self.assertIsInstance(instance, CleanGuard)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CleanGuard()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
