import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

try:
    driver.get("https://itcareerhub.de/ru")
    driver.maximize_window()

    wait = WebDriverWait(driver, 15)

    # 1. Закрытие всплывающих банеров / Cookie (если есть)
    try:
        cookie_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'Принять') or contains(., 'Accept') or contains(., 'согласен')]"))
        )
        cookie_btn.click()
    except Exception:
        pass

    # 2. Поиск элемента "Способы оплаты" (ищем среди любых тегов, содержащих текст)
    # Прокручиваем вниз, так как ссылка на способы оплаты часто находится в футере/подвале
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    payment_link = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[contains(translate(text(), 'СПОСОБЫОПЛАТЫ', 'способыоплаты'), 'способы оплаты')]"))
    )

    # Прокручиваем прямо к найденной ссылке и кликаем через JS (защита от перекрытия элемента)
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", payment_link)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", payment_link)

    # 3. Ожидание перехода и создание скриншота секции или всей страницы
    time.sleep(3)

    # Попытка найти блок с оплатой для скриншота
    try:
        payment_section = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(., 'Способы оплаты') or contains(@class, 'payment')]"))
        )
        payment_section.screenshot("payment_methods.png")
    except Exception:
        # Если блок не найден отдельно, делаем скриншот всей страницы
        driver.save_screenshot("payment_methods.png")

    print("Скриншот успешно сохранен как payment_methods.png")

finally:
    driver.quit()