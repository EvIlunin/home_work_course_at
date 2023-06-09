# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class TestHW10:
    """Домашнее задание к вебинару 11 Selenium Задачи 1 и With_star"""
    contact_tabs_txt = 'Контакты'
    sbis_page = 'https://sbis.ru/'
    tensor_page = 'https://tensor.ru/'
    about_page = 'https://tensor.ru/about'
    driver = webdriver.Chrome()
    driver.get(sbis_page)
    sleep(1)

    def setup_module(self):
        """Код который будет выполняться перед каждым тестом"""
        self.driver.get(self.sbis_page)
        sleep(1)

    def test_task1(self):
        """Тест по Заданию №1"""
        driver = self.driver
        try:
            sleep(1)
            contact_tabs = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-link[href="/contacts"]')
            assert driver.current_url == self.sbis_page, 'Неверно открыт сайт'
            assert contact_tabs.text == self.contact_tabs_txt, 'Текст вкладки не правильный'
            contact_tabs.click()
            sleep(1)
            logo_tensor = driver.find_element(By.CSS_SELECTOR,
                                               '.sbisru-Contacts__logo-tensor [alt="Разработчик системы СБИС — компания «Тензор»"]')
            logo_tensor.click()
            sleep(1)
            driver.switch_to.window(driver.window_handles[1])
            assert driver.current_url == self.tensor_page, 'Неверно открыт сайт Тензора'
            block_people = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg')
            assert block_people.is_displayed()
            about_link = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg [href="/about"]')
            about_link.location_once_scrolled_into_view
            sleep(1)
            about_link.click()
            sleep(1)
            assert driver.current_url == self.about_page, 'Неверно открыт сайт Тензор/Подробнее'
        finally:
            driver.quit()
