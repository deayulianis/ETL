import requests
from bs4 import BeautifulSoup

def extract_data():
    data = []
    try:
        for page in range(1, 51):
            if page == 1:
                url = "https://fashion-studio.dicoding.dev"
            else:
                url = f"https://fashion-studio.dicoding.dev/page{page}"

            print(f"Scraping: {url}")
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            products = soup.select("div.product-details")
            print(f"Found {len(products)} products on page {page}")

            for product in products:
                try:
                    title_tag = product.select_one(".product-title")
                    title = title_tag.text.strip() if title_tag else "N/A"

                    price_tag = product.select_one(".price")
                    price = price_tag.text.strip() if price_tag else "N/A"

                    rating_tag = product.find(string=lambda t: "Rating" in t)
                    rating = rating_tag.strip().split("Rating:")[-1].strip() if rating_tag else "N/A"

                    colors_tag = product.find(string=lambda t: "Colors" in t)
                    colors = colors_tag.strip().split("Colors")[0].strip() if colors_tag else "N/A"

                    size_tag = product.find(string=lambda t: "Size" in t)
                    size = size_tag.strip().split("Size:")[-1].strip() if size_tag else "N/A"

                    gender_tag = product.find(string=lambda t: "Gender" in t)
                    gender = gender_tag.strip().split("Gender:")[-1].strip() if gender_tag else "N/A"

                    # Tambahkan data ke list
                    data.append({
                        "Title": title,
                        "Price": price,
                        "Rating": rating,
                        "Colors": colors,
                        "Size": size,
                        "Gender": gender
                    })

                except Exception as e:
                    print("Error while extracting a product:", e)
                    continue  # skip product jika error

        return data

    except Exception as e:
        print("Error while extracting:", e)
        return []
