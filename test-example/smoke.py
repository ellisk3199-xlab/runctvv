import unittest
# Welcome skyline1
def get_greeting():
    return "Welcome back Bob!"


#index1
class TestGreeting(unittest.TestCase):
    def test_get_greeting_returns_correct_string(self):
        self.assertEqual(get_greeting(), "Welcome back Bob!")

def add_numbers(a: int, b: int):
    return a + b
    
#continue
class TestAddNumbers(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(3, 0), 3)

# The test function using standard assert statements
def test_add_numbers():
    # Test positive numbers
    assert add_numbers(3, 0) == 3

def reverse_string(text: str):
    return text[::-1].upper()

# The unit test using assert atomation
def test_reverse_string():
    # Test a standard lowercase string
    assert reverse_string("security") == "ytiruces"
    
    # Test case strings
    assert reverse_string("fun23") == "32nuf"
    
    # Test an empty string edge case
    assert reverse_string("") == ""
    
    # Test strings with spaces
    assert reverse_string("a b c") == "c b a"

if __name__ == "__main__":
    unittest.main()
    
