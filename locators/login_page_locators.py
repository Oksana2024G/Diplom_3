from selenium.webdriver.common.by import  By

class LoginPageLocators:
    FORGOT_PASSWORD_LINK = (By.XPATH, "// a[text() = 'Восстановить пароль']")
    EMAIL_FIELD = (By.XPATH, "//input[@name='name']")
    BUTTON_RECOVER = (By.XPATH, "//button[text()='Восстановить']")
    PLACEHOLDER_CODE = (By.XPATH, "//label[contains(text(), 'Введите код из письма')]")
    ICON_EYE = (By.XPATH, "//div[@class='input__icon input__icon-action']")
    INPUT_VISIBLE_PASSWORD_FIELD = (By.XPATH, ".//label[text()='Пароль']/../"
                                             "input[@type='text' and @name='Введите новый пароль']")
