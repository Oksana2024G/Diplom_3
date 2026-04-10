import allure
from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from curl import *

class AccountPage(BasePage):
    @allure.step("Заполнить поле Email и Пароль")
    def fill_field_email_and_passord(self, email, passord):
        self.send_keys_to_input(AccountPageLocators.EMAIL, email)
        self.send_keys_to_input(AccountPageLocators.PASSWORD, passord)

    @allure.step("Кликнуть по кнопке Войти")
    def click_button_login(self):
        self.click_on_element(AccountPageLocators.LOGIN_BUTTON)

    @allure.step("Кликнуть по кнопке Личный кабинет")
    def click_button_personal_account(self):
        self.click_on_element(AccountPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Кликнуть по кнопке История заказов")
    def click_button_oder_histore(self):
        self.click_on_element(AccountPageLocators.ORDER_HISTORE_BUTTON, 24)

    @allure.step("Кликнуть по кнопке Выход")
    def click_logout_button(self):
        self.driver.delete_all_cookies()
        self.click_on_element(AccountPageLocators.LOGOUT_BUTTON, 17)

    @allure.step("Дождаться кликабельности кнопки Войти")
    def wait_login_button_clickable(self):
        return self.wait_for_clickable_element(AccountPageLocators.LOGIN_BUTTON, 30)