import pytest
from selenium import webdriver
from pages.Order_page import OrderPage
import allure


class TestOrderPage:
    browser = None

    @classmethod
    def setup_class(cls):
        cls.browser = webdriver.Firefox(executable_path=r"C:\\Users\\HP\\Desktop\\Sprint_4\\Firefoxdriver\\geckodriver.exe")

    def test_order_samokat_fill_in_form_1(self):
        self.browser.get('https://qa-scooter.praktikum-services.ru/order')
        self.browser.set_window_size(1920, 1080)
        order_page=OrderPage(self.browser)
        order_page.set_order(name='Надя',surname='Терех',adress='Варшавское шоссе',telefon='+79293456778',date='21.12.2022')
        text=order_page.wait_order_is_done_text()
        assert  "Заказ оформлен" in text

    def test_order_samokat_fill_in_form_2(self):
        self.browser.get('https://qa-scooter.praktikum-services.ru/order')
        self.browser.set_window_size(1920, 1080)
        order_page = OrderPage(self.browser)
        order_page.set_order(name='Светлана', surname='Блох', adress='Проспект Боголюбова', telefon='+79295677677',date='23.12.2022')
        text = order_page.wait_order_is_done_text()
        assert "Заказ оформлен" in text

    def test_click_on_logo_samokat_go_to_start_page(self):
        self.browser.get('https://qa-scooter.praktikum-services.ru/order')
        self.browser.set_window_size(1920, 1080)
        order_page = OrderPage(self.browser)
        order_page.click_on_logo_samokat()
        order_page.browser_wait()
        cur_url=order_page.get_current_url()
        assert cur_url=='https://qa-scooter.praktikum-services.ru/'

    def test_click_on_yalogo_go_to_ya_start_page(self):
        self.browser.get('https://qa-scooter.praktikum-services.ru/order')
        self.browser.set_window_size(1920, 1080)
        order_page = OrderPage(self.browser)
        order_page.click_on_logo_yandex()
        order_page.browser_wait()
        order_page.browser_save_windows_switch_to_window(1)
        order_page.wait_url('https://dzen.ru/?yredirect=true')
        cur_url=order_page.get_current_url()
        assert cur_url=='https://dzen.ru/?yredirect=true'



    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.browser.quit()

