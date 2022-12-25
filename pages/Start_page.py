from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.start_page_locators import StartPageLocators






class StartPage:

    def __init__(self,browser):
        self.browser=browser


    # кликакем по кнопкам заказа:

    def order_button_up_is_present(self):
        WebDriverWait(self.browser,3).until(EC.presence_of_element_located(StartPageLocators.ORDER_BUTTON_UP))

    def click_order_button_up(self):
        self.browser.find_element(*StartPageLocators.ORDER_BUTTON_UP).click()

    def order_button_low_is_present(self):
        WebDriverWait(self.browser, 3).until(EC.presence_of_element_located(StartPageLocators.ORDER_BUTTON_LOW))

    def click_order_button_low(self):
        self.browser.find_element(*StartPageLocators.ORDER_BUTTON_LOW).click()

    def scroll_to_order_button(self):
        order=self.browser.find_element(*StartPageLocators.ORDER_BUTTON_LOW)
        self.browser.execute_script("arguments[0].scrollIntoView();", order)

    def get_current_url(self):
       return self.browser.current_url

    def browser_wait(self,time):
        self.browser.implicitly_wait(time)



    def wait_fq(self,time1):
        WebDriverWait(self.browser,time1).until(EC.presence_of_element_located(StartPageLocators.FAQ_TABLE))

    # скролл к аккордиону
    def scroll_to_faq_table(self):
        fq = self.browser.find_element(*StartPageLocators.FAQ_TABLE)
        self.browser.execute_script("arguments[0].scrollIntoView();", fq)


    #кликаем по аккордиону

    def click_how_to_pay_box(self):
        box= WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(StartPageLocators.HOW_TO_PAY_BOX))
        box.click()


    def click_want_many_box(self):
        box = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(StartPageLocators.WANT_MANY_BOX))
        box.click()

    def click_rent_time_box(self):
        box = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(StartPageLocators.RENT_TIME_BOX))
        box.click()

    def click_rent_now_box(self):
        box = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(StartPageLocators.RENT_NOW_BOX))
        box.click()

    def click_prolong_rent_box(self):
        box = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(StartPageLocators.PROLONG_RENT_BOX))
        box.click()

    def click_charging_set(self):
        box = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(StartPageLocators.CHARGING_SET_BOX))
        box.click()

    def click_cancel_order(self):
        box = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(StartPageLocators.CANCEL_ORDER_BOX))
        box.click()

    def click_mkad_box(self):
        box = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(StartPageLocators.MKAD_BOX))
        box.click()



    #берем значение текст, для проверки соответсвия текста
    def check_text_how_to_pay(self):
        return self.browser.find_element(*StartPageLocators.HOW_TO_PAY_EXPAND).text

    def check_text_want_many(self):
       return self.browser.find_element(*StartPageLocators.WANT_MANY_EXPAND).text

    def check_text_rent_time(self):
       return self.browser.find_element(*StartPageLocators.RENT_TIME_EXPAND).text

    def check_text_rent_now(self):
      return  self.browser.find_element(*StartPageLocators.RENT_NOW_EXPAND).text

    def check_text_prolong_rent(self):
       return self.browser.find_element(*StartPageLocators.PROLONG_RENT_EXPAND).text

    def check_text_charging_set(self):
       return self.browser.find_element(*StartPageLocators.CHARGING_SET_EXPAND).text

    def check_text_cancel_order(self):
      return  self.browser.find_element(*StartPageLocators.CANCEL_ORDER_EXPAND).text

    def check_text_mkad(self):
       return self.browser.find_element(*StartPageLocators.MKAD_EXPAND).text





    






