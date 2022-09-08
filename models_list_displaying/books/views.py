from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse

from books.models import Book


def home_view(request):
    template = 'home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Каталог книг': reverse('books')
    }
    context = {
        'pages': pages,
    }
    return render(request, template, context)


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()

    context = {
        'books': books
    }
    return render(request, template, context)


def book_view(request, date):
    page_number = 0
    date_list = []
    template = 'books/book.html'
    book = Book.objects.filter(pub_date=date)
    sort_books = Book.objects.order_by('pub_date')
    pag = Paginator(sort_books, 1)
    # Находим номер текущей страницы и создаем список отсортированных дат издания
    for index, books in enumerate(sort_books):
        date_list.append(str(books.pub_date))
        if str(books.pub_date) == date:
            page_number = index + 1
    previous_page = ''
    next_page = ''
    # Проверяем индексацию списка дат относительно текущей даты(страницы)
    if page_number - 2 >= 0:
        previous_page = date_list[page_number - 2]
    if page_number < len(date_list):
        next_page = date_list[page_number]
    page = pag.get_page(page_number)
    context = {
        'book': book[0],
        'page': page,
        'previous': previous_page,
        'next': next_page

    }
    return render(request, template, context)
