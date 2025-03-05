from django.shortcuts import render

# Create your views here.

def authorDashboard(request):
    return render(request, 'crm/author_dashboard.html')

def myBook(request):
    books = [
        {
            "cover_image": "https://via.placeholder.com/80",
            "title": "Book Title",
            "author": "Author Name",
            "pages": 500,
            "rating": 4.5
        },
        {
            "cover_image": "https://via.placeholder.com/80",
            "title": "Another Book",
            "author": "Author Name",
            "pages": 320,
            "rating": 4.2
        },
        {
            "cover_image": "https://via.placeholder.com/80",
            "title": "Final Book",
            "author": "Author Name",
            "pages": 280,
            "rating": 4.8
        },
    ]
    return render(request, 'crm/books.html', {'books': books})
