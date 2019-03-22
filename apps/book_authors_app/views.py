from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author

# Create your views here.
def index(request):
    return render(request, 'index.html')
def books(request):
    books = Book.objects.all()
    context = {
    'books': books,
    }
    return render(request, 'books.html', context)


def book_info(request, num):
    book = Book.objects.get(id=num)
    authors = book.authors.all().order_by('last_name')
    add_authors = Author.objects.exclude(books=book)
    context = {
    'book': book,
    'authors': authors,
    'add_authors':add_authors,
    'num': num
    }
    return render(request, 'info.html', context)

def add_book_author(request, num):
    if request.method == 'POST':
        if request.POST['add_author'] == 'Choose...':
            return redirect(f'/books/{num}')
        writer = Author.objects.get(id=request.POST['add_author'])
        Book.objects.get(id=num).authors.add(writer)
    return redirect(f'/books/{num}')

def remove_book_author(request, num, author_id):
    writer = Author.objects.get(id=author_id)
    Book.objects.get(id=num).authors.remove(writer)
    return redirect(f'/books/{num}')


def add_book(request):
    authors = Author.objects.all()
    context = {
    "authors": authors
    }
    return render(request, 'add_book.html', context)

def add_book_new(request):
    if request.method == 'POST':
        book = Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
        for writer in request.POST['writers']:
            book.authors.add(Author.objects.get(id=writer))
        print(request.POST, '******************************')
    return redirect(f'/books/{book.id}')

def edit_book(request, num):
    book = Book.objects.get(id=num)
    context = {
    'book': book,
    'num': num,
    'authors': Author.objects.all(),
    }
    return render(request, 'edit_book.html', context)

def edit_book_submit(request, num):
    if request.method == 'POST':
        book = Book.objects.get(id=num)
        book.title = request.POST['title']
        book.desc = request.POST['desc']
        book.authors.clear()
        for writer in request.POST.getlist('writers'):
            book.authors.add(Author.objects.get(id=writer))
        book.save()
        print(request.POST, '******************************')
    return redirect(f'/books/{num}')

def remove_book(request, num):
    book = Book.objects.get(id=num)
    book.delete()
    return redirect('/books')

def authors(request):
    authors = Author.objects.all().order_by('last_name')
    context = {
    'authors': authors,
    }
    return render(request, 'authors.html', context)

def author_info(request, num):
    author = Author.objects.get(id=num)
    books = author.books.all().order_by('title')
    add_books = Book.objects.exclude(authors=author)
    context = {
    'books': books,
    'author': author,
    'add_books':add_books,
    'num': num
    }
    return render(request, 'author_info.html', context)

def add_to_bibliography(request, num):
    if request.method == 'POST':
        if request.POST['add_book'] == 'Choose...':
            return redirect(f'/authors/{num}')
        book = Book.objects.get(id=request.POST['add_book'])
        Author.objects.get(id=num).books.add(book)
    return redirect(f'/authors/{num}')

def remove_from_bibliography(request, num, book_id):
    book = Book.objects.get(id=book_id)
    Author.objects.get(id=num).books.remove(book)
    return redirect(f'/authors/{num}')

def add_author(request):
    books = Book.objects.all()
    context = {
    "books": books
    }
    return render(request, 'authors_add.html', context)

def add_author_new(request):
    if request.method == 'POST':
        author = Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
        for book in request.POST['books']:
            author.books.add(Book.objects.get(id=book))
        print(request.POST, '******************************')
    return redirect(f'/authors')

def author_edit(request, num):
    author = Author.objects.get(id=num)
    context = {
    'author': author,
    'num': num,
    'books': Book.objects.all(),
    }
    return render(request, 'edit_author.html', context)

def author_edit_submit(request, num):
    if request.method == 'POST':
        author = Author.objects.get(id=num)
        author.first_name = request.POST['first_name']
        author.last_name = request.POST['last_name']
        author.notes = request.POST['notes']
        author.books.clear()
        for book in request.POST.getlist('books'):
            author.books.add(Book.objects.get(id=book))
            print(book, '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
        author.save()
        print(request.POST.getlist('books'), '******************************')
    return redirect(f'/authors/{num}')

def remove_author(request, num):
    author = Author.objects.get(id=num)
    author.delete()
    return redirect('/authors')
