# test_stateforge.py
"""
Tests for StateForge module.
"""

import unittest
from stateforge import StateForge

class TestStateForge(unittest.TestCase):
    """Test cases for StateForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = StateForge()
        self.assertIsInstance(instance, StateForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = StateForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
