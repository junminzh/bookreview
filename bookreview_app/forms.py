from django.forms import ModelForm
from .models import Book

#create class for book form
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


# #create class for review form
# class ReviewForm(ModelForm):
#     class Meta:
#         model = Review
#         fields = '__all__'