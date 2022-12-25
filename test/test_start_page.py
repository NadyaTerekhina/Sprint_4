import pytest
from selenium import webdriver
from pages.Start_page import StartPage
import allure

class TestStartPage:
    browser = None

    @classmethod
    def setup_class(cls):
        # создали  для браузера firefox
        cls.browser = webdriver.Firefox(executable_path=r"C:\\Users\\HP\\Desktop\\Sprint_4\\Firefoxdriver\\geckodriver.exe")

    def test_click_order_button_up(self):
        self.browser.get('https://qa-scooter.praktikum-services.ru/')
        self.browser.set_window_size(1920, 1080)
        start_page=StartPage(self.browser)
        start_page.order_button_up_is_present()
        start_page.click_order_button_up()
        start_page.browser_wait(2)
        cur_url = start_page.get_current_url()
        assert cur_url == 'https://qa-scooter.praktikum-services.ru/order'

    def test_click_order_button_low(self):
        self.browser.get('https://qa-scooter.praktikum-services.ru/')
        self.browser.set_window_size(1920, 1080)
        start_page = StartPage(self.browser)
        start_page.browser_wait(2)
        start_page.order_button_low_is_present()
        start_page.scroll_to_order_button()
        start_page.click_order_button_low()
        start_page.browser_wait(1)
        cur_url = start_page.get_current_url()
        assert cur_url == 'https://qa-scooter.praktikum-services.ru/order'

    def test_click_how_to_pay_box_opens_text(self):
        self.browser.get('https://qa-scooter.praktikum-services.ru/')
        self.browser.set_window_size(1920, 1080)
        start_page=StartPage(self.browser)
        start_page.wait_fq(2)
        start_page.scroll_to_faq_table()
        start_page.click_how_to_pay_box()
        text=start_page.check_text_how_to_pay()
        assert text == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    def test_click_want_many_box_opens_text(self):
        self.browser.get('https://qa-scooter.praktikum-services.ru/')
        self.browser.set_window_size(1920, 1080)
        start_page=StartPage(self.browser)
        start_page.wait_fq(2)
        start_page.scroll_to_faq_table()
        start_page.click_want_many_box()
        text=start_page.check_text_want_many()
        assert text == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    def test_click_rent_time_box_opens_text(self):
        self.browser.get('https://qa-scooter.praktikum-services.ru/')
        self.browser.set_window_size(1920, 1080)
        start_page=StartPage(self.browser)
        start_page.wait_fq(2)
        start_page.scroll_to_faq_table()
        start_page.click_rent_time_box()
        text=start_page.check_text_rent_time()
        assert text=='Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    def test_click_rent_now_box_opens_text(self):
        self.browser.get('https://qa-scooter.praktikum-services.ru/')
        self.browser.set_window_size(1920, 1080)
        start_page=StartPage(self.browser)
        start_page.wait_fq(2)
        start_page.scroll_to_faq_table()
        start_page.click_rent_now_box()
        text=start_page.check_text_rent_now()
        assert text == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    def test_click_prolong_rent_box_opens_text(self):
        self.browser.get('https://qa-scooter.praktikum-services.ru/')
        self.browser.set_window_size(1920, 1080)
        start_page = StartPage(self.browser)
        start_page.wait_fq(2)
        start_page.scroll_to_faq_table()
        start_page.click_prolong_rent_box()
        text=start_page.check_text_prolong_rent()
        assert text == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    def test_click_charging_set_opens_text(self):
        self.browser.get('https://qa-scooter.praktikum-services.ru/')
        self.browser.set_window_size(1920, 1080)
        start_page = StartPage(self.browser)
        start_page.wait_fq(2)
        start_page.scroll_to_faq_table()
        start_page.click_charging_set()
        text=start_page.check_text_charging_set()
        assert text =='Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    def test_cancel_order_box_opens_text(self):
        self.browser.get('https://qa-scooter.praktikum-services.ru/')
        self.browser.set_window_size(1920, 1080)
        start_page = StartPage(self.browser)
        start_page.wait_fq(2)
        start_page.scroll_to_faq_table()
        start_page.click_cancel_order()
        text=start_page.check_text_cancel_order()
        assert text == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    def test_click_mkad_box_open_text(self):
        self.browser.get('https://qa-scooter.praktikum-services.ru/')
        self.browser.set_window_size(1920, 1080)
        start_page = StartPage(self.browser)
        start_page.wait_fq(2)
        start_page.scroll_to_faq_table()
        start_page.click_mkad_box()
        text=start_page.check_text_mkad()
        assert text == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'


    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.browser.quit()


