import pytest
import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.account_page import AccountPage


class TestOrderFeed:
    @allure.title('Проверка: при клике на заказ, открывается всплывающее окно с деталями')
    def test_click_order_open_details(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page.main_page_loading_wait()
        main_page.click_on_list_order_link()
        order_feed_page.click_on_order()
        main_page.main_page_loading_wait()
        assert order_feed_page.find_element_with_orders_details_on_window()

    @allure.title('Проверка: заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_order_history_in_feed(self, driver, create_user_and_get_token, login_user):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        account_page = AccountPage(driver)
        main_page.create_order()
        main_page.main_page_loading_wait()
        get_number_of_new_order = order_feed_page.wait_to_get_actual_order_number()
        main_page.main_page_loading_wait()
        order_feed_page.click_on_close_button_information_of_order()
        main_page.click_on_account_link()
        main_page.main_page_loading_wait()
        account_page.click_button_oder_histore()
        main_page.main_page_loading_wait()
        order_feed_page.check_order_in_history(get_number_of_new_order)
        main_page.click_on_list_order_link()
        assert order_feed_page.check_order_number_in_order_list(get_number_of_new_order)

    @allure.title('При создании нового заказа счётчики "Выполнено за всё время" и "Выполнено за сегодня" увеличиваются')
    @pytest.mark.parametrize("counter_type", ["total", "today"])
    def test_order_increases_total_and_daily_counts(self, driver, create_user_and_get_token, login_user, counter_type):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page.click_on_list_order_link()
        counter_method_name = order_feed_page.get_counter_method_name(counter_type) # Получаем имя метода получения значения счетчика
        get_counter_method = getattr(order_feed_page, counter_method_name) # Получаем начальное значение счетчика
        count_before = get_counter_method()
        main_page.click_on_constructor_link()
        main_page.create_order()
        main_page.main_page_loading_wait()
        order_feed_page.click_on_close_button_information_of_order()
        main_page.click_on_list_order_link()
        count_after = get_counter_method()
        assert count_after > count_before

    @allure.title('После создании нового заказа его номер появляется в резделе "В работе"')
    def test_order_number_appears_in_progress(self, driver, create_user_and_get_token, login_user):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page.main_page_loading_wait()
        main_page.create_order()
        new_order_number = order_feed_page.wait_to_get_actual_order_number()
        main_page.main_page_loading_wait()
        order_feed_page.click_on_close_button_information_of_order()
        main_page.main_page_loading_wait()
        main_page.click_on_list_order_link()
        main_page.main_page_loading_wait()
        updated_orders_in_progress = order_feed_page.get_order_numbers_in_progress()
        # Приводим оба значения к строковому виду без начального нуля
        assert str(int(new_order_number)) in [str(int(order)) for order in updated_orders_in_progress]
