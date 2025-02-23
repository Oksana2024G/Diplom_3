import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    @allure.step('Дождаться загрузки страницы')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY, 30)

    @allure.step('Клик по кнопке "Войти в аккаунт"')
    def click_on_login_button(self):
        self.main_page_loading_wait()
        self.click_on_element(MainPageLocators.BUTTON_LOGIN)

    @allure.step('Клик по ссылке "Личный кабинет"')
    def click_on_account_link(self):
        self.main_page_loading_wait()
        self.click_on_element(MainPageLocators.PROFILE_LINK)

    @allure.step('Клик по ссылке "Конструктор"')
    def click_on_constructor_link(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_LINK)
        self.main_page_loading_wait()

    @allure.step('Клик по ссылке "Лента заказов"')
    def click_on_list_order_link(self):
        self.main_page_loading_wait()
        self.click_on_element(MainPageLocators.LIST_ORDER_LINK)
        self.main_page_loading_wait()

    @allure.step('Клик по ингредиенту')
    def click_on_ingredient(self):
        self.click_on_element(MainPageLocators.INGREDIENT_BUN_R2_D3)
        self.main_page_loading_wait()

    @allure.step('Проверка видимости элемента "Детали ингридиента"')
    def find_element_with_ingredients_details_on_window(self):
        element = self.wait_for_element(MainPageLocators.INGREDIENT_DETAILS_TEXT, 20)
        return element.text

    @allure.step('Клик по крестику всплывающего окна')
    def click_on_cross_button_modal_window(self):
        self.click_on_element(MainPageLocators.CROSS_BUTTON)

    @allure.step('Проверка НЕвидимости элемента "Детали ингридиента"')
    def check_invisible_ingredient_detail_on_window(self):
        return self.wait_for_element_hide(MainPageLocators.INGREDIENT_DETAILS_TEXT)

    @allure.step('Перетащить ингредиент булка в корзину')
    def drag_and_drop_ingredient_bun_R2_D3(self):
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_BUN_R2_D3, MainPageLocators.BASKET)

    @allure.step('Перетащить ингредиент соус в корзину')
    def drag_and_drop_ingredient_sauce_spicy(self):
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_SAUCE_SPICY, MainPageLocators.BASKET)

    @allure.step('Дождаться элемента количество ингредиента')
    def counter_value_bun_R2_D3(self):
        return self.wait_for_element(MainPageLocators.COUNTER_BUN_R2_D3)

    @allure.step('Клик на кнопку Оформить заказ')
    def click_make_order_button(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON)

    @allure.step('Проверка видимости элемента "Идентификатор заказа"')
    def find_element_id_order(self):
        return self.wait_for_element(MainPageLocators.ID_ORDER)

    @allure.step('Создаем заказ и передаем его номер')
    # Не оформлено в фикстуру, т.к. нет функционала для удаления ненужных заказов
    def create_order(self):
        self.main_page_loading_wait()
        self.drag_and_drop_ingredient_bun_R2_D3()
        self.drag_and_drop_ingredient_sauce_spicy()
        self.click_make_order_button()
        self.main_page_loading_wait()
        self.find_element_id_order()
