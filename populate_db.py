import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ipswich_ecommerce.settings')
django.setup()

from products.models import Category, Product

# Create categories
categories_data = [
    {'name': 'Electronics', 'description': 'Electronic devices and gadgets'},
    {'name': 'Clothing', 'description': 'Fashion and apparel'},
    {'name': 'Books', 'description': 'Books and educational materials'},
    {'name': 'Home & Garden', 'description': 'Home decor and gardening supplies'},
]

print('Creating categories...')
for cat_data in categories_data:
    cat, created = Category.objects.get_or_create(
        name=cat_data['name'],
        defaults={'description': cat_data['description']}
    )
    if created:
        print(f'  ✓ Created: {cat.name}')
    else:
        print(f'  - Already exists: {cat.name}')

# Create products
electronics = Category.objects.get(name='Electronics')
clothing = Category.objects.get(name='Clothing')
books = Category.objects.get(name='Books')
home = Category.objects.get(name='Home & Garden')

products_data = [
    # Electronics
    {'name': 'Wireless Headphones', 'category': electronics, 'description': 'Premium noise-cancelling wireless headphones with 30-hour battery life', 'price': 199.99, 'stock': 50},
    {'name': 'Smartphone', 'category': electronics, 'description': 'Latest flagship smartphone with 5G connectivity and triple camera system', 'price': 899.99, 'stock': 30},
    {'name': 'Laptop', 'category': electronics, 'description': 'High-performance laptop for work and gaming with 16GB RAM', 'price': 1299.99, 'stock': 20},
    {'name': 'Smartwatch', 'category': electronics, 'description': 'Fitness tracking smartwatch with heart rate monitor', 'price': 249.99, 'stock': 45},
    
    # Clothing
    {'name': 'Classic T-Shirt', 'category': clothing, 'description': 'Comfortable cotton t-shirt in various colors', 'price': 24.99, 'stock': 100},
    {'name': 'Jeans', 'category': clothing, 'description': 'Premium denim jeans with perfect fit', 'price': 79.99, 'stock': 75},
    {'name': 'Winter Jacket', 'category': clothing, 'description': 'Warm and stylish winter jacket for cold weather', 'price': 149.99, 'stock': 40},
    {'name': 'Running Shoes', 'category': clothing, 'description': 'Lightweight running shoes with excellent cushioning', 'price': 119.99, 'stock': 60},
    
    # Books
    {'name': 'Python Programming', 'category': books, 'description': 'Comprehensive guide to Python programming for beginners', 'price': 39.99, 'stock': 80},
    {'name': 'DevOps Handbook', 'category': books, 'description': 'Master DevOps practices and CI/CD pipelines', 'price': 44.99, 'stock': 65},
    {'name': 'Web Development', 'category': books, 'description': 'Learn modern web development with Django and React', 'price': 49.99, 'stock': 55},
    {'name': 'Data Science', 'category': books, 'description': 'Introduction to data science and machine learning', 'price': 54.99, 'stock': 50},
    
    # Home & Garden
    {'name': 'Coffee Maker', 'category': home, 'description': 'Automatic coffee maker with programmable timer', 'price': 89.99, 'stock': 35},
    {'name': 'Indoor Plant Set', 'category': home, 'description': 'Set of 3 easy-care indoor plants with pots', 'price': 34.99, 'stock': 70},
    {'name': 'LED Desk Lamp', 'category': home, 'description': 'Adjustable LED desk lamp with USB charging port', 'price': 29.99, 'stock': 90},
    {'name': 'Garden Tools Set', 'category': home, 'description': 'Complete set of essential gardening tools', 'price': 64.99, 'stock': 45},
]

print('\nCreating products...')
for prod_data in products_data:
    prod, created = Product.objects.get_or_create(
        name=prod_data['name'],
        defaults=prod_data
    )
    if created:
        print(f'  ✓ Created: {prod.name} - ${prod.price}')
    else:
        print(f'  - Already exists: {prod.name}')

print(f'\n✅ Database populated successfully!')
print(f'Total categories: {Category.objects.count()}')
print(f'Total products: {Product.objects.count()}')
