import unittest
import magic_store as ms

class TestMagicStore(unittest.TestCase):
    def test_cart_length(self):
        ms.cart = ["Magic Wand", "Flying Broom", "Invisibility Cloak"]
        assert len(ms.cart) == 3, "AssertionError: The cart should contain exactly 3 magic items!"