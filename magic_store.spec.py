import unittest
import magic_store as ms

class TestMagicStore(unittest.TestCase):
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