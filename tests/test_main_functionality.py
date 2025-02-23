import pytest
import allure
from pages.main_page import MainPage
from curl import *

class TestMainFunctionality:
    @allure.title('Проверка перехода по клику на «Конструктор»')
    def test_click_on_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        main_page.click_on_account_link()
        main_page.click_on_constructor_link()
        current_url = main_page.get_current_url()
        assert current_url == Url.TEST_URL

    @allure.title('Проверка перехода по клику на «Лента заказов»')
    def test_click_on_list_order_button(self, driver):
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        main_page.click_on_list_order_link()
        current_url = main_page.get_current_url()
        assert current_url == Url.LIST_OF_ORDER_URL

    @allure.title('Проверка появления всплывающего окна с деталями по клику на ингредиент')
    def test_click_on_ingredient_button(self, driver):
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        main_page.click_on_ingredient()
        assert main_page.find_element_with_ingredients_details_on_window()

    @allure.title('Проверка закрытия всплывающего окна по клику на крестик')
    def test_click_on_cross_button_modal_window(self, driver):
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        main_page.click_on_ingredient()
        main_page.find_element_with_ingredients_details_on_window()
        main_page.click_on_cross_button_modal_window()
        assert main_page.check_invisible_ingredient_detail_on_window()

    @allure.title('Проверка: при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_add_ingredient_in_basket_counter_growth(self, driver):
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        counter_element_before = main_page.counter_value_bun_R2_D3()
        counter_value_before = int(counter_element_before.text)
        main_page.drag_and_drop_ingredient_bun_R2_D3()
        counter_element_after = main_page.counter_value_bun_R2_D3()
        counter_value_after = int(counter_element_after.text)
        assert counter_value_before < counter_value_after

    @allure.title('Проверка: залогиненный пользователь может оформить заказ')
    def test_logged_user_can_place_order(self, driver, create_user_and_get_token, login_user):
        main_page = MainPage(driver)
        main_page.create_order()
        assert main_page.find_element_id_order()
