import pytest
import allure
from pages.main_page import MainPage
from pages.account_page import AccountPage
from curl import *


class TestPersonalAccount:
    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    def test_click_personal_account_button(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        main_page.main_page_loading_wait()
        main_page.click_on_account_link()
        current_url = account_page.get_current_url()
        assert current_url == Url.LOGIN_URL

    @allure.title('Проверка перехода в раздел «История заказов»')
    def test_click_button_order_history(self, driver, create_user_and_get_token, login_user):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        account_page.click_button_personal_account()
        main_page.main_page_loading_wait()
        account_page.click_button_oder_histore()
        current_url = account_page.get_current_url()
        assert current_url == Url.ORDER_HISTORY_URL

    @allure.title('Проверка выхода из аккаунта')
    def test_account_logout(self, driver, create_user_and_get_token, login_user):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        account_page.click_button_personal_account()
        main_page.main_page_loading_wait()
        account_page.click_logout_button()
        main_page.main_page_loading_wait()
        assert account_page.wait_login_button_clickable()
