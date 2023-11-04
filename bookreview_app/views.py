from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from django.views import generic
from .forms import BookForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render( request, 'bookreview_app/index.html')


class BookListView(generic.ListView):
    model = Book
class BookDetailView(generic.DetailView):
    model = Book

def createBook(request):
    form = BookForm()
   #  portfolio = Portfolio.objects.get(pk=portfolio_id)
    
    if request.method == 'POST':
        # Create a new dictionary with form data and portfolio_id
        book_data = request.POST.copy()
      #   project_data['portfolio_id'] = portfolio_id    
        form = BookForm(book_data)
        if form.is_valid():
            # Save the form without committing to the database
            book = form.save(commit=False)
            # Set the portfolio relationship
            # project.portfolio = portfolio
            book.save()

            # Redirect back to the portfolio detail page
            return redirect('books')

    context = {'form': form}
    return render(request, 'bookreview_app/book_form.html', context) 

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


def deleteBook(request, pk):
    book = Book.objects.get(id=pk)
    if request.method == "POST":
        book.delete()
        messages.success(request, "The book has been deleted.")
        # Redirect back to the book list page
        return redirect('books')
    
    context = {'item': book}
    return render(request, 'bookreview_app/book_delete.html', context)   



# class StudentListView(generic.ListView):
#     model = Student
# class StudentDetailView(generic.DetailView):
#     model = Student


# class PortfolioListView(generic.ListView):
#     model = Portfolio
# class PortfolioDetailView(generic.DetailView):
#     model = Portfolio
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get the context
#         context = super(PortfolioDetailView, self).get_context_data(**kwargs)
#         # Create 'projects' and add it to the context
#         #context['projects'] = Project.objects.filter(portfolio__pk=self.kwargs['pk'])
#         context['projects'] = Project.objects.filter(portfolio=kwargs['object'])
#         # context['projects'] = Project.objects.all()
#         return context


# class ProjectListView(generic.ListView):
#     model = Project
# class ProjectDetailView(generic.DetailView):
#     model = Project


# def createProject(request, portfolio_id):
#     form = ProjectForm()
#     portfolio = Portfolio.objects.get(pk=portfolio_id)
    
#     if request.method == 'POST':
#         # Create a new dictionary with form data and portfolio_id
#         project_data = request.POST.copy()
#         project_data['portfolio_id'] = portfolio_id    
#         form = ProjectForm(project_data)
#         if form.is_valid():
#             # Save the form without committing to the database
#             project = form.save(commit=False)
#             # Set the portfolio relationship
#             project.portfolio = portfolio
#             project.save()

#             # Redirect back to the portfolio detail page
#             return redirect('portfolio-detail', portfolio_id)

#     context = {'form': form}
#     return render(request, 'portfolio_app/project_form.html', context) 

# def updateProject(request, portfolio_id, project_id):
#     project = Project.objects.get(id=project_id)
#     form = ProjectForm(instance=project)
#     portfolio = Portfolio.objects.get(pk=portfolio_id)

#     if request.method == 'POST':
#         # Retrieve the portfolio based on the portfolio_id
#         # print('printing POST:', request.POST)
#         # print('project id:', project_id)
#         form = ProjectForm(request.POST, instance=project)
        
#         if form.is_valid():
#             # Save the form without committing to the database
#             project = form.save(commit=False)
#             # Set the portfolio relationship
#             project.portfolio = portfolio
#             project.save()
#             # Redirect back to the portfolio detail page
#             return redirect('portfolio-detail', portfolio_id)

#     context = {'form' :form}
#     return render(request, 'portfolio_app/project_form.html', context) 


# def deleteProject(request, portfolio_id, project_id):
#     project = Project.objects.get(id=project_id)
#     if request.method == "POST":
#         project.delete()
#         messages.success(request, "The project has been deleted.")
        
#         return redirect('portfolio-detail', portfolio_id)
    
#     context = {'item':project, 'portfolio_id':portfolio_id}
#     return render(request, 'portfolio_app/project_delete.html', context)   


# def updatePortfolio(request, portfolio_id):
#     portfolio = Portfolio.objects.get(id=portfolio_id)
#     form = PortfolioForm(instance=portfolio)

#     if request.method == 'POST':
#         # Retrieve the portfolio based on the portfolio_id
#         # print('printing POST:', request.POST)
#         # print('portfolio:', portfolio_id)
#         form = PortfolioForm(request.POST)
#         if form.is_valid():
#             form.save()

#         # Redirect back to the portfolio detail page
#             return redirect('portfolio-detail', portfolio_id)

#     context = {'form': form}
#     return render(request, 'portfolio_app/portfolio_form.html', context)  
