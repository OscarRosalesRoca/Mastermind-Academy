import random
import re
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from speak_and_listen import speak, hear_me
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By



def select_all_available_items(driver):
    items = driver.find_elements(By.XPATH, "//*")
    return items


def main():
    #speak("Welcome to the Right Price! We are going to guess the right price of items in the website PcComponentes")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument('--disable-extensions')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-browser-side-navigation')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.pccomponentes.com/")

    try:
        reject_cookies = driver.find_element(By.ID, "cookiesrejectAll").click()
        print("Click on reject cookies")
        sleep(1)

        menu = driver.find_element(By.XPATH, '//*[@aria-labelledby="menu-btn-text"]').click()
        print("\nClick on menu")
        sleep(1)

        items_1 = select_all_available_items(driver)
        categories = [element for element in items_1
                              if re.match(r"^first-level-section-2.*", element.get_attribute("id"))]

        random_category = random.choice(categories)
        print("\nRandom category: {}".format(random_category.get_attribute("id")))
        random_category.click()
        print("Click on random category")
        sleep(2)


        items_2 = select_all_available_items(driver)
        second_categories = [element for element in items_2
                             if re.match(r"^third-level-section.*", element.get_attribute("id"))]

        random_second_category = random.choice(second_categories)
        while random_second_category.text == "Configurador de PCs":
            random_second_category = random.choice(second_categories)
        print("\nRandom second category: {}".format(random_second_category.get_attribute("id")))
        random_second_category.click()
        print("\nClick on a random second category")
        sleep(5)


        items_3 = random_second_category.find_elements(By.XPATH, ".//*")
        third_categories = [element for element in items_3
                            if re.match(r"^third-level-(\d+)$", element.get_attribute("id"))]
        random_third_category = random.choice(third_categories)
        while random_third_category.text == "Ver todo":
            random_third_category = random.choice(third_categories)
        print("\nRandom third category: {}".format(random_third_category.get_attribute("id")))

        new_window = random_third_category.get_attribute("href")

        driver.execute_script("window.open(arguments[0], '_blank');", new_window)
        sleep(3)

        # Cambiar a la nueva pestaña abierta
        driver.switch_to.window(driver.window_handles[1])

        all_items = driver.find_elements(By.XPATH, "//*")
        special_div = None
        for item in all_items:
            if item.get_attribute("id") == "TAYH8":
                print(item.get_attribute("id"))
                special_div = item

        if special_div:
            # Buscar elementos de tipo 'input' dentro del div con id 'TAYH8'
            input_elements = special_div.find_elements(By.XPATH, ".//input")

            if input_elements:
                print(f"Se encontraron {len(input_elements)} elementos 'input' dentro del div.")
                # Aquí puedes proceder con cualquier acción sobre esos inputs
                for input_element in input_elements:
                    print(input_element.get_attribute(
                        "type"))  # Imprime el tipo de cada input (checkbox, radio, text, etc.)
            else:
                print("No se encontraron elementos 'input' dentro del div.")
        else:
            print("El div con id 'TAYH8' no fue encontrado.")


    except NoSuchElementException:
        print("Item not found")


if __name__ == "__main__":
    main()
