from pages.base_page import BasePage
from data import URL
from conftest import driver
import allure


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open(self, url):
        with allure.step("Открываем страницу"):
            self.navigate(URL)

    def first_question_btn(self, question_locator):
        with allure.step("Ищем заданный элемент"):
            return self.find_element(question_locator, 15)

    def get_answer_for_question(self, answer_locator):
        with allure.step("Ищем заданный элемент и счтываем текст"):
            return self.find_element(answer_locator, 15).text
