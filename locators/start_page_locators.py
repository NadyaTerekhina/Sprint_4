from selenium.webdriver.common.by import By


class StartPageLocators:

    ORDER_BUTTON_UP = [By.CSS_SELECTOR, '.Header_Nav__AGCXC .Button_Button__ra12g']  # кнопка "заказть" верхняя
    ORDER_BUTTON_LOW = [By.CSS_SELECTOR, '.Home_FinishButton__1_cWm .Button_Button__ra12g']  # кнопка "заказать" нижняя

    #  вопросы о важном
    FAQ_TABLE = [By.CLASS_NAME, 'Home_FAQ__3uVm4']  # класс к таблице, чтобы до нее проскроллить

    HOW_TO_PAY_BOX = [By.ID, 'accordion__heading-0']#сколько стоит и как платить
    WANT_MANY_BOX = [By.ID, 'accordion__heading-1']  # Хочу сразу несколько самокатов! Так можно?
    RENT_TIME_BOX = [By.ID, 'accordion__heading-2']  # Как рассчитывается время аренды?
    RENT_NOW_BOX = [By.ID, 'accordion__heading-3']  # Можно ли заказать самокат прямо на сегодня?
    PROLONG_RENT_BOX = [By.ID, 'accordion__heading-4']  # Можно ли продлить заказ или вернуть самокат раньше?
    CHARGING_SET_BOX =  [By.ID, 'accordion__heading-5'] # Вы привозите зарядку вместе с самокатом?
    CANCEL_ORDER_BOX = [By.ID, 'accordion__heading-6']  # Можно ли отменить заказ?
    MKAD_BOX = [By.ID, 'accordion__heading-7'] # Я жизу за МКАДом, привезёте?

    # вопросы о важном элемент с id  для взятия текста
    HOW_TO_PAY_EXPAND = [By.ID,'accordion__panel-0' ]
    WANT_MANY_EXPAND = [By.ID, 'accordion__panel-1']
    RENT_TIME_EXPAND = [By.ID, 'accordion__panel-2']
    RENT_NOW_EXPAND = [By.ID, 'accordion__panel-3']
    PROLONG_RENT_EXPAND = [By.ID, 'accordion__panel-4']
    CHARGING_SET_EXPAND = [By.ID, 'accordion__panel-5']
    CANCEL_ORDER_EXPAND = [By.ID, 'accordion__panel-6']
    MKAD_EXPAND = [By.ID, 'accordion__panel-7']
