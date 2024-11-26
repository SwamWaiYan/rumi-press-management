# rumi-press-management
  A Django web application to manage book distribution for Rumi Press. The app supports CRUD operations for book categories and books, allows importing data from spreadsheets (CSV), and provides a report view for distribution expenses by category.

## Features
CRUD operations for book categories and books (including title, author, publisher, category, and distribution expenses).
Import book data from a CSV file.
Report view to display distribution expenses by category using charts.
## Technologies
Django for backend development
SQLite (default) for the database
Chart.js for reports
## Installation
### 1. Clone the Repo
`git clone https://github.com/SwamWaiYan/rumi-press-management.git`

`cd rumi-press-management`
### 2. Set up Virtual Environment
`python3 -m venv env`

`source env/bin/activate`  # On Windows: `env\Scripts\activate`
### 3. Set up Database
`python manage.py makemigrations`

`python manage.py migrate`
### 4. Create Admin User
`python manage.py createsuperuser`
### 5. Run Development Server
`python manage.py runserver`
Access the app at http://127.0.0.1:8000/ and the admin at http://127.0.0.1:8000/admin.

## Usage
Manage Categories: Add, edit, or delete book categories in the Django Admin.
Add Books: Add book details (ID, title, author, category, distribution expense).
Import Data: Prepare a CSV file and run python manage.py import_data to import books.
View Reports: Access distribution expenses by category with charts.
## Running Tests
`python manage.py test`
## Deployment
Follow Django’s deployment checklist for production setup. Use a production database (e.g., PostgreSQL), set DEBUG = False, and configure a web server like Gunicorn or Nginx.

## Contributing
1. Fork the repo.
2. Create a branch for your feature.
3. Commit and push changes.
4. Create a pull request.
## License
MIT License.
