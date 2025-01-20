import pandas as pd

# Define the modified dataset
data = {
    'user_id': [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4,
                5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8,
                9, 9, 9, 9, 9, 10, 10, 10, 10, 10],
    'product_id': [1, 3, 5, 8, 10, 2, 4, 6, 9, 7, 1, 3, 5, 8, 2, 2, 4, 6, 5, 1,
                   3, 8, 4, 2, 7, 1, 9, 5, 3, 10, 2, 3, 4, 9, 6, 6, 5, 10, 1, 3,
                   1, 7, 10, 5, 8, 2, 4, 6, 5, 9],
    'product_name': ['Laptop', 'Smartphone', 'Tablet', 'Camera', 'Speakers', 'Headphones', 'Keyboard', 'Monitor', 'Printer', 'Smartwatch',
                     'Laptop', 'Smartphone', 'Tablet', 'Camera', 'Headphones', 'Headphones', 'Keyboard', 'Monitor', 'Tablet', 'Laptop',
                     'Smartphone', 'Camera', 'Keyboard', 'Headphones', 'Smartwatch', 'Laptop', 'Printer', 'Tablet', 'Smartphone', 'Speakers',
                     'Headphones', 'Smartphone', 'Keyboard', 'Printer', 'Monitor', 'Monitor', 'Tablet', 'Speakers', 'Laptop', 'Smartphone',
                     'Laptop', 'Smartwatch', 'Speakers', 'Tablet', 'Camera', 'Headphones', 'Keyboard', 'Monitor', 'Tablet', 'Printer'],
    'category': ['Electronics'] * 50,
    'brand': ['BrandA', 'BrandA', 'BrandA', 'BrandE', 'BrandG', 'BrandB', 'BrandC', 'BrandB', 'BrandF', 'BrandD',
              'BrandA', 'BrandA', 'BrandA', 'BrandE', 'BrandB', 'BrandB', 'BrandC', 'BrandB', 'BrandA', 'BrandA',
              'BrandA', 'BrandE', 'BrandC', 'BrandB', 'BrandD', 'BrandA', 'BrandF', 'BrandA', 'BrandA', 'BrandG',
              'BrandB', 'BrandA', 'BrandC', 'BrandF', 'BrandB', 'BrandB', 'BrandA', 'BrandG', 'BrandA', 'BrandA',
              'BrandA', 'BrandD', 'BrandG', 'BrandA', 'BrandE', 'BrandB', 'BrandC', 'BrandB', 'BrandA', 'BrandF'],
    'price': [1000, 600, 400, 800, 200, 150, 100, 300, 350, 200, 1000, 600, 400, 800, 150, 150, 100, 300, 400, 1000,
              600, 800, 100, 150, 200, 1000, 350, 400, 600, 200, 150, 600, 100, 350, 300, 300, 400, 200, 1000, 600,
              1000, 200, 200, 400, 800, 150, 100, 300, 400, 350]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Save to CSV
file_name = "customer_browsing_history_with_products.csv"
df.to_csv(file_name, index=False)

print(f"Dataset saved to '{file_name}'.")
