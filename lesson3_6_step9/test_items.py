link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"


def test_lesson3_6_step9(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    button = browser.find_element_by_css_selector("[class = 'btn btn-lg btn-primary btn-add-to-basket']")
    assert button == True, "Кнопка не найдена"
    