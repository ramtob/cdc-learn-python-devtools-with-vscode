import unittest
import magic_store as ms

class TestMagicStore(unittest.TestCase):
    def setUp(self):
        self.cart = []  # Empty cart at the start of each test

    def tearDown(self):
        self.cart = None  # Ensure the cart is cleared

    # Test case for adding items to the cart
    def test_cart_length(self):
        cart = ["Magic Wand", "Flying Broom", "Invisibility Cloak"]
        assert len(cart) == 3, "AssertionError: The cart should contain exactly 3 magic items!"

    # Test case for checkout with items in the cart
    def test_checkout(self):
        cart = ["Magic Wand", "Flying Broom", "Invisibility Cloak"]
        result = ms.checkout(cart)
        self.assertEqual(result, "Checking out with 3 items!")  # Testing checkout with items in the cart

    # Test case for checkout with an empty cart
    def test_checkout_empty(self):
        cart = []
        result = ms.checkout(cart)
        self.assertEqual(result, "Your cart is empty! Add some magic items first!")  # Testing checkout with an empty cart

    # Test for warning when adding a duplicate item
    def test_add_to_cart_warning(self):
        cart = []
        with self.assertWarns(UserWarning):
            ms.add_to_cart("Magic Wand", cart)  # First time adding the item
            ms.add_to_cart("Magic Wand", cart)  # Trying to add the same item again
    
    @unittest.skip("This test is skipped because the discount feature is under development.")  
    def test_discount_feature(self):  
        # Placeholder test for the future discount system  
        cart = ["Magic Wand", "Flying Broom"]  
        self.assertEqual(len(cart), 2)  # Dummy assertion for now 
    
    @unittest.skipIf(sys.platform == "win32", "Hologram checkout is not compatible with Windows.") 
    def test_hologram_checkout(self): 
        pass # placeholder to implement the hologram logic

# Run the tests 
if __name__ == '__main__': 
    unittest.main() 
