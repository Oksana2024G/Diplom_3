class Url:
    TEST_URL = 'https://stellarburgers.nomoreparties.site/'  # Базовый URL (без завершающего слеша)

    FORGOT_PASSWORD_URL = TEST_URL + 'forgot-password'
    RESET_PASSWORD_URL = TEST_URL + 'reset-password'
    LOGIN_URL = TEST_URL + 'login'
    ORDER_HISTORY_URL = TEST_URL + 'account/order-history'
    LIST_OF_ORDER_URL = TEST_URL + 'feed'


class UrlApi:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    CREATE_USER_URL = '/api/auth/register'
    USER_URL = '/api/auth/user'
