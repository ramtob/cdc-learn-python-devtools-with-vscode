import unittest
import pet_adoption_center as pac

class TestPetAdoptionCenter(unittest.TestCase):
    def test_matching_pets(self):
        adopter_preferences = {"type": "Dog", "size": "Medium", "age": "Young"}
        pets = [
            {"name": "Buddy", "type": "Dog", "size": "Medium", "age": "Young"},
            {"name": "Max", "type": "Dog", "size": "Large", "age": "Adult"},
            {"name": "Lucy", "type": "Cat", "size": "Small", "age": "Young"}
        ]
        result = pac.match_pet(adopter_preferences, pets)
        self.assertEqual(result, "Buddy")
    
    def test_no_matching_pets(self):
        adopter_preferences = {"type": "Dog", "size": "Small", "age": "Adult"}
        pets = [
            {"name": "Buddy", "type": "Dog", "size": "Medium", "age": "Young"},
            {"name": "Max", "type": "Dog", "size": "Large", "age": "Adult"},
            {"name": "Lucy", "type": "Cat", "size": "Small", "age": "Young"}
        ]
        result = pac.match_pet(adopter_preferences, pets)
        self.assertEqual(result, "No match found")

if __name__ == "__main__":
    unittest.main()
