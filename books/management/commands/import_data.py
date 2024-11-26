import csv
from django.core.management.base import BaseCommand
from books.models import Book, BookCategory
from datetime import datetime

class Command(BaseCommand):
    help = 'Imports books data from a CSV file into the database'

    def handle(self, *args, **kwargs):
        # Open the CSV file
        with open('books_data.csv', 'r') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                # Skip empty or malformed rows
                if not row or not row.get('published_date'):
                    self.stdout.write(self.style.ERROR(f"Empty or malformed row, skipping: {row}"))
                    continue

                # Strip any extra spaces from the 'published_date' column
                published_date_str = row['published_date'].strip()
                
                if not published_date_str:
                    self.stdout.write(self.style.ERROR(f"Empty date for book: {row['title']}, skipping."))
                    continue

                try:
                    # Try to convert the published_date from MM/DD/YYYY to YYYY-MM-DD
                    published_date = datetime.strptime(published_date_str, '%m/%d/%Y').date()
                except ValueError:
                    # Print the exact date that caused the issue
                    self.stdout.write(self.style.ERROR(f"Invalid date format for book: {row['title']}, date: {published_date_str}, skipping."))
                    continue
                
                # Extract or create the category
                category, created = BookCategory.objects.get_or_create(name=row['category'])
                
                # Create the book record
                Book.objects.create(
                    book_id=row['id'],  # ID field as book_id
                    title=row['title'],
                    subtitle=row.get('subtitle', ''),  # Subtitle can be empty or null
                    authors=row['authors'],
                    publisher=row['publisher'],
                    published_date=published_date,
                    category=category,
                    distribution_expense=row['distribution_expense']
                )
                
                self.stdout.write(self.style.SUCCESS(f"Successfully imported book: {row['title']}"))
