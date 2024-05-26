from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.order_page import OrderPage
from pages.main_page import MainPage
from data import URL
from conftest import driver
from locators.order_page_locators import OrderPageLocators
import pytest
import allure


class TestOrderPage:

    @allure.title('Проверка работы формы заказа с помощью параметризации')
    @allure.description('На странице ищем поля ввода, заполняем данными и проверяем, что заказ будет оформлен при '
                        'условии корректного заполнения формы')
    @pytest.mark.parametrize(
        'name, surname, address, metro, phone, date_deliver',
        [
            ['Эдуард', 'Шеварнадзе', 'Измайловский проспект, 59', 'Измайловская', '89139139133', '25.05.2022'],
            ['Эдуард', 'Шеварнадзе', 'Измайловский проспект, 59', 'Измайловская', '89139139133', '25.06.2022'],
            ['', 'Шеварнадзе', 'Измайловский проспект, 59', 'Измайловская', '89139139133', '25.05.2022'],
            ['Эдуард', '', 'Измайловский проспект, 59', 'Измайловская', '89139139133', '25.05.2022'],
            ['Эдуард', 'Шеварнадзе', '', 'Измайловская', '89139139133', '25.05.2022'],
            ['Эдуард', 'Шеварнадзе', 'Измайловский проспект, 59', '', '89139139133', '25.05.2022'],
            ['Эдуард', 'Шеварнадзе', 'Измайловский проспект, 59', 'Измайловская', '', '25.05.2022']
        ]
    )
    def test_order_form(self, driver, name, surname, address, metro, phone, date_deliver):
        order_page = OrderPage(driver)
        order_page.open_page()
        order_page.enter_text(OrderPageLocators.NAME_ORDER, name, 5)
        order_page.enter_text(OrderPageLocators.SURNAME_ORDER, surname, 5)
        order_page.enter_text(OrderPageLocators.ADDRESS_ORDER, address, 5)
        order_page.select_metro(metro)
        order_page.enter_text(OrderPageLocators.PHONE_ORDER, phone, 5)
        order_page.click_element(OrderPageLocators.FURTHER_BUTTON, 5)
        order_page.select_date_deliver(date_deliver)
        order_page.select_rental_period('сутки')
        order_page.check_scooter_color('серая безысходность')
        order_page.enter_text(OrderPageLocators.COMMENT_ORDER, 'Наталья, морская пехота!', 5)
        order_page.click_element(OrderPageLocators.ORDER_BTN, 5)
        order_page.click_element(OrderPageLocators.APPROVAL_BTN, 5)
        text_header = driver.find_element(*OrderPageLocators.ORDER_PLACED)
        assert 'Заказ оформлен' in text_header.text

    @allure.step('Проверка перехода на страницу Дзен по клику на логотип Яндекс')
    def test_scooter_link(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page()
        order_page.find_element(OrderPageLocators.SCOOTER, 5).click()
        current_url = driver.current_url
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.step('Проверка перехода на главную страницу Самокат по клику на логотип Самокат')
    def test_dzen_link(self, driver):
        wait = WebDriverWait(driver, 10)
        main_page = MainPage(driver)
        main_page.open(URL)
        original_window = driver.current_window_handle
        dzen_button = driver.find_element(*OrderPageLocators.DZEN_BUTTON)
        dzen_button.click()
        wait.until(expected_conditions.number_of_windows_to_be(2))
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break
