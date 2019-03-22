# Books and Authors

In this assignment from Coding Dojo I am using Django to implement an app that
keeps track of books and authors, through use of Object-Relational Mapping, creating
a many-to-many relationship between the Author and Book models.

Routes:
* / -- home route displays all books in the database and has a form to add a new book
* /books/<num> -- displays full information about a book, including authors
* /authors -- displays all authors in database, allows users to add an author
* /authors/<num> -- displays full information about an author, including books
