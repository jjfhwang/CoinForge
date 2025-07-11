# test_coinforge.py
"""
Tests for CoinForge module.
"""

import unittest
from coinforge import CoinForge

class TestCoinForge(unittest.TestCase):
    """Test cases for CoinForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CoinForge()
        self.assertIsInstance(instance, CoinForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CoinForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
