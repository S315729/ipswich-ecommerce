"""
Management command to populate products with proper images
"""
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from products.models import Category, Product
import urllib.request
import io
from PIL import Image


class Command(BaseCommand):
    help = 'Populates database with sample products and images'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting product population...'))
        
        # Clear existing data
        Product.objects.all().delete()
        Category.objects.all().delete()
        
        # Create categories
        categories_data = {
            'Electronics': 'Latest electronic devices and gadgets',
            'Clothing': 'Fashion and apparel for everyone',
            'Books': 'Books for all interests and ages',
            'Home & Garden': 'Items for your home and garden',
        }
        
        categories = {}
        for name, desc in categories_data.items():
            category = Category.objects.create(name=name, description=desc)
            categories[name] = category
            self.stdout.write(self.style.SUCCESS(f'Created category: {name}'))
        
        # Products with proper placeholder images
        products_data = [
            # Electronics
            {
                'name': 'Wireless Headphones',
                'category': 'Electronics',
                'description': 'Premium noise-cancelling wireless headphones with 30-hour battery life and crystal-clear sound quality.',
                'price': 199.99,
                'stock': 50,
                'image_url': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500&h=500&fit=crop',
            },
            {
                'name': 'Smart Watch',
                'category': 'Electronics',
                'description': 'Feature-rich smartwatch with fitness tracking, heart rate monitor, and smartphone notifications.',
                'price': 299.99,
                'stock': 35,
                'image_url': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500&h=500&fit=crop',
            },
            {
                'name': 'Laptop Stand',
                'category': 'Electronics',
                'description': 'Ergonomic aluminum laptop stand with adjustable height and angle for better posture.',
                'price': 49.99,
                'stock': 100,
                'image_url': 'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500&h=500&fit=crop',
            },
            {
                'name': 'USB-C Hub',
                'category': 'Electronics',
                'description': '7-in-1 USB-C hub with HDMI, USB 3.0, SD card reader, and charging port.',
                'price': 39.99,
                'stock': 75,
                'image_url': 'https://images.unsplash.com/photo-1625948515291-69613efd103f?w=500&h=500&fit=crop',
            },
            
            # Clothing
            {
                'name': 'Classic Denim Jacket',
                'category': 'Clothing',
                'description': 'Timeless denim jacket with a modern fit. Perfect for layering in any season.',
                'price': 79.99,
                'stock': 60,
                'image_url': 'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=500&h=500&fit=crop',
            },
            {
                'name': 'Cotton T-Shirt Pack',
                'category': 'Clothing',
                'description': 'Pack of 3 premium cotton t-shirts in classic colors. Comfortable and breathable.',
                'price': 29.99,
                'stock': 120,
                'image_url': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=500&h=500&fit=crop',
            },
            {
                'name': 'Running Shoes',
                'category': 'Clothing',
                'description': 'Lightweight running shoes with cushioned sole and breathable mesh upper.',
                'price': 89.99,
                'stock': 45,
                'image_url': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500&h=500&fit=crop',
            },
            {
                'name': 'Winter Coat',
                'category': 'Clothing',
                'description': 'Warm and stylish winter coat with insulated lining and water-resistant exterior.',
                'price': 149.99,
                'stock': 30,
                'image_url': 'https://images.unsplash.com/photo-1539533018447-63fcce2678e3?w=500&h=500&fit=crop',
            },
            
            # Books
            {
                'name': 'The DevOps Handbook',
                'category': 'Books',
                'description': 'Essential guide to building world-class agility, reliability, and security in technology organizations.',
                'price': 34.99,
                'stock': 80,
                'image_url': 'https://images.unsplash.com/photo-1532012197267-da84d127e765?w=500&h=500&fit=crop',
            },
            {
                'name': 'Python Programming Guide',
                'category': 'Books',
                'description': 'Comprehensive guide to Python programming for beginners and advanced developers.',
                'price': 44.99,
                'stock': 65,
                'image_url': 'https://images.unsplash.com/photo-1526243741027-444d633d7365?w=500&h=500&fit=crop',
            },
            {
                'name': 'Web Development Essentials',
                'category': 'Books',
                'description': 'Learn modern web development with HTML, CSS, JavaScript, and popular frameworks.',
                'price': 39.99,
                'stock': 55,
                'image_url': 'https://images.unsplash.com/photo-1516979187457-637abb4f9353?w=500&h=500&fit=crop',
            },
            {
                'name': 'Cloud Computing Fundamentals',
                'category': 'Books',
                'description': 'Master cloud computing concepts with AWS, Azure, and Google Cloud Platform.',
                'price': 49.99,
                'stock': 40,
                'image_url': 'https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=500&h=500&fit=crop',
            },
            
            # Home & Garden
            {
                'name': 'Indoor Plant Collection',
                'category': 'Home & Garden',
                'description': 'Set of 3 easy-care indoor plants perfect for home or office decoration.',
                'price': 59.99,
                'stock': 40,
                'image_url': 'https://images.unsplash.com/photo-1459411621453-7b03977f4bfc?w=500&h=500&fit=crop',
            },
            {
                'name': 'Kitchen Knife Set',
                'category': 'Home & Garden',
                'description': 'Professional 5-piece kitchen knife set with ergonomic handles and storage block.',
                'price': 129.99,
                'stock': 25,
                'image_url': 'https://images.unsplash.com/photo-1593618998160-e34014e67546?w=500&h=500&fit=crop',
            },
            {
                'name': 'Decorative Throw Pillows',
                'category': 'Home & Garden',
                'description': 'Set of 2 decorative throw pillows with removable covers in modern designs.',
                'price': 34.99,
                'stock': 90,
                'image_url': 'https://images.unsplash.com/photo-1584100936595-c0654b55a2e2?w=500&h=500&fit=crop',
            },
            {
                'name': 'LED Desk Lamp',
                'category': 'Home & Garden',
                'description': 'Adjustable LED desk lamp with touch control and multiple brightness levels.',
                'price': 44.99,
                'stock': 70,
                'image_url': 'https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=500&h=500&fit=crop',
            },
        ]
        
        # Create products
        for product_data in products_data:
            category_name = product_data.pop('category')
            image_url = product_data.pop('image_url')
            
            product = Product(
                category=categories[category_name],
                image_url=image_url,
                **product_data
            )
            
            try:
                product.save()
                self.stdout.write(self.style.SUCCESS(f'✅ Created product: {product.name}'))
            except Exception as e:
                self.stdout.write(self.style.WARNING(f'❌ Error creating {product.name}: {e}'))
                continue
        
        total_products = Product.objects.count()
        self.stdout.write(self.style.SUCCESS(f'\n✅ Successfully populated database with {total_products} products!'))
        self.stdout.write(self.style.SUCCESS('Run the development server to see the products.'))
