from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions, wait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from conftest import driver
import allure


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def navigate(self, url: str):
        with allure.step("Открываем страницу"):
            self.driver.get(url)

    def find_element(self, locator: tuple, timeout: 15):
        with allure.step("Ищем элемент на странице"):
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click_element(self, locator: tuple, timeout: 15):
        with allure.step("Ищем и кликаем по найденому элементу"):
            element = self.find_element(locator, timeout)
            element.click()

    def click_el(self, element):
        with allure.step("Кликаем по элементу"):
            element.click()

    def enter_text(self, locator: tuple, text: str, timeout: 15):
        with allure.step("Вводим текст"):
            element = self.find_element(locator, timeout)
            element.click()
            element.send_keys(text)

    def select_by_list(self, element, text: str):
        with allure.step("Ищем элемент в списке и кликаем по нему"):
            element.click()
            element.send_keys(text)
            try:
                list_element = self.driver.find_element(By.XPATH, f"//button/div[text()= '{text}']")
            except NoSuchElementException:
                list_element = self.driver.find_element(By.CSS_SELECTOR, ".react-datepicker__day--selected")

            list_element.click()

    def select_by_list_in_div(self, element, text: str):
        with allure.step("Ищем элемент в списке и кликаем по нему"):
            element.click()
            list_element = self.driver.find_element(By.XPATH, f"//div[text()= '{text}']")
            list_element.click()

    def scroll(self, element):
        with allure.step("Скролим страницу до заданного элемента"):
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
