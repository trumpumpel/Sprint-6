from selenium.webdriver.common.by import By


class MainPageLocators:
    FIRST_QUESTION = (By.XPATH, "//div[contains(text(), 'Сколько это стоит? И как оплатить?')]")
    SECOND_QUESTION = (By.XPATH, "//div[contains(text(), 'Хочу сразу несколько самокатов! Так можно?')]")
    THIRD_QUESTION = (By.XPATH, "//div[contains(text(), 'Как рассчитывается время аренды?')]")
    FOURTH_QUESTION = (By.XPATH, "//div[contains(text(), 'Можно ли заказать самокат прямо на сегодня?')]")
    FIFTH_QUESTION = (By.XPATH, "//div[contains(text(), 'Можно ли продлить заказ или вернуть самокат раньше?')]")
    SIXTH_QUESTION = (By.XPATH, "//div[contains(text(), 'Вы привозите зарядку вместе с самокатом?')]")
    SEVENTH_QUESTION = (By.XPATH, "//div[contains(text(), 'Можно ли отменить заказ?')]")
    EIGHTH_QUESTION = (By.XPATH, "//div[contains(text(), 'Я жизу за МКАДом, привезёте?')]")
    FIRST_ANSWER = (By.XPATH, "//p[contains(text(), 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.')]")
    SECOND_ANSWER = (By.XPATH, "//p[contains(text(), 'Пока что у нас так:')]")
    THIRD_ANSWER = (By.XPATH, "//p[contains(text(), 'Допустим, вы оформляете заказ на 8 мая.')]")
    FOURTH_ANSWER = (By.XPATH, "//p[contains(text(), 'Только начиная с завтрашнего дня.')]")
    FIFTH_ANSWER = (By.XPATH, "//p[contains(text(), 'Пока что нет!')]")
    SIXTH_ANSWER = (By.XPATH, "//p[contains(text(), 'Самокат приезжает к вам с полной зарядкой.')]")
    SEVENTH_ANSWER = (By.XPATH, "//p[contains(text(), 'Штрафа не будет,')]")
    EIGHTH_ANSWER = (By.XPATH, "//p[contains(text(), 'Всем самокатов!')]")
    UPPER_ORDER_BUTTON = (By.XPATH, "//*[@class='Button_Button__ra12g']")
    LOWER_ORDER_BUTTON = (By.XPATH, "//*[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    ORDER_HEADER = (By.XPATH, "//div[contains(text(), 'Для кого самокат')]")
