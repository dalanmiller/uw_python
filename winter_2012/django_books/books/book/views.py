from django.shortcuts import render_to_response, get_object_or_404
from book.models import Book

def index(request):

    book_list = Book.objects.all().order_by('title')

    return render_to_response('index.html', {'book_list':book_list})

def book(request, book_id):

	book = get_object_or_404(Book, id=book_id)

	return render_to_response('book.html', {'book':book})