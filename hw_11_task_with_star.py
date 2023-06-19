# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pathlib import Path
from selenium.webdriver.chrome.options import Options


work_dir = Path.cwd()
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
  "download.default_directory": str(work_dir),
  "safebrowsing.enabled": 'false'
})
driver = webdriver.Chrome(options=chrome_options)
sbis_page = 'https://sbis.ru/'

try:
    driver.get(sbis_page)
    driver.maximize_window()
    sleep(1)
    footer = driver.find_element(By.CSS_SELECTOR, '.sbisru-Footer [href="/download?tab=ereport&innerTab=ereport25"]')
    footer.location_once_scrolled_into_view
    sleep(0.5)
    footer.click()
    sleep(1)
    assert driver.current_url == 'https://sbis.ru/download?tab=ereport&innerTab=ereport25', 'Неверно открыт сайт'
    plugin_list = driver.find_element(By.CSS_SELECTOR, '[data-id="plugin"]')
    plugin_list.click()
    sleep(1)
    assert driver.current_url == 'https://sbis.ru/download?tab=plugin&innerTab=default', 'Неверно открыт сайт'
    download_plugin_link = driver.find_element(By.CSS_SELECTOR,
                                               '[data-for="plugin"] [href="https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]')
    download_plugin_link.click()
    sleep(4)
    plugin_exe = Path(work_dir, 'sbisplugin-setup-web.exe')
    assert plugin_exe.exists(), 'Файл не скачался либо указан не правильный путь до файла'
    plugin_file = work_dir.glob('sbisplugin-setup-web*')
    for file in plugin_file:
        print(f'размер скачанного файла {round(file.stat().st_size/1024/1024,2)} в мегабайтах')
        print()
finally:
    driver.quit()
