from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from django.views import generic
from .forms import BookForm, CreateUserForm
from django.contrib import messages
from .decorators import allowed_users

# Create your views here.
def index(request):
    return render( request, 'bookreview_app/index.html')


class BookListView(generic.ListView):
    model = Book
class BookDetailView(generic.DetailView):
    model = Book

@login_required
@allowed_users(allowed_roles=['Reviewers'])
def createBook(request):
    form = BookForm()
    if request.method == 'POST':
        # Create a new dictionary with form data and portfolio_id
        book_data = request.POST.copy()
        form = BookForm(book_data)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()

            # Redirect back to the portfolio detail page
            return redirect('books')

    context = {'form': form}
    return render(request, 'bookreview_app/book_form.html', context) 

@login_required
@allowed_users(allowed_roles=['Reviewers'])
def updateBook(request, pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()

            # Redirect back to the book detail page
            return redirect('book-detail', book.id)

    context = {'form': form}
    return render(request, 'bookreview_app/book_form.html', context) 


@login_required
@allowed_users(allowed_roles=['Reviewers'])
def deleteBook(request, pk):
    book = Book.objects.get(id=pk)
    if request.method == "POST":
        book.delete()
        messages.success(request, "The book has been deleted.")
        # Redirect back to the book list page
        return redirect('books')
    
    context = {'item': book}
    return render(request, 'bookreview_app/book_delete.html', context)   


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid(): 
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='Reviewers')
            user.groups.add(group)
            messages.success(request, 'Account was created for' + username)
            return redirect('login')
    
    context = {'form':form}
    return render(request, 'registration/register.html', context)
