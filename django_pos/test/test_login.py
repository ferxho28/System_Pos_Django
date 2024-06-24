
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    firefox_options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=firefox_options)
    yield driver
    driver.quit()

def test_login_component_renders_correctly(browser):
    # Navega a la página de login
    browser.get('http://127.0.0.1:8000/accounts/login/')
    
    # Verifica que los elementos de entrada y el botón están presentes
    username_input = browser.find_element(By.NAME, 'username')
    password_input = browser.find_element(By.NAME, 'password')
    login_button = browser.find_element(By.XPATH, '//button[text()="Login"]')

    assert username_input.is_displayed()
    assert password_input.is_displayed()
    assert login_button.is_displayed()
