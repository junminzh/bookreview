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

# #path to portfolio list and detail views
# path('portfolios/', views.PortfolioListView.as_view(), name= 'portfolio'),
# path('portfolio/<int:pk>', views.PortfolioDetailView.as_view(), name='portfolio-detail'),

# #path to project list and detail views
# path('projects/', views.ProjectListView.as_view(), name= 'project'),
# path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),

# #path to create a project
# path('portfolio/<int:portfolio_id>/create_project/', views.createProject, name='create_project'),

# #path to update a project
# path('portfolio/<int:portfolio_id>/update_project/<int:project_id>/', views.updateProject, name='update_project'),

# #path to delete a project
# path('portfolio/<int:portfolio_id>/delete_project/<int:project_id>/', views.deleteProject, name='delete_project'),

# #path to update a portfolio
# path('portfolio/update_portfolio/<int:portfolio_id>/', views.updatePortfolio, name='update_portfolio'),

]
