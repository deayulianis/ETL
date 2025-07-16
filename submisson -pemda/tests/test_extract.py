import unittest
from utils.extract import extract_data

class TestExtract(unittest.TestCase):
    def test_extract_data_returns_list_of_dict(self):
        data = extract_data()
        
        # Pastikan hasilnya adalah list
        self.assertIsInstance(data, list)
        
        # Pastikan list tidak kosong
        self.assertGreater(len(data), 0)
        
        # Pastikan elemen dalam list adalah dictionary
        self.assertIsInstance(data[0], dict)
        
        # Pastikan semua key ada
        expected_keys = {"Title", "Price", "Rating", "Colors", "Size", "Gender"}
        self.assertTrue(expected_keys.issubset(data[0].keys()))

if __name__ == '__main__':
    unittest.main()