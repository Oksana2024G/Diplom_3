import pytest
import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from curl import *

class TestForgotPassword:
    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль» ')
    def test_click_recover_password_button(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.click_on_login_button()
        login_page.click_forgot_password_link()
        current_url = login_page.get_current_url()
        assert current_url == Url.FORGOT_PASSWORD_URL

    @allure.title('Проверка ввода почты и клик по кнопке «Восстановить»')
    def test_enter_email_and_click_recover(self, driver, create_user_and_get_token):
        user_data, access_token = create_user_and_get_token
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.click_on_login_button()
        login_page.click_forgot_password_link()
        login_page.fill_field_email(user_data["email"])
        login_page.click_button_recover()
        main_page.main_page_loading_wait()
        login_page.find_field_for_code()
        current_url = login_page.get_current_url()
        assert current_url == Url.RESET_PASSWORD_URL

    @allure.title('Проверка: клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_show_hide_password_input_active(self, driver, create_user_and_get_token):
        user_data, access_token = create_user_and_get_token
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.click_on_login_button()
        login_page.click_forgot_password_link()
        login_page.fill_field_email(user_data["email"])
        login_page.click_button_recover()
        main_page.main_page_loading_wait()
        login_page.click_on_eye_show_password()
        assert login_page.get_attribute_password_field() == 'text'
