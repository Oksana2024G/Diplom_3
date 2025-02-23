from selenium.webdriver.common.by import  By

class OrderFeedPageLocators:
    TOP_ORDER = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_list')]/li[1]/a")
    INFORMATION_OF_ORDER = (By.XPATH, "//p[@class='text text_type_digits-default mb-10 mt-5']")

    ORDER_NUMBER_IN_MODAL_WINDOW = (By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")
    BUTTON_CLOSE_ORDER = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")

    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")

    IN_PROGRESS_ORDERS_SECTION = (By.XPATH, "//p[text()='В работе:']/following-sibling::ul")
    ORDER_NUMBER_IN_PROGRESS = (By.XPATH, "//li[contains(@class, 'text_type_digits-default')]")
