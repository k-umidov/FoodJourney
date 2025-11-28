🥗 Food Journey

Food Journey is a Django-based web application for adding, viewing, and editing dishes.
The project helps you keep a personal food journal with photos, descriptions, and dish categories.

🚀 Features

📸 Uploading dish photos

📝 Adding and editing dish information

🔍 Detailed dish page
💬 Comments & Video Tutorials

The project also includes an additional feature where users can:

Leave comments under each dish
This allows users to share their thoughts, feedback, suggestions, or personal experiences related to the dish.

Watch cooking videos
Each dish can include a link to a YouTube cooking video or any other video tutorial.
This makes it easier for users to learn how the dish is prepared and follow step-by-step instructions.

This improves user engagement and makes the Food Journey project more interactive and helpful.
🎨 Responsive interface (Bootstrap)

🗂 Dish categories

👤 User profile with editable information and avatar

🛠 Technologies Used

Backend: Django

Frontend: HTML, CSS, Bootstrap

Database: SQLite (default)

Image processing: Pillow
Screenshot of the page:
![Screenshot](./Screenshot.png)


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
