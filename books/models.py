from django.db import models

class BookCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    book_id = models.CharField(max_length=14, null=False, default='DEFAULT_VALUE')
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    authors = models.CharField(max_length=500)  # To store authors as a comma-separated string
    publisher = models.CharField(max_length=200)
    published_date = models.DateField()
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    distribution_expense = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.title} by {self.authors}"


