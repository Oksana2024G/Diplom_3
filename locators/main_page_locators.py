from selenium.webdriver.common.by import  By

class MainPageLocators:
    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")
    BUTTON_LOGIN = (By.XPATH, '//button[text()="Войти в аккаунт"]')

    PROFILE_LINK = (By.XPATH, "//a[@href='/account']")

    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
    LIST_ORDER_LINK = (By.XPATH, "//a[@href='/feed']")

    INGREDIENT_BUN_R2_D3 = (By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']")
    INGREDIENT_DETAILS_TEXT = (By.XPATH, "//h2[text()='Детали ингредиента']")
    CROSS_BUTTON = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")

    BASKET = (By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket')]")
    INGREDIENT_SAUCE_SPICY = (By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa72']/img")
    COUNTER_BUN_R2_D3 = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']//p[@class='counter_counter__num__3nue1']")


    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ID_ORDER = (By.XPATH, "//p[text()='идентификатор заказа']")
