import unittest
import warnings

# Function to match a pet with an adopter based on preferences
def match_pet(adopter_preferences, pets):
    for pet in pets:
        if (adopter_preferences["type"] == pet["type"] or 
            adopter_preferences["size"] == pet["size"] or 
            adopter_preferences["age"] == pet["age"]):
            return pet["name"]
    return "No match found"

# Function to calculate adoption fee based on the pet's age
def calculate_adoption_fee(pet_age):
    if pet_age < 2:
        return 100  # Younger pets have higher fees
    return 50  # Adult pets have lower fees

# Function to add a new pet to the adoption list
def register_new_pet(new_pet, adoption_list):
    if any(existing_pet["type"] == new_pet["name"] for existing_pet in adoption_list):
        warnings.warn(f"{new_pet['name']} is already in the adoption list", UserWarning)
    else:
        adoption_list.append(new_pet)
    return adoption_list

class TestPetAdoptionCenter(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()
