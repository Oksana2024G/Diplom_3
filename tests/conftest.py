import pytest
import requests
from generators import Person
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import MainPage
from pages.account_page import AccountPage
from curl import *
from pages.order_feed_page import OrderFeedPage


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        chrome_options = ChromeOptions()
        chrome_service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        driver.set_window_size(1920, 1080)
        driver.get(Url.TEST_URL)
    elif request.param == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.profile = webdriver.FirefoxProfile()
        firefox_service = FirefoxService()
        driver = webdriver.Firefox(service=firefox_service, options=firefox_options)
        driver.set_window_size(1920, 1080)
        driver.get(Url.TEST_URL)
    yield driver
    driver.quit()

    # Создаем тестового пользователя и удаляем после теста
@pytest.fixture(scope="function")
def create_user_and_get_token():
    user_data = Person.generate_user_body()
    register_response = requests.post(f'{UrlApi.BASE_URL}{UrlApi.CREATE_USER_URL}', json=user_data)
    access_token = register_response.json().get("accessToken")
    yield user_data, access_token  # возвращаем user_data и accessToken
    delete_response = requests.delete(f'{UrlApi.BASE_URL}{UrlApi.USER_URL}', headers={"Authorization": f"{access_token}"})

@pytest.fixture
def login_user(driver, create_user_and_get_token):
    user_data = create_user_and_get_token[0]
    main_page = MainPage(driver)
    account_page = AccountPage(driver)
    main_page.main_page_loading_wait()
    main_page.click_on_account_link()
    account_page.fill_field_email_and_passord(user_data["email"], user_data["password"])
    main_page.main_page_loading_wait()
    account_page.click_button_login()
    main_page.main_page_loading_wait()

@pytest.fixture
def prepared_order(driver, create_user_and_get_token, login_user):
    main_page = MainPage(driver)
    order_feed_page = OrderFeedPage(driver)
    account_page = AccountPage(driver)
    main_page.create_order()
    main_page.main_page_loading_wait()
    return main_page, order_feed_page, account_page
