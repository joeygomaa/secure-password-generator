import password_generator
import unittest

class TestPasswordGenerator(unittest.TestCase):

    def test_pool_size(self):
        
        self.assertEqual(password_generator.get_pool_size(["low"]),26)
        self.assertEqual(password_generator.get_pool_size(["num"]),10)
        self.assertEqual(password_generator.get_pool_size(["low","num"]),36)
        self.assertEqual(password_generator.get_pool_size(["low","num","sym","up"]),94)

    
    def test_validate_length(self):
        self.assertFalse(password_generator.validate_length("n"))
        self.assertFalse(password_generator.validate_length("0"))
        self.assertFalse(password_generator.validate_length("129"))
        self.assertFalse(password_generator.validate_length(None))
        self.assertTrue(password_generator.validate_length("5"))
    
    
    def test_validate_amount(self):
        self.assertFalse(password_generator.validate_amount("n"))
        self.assertFalse(password_generator.validate_amount("0"))
        self.assertFalse(password_generator.validate_amount("101"))
        self.assertFalse(password_generator.validate_amount(None))
        self.assertTrue(password_generator.validate_amount("5"))


    def test_validate_selection(self):
        self.assertFalse(password_generator.validate_selection(["banana"]))
        self.assertFalse(password_generator.validate_selection("apple"))
        self.assertFalse(password_generator.validate_selection(None))
        self.assertFalse(password_generator.validate_selection("low"))
        self.assertTrue(password_generator.validate_selection(["low"]))
        self.assertTrue(password_generator.validate_selection(["low","num"]))
        self.assertTrue(password_generator.validate_selection(["low","num","up","sym"]))


    def test_entropy(self):
        self.assertAlmostEqual(password_generator.get_entropy(1,{"low"}),4.70,places=2)
        self.assertAlmostEqual(password_generator.get_entropy(1,{"num"}),3.32,places=2)
        self.assertAlmostEqual(password_generator.get_entropy(2,{"low","num"}),9.02,places=2)
        self.assertAlmostEqual(password_generator.get_entropy(3,{"low","up","sym"}),16.99,places=2)
        self.assertAlmostEqual(password_generator.get_entropy(4,{"low","up","num","sym"}),22.31,places=2)
        self.assertAlmostEqual(password_generator.get_entropy(12,{"low","up","num","sym"}),78.14,places=2)
        self.assertAlmostEqual(password_generator.get_entropy(128,{"low","up","num","sym"}),838.99,places=2)

    def test_valid_password(self):
        self.assertTrue(password_generator.is_valid_password({"low"}, "abc"))
        self.assertFalse(password_generator.is_valid_password({"low"}, "abc1"))
        self.assertTrue(password_generator.is_valid_password({"low", "num"}, "abc123"))
        self.assertFalse(password_generator.is_valid_password({"low", "num"}, "abcdef"))
        self.assertFalse(password_generator.is_valid_password({"low", "num"}, "abc123!"))
        self.assertTrue(password_generator.is_valid_password({"low", "up", "num", "sym"},"aA1!"))

    def test_generate(self):
        passwords = password_generator.generate_passwords(10, 12, {"low","num","sym"})
        self.assertTrue(len(passwords) == 10)
        for password in passwords:
            self.assertTrue(len(password) == 12)
            self.assertTrue(password_generator.is_valid_password({"low","num","sym"},password))
    