import unittest
import os
import pandas as pd
from utils.load import save_to_csv

class TestLoad(unittest.TestCase):
    def test_save_to_csv_creates_file(self):
        # Buat DataFrame dummy
        df = pd.DataFrame({
            "Title": ["Jacket A"],
            "Price": [160000],
            "Rating": [4.5],
            "Colors": [3],
            "Size": ["M"],
            "Gender": ["Unisex"]
        })

        filename = "test_output.csv"

        # Panggil fungsi
        save_to_csv(df, filename)

        # Cek apakah file dibuat
        self.assertTrue(os.path.exists(filename))

        # Baca ulang file dan cek isinya
        loaded_df = pd.read_csv(filename)
        self.assertEqual(loaded_df.shape[0], 1)
        self.assertEqual(loaded_df.iloc[0]["Title"], "Jacket A")

        # Hapus file setelah test
        os.remove(filename)

if __name__ == "__main__":
    unittest.main()