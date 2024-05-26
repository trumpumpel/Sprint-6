from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_ORDER = (
        By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_ORDER = (
        By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_ORDER = (
        By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_ORDER = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_ORDER = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    FURTHER_BUTTON = (By.XPATH, "//button[contains(text(), 'Далее')]")
    UPPER_ORDER_BUTTON = (By.XPATH, "//*[@class='Button_Button__ra12g']")
    RENTAL_PERIOD = (By.CSS_SELECTOR, ".Dropdown-root")
    DATE_DELIVER = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    COMMENT_ORDER = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    SCOOTER_COLOR_ELEMENT = (By.CSS_SELECTOR, ".Order_Checkboxes__3lWSI")
    ORDER_PLACED = (By.XPATH, "//div[text()= 'Заказ оформлен']")
    ORDER_BTN = (By.XPATH, "//*[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    APPROVAL_BTN = (By.XPATH, "//button[text()= 'Да']")
    YANDEX = (By.XPATH, "//img[@alt= 'Yandex']")
    SCOOTER = (By.XPATH, "//img[@alt= 'Scooter']")
    CALENDAR = (By.XPATH, "//div[text()='1']")
    DZEN_BUTTON = By.CSS_SELECTOR, ".Header_LogoYandex__3TSOI"
