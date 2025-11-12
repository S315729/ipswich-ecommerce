"""
Generate placeholder images for products
This script creates simple colored placeholder images for demo purposes
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ipswich_ecommerce.settings')
django.setup()

from PIL import Image, ImageDraw, ImageFont
from products.models import Product
import random

def create_placeholder_image(product_name, output_path):
    """Create a simple placeholder image with product name"""
    # Create image with random pastel background
    colors = [
        (173, 216, 230),  # Light Blue
        (255, 182, 193),  # Light Pink
        (144, 238, 144),  # Light Green
        (255, 218, 185),  # Peach
        (221, 160, 221),  # Plum
        (176, 224, 230),  # Powder Blue
    ]
    
    bg_color = random.choice(colors)
    
    # Image size for product display
    width, height = 800, 600
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Draw border
    border_color = tuple(max(0, c - 30) for c in bg_color)
    draw.rectangle([10, 10, width-10, height-10], outline=border_color, width=5)
    
    # Add product name text
    # Try to use default font (will be basic but works)
    try:
        font_size = 48
        # Try to load a better font if available
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            font = ImageFont.load_default()
    except:
        font = None
    
    # Calculate text position (centered)
    text = product_name
    # Simple centering (works with basic font)
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2
    
    # Draw text with shadow for better visibility
    shadow_color = (50, 50, 50)
    draw.text((text_x + 2, text_y + 2), text, fill=shadow_color, font=font)
    draw.text((text_x, text_y), text, fill=(255, 255, 255), font=font)
    
    # Draw a simple icon (circle) at the top
    circle_radius = 60
    circle_center = (width // 2, height // 4)
    draw.ellipse([
        circle_center[0] - circle_radius,
        circle_center[1] - circle_radius,
        circle_center[0] + circle_radius,
        circle_center[1] + circle_radius
    ], fill=(255, 255, 255), outline=border_color, width=3)
    
    # Save the image
    img.save(output_path, 'JPEG', quality=85)
    print(f'  ✓ Created image: {output_path}')


def main():
    """Generate placeholder images for all products without images"""
    products = Product.objects.all()
    
    print('Generating placeholder images for products...\n')
    
    created_count = 0
    skipped_count = 0
    
    for product in products:
        if product.image:
            print(f'  - Skipped (has image): {product.name}')
            skipped_count += 1
            continue
        
        # Create filename from product slug
        filename = f'{product.slug}.jpg'
        filepath = os.path.join('media', 'products', filename)
        
        # Create the image
        create_placeholder_image(product.name, filepath)
        
        # Update product with image path
        product.image = f'products/{filename}'
        product.save()
        
        created_count += 1
    
    print(f'\n✅ Image generation complete!')
    print(f'   Created: {created_count} images')
    print(f'   Skipped: {skipped_count} products (already had images)')
    print(f'\nℹ️  Refresh your browser to see the images!')


if __name__ == '__main__':
    main()
