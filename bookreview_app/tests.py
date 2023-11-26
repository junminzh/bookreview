from django.test import TestCase
from django.urls import reverse
from .models import Book
from selenium import webdriver
from selenium.webdriver.common.by import By


# setUpTestData() lets us create initial data once, at the class level,
# for the entire TestCase. This technique allows for much faster tests
# than creating the data from scratch for each individual unit test
# within the class.
class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(title="Designing Data Structures in Java",
                                       author="Albert A. Brouillette",
                                       genre="Narrative",
                                       description="A Software Engineering Approach")
        print("Test Case - setUpTestData - Passed!")

    # Check that the data in our mock database matches what was initially created in setUpTestData
    def test_model_content(self):
        self.assertEqual(self.book.title, "Designing Data Structures in Java")
        self.assertEqual(self.book.author, "Albert A. Brouillette")
        self.assertEqual(self.book.genre, "Narrative")
        self.assertEqual(self.book.description, "A Software Engineering Approach")
        print("Test Case - test_model_content - Passed!")

    # Check the URL to confirm it returns an HTTP 200 Response
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/books/")
        self.assertEqual(response.status_code, 200)
        print("Test Case - test_url_exists_at_correct_location - Passed!")

    
    # Uses reverse to call the URL name,
    # Check for an HTTP 200 Response,
    # Verify the correct template is used, and
    # Confirm that HTML content matches what is expected.
    def test_listpage(self):
        response = self.client.get(reverse("books"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bookreview_app/book_list.html")
        # print("test_homepage Response:")
        # print(response)
        self.assertContains(response, "Designing Data Structures in Java")
        print("Test Case - test_homepage - Passed!")


    # selenium webdriver test - login passed
    def test_login_passed(self):
        driver = webdriver.Chrome()

        driver.get("http://127.0.0.1:8000/accounts/login/?next=/")
        driver.implicitly_wait(1)

        title = driver.title
        self.assertEqual(title, "BookOcean")

        username_text_box = driver.find_element(by=By.NAME, value="username")
        password_text_box = driver.find_element(by=By.NAME, value="password")
        login_button = driver.find_element(by=By.NAME, value="login")

        username_text_box.send_keys("reviewer1")
        password_text_box.send_keys("rw1_pass")
        login_button.click()

        message = driver.find_element(by=By.CLASS_NAME, value="text-success")
        value = message.text
        self.assertEqual(value, "Welcome to BookOcean!")
        print("Test Case - test_login_passed - Passed!")
        driver.quit()


    # selenium webdriver test - login failed with wrong password
    def test_login_failed(self):
        driver = webdriver.Chrome()

        driver.get("http://127.0.0.1:8000/accounts/login/?next=/")
        driver.implicitly_wait(1)

        title = driver.title
        self.assertEqual(title, "BookOcean")

        username_text_box = driver.find_element(by=By.NAME, value="username")
        password_text_box = driver.find_element(by=By.NAME, value="password")
        login_button = driver.find_element(by=By.NAME, value="login")

        username_text_box.send_keys("reviewer1")
        password_text_box.send_keys("failed_pass")
        login_button.click()

        message = driver.find_element(by=By.ID, value="message")
        value = message.text
        self.assertEqual(value, "Your username and password didn't match. Please try again.")
        print("Test Case - test_login_failed - Passed!")
        driver.quit()

