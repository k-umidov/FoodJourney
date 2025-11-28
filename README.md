🥗 Food Journey

Food Journey is a Django-based web application for adding, viewing, and editing dishes.
The project helps you keep a personal food journal with photos, descriptions, and dish categories.

🚀 Features

📸 Uploading dish photos

📝 Adding and editing dish information

🔍 Detailed dish page

🎨 Responsive interface (Bootstrap)

🗂 Dish categories

👤 User profile with editable information and avatar

🛠 Technologies Used

Backend: Django

Frontend: HTML, CSS, Bootstrap

Database: SQLite (default)

Image processing: Pillow

🚀 How to Run the Food Journey Server

Follow these steps:

1️⃣ Navigate to the foodProject folder

Open your terminal and go to the project directory.

2️⃣ Create a virtual environment
python -m venv venv

3️⃣ Activate the virtual environment

Windows:

venv\Scripts\activate

4️⃣ Install the required libraries
pip install -r requirements.txt

5️⃣ Apply database migrations
python manage.py migrate

6️⃣ Start the server
python manage.py runserver


After launch, open the app in your browser:
👉 http://127.0.0.1:8000/

7️⃣ Admin panel (optional)

Create a superuser:

python manage.py createsuperuser


Admin panel address:
👉 http://127.0.0.1:8000/admin/
