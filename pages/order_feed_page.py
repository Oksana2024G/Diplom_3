import allure
from pages import main_page
from pages.base_page import BasePage
from pages.main_page import MainPage
from locators.order_feed_page_locators import OrderFeedPageLocators

class OrderFeedPage(BasePage):
    @allure.step('Клик по заказу')
    def click_on_order(self):
        self.click_on_element(OrderFeedPageLocators.TOP_ORDER)

    @allure.step('Проверка видимости элемента "Детали заказа"')
    def find_element_with_orders_details_on_window(self):
        return self.wait_for_element(OrderFeedPageLocators.INFORMATION_OF_ORDER)

    @allure.step('Проверка: ждем и забираем "Номер заказа"')
    def wait_to_get_actual_order_number(self):
        return self.wait_for_text_to_change(OrderFeedPageLocators.ORDER_NUMBER_IN_MODAL_WINDOW, '9999')

    @allure.step('Закрыть окно с информацией о заказе')
    def click_on_close_button_information_of_order(self):
        self.click_on_element(OrderFeedPageLocators.BUTTON_CLOSE_ORDER)

    @allure.step('Проверяем текст закза на странице История заказов')
    def check_order_in_history(self, expected_value):
        return self.check_text_on_page()

    @allure.step('Проверяем номер заказа на странице Список заказов')
    def check_order_number_in_order_list(self, expected_value):
        return self.check_text_on_page()

    @allure.step("Получить значение счетчика 'Выполнено всего'")
    def get_total_orders_count(self):
        element = self.wait_for_element(OrderFeedPageLocators.TOTAL_ORDERS_COUNTER)
        return int(element.text)

    @allure.step("Получить значение счетчика 'Выполнено сегодня'")
    def get_today_orders_count(self):
        element = self.wait_for_element(OrderFeedPageLocators.TODAY_ORDERS_COUNTER)
        return int(element.text)

    @allure.step("Получить список номеров заказов в разделе 'В работе'")
    def get_order_numbers_in_progress(self):
       self.wait_for_element_presence(OrderFeedPageLocators.IN_PROGRESS_ORDERS_SECTION)
       order_elements = self.driver.find_elements(*OrderFeedPageLocators.ORDER_NUMBER_IN_PROGRESS)
       return [element.text for element in order_elements]
