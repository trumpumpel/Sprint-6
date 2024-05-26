from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data import URL, ADDRESS, METRO, NAME, SURNAME, PHONE, COLORS
from conftest import driver
from locators.order_page_locators import OrderPageLocators
import allure


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        with allure.step("Открываем страницу"):
            self.navigate(f"{URL}order")

    def find_elem(self):
        with allure.step("Ищем элемент"):
            self.find_element(OrderPageLocators.NAME_ORDER)

    def set_button_click(self):
        with allure.step("Кликаем по элементу"):
            self.click_element(OrderPageLocators.UPPER_ORDER_BUTTON, 5)

    def set_name(self):
        with allure.step("Вводим в поле {NAME}"):
            self.enter_text(OrderPageLocators.NAME_ORDER, NAME)

    def set_surname(self):
        with allure.step("Вводим в поле {SURNAME}"):
            self.enter_text(OrderPageLocators.SURNAME_ORDER, SURNAME)

    def set_address(self):
        with allure.step("Вводим в поле {ADDRESS}"):
            self.enter_text(OrderPageLocators.ADDRESS_ORDER, ADDRESS)

    def set_metro(self):
        with allure.step("Вводим в поле {METRO}"):
            self.enter_text(OrderPageLocators.METRO_ORDER, METRO)

    def select_metro(self, text):
        with allure.step("Выбираем из списка текст {metro_element} и кликаем"):
            metro_element = self.find_element(OrderPageLocators.METRO_ORDER, 5)
            self.select_by_list(metro_element, text)

    def set_phone(self):
        with allure.step("Вводим в поле {PHONE}"):
            self.enter_text(OrderPageLocators.PHONE_ORDER, PHONE)

    def submit_button_click(self):
        with allure.step("Кликаем по кнопке"):
            self.click_element(OrderPageLocators.FURTHER_BUTTON)

    def select_date_deliver(self, text):
        with allure.step("Выбираем из списка дату и кликаем"):
            date_deliver_element = self.find_element(OrderPageLocators.DATE_DELIVER, 5)
        self.select_by_list(date_deliver_element, text)

    def select_rental_period(self, text):
        with allure.step("Выбираем из списка текст {rental_element} и кликаем"):
            rental_element = self.find_element(OrderPageLocators.RENTAL_PERIOD, 5)
            self.select_by_list_in_div(rental_element, text)

    def check_scooter_color(self, color):
        with allure.step("Выбираем из цвет самоката"):
            scooter_color_element = self.find_element(OrderPageLocators.SCOOTER_COLOR_ELEMENT, 5)
            if scooter_color_element:
                if color in COLORS.keys():
                    print(COLORS.get(color))
                    element_for_check = self.driver.find_element(By.XPATH,
                                                                 f"//input[@id='{COLORS.get(color)}']/parent::label")
                    element_for_check.click()
                else:
                    print(f"Color of scooter is absent")
            else:
                print(f"Failed to check an element")
