import unittest
import mission_control as mc

# Test case class for Astronauts' Space Mission
class TestMissionControl(unittest.TestCase):
    def setUp(self):
        # Test fixture: Initial setup for mission plan
        self.mission_plan = []

    def tearDown(self):
        # Test fixture cleanup
        self.mission_plan = None

    def test_calculate_gravity(self):
        # Test known planet
        result = mc.calculate_gravity("Earth")
        self.assertEqual(result, 9.8)

        # Test unknown planet
        result = mc.calculate_gravity("Pluto")
        self.assertEqual(result, "Unknown planet")

    def test_check_astronaut_health(self):
        # Test valid health score
        result = mc.check_astronaut_health(70)
        self.assertEqual(result, "Astronaut is fit for the mission")

        # Test low health score
        result = mc.check_astronaut_health(40)
        self.assertEqual(result, "Astronaut not fit for the mission")
    
        # Test invalid health score
        result = mc.check_astronaut_health(-10)
        self.assertEqual(result, "Invalid health score")

    def test_add_planet_to_mission(self):
        # Test adding a new planet
        mission_plan = mc.add_planet_to_mission("Mars", self.mission_plan)
        self.assertIn("Mars", mission_plan)
    
        # Test adding a duplicate planet (now fixed)
        with self.assertWarns(UserWarning):
            mission_plan = mc.add_planet_to_mission("Mars", self.mission_plan)
        self.assertEqual(len(mission_plan), 1)

    @unittest.skip("Skipping this test as we need more research on Jupiter!") 
    def test_add_jupiter_planet(self): 
        # Test for adding Jupiter (which is still being considered for the mission) 
        mission_plan = mc.add_planet_to_mission("Jupiter", self.mission_plan) 
        self.assertIn("Jupiter", mission_plan)

if __name__ == "__main__":
    unittest.main()
