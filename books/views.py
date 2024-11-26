from django.shortcuts import render
from django.db.models import Sum
from .models import Book

def report_view(request):
    # Calculate total distribution expenses by category, excluding empty categories
    category_expenses = Book.objects.filter(category__isnull=False, category__name__gt='') \
                                        .values('category__name') \
                                        .annotate(total_expenses=Sum('distribution_expense'))

    report_data = {}
    for entry in category_expenses:
        category_name = entry['category__name']
        total_expenses = entry['total_expenses']
        report_data[category_name] = total_expenses


    return render(request, 'report.html', {'report_data': report_data})
