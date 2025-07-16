import unittest
from utils.transform import transform_data

class TestTransform(unittest.TestCase):
    def test_transform_data_cleaning(self):
        raw_data = [
            {
                "Title": "Nice Jacket",
                "Price": "$10.0",
                "Rating": "4.5 / 5",
                "Colors": "3 Colors",
                "Size": "Size: M",
                "Gender": "Gender: Unisex"
            },
            {
                "Title": "Unknown Product",
                "Price": "Price Unavailable",
                "Rating": "Invalid Rating / 5",
                "Colors": "3 Colors",
                "Size": "Size: XL",
                "Gender": "Gender: Male"
            }
        ]

        df = transform_data(raw_data)

        # Hanya 1 data yang valid, pastikan hasilnya hanya 1 baris
        self.assertEqual(len(df), 1)

        # Periksa tipe data dan hasil transformasi
        self.assertEqual(df.iloc[0]["Title"], "Nice Jacket")
        self.assertEqual(df.iloc[0]["Price"], 160000.0)  # 10.0 * 16000
        self.assertEqual(df.iloc[0]["Rating"], 4.5)
        self.assertEqual(df.iloc[0]["Colors"], 3)
        self.assertEqual(df.iloc[0]["Size"], "M")
        self.assertEqual(df.iloc[0]["Gender"], "Unisex")

if __name__ == "__main__":
    unittest.main()