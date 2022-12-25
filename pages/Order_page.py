from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from locators.order_page_locators import OrderPageLocators




class OrderPage:

    def __init__(self,browser):
        self.browser=browser

    def wait_fill_in_name(self,name):
        field = WebDriverWait(self.browser,5).until(EC.presence_of_element_located(OrderPageLocators.NAME_FIELD))
        field.send_keys(name)

    def fill_in_surname(self,surname):
        self.browser.find_element(*OrderPageLocators.SURNAME_FIELD).send_keys(surname)

    def fill_in_adress(self,adress):
        self.browser.find_element(*OrderPageLocators.ADRESS_FIELD).send_keys(adress)

    def select_metro(self):
        self.browser.find_element(*OrderPageLocators.METRO).click()
        self.browser.find_element(*OrderPageLocators.select).click()


    def fill_in_telefon(self,telefon):
        self.browser.find_element(*OrderPageLocators.TELEFON).send_keys(telefon)

    def click_on_futher(self):
        self.browser.find_element(*OrderPageLocators.FUTHER_BUTTON).click()

    def set_kallendar(self,date):
        field= WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(OrderPageLocators.KALLENDAR))
        field.send_keys(date)

    # def open_list_rent(self):
    #     self.browser.find_element(*OrderPageLocators.RENT_TIME).click()

    def choose_from_list_2DAYS(self):
        #сначала закрыть календарь
        kalend = self.browser.find_element(*OrderPageLocators.KALLENDAR)
        kalend.send_keys(Keys.ESCAPE)
        self.browser.find_element(*OrderPageLocators.RENT_TIME).click()
        self.browser.find_element(*OrderPageLocators.HOURS).click()

    def choose_black_color_in_checkbox(self):
        self.browser.find_element(*OrderPageLocators.CHECK_BOX_BLACK).click()

    def click_order_button(self):
        self.browser.find_element(*OrderPageLocators.ORDER_BUTTON).click()

    def wait_and_confirm_order(self):
        yes=WebDriverWait(self.browser, 3).until(EC.presence_of_element_located(OrderPageLocators.YES_BUTTON))
        yes.click()
    def wait_order_is_done_text(self):
        form = WebDriverWait(self.browser, 3).until(EC.presence_of_element_located(OrderPageLocators.ORDER_DONE_FORM))
        return form.text

    def set_order(self,name,surname,adress,telefon,date):
        self.wait_fill_in_name(name)
        self.fill_in_surname(surname)
        self.fill_in_adress(adress)
        self.select_metro()
        self.fill_in_telefon(telefon)
        self.click_on_futher()
        self.set_kallendar(date)
        self.choose_from_list_2DAYS()
        self.choose_black_color_in_checkbox()
        self.click_order_button()
        self.wait_and_confirm_order()


    def click_on_logo_samokat(self):
        self.browser.find_element(*OrderPageLocators.SAMOKAT_LOGO).click()

    def click_on_logo_yandex(self):
        self.browser.find_element(*OrderPageLocators.YANDEX_LOGO).click()

    def browser_wait(self):
        self.browser.implicitly_wait(3)

    def wait_url(self,url):
        WebDriverWait(self.browser, 10).until(EC.url_to_be(url))

    def browser_save_windows_switch_to_window(self,number):
        windows = self.browser.window_handles
        self.browser.switch_to.window(windows[number])

    def get_current_url(self):
        return self.browser.current_url













