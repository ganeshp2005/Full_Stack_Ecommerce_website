"""
Run this script to seed demo data:
    venv\Scripts\python.exe manage.py shell < home/seed_data.py
"""
from home.models import Category, Product

# ============ Create Categories ============
categories_data = [
    {'name': 'Electronics', 'slug': 'electronics', 'description': 'Gadgets, devices and electronic accessories'},
    {'name': 'Mobile Phones', 'slug': 'mobile-phones', 'description': 'Smartphones and mobile accessories'},
    {'name': 'Laptops', 'slug': 'laptops', 'description': 'Laptops and computing devices'},
    {'name': 'Fashion', 'slug': 'fashion', 'description': 'Clothing, shoes and accessories'},
    {'name': 'Home & Kitchen', 'slug': 'home-kitchen', 'description': 'Home appliances and kitchen essentials'},
    {'name': 'Books', 'slug': 'books', 'description': 'Books, eBooks and learning materials'},
    {'name': 'Toys & Games', 'slug': 'toys-games', 'description': 'Toys, games and entertainment for kids'},
    {'name': 'Sports & Fitness', 'slug': 'sports-fitness', 'description': 'Sports equipment and fitness gear'},
]

categories = {}
for cat_data in categories_data:
    cat, created = Category.objects.get_or_create(
        slug=cat_data['slug'],
        defaults={'name': cat_data['name'], 'description': cat_data['description']}
    )
    categories[cat.slug] = cat
    print(f"{'Created' if created else 'Exists'} category: {cat.name}")

