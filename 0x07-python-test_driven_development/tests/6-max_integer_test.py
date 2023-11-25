import unittest
"""unittests of the function max_integer"""
max_integer = __import__('6-max_integer').max_integer
class Testing(unittest.TestCase):
    """tests function max-integer using unittests"""
    def test_random_list(self):
        my_list = [10,25,30,100,3000,20,55]
        self.assertEqual(max_integer(my_list),3000)
    
    def test_ordered_list(self):
        list_ordered = [1,10,90,100,1000]
        self.assertEqual(max_integer(list_ordered),1000)
    
    def test_empty(self):
        empty_list = []
        self.assertEqual(max_integer(empty_list),None)
    
    def test_only_one(self):
        empty_list = [10]
        self.assertEqual(max_integer(empty_list),10)
    
    def test_floats(self):
        floats = [203.2, -35.6, 10.2, 5.0, 603.1]
        self.assertEqual(max_integer(floats), 603.1)

    def test_multiple_types(self):
        list_floats = [120, -99.9, 100.12, -100, 10.25]
        self.assertEqual(max_integer(list_floats), 120)
    
    def test_first_max(self):
        list_floats = [450,50,20,5,1]
        self.assertEqual(max_integer(list_floats), 450)

    def test_string(self):
        string = "ilyas"
        self.assertEqual(max_integer(string), 'y')

    def test_list(self):
        list_strings = ["morocco", "software", "alx", "ilyas"]
        self.assertEqual(max_integer(list_strings), "software")
    
    def test_empty_string(self):
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
