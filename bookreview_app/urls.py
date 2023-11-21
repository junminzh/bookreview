from django.urls import path
from . import views

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create urlw
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),

#path to book list and detail views
path('books/', views.BookListView.as_view(), name= 'books'),
path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),

#path to create a book
path('books/create_book/', views.createBook, name='create_book'),

#path to create a book
path('update_book/<int:pk>', views.updateBook, name='update_book'),

#path to delete a book
path('delete_book/<int:pk>/', views.deleteBook, name='delete_book'),

#path to register
path('accounts/register/', views.registerPage, name = 'register_page'),
]
