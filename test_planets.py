import unittest
from main import load_planets

class TestPlanets(unittest.TestCase):

    def setUp(self):
        # Load all planets once before each test
        self.planets = load_planets()

    # --- Basic checks ---

    def test_planet_count(self):
        # Should be 8 planets
        self.assertEqual(len(self.planets), 8)

    def test_earth_exists(self):
        # Earth should be present
        self.assertIn("earth", self.planets)

    # --- Moon tests ---

    def test_earth_moons(self):
        earth = self.planets["earth"]
        self.assertEqual(len(earth.moons), 1)

    def test_mars_moons(self):
        mars = self.planets["mars"]
        self.assertEqual(len(mars.moons), 2)

    # --- Value checks ---

    def test_jupiter_mass(self):
        jupiter = self.planets["jupiter"]
        self.assertEqual(jupiter.mass, 1.90e27)

    def test_saturn_distance(self):
        saturn = self.planets["saturn"]
        self.assertEqual(saturn.distance, 1433000000)

    # --- Method test ---

    def test_info_returns_string(self):
        earth = self.planets["earth"]
        result = earth.info()
        self.assertIsInstance(result, str)

if __name__ == "__main__":
    unittest.main()
    