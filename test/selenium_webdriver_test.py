from selenium import webdriver
from selenium.webdriver.common.by import By


def test_eight_components():
    driver = webdriver.Chrome()

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    driver.implicitly_wait(10035)

    title = driver.title
    assert title == "Web form"

    driver.implicitly_wait(11035)

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    driver.implicitly_wait(1035)

    text_box.send_keys("Selenium")
    submit_button.click()
    driver.implicitly_wait(35)

    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"
    driver.implicitly_wait(35)
    print("OK!")
    driver.implicitly_wait(35)
    driver.quit()


def main():
    test_eight_components()


if __name__ == '__main__':
    main()

