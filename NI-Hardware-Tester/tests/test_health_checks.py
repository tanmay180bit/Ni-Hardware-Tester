 import unittest
import health_checks

class TestHealthChecks(unittest.TestCase):

    def test_check_ni_hardware(self):
        """Test if NI hardware detection runs without error."""
        result = health_checks.check_ni_hardware()
        self.assertIsInstance(result, bool)

    def test_check_voltage(self):
        """Test voltage function (device name should exist for this to pass)."""
        result = health_checks.check_voltage("Dev1")
        self.assertTrue(result is None or isinstance(result, float))

if __name__ == "__main__":
    unittest.main()

