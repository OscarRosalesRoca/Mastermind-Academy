from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def check_stock(url):
    try:
        driver = webdriver.Firefox()
        driver.get(url)

        can_buy = False

        while True:
            try:
                sleep(5)
                reject_cookies = driver.find_element(By.CLASS_NAME, "sc-2c264fcb-1 hlqBNA")
                reject_cookies.click()
                sleep(5)
                add_to_cart = driver.find_element(By.CLASS_NAME, "sc-2c264fcb-1 iDrqgP")
                if add_to_cart.is_displayed():
                    print_YES_stock()
                    can_buy = True
                else:
                    print_NO_stock()
            except NoSuchElementException:
                print_NO_stock()

            if can_buy:
                driver.quit()  # Cerrar el navegador cuando el producto esté disponible
                return can_buy
            else:
                sleep(5)
                driver.refresh()

    except Exception as e:
        print(f"Error: {e}")


def print_YES_stock():
    print("The product is available to buy")


def print_NO_stock():
    print("The product isn't available to buy")


def main():
    URL_MediaMarkt = "https://www.mediamarkt.es/es/product/_nintendo-nintendo-switch-oled-blanca-1512119.html"

    print("Launching browser to buy...")
    driver = webdriver.Firefox()
    driver.get(URL_MediaMarkt)

    try:
        sleep(3)
        reject_cookies = driver.find_element(By.CLASS_NAME, "sc-2c264fcb-1 hlqBNA")
        reject_cookies.click()
        sleep(2)

        add_to_cart= driver.find_element(By.CLASS_NAME, "sc-2c264fcb-1 iDrqgP")
        add_to_cart.click()
        sleep(2)

        finish_purchase = driver.find_element(By.CLASS_NAME, "sc-2c264fcb-1 fCmQLQ")
        finish_purchase.click()
        sleep(2)
        
        login_mail = driver.find_element(By.ID, "mms-login-form__email")
        login_password = driver.find_element(By.ID, "mms-login-form__password")
        login_mail.send_keys("micorreo@gmail.com")
        login_password.send_keys("1234")

    except NoSuchElementException:
        print("Some button to click not found")

if __name__ == "__main__":
    main()
