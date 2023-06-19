# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium.webdriver import ActionChains
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


driver = webdriver.Chrome()
try:
    epm_fio = 'Орлов Азамат'
    sbis_page = 'https://fix-online.sbis.ru/'
    driver.get(sbis_page)
    driver.maximize_window()
    sleep(2)

    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    login.send_keys('Stat_o', Keys.ENTER)
    password.send_keys('Video84', Keys.ENTER)
    sleep(3)

    contact_point = driver.find_element(By.CSS_SELECTOR, '[data-qa="Контакты"]')
    sleep(1)
    contact_point.click()
    sleep(1)
    contact_sub_point = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle')
    contact_sub_point.click()
    sleep(1)
    assert driver.current_url == 'https://fix-online.sbis.ru/page/dialogs', 'Неверно открыт сайт'

    dialog_tab = driver.find_element(By.CSS_SELECTOR, '[data-name="dialogs"]')
    dialog_tab.click()
    add_btn = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    add_btn.click()
    sleep(1)

    search_field = driver.find_element(By.CSS_SELECTOR, '[data-qa="addressee-selector-root"] input')
    search_field.send_keys(epm_fio, Keys.ENTER)
    sleep(1)
    emp_contact = driver.find_element(By.CSS_SELECTOR, '.controls-StackTemplate-content [title="Орлов Азамат"]')
    sleep(0.5)
    emp_contact.click()
    sleep(1)
    msg_field = driver.find_element(By.CSS_SELECTOR,
                                    '[templatename="Addressee/popup:Stack"] [data-qa="textEditor_slate_Field"]')
    msg = 'Новое сообщение'
    msg_field.send_keys(msg)
    sleep(1)
    send_btn = driver.find_element(By.CSS_SELECTOR, ".icon-BtArrow")
    send_btn.click()
    sleep(2)

    msg_list = driver.find_element(By.CSS_SELECTOR, '[data-qa="items-container"] [data-qa="item"] p')
    assert msg_list.is_displayed()
    assert msg_list.text == msg
    ActionChains(driver).context_click(msg_list).perform()
    sleep(1)
    del_btn = driver.find_element(By.CSS_SELECTOR, '[title="Перенести в удаленные"]')
    del_btn.click()
    empty_view = driver.find_element(By.CSS_SELECTOR, '[data-qa="items-container"]')
    assert driver.find_element(By.CSS_SELECTOR, '[data-qa="items-container"] [data-qa="item"] p').text != msg, \
        'Созданное сообщение не удалилось'
finally:
    driver.quit()

