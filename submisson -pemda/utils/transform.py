import pandas as pd

dirty_patterns = {
    "title": ["Unknown Product"],
    "Rating": ["Invalid Rating / 5", "Not Rated"],
    "Price": ["Price Unavailable", None]
}

def clean_text(text, prefix=""):
    return text.replace(prefix, "").strip()

def transform_data(raw_data):
    df = pd.DataFrame(raw_data)

    # Debug: lihat kolom yang tersedia
    print("Kolom tersedia:", df.columns.tolist())

    # Remove dirty data, hanya jika kolomnya ada
    for col, patterns in dirty_patterns.items():
        if col in df.columns:
            for pattern in patterns:
                df = df[df[col] != pattern]

    # Clean and convert columns (hanya jika kolomnya ada)
    if "Price" in df.columns:
        df["Price"] = df["Price"].str.replace("$", "").astype(float) * 16000

    if "Rating" in df.columns:
        df["Rating"] = df["Rating"].str.extract(r"(\d+\.?\d*)").astype(float)

    if "Colors" in df.columns:
        df["Colors"] = df["Colors"].str.extract(r"(\d+)").astype(int)

    if "Size" in df.columns:
        df["Size"] = df["Size"].apply(lambda x: clean_text(x, "Size: "))

    if "Gender" in df.columns:
        df["Gender"] = df["Gender"].apply(lambda x: clean_text(x, "Gender: "))

    # Remove duplicates and nulls
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    return df