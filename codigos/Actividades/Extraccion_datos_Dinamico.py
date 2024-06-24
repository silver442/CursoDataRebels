from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Iniciar el navegador
driver = webdriver.Chrome()

try:
    # Navegar a la URL del sitio web
    driver.get('http://quotes.toscrape.com/js/')

    # Hacer scroll para cargar todo el contenido dinámico (ejemplo)
    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(2)  # Esperar para que cargue más contenido (ajustar según la velocidad de carga)
        new_height = driver.execute_script('return document.body.scrollHeight')
        if new_height == last_height:
            break
        last_height = new_height

    # Extraer citas y autores
    quotes = driver.find_elements(By.CSS_SELECTOR, '.quote span.text')
    authors = driver.find_elements(By.CSS_SELECTOR, '.quote span small.author')

    # Mostrar las citas y autores extraídos
    for quote, author in zip(quotes, authors):
        print(f'Cita: {quote.text} - Autor: {author.text} \n')

finally:
    # Cerrar el navegador al finalizar
    driver.quit()
