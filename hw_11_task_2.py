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


def test_create_and_delete_msg():
    """"""
    driver = webdriver.Chrome()
    try:
        epm_fio = 'Орлов Азамат'
        sbis_page = 'https://fix-online.sbis.ru/'
        driver.get(sbis_page)
        sleep(1)

        login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
        password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
        login.send_keys('Stat_o', Keys.ENTER)
        password.send_keys('Video84', Keys.ENTER)
        sleep(10)

        contact_point = driver.find_element(By.CSS_SELECTOR, '[data-qa="Контакты"]')
        sleep(10)
        contact_point.click()
        sleep(2)
        contact_sub_point = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle')
        contact_sub_point.click()
        sleep(2)
        assert driver.current_url == 'https://fix-online.sbis.ru/page/dialogs', 'Неверно открыт сайт'
        sleep(10)

        dialog_tab = driver.find_element(By.CSS_SELECTOR, '[data-name="dialogs"]')
        dialog_tab.click()
        add_btn = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
        add_btn.click()
        sleep(4)

        search_field = driver.find_element(By.CSS_SELECTOR, '[data-qa="addressee-selector-root"] input')
        search_field.send_keys(epm_fio, Keys.ENTER)
        sleep(10)
        emp_contact = driver.find_element(By.CSS_SELECTOR, '.controls-StackTemplate-content [title="Орлов Азамат"]')
        sleep(1)
        emp_contact.click()
        sleep(10)
        msg_field = driver.find_element(By.CSS_SELECTOR,
                                        '[templatename="Addressee/popup:Stack"] [data-qa="textEditor_slate_Field"]')
        send_btn = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
        msg = 'Новое сообщениеНовое сообщение'
        msg_field.send_keys(msg)
        send_btn.click()
        sleep(3)

        msg_list = driver.find_element(By.CSS_SELECTOR, '[data-qa="items-container"] [data-qa="item"] p')
        assert msg_list.is_displayed()
        assert msg_list.text == msg
        ActionChains(driver).context_click(msg_list).perform()
        del_btn = driver.find_element(By.CSS_SELECTOR, '[title="Перенести в удаленные"]')
        del_btn.click()
        assert msg_list.is_displayed() != False, 'Сообщение не удалилось'
    finally:
        driver.quit()

