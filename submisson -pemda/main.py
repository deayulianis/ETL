from utils.extract import extract_data
from utils.transform import transform_data
from utils.load import save_to_csv

def main():
    print("📦 Extracting data...")
    raw_data = extract_data()

    print("🧼 Transforming data...")
    clean_data = transform_data(raw_data)

    print("💾 Saving to CSV...")
    save_to_csv(clean_data, "products.csv")
    print("✅ ETL pipeline completed!")

if __name__ == "__main__":
    main()