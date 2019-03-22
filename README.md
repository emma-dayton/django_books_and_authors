# Books and Authors

In this assignment from Coding Dojo I am using Django to implement an app that
keeps track of books and authors, through use of Object-Relational Mapping, creating
a many-to-many relationship between the Author and Book models.

Routes:
* / -- Home route that displays a welcome message and offers two paths, books or authors, into the app
* /books -- displays all books in the database
* /books/<num> -- displays full information about a book, including authors
* /books/<num>/add_author -- adds an author to a specific book, redirects to the book's info page
* /books/<num>/remove_<author_id> -- removes an author from a specific book, redirects to the book's info page
* /books/add_book -- provides a form to add a new book to the database
* /books/add_book/new -- submits a form to add a new book to the database, redirects to book's info page
* /books/<num>/edit -- displays pre-populated form to update info of a book
* /books/<num>/edit/submit -- submits form to update info of a book, redirects to book's info page
* /books/<num>/remove -- removes a book from the database

* /authors -- displays all authors in database, allows users to add an author
* /authors/<num> -- displays full information about an author, including books
* /authors/<num>/add_book -- adds a book to a specific author, redirects to the author's info page
* /authors/<num>/remove_<book_id> -- removes a book from a specific author, redirects to the author's info page
* /authors/add_author -- provides a form to add a new author to the database
* /authors/add_author/new -- submits a form to add a new author to the database, redirects to author's info page
* /authors/<num>/edit -- displays pre-populated form to update info of an author
* /authors/<num>/edit/submit -- submits form to update info of a author, redirects to author's info page
* /authors/<num>/remove -- removes an author from the database
