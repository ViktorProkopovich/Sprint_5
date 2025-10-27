from selenium.webdriver.common.by import By

class Locators:

    # Входа в "ЛК"
    BTN_ACC_ENTER = (By.XPATH, "//button[text()='Войти в аккаунт']") # Кнопка "Войти в аккаунт" на главной странице
    BTN_P_ACC = (By.XPATH, "//p[contains(@class,'AppHeader_header__linkText__3q_va ml-2') and text()='Личный Кабинет']") # Кнопка "Личный Кабинет" на главной странице
    BTN_LOGIN_iN_ACC = (By.XPATH, "//button[text()='Войти']") # Кнопка "Войти" на странице идентификации 
    LINK_LOGIN_REGFORM = (By.XPATH, "//a[contains(@class,'Auth_link') and (text())='Войти']") # Ссылка "Войти" на странице "регистрации"
    LINK_LOGIN_RECPASS = (By.XPATH, "//a[text()='Войти']") # Ссылка "Войти" на странице "восстановления пароля"
    LINK_REC_PASS = (By.XPATH, "//a[contains(@class,'Auth_link') and (text())='Восстановить пароль']") # Ссылка "Восстановление пароля" на странице входа в "Личный кабинет"
    
    # "ЛК"
    FIELD_EMAIL_ID = (By.XPATH, "//input[@name='name']") # Поле ввода "Email" для авторизации
    FIELD_PASS_ID = (By.XPATH, "//input[@name='Пароль']") # Поле ввода "Пароль" для авторизации
    BTN_LOGIN = (By.XPATH, "//button[text()='Войти']") # Кнопка "Войти"
    BTN_ORDER = (By.XPATH, "//button[text()='Оформить заказ']") # Кнопка "Оформить заказ"
    
    #локаторы регистрации
    LINK_REG = (By.XPATH, "//a[(text())='Зарегистрироваться']") # Ссылка "Регистрации" на странице "Входа"
    FIELD_REG_NAME = (By.XPATH, "//label[text()='Имя']/../input") # Поле ввода "Имя" для регистрации
    FIELD_REG_EMAIL = (By.XPATH, "//label[text()='Email']/../input") # Поле ввода "Email" для регистрации
    FIELD_REG_PASSWORD = (By.XPATH, "//input[@type='password']") # Поле ввода "Пароль" для регистрации
    BTN_REG = (By.XPATH, "//button[text()='Зарегистрироваться']") # Кнопка "Зарегистрироваться"
    MSG_PASS_ERROR =(By.XPATH, "//p[text()='Некорректный пароль']") # Сообщение о некорректном пароле

    #локаторы перехода
    BTN_CONSTR = (By.XPATH, "//p[contains(@class,'AppHeader_header__linkText__3q_va ml-2') and text()='Конструктор']") # Кнопка "Конструктор" в шапке
    BTN_LOGO_SB = (By.XPATH, "//div[contains(@class,'AppHeader_header__logo__2D0X2')]") # Логотип Stellar Burgers в шапке
    BTN_EXIT = (By.XPATH, "//button[contains(@class,'Account_button__14Yp3') and (text())='Выход']") # Кнопка "Выход" в ЛК

    # Раздел "Конструктор"
    BTN_BUNS = (By.XPATH, "//span[contains(@class,'text_type_main-default') and (text())='Булки']") # Булки
    BTN_SAUCES = (By.XPATH, "//span[contains(@class,'text_type_main-default') and (text())='Соусы']") # Соусы
    BTN_FILLINGS = (By.XPATH, "//span[contains(@class,'text_type_main-default') and (text())='Начинки']") # Начинки







