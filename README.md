# 🏸 RacketHub — Badminton Racket Store

RacketHub is a full-stack e-commerce web application for browsing and purchasing badminton rackets, built with Django and Tailwind CSS as a learning project during my MCA studies.

The idea was simple — build something real, not just a tutorial project. So instead of a basic todo app I built an actual product store with multiple pages, a database with 4 models covering all three Django relationships (OneToOne, OneToMany, ManyToMany), a working review system, search and filter by racket type, and a complete checkout flow with order confirmation.

The project covers everything from setting up Django from scratch, configuring Tailwind CSS, designing templates with a base layout, working with the ORM, handling forms and form validation, serving media files, and managing everything through the Django admin panel. Each feature was built step by step and documented as daily notes throughout the build.

---

## ✨ Features

- 🏸 **Racket Listing** — Browse all rackets with image, brand, price and description
- 🔍 **Search by Type** — Filter rackets by category (Head Heavy, Lightweight, Professional etc.)
- 📄 **Racket Detail Page** — View full details with laser serial number and warranty info
- ⭐ **Customer Reviews** — Leave star ratings and comments on any racket
- 🛒 **Checkout Page** — Enter delivery address and choose payment method (COD / UPI / Card)
- ✅ **Order Confirmation** — Summary page after placing an order
- 🔐 **Admin Panel** — Manage rackets, types, reviews and serials via Django admin

---

## 🛠️ Tech Stack

| Technology | Usage |
|------------|-------|
| Python 3.13 | Backend language |
| Django 6.0 | Web framework |
| Tailwind CSS | Styling |
| SQLite | Database |
| Pillow | Image handling |

---

## 🗄️ Database Models

- **rackets** — Stores racket info (name, image, type, price, description)
- **racket_type** — Categories with ManyToMany relation to rackets
- **racket_reviews** — Reviews with ForeignKey to racket and user (OneToMany)
- **LaserSerial** — Unique serial code per racket (OneToOne)

---

## ⚙️ How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/racket-hub.git
cd racket-hub
```

**2. Create and activate virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Mac/Linux
```

**3. Install dependencies**
```bash
pip install django pillow django-tailwind django-browser-reload
```

**4. Run migrations**
```bash
python manage.py migrate
```

**5. Create admin user**
```bash
python manage.py createsuperuser
```

**6. Start Tailwind (in a separate terminal)**
```bash
python manage.py tailwind start
```

**7. Run the server**
```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000` in your browser.

---

## 👨‍💻 Author

**Deep Sambhavani**
- 🌐 Portfolio: [deepsambhavani.pythonanywhere.com](http://deepsambhavani.pythonanywhere.com)
- 💼 LinkedIn: [linkedin.com/in/deepsambhavani](https://linkedin.com/in/deepsambhavani)
- 🐙 GitHub: [github.com/deepsambhavani](https://github.com/deepsambhavani)

---

## 📌 Note

This is a learning project built during my MCA studies at Silver Oak University to practice Django fundamentals including models, views, templates, forms, ORM relationships and admin panel.
