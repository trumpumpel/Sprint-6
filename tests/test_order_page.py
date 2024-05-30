from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.order_page import OrderPage
from data import URL, DZEN
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
        order_page.navigate(f"{URL}order")
        order_page.enter_text(OrderPageLocators.NAME_ORDER, name, 15)
        order_page.enter_text(OrderPageLocators.SURNAME_ORDER, surname, 15)
        order_page.enter_text(OrderPageLocators.ADDRESS_ORDER, address, 15)
        order_page.select_metro(metro)
        order_page.enter_text(OrderPageLocators.PHONE_ORDER, phone, 15)
        order_page.click_element(OrderPageLocators.FURTHER_BUTTON, 15)
        order_page.select_date_deliver(date_deliver)
        order_page.select_rental_period('сутки')
        order_page.check_scooter_color('серая безысходность')
        order_page.enter_text(OrderPageLocators.COMMENT_ORDER, 'Наталья, морская пехота!', 15)
        order_page.click_element(OrderPageLocators.ORDER_BTN, 15)
        order_page.click_element(OrderPageLocators.APPROVAL_BTN, 15)
        text_header = driver.find_element(*OrderPageLocators.ORDER_PLACED)
        assert 'Заказ оформлен' in text_header.text

    @allure.step('Проверка перехода на главную страницу Самокат по клику на логотип Самокат')
    def test_scooter_link(self, driver):
        order_page = OrderPage(driver)
        order_page.find_element(OrderPageLocators.SCOOTER, 15).click()
        assert driver.current_url == f"{URL}"

    @allure.step('Проверка перехода на страницу Дзен по клику на логотип Яндекс')
    def test_dzen_link(self, driver):
        order_page = OrderPage(driver)
        original_window = driver.current_window_handle
        order_page.dzen_button_click(original_window)
        current_url = driver.current_url
        assert current_url == DZEN
