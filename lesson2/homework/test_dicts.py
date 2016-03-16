import unittest
import json
import dicts

with open('lists.json') as data_file:
    data = json.load(data_file)


class TestMakeDicts(unittest.TestCase):

    def test_creates_dict(self):
        self.assertTrue(isinstance(dicts.make_dict(data), dict))

if __name__ == '__main__':
    unittest.main()
