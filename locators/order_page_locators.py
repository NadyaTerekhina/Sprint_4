from selenium.webdriver.common.by import By

class OrderPageLocators:

#поля
    NAME_FIELD = [By.XPATH,".//input[@placeholder='* Имя']"]
    SURNAME_FIELD = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    ADRESS_FIELD = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
    METRO = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
    select=[By.CSS_SELECTOR, ".select-search__select button > div:nth-child(2)"]#бульвар Рокоссовского
    TELEFON = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]

#кнопка "далее"

    FUTHER_BUTTON = [By.CLASS_NAME, 'Button_Middle__1CSJM']

# поля дополнительные
    KALLENDAR = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]

#список "срок арренды"
    RENT_TIME = [By.CLASS_NAME, "Dropdown-root"]



    HOURS = [By.XPATH, ".//div[text()='двое суток']"]
#чекбокс черный
    CHECK_BOX_BLACK = [By.ID, 'black']

# кнопка заказать
    ORDER_BUTTON = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]

#кнопка "да"
    YES_BUTTON = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']"]
#заказ оформлен
    ORDER_DONE_FORM = [By.CLASS_NAME, "Order_ModalHeader__3FDaJ"]
#logosamokat
    SAMOKAT_LOGO = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]
#logoyandex
    YANDEX_LOGO = [By.CLASS_NAME,"Header_LogoYandex__3TSOI"]

