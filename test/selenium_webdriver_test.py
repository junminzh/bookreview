from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_passed():
    driver = webdriver.Chrome()

    driver.get("http://127.0.0.1:8000/accounts/login/?next=/")
    driver.implicitly_wait(1)

    title = driver.title
    assert title == "BookOcean"

    username_text_box = driver.find_element(by=By.NAME, value="username")
    password_text_box = driver.find_element(by=By.NAME, value="password")
    login_button = driver.find_element(by=By.NAME, value="login")

    username_text_box.send_keys("reviewer1")
    password_text_box.send_keys("rw1_pass")
    login_button.click()

    message = driver.find_element(by=By.CLASS_NAME, value="text-success")
    value = message.text
    assert value == "Welcome to BookOcean!"
    print("Test Case - test_login_passed - Passed!")
    driver.quit()

def test_login_failed():
    driver = webdriver.Chrome()

    driver.get("http://127.0.0.1:8000/accounts/login/?next=/")
    driver.implicitly_wait(1)

    title = driver.title
    assert title == "BookOcean"

    username_text_box = driver.find_element(by=By.NAME, value="username")
    password_text_box = driver.find_element(by=By.NAME, value="password")
    login_button = driver.find_element(by=By.NAME, value="login")

    username_text_box.send_keys("reviewer1")
    password_text_box.send_keys("failed_pass")
    login_button.click()

    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Your username and password didn't match. Please try again."
    print("Test Case - test_login_failed - Passed!")
    driver.quit()


def main():
    test_login_passed()
    test_login_failed()


if __name__ == '__main__':
    main()

