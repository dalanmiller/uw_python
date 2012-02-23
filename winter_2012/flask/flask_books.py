"""
This flask app takes the bookdb and creates an index of the books on the index page 

Each listing also has a button to an individual book page where once can find the 
details of the book, including a picture of the book cover and description
courtesy of Google Books API. 

Uses the default jinja templating to render both the index page and the individual 
book page. 

The requests module is used to grab the Google Books API json and the json
library to load the json as a Python dictionary.

"""

from flask import Flask, request, url_for, render_template, redirect
import bookdb
import bookdb_test
import requests
import json
from operator import itemgetter


books = Flask(__name__)

books.debug = True

db = bookdb.BookDB()

@books.route('/', methods=['GET'])
def home():
	#Get all the books in this weird method
	b = [(x, db.title_info(x)) for x in [x['id'] for x in db.titles()]]

	#sort the list based on the id
	books = sorted(b, key=itemgetter(0))

	return render_template('index.html', books = books)

@books.route('/book/<book_id>', methods=['GET'])
def book(book_id):
	if book_id and book_id in [x['id'] for x in db.titles()]:
		book = db.title_info(book_id)

		#make the request
		r = requests.get("https://www.googleapis.com/books/v1/volumes?q=%s" % (book['isbn'])).content 

		#jsonify
		r_json = json.loads(r)

		#isolate the book description
		book_desc = r_json['items'][0]['volumeInfo']['description']

		#isolate a book image
		book_image = r_json['items'][0]['volumeInfo']['imageLinks']['thumbnail']

		return render_template('book.html', book = book, i = book_image, d = book_desc)
	
	else:
		return redirect('/')


if __name__ == "__main__":
	
	#bookdb_test.test_list_books()
	#bookdb_test.test_get_book_info()
	books.run(port=6001)
	

	