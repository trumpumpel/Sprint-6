from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
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
            try:
                return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            except TimeoutException:
                print(f"Element with locator {locator} not found within {timeout} seconds.")
                return None

    def click_element(self, locator: tuple, timeout: 15):
        with allure.step("Ищем и кликаем по найденому элементу"):
            element = self.find_element(locator, timeout)
            if element:
                element.click()
            else:
                print(f"Failed to click on element with locator {locator}")

    def click_el(self, element):
        with allure.step("Кликаем по элементу"):
            if element:
                element.click()
            else:
                print(f"Failed to click on element")

    def enter_text(self, locator: tuple, text: str, timeout: 15):
        with allure.step("Вводим текст"):
            element = self.find_element(locator, timeout)
            if element:
                element.click()
                element.send_keys(text)
            else:
                print(f"Failed to enter_text on element with locator {locator}")

    def select_by_list(self, element, text: str):
        with allure.step("Ищем элемент в списке и кликаем по нему"):
            if element:
                element.click()
                element.send_keys(text)
                try:
                    list_element = self.driver.find_element(By.XPATH, f"//button/div[text()= '{text}']")
                except NoSuchElementException:
                    list_element = self.driver.find_element(By.CSS_SELECTOR, ".react-datepicker__day--selected")

                list_element.click()
            else:
                print(f"Failed to enter_text on element")

    def select_by_list_in_div(self, element, text: str):
        with allure.step("Ищем элемент в списке и кликаем по нему"):
            if element:
                element.click()
                list_element = self.driver.find_element(By.XPATH, f"//div[text()= '{text}']")
                list_element.click()
            else:
                print(f"Failed to enter_text on element")

    def scroll(self, element):
        with allure.step("Скролим страницу до заданного элемента"):
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
