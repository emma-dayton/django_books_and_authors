from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index),
  url(r'^books$', views.books),
  url(r'^books/(?P<num>\d+)$', views.book_info),
  url(r'^books/(?P<num>\d+)/add_author$', views.add_book_author),
  url(r'^books/(?P<num>\d+)/remove_(?P<author_id>\d+)$', views.remove_book_author), #do this one
  url(r'^books/add_book$', views.add_book),
  url(r'^books/add_book/new$', views.add_book_new),
  url(r'^books/(?P<num>\d+)/edit$', views.edit_book),
  url(r'^books/(?P<num>\d+)/edit/submit$', views.edit_book_submit),
  url(r'^books/(?P<num>\d+)/remove_book$', views.remove_book),
  url(r'^authors$', views.authors),
  url(r'^authors/(?P<num>\d+)$', views.author_info),
  url(r'^authors/(?P<num>\d+)/add_book$', views.add_to_bibliography),
  url(r'^authors/add_author$', views.add_author),
  url(r'^authors/add_author/new$', views.add_author_new),
  url(r'^authors/(?P<num>\d+)/remove_(?P<book_id>\d+)$', views.remove_from_bibliography), # do this one
  url(r'^authors/(?P<num>\d+)/edit$', views.author_edit),
  url(r'^authors/(?P<num>\d+)/edit/submit$', views.author_edit_submit),
  url(r'^authors/(?P<num>\d+)/remove_author$', views.remove_author),
]
