from selenium.webdriver.common.by import  By

class AccountPageLocators:
    EMAIL = (By.XPATH, ".//div[contains(@class, 'Auth_login')]//label[text()='Email']/../input[@name='name']")
    PASSWORD = (By.XPATH, ".//div[contains(@class, 'Auth_login')]//label[text()='Пароль']/../input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH,"//button[contains(text(), 'Войти')]")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")
    ORDER_HISTORE_BUTTON = (By.XPATH, ".//nav[contains(@class, 'Account_nav')]//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
