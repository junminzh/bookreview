from django.forms import ModelForm
from .models import Book
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#create class for book form
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

#create class for user form
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

#create CreateUserForm
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        # fields = ['username', 'email', 'password', 'password2']
        # fields = ['groups', 'username', 'email']
        fields = ['username', 'email']
        # fields = '__all__'
        # fields = 'REQUIRED_FIELDS'
