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
        self.assertEqual(password_generator.get_entropy(1,{"low"}),4.70)
        self.assertEqual(password_generator.get_entropy(1,{"num"}),3.32)
        self.assertEqual(password_generator.get_entropy(2,{"low","num"}),9.02)
        self.assertEqual(password_generator.get_entropy(3,{"low","up","sym"}),16.99)
        self.assertEqual(password_generator.get_entropy(4,{"low","up","num","sym"}),22.31)
        self.assertEqual(password_generator.get_entropy(12,{"low","up","num","sym"}),78.14)
        self.assertEqual(password_generator.get_entropy(128,{"low","up","num","sym"}),838.99)

    def test_valid_password(self):
        self.assertFalse(password_generator.is_valid_password({"low"},"APC8796234$$"))
        self.assertFalse(password_generator.is_valid_password({"num"},"uiahsdIUHDSAUSDH!A£"))
        self.assertFalse(password_generator.is_valid_password({"sym","up"},"/&ç*(&)&ç*)lsdha54sdffs9287"))
        self.assertFalse(password_generator.is_valid_password({"sym","up","num"},"IUASHDIUH234729874"))                                 #test for unwanted character types
        self.assertFalse(password_generator.is_valid_password({"sym","up","num","low"},"aoisdjad9q83ueqnASD"))
        self.assertFalse(password_generator.is_valid_password({"sym","up","num"},"aoisdjad!(/&/&%ç*9q83ueqnASD"))
        self.assertTrue(password_generator.is_valid_password({"sym","up","num","low"},"aIUASHDIUH234729874!"))
    