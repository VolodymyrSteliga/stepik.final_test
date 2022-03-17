from selenium.webdriver.common.by import By
from selenium import webdriver


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    CORECT_URL = webdriver.Chrome.current_url  # корректный url адрес
    LOG_FORM = (By.CSS_SELECTOR, "#login_form")  # что есть форма логина
    REG_FORM = (By.CSS_SELECTOR, "#register_form")  # fорма регистрации на
