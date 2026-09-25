# 🛒 YourChoice - Full Stack E-Commerce & Interactive SQL Terminal Platform

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0.7-092E20?logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3.0-003B57?logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-Modern-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-Animations%20%26%20Glassmorphism-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6%2B-F7DF1E?logo=javascript&logoColor=black)

**YourChoice** is a feature-packed, classic animated full-stack e-commerce web application inspired by modern shopping experiences like Amazon. Built using **Django** and **SQLite**, it combines secure user authentication, multi-seller marketplace support, shopping cart management, seamless checkout, personalized user themes, and a built-in **Interactive Web-Based SQL Command Console & Database Explorer**.

---

## 🌟 Key Features

### ⚡ 1. Built-in Interactive SQL Command Console (`/sql-console/`)
A dedicated web-based database management terminal integrated into the application:
* **Live SQL Command Execution:** Write and execute standard SQL queries (`SELECT`, `INSERT`, `UPDATE`, `DELETE`, `JOIN`, `GROUP BY`) directly against `db.sqlite3`.
* **Database Schema Inspector:** Sidebar tree listing all database tables (`home_product`, `home_category`, `auth_user`, `home_order`, `home_cart`, `home_userprofile`) with live record counts.
* **Instant Query Presets:** One-click shortcuts for common queries:
  * 📦 *All Products Listing*
  * 📁 *Category Breakdown*
  * 👤 *User Accounts*
  * 🛒 *Customer Orders*
  * 🔥 *Top-Rated Products*
  * 📊 *Stock & Category Analytics*
  * 🗄️ *Database Tables Schema*
* **Metrics & Exporting:** Real-time query execution benchmarks in milliseconds, row counts, tabular result views, NULL value formatting, and **One-Click CSV Export**.

---

### 🎨 2. Classic Animated UI & Modern WOW Aesthetics
* **3D Perspective Tilt Effect:** Interactive mouse hover elevation on product cards.
* **Particle Canvas Background:** Animated background canvas graphics for visual depth.
* **Glassmorphism & Neon Glows:** Modern frosted blur cards (`backdrop-filter`), vibrant color gradients (`#6366f1`, `#a855f7`, `#ec4899`), and glowing status badges.
* **Personalized User Themes:** Persistent Dark/Light themes, custom accent colors (Orange, Cyber Neon, Gold), and adjustable typography.

---

### 🛍️ 3. Full-Featured E-Commerce Storefront
* **Product Catalog:** Product browsing with high-resolution image support, discount badges, ratings, and stock status.
* **Search & Filter Engine:** Real-time keyword search, category filtering, and multi-criteria sorting (Price Low to High, Price High to Low, Highest Rated, Newest Releases).
* **Product Details Page:** Comprehensive product specifications, stock status, seller details, and related item recommendations.

---

### 🏪 4. Multi-Seller Marketplace
* **Become a Seller:** Any registered user can list products for sale.
* **Seller Dashboard:** Sales statistics dashboard displaying total revenue, order item breakdown, and active product management.
* **Product Management:** Full CRUD capabilities (Create listing, Edit details/pricing, Delete product).

---

### 🛒 5. Shopping Cart & Checkout System
* **Dynamic Cart Management:** Real-time item additions, quantity updates, subtotal calculations, and item removals.
* **Smart Shipping Calculation:** Free shipping thresholds for orders exceeding ₹499.
* **Checkout & Address System:** Full delivery address form with payment gateway simulations (Cash on Delivery, Credit/Debit Card, UPI).
* **Order History & Confirmation:** Instant order ID generation, order breakdown receipts, and historical order tracking.

---

### 🔐 6. Security & Data Integrity
* **Password Hashing:** PBKDF2-SHA256 password security via Django auth.
* **Form Protection:** CSRF tokens enforced on all POST forms.
* **Session Protection:** HTTPOnly cookies with 24-hour timeout.
* **Security Headers:** Defense against XSS, clickjacking, and MIME-type sniffing.

---

## 📂 Database Schema Overview

The database uses **SQLite3** (`db.sqlite3`) with the following core relational models:

