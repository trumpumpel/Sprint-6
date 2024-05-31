from pages.main_page import MainPage
from data import URL, FIRST_ANS, SECOND_ANS, THIRD_ANS, FOURTH_ANS, FIFTH_ANS, SIXTH_ANS, SEVENTH_ANS, EIGHTH_ANS
from conftest import driver
from locators.main_page_locators import MainPageLocators
import allure


class TestMainPage:

    @allure.title('Проверка ответа при клике на первый вопрос')
    def test_click_first_question(self, driver):
        main_page = MainPage(driver)
        question_btn = main_page.first_question_btn(MainPageLocators.FIRST_QUESTION)
        main_page.click_el(question_btn)
        answer_for_question = main_page.get_answer_for_question(MainPageLocators.FIRST_ANSWER)
        assert answer_for_question == f'{FIRST_ANS}'

    @allure.title('Проверка ответа при клике на второй вопрос')
    def test_click_second_question(self, driver):
        main_page = MainPage(driver)
        question_btn = main_page.first_question_btn(MainPageLocators.SECOND_QUESTION)
        main_page.click_el(question_btn)
        answer_for_question = main_page.get_answer_for_question(MainPageLocators.SECOND_ANSWER)
        assert answer_for_question == f'{SECOND_ANS}'

    @allure.title('Проверка ответа при клике на третий вопрос')
    def test_click_third_question(self, driver):
        main_page = MainPage(driver)
        question_btn = main_page.first_question_btn(MainPageLocators.THIRD_QUESTION)
        main_page.click_el(question_btn)
        answer_for_question = main_page.get_answer_for_question(MainPageLocators.THIRD_ANSWER)
        assert answer_for_question == f'{THIRD_ANS}'

    @allure.title('Проверка ответа при клике на четвёртый вопрос')
    def test_click_fourth_question(self, driver):
        main_page = MainPage(driver)
        question_btn = main_page.first_question_btn(MainPageLocators.FOURTH_QUESTION)
        main_page.click_el(question_btn)
        answer_for_question = main_page.get_answer_for_question(MainPageLocators.FOURTH_ANSWER)
        assert answer_for_question == f'{FOURTH_ANS}'

    @allure.title('Проверка ответа при клике на пятый вопрос')
    def test_click_fifth_question(self, driver):
        main_page = MainPage(driver)
        question_btn = main_page.first_question_btn(MainPageLocators.FIFTH_QUESTION)
        main_page.click_el(question_btn)
        answer_for_question = main_page.get_answer_for_question(MainPageLocators.FIFTH_ANSWER)
        assert answer_for_question == f'{FIFTH_ANS}'

    @allure.title('Проверка ответа при клике на шестой вопрос')
    def test_click_sixth_question(self, driver):
        main_page = MainPage(driver)
        question_btn = main_page.first_question_btn(MainPageLocators.SIXTH_QUESTION)
        main_page.click_el(question_btn)
        answer_for_question = main_page.get_answer_for_question(MainPageLocators.SIXTH_ANSWER)
        assert answer_for_question == f'{SIXTH_ANS}'

    @allure.title('Проверка ответа при клике на седьмой вопрос')
    def test_click_seventh_question(self, driver):
        main_page = MainPage(driver)
        question_btn = main_page.first_question_btn(MainPageLocators.SEVENTH_QUESTION)
        main_page.click_el(question_btn)
        answer_for_question = main_page.get_answer_for_question(MainPageLocators.SEVENTH_ANSWER)
        assert answer_for_question == f'{SEVENTH_ANS}'

    @allure.title('Проверка ответа при клике на восьмой вопрос')
    def test_click_eighth_question(self, driver):
        main_page = MainPage(driver)
        question_btn = main_page.first_question_btn(MainPageLocators.EIGHTH_QUESTION)
        main_page.click_el(question_btn)
        answer_for_question = main_page.get_answer_for_question(MainPageLocators.EIGHTH_ANSWER)
        assert answer_for_question == f'{EIGHTH_ANS}'

    @allure.title('Проверка перехода при клике на кнопку Заказать (верхняя)')
    def test_upper_order_button(self, driver):
        main_page = MainPage(driver)
        order_btn = main_page.first_question_btn(MainPageLocators.UPPER_ORDER_BUTTON)
        main_page.click_el(order_btn)
        text_header = driver.find_element(*MainPageLocators.ORDER_HEADER)
        assert text_header.text == 'Для кого самокат'

    @allure.title('Проверка перехода при клике на кнопку Заказать (нижняя)')
    def test_lower_order_button(self, driver):
        main_page = MainPage(driver)
        order_btn = main_page.first_question_btn(MainPageLocators.LOWER_ORDER_BUTTON)
        main_page.click_el(order_btn)
        text_header = driver.find_element(*MainPageLocators.ORDER_HEADER)
        assert text_header.text == 'Для кого самокат'
