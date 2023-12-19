from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


def main():
    # Ścieżka do sterownika przeglądarki, np. chromedriver.exe dla Google Chrome
    driver_path = r'C:\Users\adamw\PycharmProjects\Safeanimals\chromedriver.exe'

    # Inicjalizacja przeglądarki (w tym przypadku Google Chrome)
    driver = webdriver.Chrome()

    try:
        # Adres URL strony, na której chcemy działać
        url = 'https://www.safe-animal.eu/pl/dodaj-zwierze/Animals/add'
        driver.get(url)

        name_form = driver.find_element(By.XPATH, '//*[@id="zImie"]')
        name_form.send_keys()

        race_form = driver.find_element(By.XPATH, '//*[@id="zRasa"]')
        race_form.send_keys()

        colour_form = driver.find_element(By.XPATH, '//*[@id="zMasc"]')
        colour_form.send_keys()                                                                                         # maść


        # Po zakończeniu operacji poczekaj chwilę, aby zobaczyć efekty
        input("Zakończono. Wciśnij Enter, aby zamknąć przeglądarkę.")

    except Exception as e:
        print("Wystąpił błąd:", e)

    finally:
        # Zamknij przeglądarkę
        driver.quit()


if __name__ == "__main__":
    main()