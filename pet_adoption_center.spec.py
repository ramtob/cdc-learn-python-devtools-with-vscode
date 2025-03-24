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
    
    def test_adoption_fee_young_pet(self):
        result = pac.calculate_adoption_fee(1)  # Young pet
        self.assertEqual(result, 100)

    def test_adoption_fee_adult_pet(self):
        result = pac.calculate_adoption_fee(5)  # Adult pet
        self.assertEqual(result, 50)

    def test_adoption_fee_illegal_age(self):
        with self.assertRaises(ValueError):
            pac.calculate_adoption_fee(-1)  # Negative age
    
    def test_register_new_pet(self):
        new_pet = {"name": "Buddy", "type": "Dog", "size": "Medium", "age": "Young"}
        adoption_list = []
        result = pac.register_new_pet(new_pet, adoption_list)
        self.assertEqual(result, [new_pet])
    
    def test_register_existing_pet(self):
        new_pet = {"name": "Buddy", "type": "Dog", "size": "Medium", "age": "Young"}
        adoption_list = [new_pet]
        with self.assertWarns(UserWarning):
            result = pac.register_new_pet(new_pet, adoption_list)
            self.assertEqual(result, [new_pet])
    

if __name__ == "__main__":
    unittest.main()