# ============ Create Products ============
products_data = [
    # Electronics
    {
        'name': 'Sony WH-1000XM4 Wireless Noise Cancelling Headphones',
        'slug': 'sony-wh-1000xm4-headphones',
        'category': 'electronics',
        'description': 'Industry-leading noise cancellation with Adaptive Sound Control. 30-hour battery life, touch controls, and premium sound quality. Comes with carry case and charging cable.',
        'price': 29990, 'original_price': 34990, 'stock': 25, 'rating': 4.8, 'reviews_count': 2341, 'featured': True,
    },
    {
        'name': 'Samsung 55" Crystal 4K UHD Smart TV',
        'slug': 'samsung-55-crystal-4k-tv',
        'category': 'electronics',
        'description': 'Crystal Processor 4K with 4K UHD upscaling, HDR support, and Smart Hub. Slim design with 3 HDMI ports. Stream your favorite content in stunning detail.',
        'price': 54999, 'original_price': 65999, 'stock': 12, 'rating': 4.6, 'reviews_count': 890, 'featured': True,
    },
    {
        'name': 'Bose SoundLink Revolve+ Portable Bluetooth Speaker',
        'slug': 'bose-soundlink-revolve-plus',
        'category': 'electronics',
        'description': '360-degree sound with deep bass. Water-resistant design, 17-hour battery life, and built-in microphone for calls. Perfect for indoor and outdoor use.',
        'price': 19999, 'original_price': 24999, 'stock': 30, 'rating': 4.7, 'reviews_count': 567, 'featured': False,
    },
    {
        'name': 'GoPro HERO12 Black Waterproof Action Camera',
        'slug': 'gopro-hero12-black',
        'category': 'electronics',
        'description': '5.3K video with HyperSmooth 6.0 stabilization. Waterproof to 10m, 27MP photos, and improved battery life. Includes mounting accessories.',
        'price': 39990, 'original_price': 45990, 'stock': 15, 'rating': 4.9, 'reviews_count': 432, 'featured': True,
    },

    # Mobile Phones
    {
        'name': 'Apple iPhone 15 Pro Max 256GB Black Titanium',
        'slug': 'apple-iphone-15-pro-max-256gb',
        'category': 'mobile-phones',
        'description': 'A17 Pro chip with ProMotion display. 48MP main camera with 5x optical zoom. Titanium design, USB-C, and all-day battery life. 256GB storage.',
        'price': 159900, 'original_price': 169900, 'stock': 10, 'rating': 4.9, 'reviews_count': 4321, 'featured': True,
    },
    {
        'name': 'Samsung Galaxy S24 Ultra 5G 256GB Titanium',
        'slug': 'samsung-galaxy-s24-ultra',
        'category': 'mobile-phones',
        'description': 'Snapdragon 8 Gen 3 processor with Galaxy AI. 200MP camera with 100x Space Zoom. S-Pen included, 5000mAh battery. 256GB storage.',
        'price': 129999, 'original_price': 139999, 'stock': 18, 'rating': 4.8, 'reviews_count': 2890, 'featured': True,
    },
    {
        'name': 'Google Pixel 8 Pro 128GB Obsidian',
        'slug': 'google-pixel-8-pro',
        'category': 'mobile-phones',
        'description': 'Tensor G3 chip with AI features. 50MP triple camera system, 7 years of OS updates, and advanced photo editing. 6.7-inch OLED display.',
        'price': 99999, 'original_price': 109999, 'stock': 20, 'rating': 4.7, 'reviews_count': 1567, 'featured': True,
    },
    {
        'name': 'OnePlus 12 5G 256GB Flowy Emerald',
        'slug': 'oneplus-12-5g',
        'category': 'mobile-phones',
        'description': 'Snapdragon 8 Gen 3 with 16GB RAM. Hasselblad camera system, 5400mAh battery with 100W fast charging. 2K 120Hz AMOLED display.',
        'price': 64999, 'original_price': 69999, 'stock': 22, 'rating': 4.6, 'reviews_count': 1234, 'featured': False,
    },

    # Laptops
    {
        'name': 'MacBook Pro 14" M3 Pro Chip 18GB RAM 512GB SSD',
        'slug': 'macbook-pro-14-m3-pro',
        'category': 'laptops',
        'description': 'M3 Pro chip with 12-core CPU and 18-core GPU. 14.2-inch Liquid Retina XDR display. 18GB unified memory, 512GB SSD. Up to 18 hours battery.',
        'price': 199900, 'original_price': 214900, 'stock': 8, 'rating': 4.9, 'reviews_count': 876, 'featured': True,
    },
    {
        'name': 'Dell XPS 15 Laptop Intel i7-13700H 16GB 512GB',
        'slug': 'dell-xps-15-i7',
        'category': 'laptops',
        'description': 'Intel Core i7-13700H with NVIDIA RTX 4060. 15.6-inch 3.5K OLED touch display. 16GB DDR5 RAM, 512GB NVMe SSD. Premium aluminum build.',
        'price': 189990, 'original_price': 199990, 'stock': 12, 'rating': 4.7, 'reviews_count': 654, 'featured': True,
    },
    {
        'name': 'ASUS ROG Zephyrus G14 Gaming Laptop RTX 4060',
        'slug': 'asus-rog-zephyrus-g14',
        'category': 'laptops',
        'description': 'AMD Ryzen 9 7940HS with RTX 4060. 14-inch QHD 165Hz display, 16GB RAM, 1TB SSD. Compact design with advanced cooling.',
        'price': 154990, 'original_price': 164990, 'stock': 10, 'rating': 4.8, 'reviews_count': 789, 'featured': False,
    },
    {
        'name': 'HP Pavilion 15 Intel i5 13th Gen 8GB 512GB SSD',
        'slug': 'hp-pavilion-15-i5',
        'category': 'laptops',
        'description': 'Intel Core i5-1335U, 8GB DDR4 RAM, 512GB NVMe SSD. 15.6-inch FHD IPS display. Great for everyday productivity and multimedia.',
        'price': 59990, 'original_price': 64990, 'stock': 35, 'rating': 4.5, 'reviews_count': 2345, 'featured': False,
    },

    # Fashion
    {
        'name': 'Men\'s Slim Fit Formal Shirt - Premium Cotton',
        'slug': 'mens-slim-fit-formal-shirt',
        'category': 'fashion',
        'description': 'Premium pure cotton formal shirt with slim fit design. Wrinkle-resistant, breathable fabric. Available in multiple colors and sizes.',
        'price': 1499, 'original_price': 2499, 'stock': 100, 'rating': 4.4, 'reviews_count': 5678, 'featured': True,
    },
    {
        'name': 'Women\'s Elegant Floral Print Maxi Dress',
        'slug': 'womens-elegant-floral-maxi-dress',
        'category': 'fashion',
        'description': 'Beautiful floral print maxi dress with flowy design. Made from soft, comfortable fabric. Perfect for casual and semi-formal occasions.',
        'price': 2299, 'original_price': 3299, 'stock': 80, 'rating': 4.6, 'reviews_count': 3456, 'featured': True,
    },
    {
        'name': 'Classic Leather Sneakers - Men\'s Casual Shoes',
        'slug': 'classic-leather-sneakers',
        'category': 'fashion',
        'description': 'Stylish leather sneakers with cushioned insole. Durable rubber sole with excellent grip. Perfect for daily wear and casual outings.',
        'price': 3499, 'original_price': 4999, 'stock': 60, 'rating': 4.5, 'reviews_count': 4567, 'featured': False,
    },
    {
        'name': 'Designer Sunglasses UV Protection Polarized',
        'slug': 'designer-sunglasses-polarized',
        'category': 'fashion',
        'description': 'Premium polarized sunglasses with UV400 protection. Lightweight frame with anti-glare lenses. Includes hard carry case and microfiber cloth.',
        'price': 1999, 'original_price': 2999, 'stock': 120, 'rating': 4.3, 'reviews_count': 2345, 'featured': False,
    },

    # Home & Kitchen
    {
        'name': 'Instant Pot Duo 7-in-1 Electric Pressure Cooker 6Qt',
        'slug': 'instant-pot-duo-7-in-1-6qt',
        'category': 'home-kitchen',
        'description': '7-in-1 multi cooker: pressure cooker, slow cooker, rice cooker, steamer, sauté, yogurt maker, and warmer. 6-quart capacity for family meals.',
        'price': 8999, 'original_price': 12999, 'stock': 40, 'rating': 4.7, 'reviews_count': 6789, 'featured': True,
    },
    {
        'name': 'Robot Vacuum Cleaner with Laser Navigation',
        'slug': 'robot-vacuum-cleaner-laser-nav',
        'category': 'home-kitchen',
        'description': 'Smart robot vacuum with LiDAR navigation. 2500Pa suction, HEPA filter, 180-min runtime. App control with scheduled cleaning and zone mapping.',
        'price': 18999, 'original_price': 24999, 'stock': 20, 'rating': 4.5, 'reviews_count': 3456, 'featured': True,
    },
    {
        'name': 'Air Fryer XL 5.5L Digital Touch Screen',
        'slug': 'air-fryer-xl-55l-digital',
        'category': 'home-kitchen',
        'description': '5.5L capacity air fryer with 8 presets. Rapid air circulation for crispy results with 90% less oil. Digital touch screen with timer.',
        'price': 5999, 'original_price': 8999, 'stock': 50, 'rating': 4.6, 'reviews_count': 5678, 'featured': False,
    },
    {
        'name': 'Electric Kettle 1.5L Stainless Steel',
        'slug': 'electric-kettle-15l-stainless',
        'category': 'home-kitchen',
        'description': '1.5L stainless steel electric kettle. 1500W rapid boiling, auto shut-off, and boil-dry protection. BPA-free with cool-touch handle.',
        'price': 1299, 'original_price': 1999, 'stock': 150, 'rating': 4.4, 'reviews_count': 4567, 'featured': False,
    },

    # Books
    {
        'name': 'The Psychology of Money - Morgan Housel',
        'slug': 'the-psychology-of-money',
        'category': 'books',
        'description': 'Timeless lessons on wealth, greed, and happiness. Explores how our mindset shapes financial success more than raw intelligence.',
        'price': 399, 'original_price': 499, 'stock': 200, 'rating': 4.8, 'reviews_count': 8901, 'featured': True,
    },
    {
        'name': 'Atomic Habits - James Clear',
        'slug': 'atomic-habits-james-clear',
        'category': 'books',
        'description': 'An easy and proven way to build good habits and break bad ones. The #1 New York Times bestseller for personal transformation.',
        'price': 599, 'original_price': 799, 'stock': 250, 'rating': 4.9, 'reviews_count': 12345, 'featured': True,
    },
    {
        'name': 'Dune - Frank Herbert (Deluxe Edition)',
        'slug': 'dune-frank-herbert-deluxe',
        'category': 'books',
        'description': 'The epic science fiction masterpiece about Paul Atreides and the desert planet Arrakis. This deluxe edition includes a new introduction.',
        'price': 899, 'original_price': 1199, 'stock': 90, 'rating': 4.7, 'reviews_count': 5678, 'featured': False,
    },
    {
        'name': 'Rich Dad Poor Dad - Robert Kiyosaki',
        'slug': 'rich-dad-poor-dad',
        'category': 'books',
        'description': 'What the rich teach their kids about money that the poor and middle class do not. A classic guide to financial literacy.',
        'price': 499, 'original_price': 599, 'stock': 300, 'rating': 4.6, 'reviews_count': 7890, 'featured': False,
    },

    # Toys & Games
    {
        'name': 'LEGO Star Wars Millennium Falcon Building Set (7541 pcs)',
        'slug': 'lego-star-wars-millennium-falcon',
        'category': 'toys-games',
        'description': 'The ultimate LEGO Star Wars collectors set. 7541 pieces with detailed interior, minifigures, and display stand. For ages 12+.',
        'price': 49999, 'original_price': 54999, 'stock': 5, 'rating': 4.9, 'reviews_count': 1234, 'featured': True,
    },
    {
        'name': 'Nintendo Switch OLED Model with White Joy-Con',
        'slug': 'nintendo-switch-oled',
        'category': 'toys-games',
        'description': 'Nintendo Switch OLED Model with vibrant 7-inch OLED screen, enhanced audio, and wide adjustable stand. Includes docks and controllers.',
        'price': 28999, 'original_price': 31999, 'stock': 15, 'rating': 4.8, 'reviews_count': 3456, 'featured': True,
    },
    {
        'name': 'Hot Wheels 50-Car Mega Box Collection',
        'slug': 'hot-wheels-50-car-mega-box',
        'category': 'toys-games',
        'description': 'Mega box with 50 Hot Wheels cars. Mix of favorite and new models. Perfect for collectors and kids who love racing fun.',
        'price': 4999, 'original_price': 6999, 'stock': 45, 'rating': 4.7, 'reviews_count': 2345, 'featured': False,
    },

    # Sports & Fitness
    {
        'name': 'Pro Fitness Dumbbell Set 20kg with Weights',
        'slug': 'pro-fitness-dumbbell-set-20kg',
        'category': 'sports-fitness',
        'description': 'Professional dumbbell set with 20kg total weight. Includes adjustable handles, weight plates, and sturdy storage rack. Chrome-plated.',
        'price': 2999, 'original_price': 4999, 'stock': 40, 'rating': 4.5, 'reviews_count': 3456, 'featured': True,
    },
    {
        'name': 'Yoga Mat Premium 6mm Non-Slip Extra Thick',
        'slug': 'yoga-mat-premium-6mm',
        'category': 'sports-fitness',
        'description': 'Premium 6mm thick yoga mat with non-slip surface. Eco-friendly TPE material. Includes carry strap for easy portability.',
        'price': 999, 'original_price': 1499, 'stock': 200, 'rating': 4.6, 'reviews_count': 6789, 'featured': False,
    },
    {
        'name': 'Smart Fitness Band with Heart Rate Monitor',
        'slug': 'smart-fitness-band-heart-rate',
        'category': 'sports-fitness',
        'description': 'Advanced fitness tracker with heart rate, SpO2, and sleep monitoring. 15-day battery life, 5ATM waterproof, and smartphone notifications.',
        'price': 2999, 'original_price': 3999, 'stock': 75, 'rating': 4.4, 'reviews_count': 4567, 'featured': False,
    },
]

for product_data in products_data:
    cat_slug = product_data.pop('category')
    category = categories[cat_slug]
    product_data['category'] = category

    product, created = Product.objects.get_or_create(
        slug=product_data['slug'],
        defaults=product_data
    )
    print(f"{'Created' if created else 'Exists'} product: {product.name}")

print("\n========================================")
print("Seeding complete!")
print(f"Categories: {Category.objects.count()}")
print(f"Products: {Product.objects.count()}")
print("========================================")