```mermaid
erDiagram
    User ||--o{ Product : "sells"
    User ||--o{ Order : "places"
    User ||--o1 UserProfile : "has"
    User ||--o1 Cart : "owns"
    Category ||--o{ Product : "contains"
    Cart ||--o{ CartItem : "contains"
    Product ||--o{ CartItem : "referenced in"
    Order ||--o{ OrderItem : "contains"
    Product ||--o{ OrderItem : "referenced in"
```

| Table Name | Description |
|------------|-------------|
| `auth_user` | User authentication records (username, email, password hash, staff status). |
| `home_userprofile` | User customization preferences (theme, font size, color scheme). |
| `home_category` | Product categories (slug, name, icons). |
| `home_product` | Product listings (name, description, price, stock, rating, discount, seller). |
| `home_cart` & `home_cartitem` | Shopping carts and individual cart items tied to sessions/users. |
| `home_order` & `home_orderitem` | Completed customer orders and snapshot receipts of purchased items. |

---

## 🛠️ Tech Stack

* **Backend Framework:** Django 6.0 (Python 3.10+)
* **Database:** SQLite 3
* **Frontend:** HTML5, Modern CSS3 (CSS Variables, Flexbox, CSS Grid, Glassmorphism, Keyframe Animations), Vanilla JavaScript ES6+
* **Icons & Typography:** FontAwesome 6.5, Google Fonts (Outfit, Poppins, Fira Code)
* **Image Processing:** Pillow 12.3.0

---

## 🚀 Installation & Setup Guide

### 1. Prerequisites
Ensure you have **Python 3.10+** installed on your machine.

### 2. Clone the Repository
```bash
git clone https://github.com/ganeshp2005/Full_Stack_Ecommerce_website.git
cd Full_Stack_Ecommerce_website
```

### 3. Create & Activate Virtual Environment
* **Windows:**
  ```powershell
  python -m venv venv
  .\venv\Scripts\activate
  ```
* **Mac/Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Apply Database Migrations
```bash
python manage.py migrate
```

### 6. (Optional) Seed Demo Data
Populate 30 sample products across 8 categories:
```bash
python -c "import os; os.environ['DJANGO_SETTINGS_MODULE']='config.settings'; import django; django.setup(); exec(open('home/seed_data.py').read())"
```

### 7. Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```

### 8. Run Development Server
```bash
python manage.py runserver
```

---

## 🌐 Application URLs

| Feature | URL Path | Access Level |
|---------|----------|--------------|
| 🛒 **Store Front** | `/` | Public |
| ⚡ **SQL Terminal & DB Console** | `/sql-console/` | Public / Admin |
| 🔐 **Login** | `/login/` | Public |
| 📝 **Register** | `/register/` | Public |
| 🛍️ **Product Details** | `/product/<slug>/` | Public |
| 🛒 **Cart** | `/cart/` | Public / User |
| 💳 **Checkout** | `/checkout/` | Logged In |
| 📦 **Order History** | `/my-orders/` | Logged In |
| 🏪 **Seller Dashboard** | `/sell/` | Logged In |
| ➕ **Add Product** | `/sell/add/` | Logged In |
| ⚙️ **User Preferences** | `/settings/` | Logged In |
| ⚙️ **Django Admin Panel** | `/admin/` | Admin Superuser |

---

## 📊 Sample SQL Commands for SQL Console

Try running these queries inside the built-in **SQL Console** at `http://127.0.0.1:8000/sql-console/`:

```sql
-- View top 10 products sorted by rating
SELECT name, price, stock, rating, discount_percent 
FROM home_product 
WHERE stock > 0 
ORDER BY rating DESC 
LIMIT 10;

-- Calculate category analytics (product count & average price)
SELECT c.name AS category, COUNT(p.id) AS product_count, ROUND(AVG(p.price), 2) AS avg_price 
FROM home_category c 
LEFT JOIN home_product p ON c.id = p.category_id 
GROUP BY c.id;

-- View all user accounts and their joined dates
SELECT username, email, is_staff, date_joined 
FROM auth_user 
ORDER BY date_joined DESC;

-- List database tables schema
SELECT name, type, sql 
FROM sqlite_master 
WHERE type='table';
```

---

## 📄 License
This project is licensed under the MIT License - feel free to customize and expand for personal or educational use!