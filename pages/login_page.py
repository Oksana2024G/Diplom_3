import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):
    @allure.step('Клик по ссылке "Восстановить пароль"')
    def click_forgot_password_link(self):
        self.click_on_element(LoginPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step("Заполнить поле Email")
    def fill_field_email(self, email):
        self.send_keys_to_input(LoginPageLocators.EMAIL_FIELD, email)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_button_recover(self):
        self.click_on_element(LoginPageLocators.BUTTON_RECOVER)

    @allure.step('Дождаться поля "Введите код из письма"')
    def find_field_for_code(self):
        self.wait_for_element(LoginPageLocators.PLACEHOLDER_CODE)

    @allure.step('Клик по иконке глаз')
    def click_on_eye_show_password(self):
       self.click_on_element(LoginPageLocators.ICON_EYE)

    @allure.step('Определить тип данных в поле пароль')
    def get_attribute_password_field(self):
        return self.get_attribute(LoginPageLocators.INPUT_VISIBLE_PASSWORD_FIELD, "type")
