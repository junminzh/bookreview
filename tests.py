from django.test import TestCase
from django.urls import reverse
from bookreview_app.models import Book


# setUpTestData() lets us create initial data once, at the class level,
# for the entire TestCase. This technique allows for much faster tests 
# than creating the data from scratch for each individual unit test 
# within the class.
class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Book.objects.create(title="Designing Data Structures in Java", 
                                       author="Albert A. Brouillette",
                                       genre="Narrative",
                                       description="A Software Engineering Approach")
    
    # Check that the data in our mock database matches what was initially created in setUpTestData
    def test_model_content(self):
        self.assertEqual(self.book.title, "Designing Data Structures in Java")
        self.assertEqual(self.book.author, "Albert A. Brouillette")
        self.assertEqual(self.book.genre, "Narrative")
        self.assertEqual(self.book.description, "A Software Engineering Approach")

    # Check the URL to confirm it returns an HTTP 200 Response
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/books/")
        self.assertEqual(response.status_code, 200)

    # TODO:change the func name
    # Uses reverse to call the URL name, 
    # Check for an HTTP 200 Response, 
    # Verify the correct template is used, and 
    # Confirm that HTML content matches what is expected.
    def test_homepage(self):
        response = self.client.get(reverse("books"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bookreview_app/templates/bookreview_app/book_list.html")
        self.assertContains(response, "Designing Data Structures in Java")
        