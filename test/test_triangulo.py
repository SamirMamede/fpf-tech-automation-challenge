import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_identificar_triangulo_equilatero(browser):
    browser.get("http://www.vanilton.net/triangulo/")

    vertice1 = browser.find_element(By.NAME, "V1")
    vertice2 = browser.find_element(By.NAME, "V2")
    vertice3 = browser.find_element(By.NAME, "V3")

    vertice1.clear()
    vertice1.send_keys("10")
    vertice2.clear()
    vertice2.send_keys("10")
    vertice3.clear()
    vertice3.send_keys("10")

    identify_button = browser.find_element(By.XPATH, "//input[@value='Identificar']")
    identify_button.click()

    try:
        resultado = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Equilátero')]"))
        )
        assert "Equilátero" in resultado.text
    except Exception as e:
        pytest.fail(f"The result did not appear on the page. Error: {str(e)}")

def test_identificar_triangulo_isosceles(browser):
    browser.get("http://www.vanilton.net/triangulo/")

    vertice1 = browser.find_element(By.NAME, "V1")
    vertice2 = browser.find_element(By.NAME, "V2")
    vertice3 = browser.find_element(By.NAME, "V3")

    vertice1.clear()
    vertice1.send_keys("10")
    vertice2.clear()
    vertice2.send_keys("10")
    vertice3.clear()
    vertice3.send_keys("5")

    identify_button = browser.find_element(By.XPATH, "//input[@value='Identificar']")
    identify_button.click()

    try:
        resultado = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Isósceles')]"))
        )
        assert "Isósceles" in resultado.text
    except Exception as e:
        pytest.fail(f"The result did not appear on the page. Error: {str(e)}")

def test_identificar_triangulo_escaleno(browser):
    browser.get("http://www.vanilton.net/triangulo/")

    vertice1 = browser.find_element(By.NAME, "V1")
    vertice2 = browser.find_element(By.NAME, "V2")
    vertice3 = browser.find_element(By.NAME, "V3")

    vertice1.clear()
    vertice1.send_keys("10")
    vertice2.clear()
    vertice2.send_keys("8")
    vertice3.clear()
    vertice3.send_keys("5")

    identify_button = browser.find_element(By.XPATH, "//input[@value='Identificar']")
    identify_button.click()

    try:
        resultado = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Escaleno')]"))
        )
        assert "Escaleno" in resultado.text
    except Exception as e:
        pytest.fail(f"The result did not appear on the page. Error: {str(e)}")

def test_identificar_triangulo_letras(browser):
    browser.get("http://www.vanilton.net/triangulo/")

    vertice1 = browser.find_element(By.NAME, "V1")
    vertice2 = browser.find_element(By.NAME, "V2")
    vertice3 = browser.find_element(By.NAME, "V3")

    vertice1.clear()
    vertice1.send_keys("a")
    vertice2.clear()
    vertice2.send_keys("b")
    vertice3.clear()
    vertice3.send_keys("c")

    identify_button = browser.find_element(By.XPATH, "//input[@value='Identificar']")
    identify_button.click()

    try:
        resultado = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Erro')]"))
        )
        assert "Erro" in resultado.text
    except Exception as e:
        pytest.fail(f"The error message did not appear on the page. Error: {str(e)}")


def test_identificar_triangulo_espacos(browser):
    browser.get("http://www.vanilton.net/triangulo/")

    vertice1 = browser.find_element(By.NAME, "V1")
    vertice2 = browser.find_element(By.NAME, "V2")
    vertice3 = browser.find_element(By.NAME, "V3")

    vertice1.clear()
    vertice1.send_keys("   ")
    vertice2.clear()
    vertice2.send_keys("   ")
    vertice3.clear()
    vertice3.send_keys("   ")

    identify_button = browser.find_element(By.XPATH, "//input[@value='Identificar']")
    identify_button.click()

    try:
        resultado = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Erro')]"))
        )
        assert "Erro" in resultado.text
    except Exception as e:
        pytest.fail(f"The error message did not appear on the page. Error: {str(e)}")

def test_identificar_triangulo_degenerado(browser):
    browser.get("http://www.vanilton.net/triangulo/")

    vertice1 = browser.find_element(By.NAME, "V1")
    vertice2 = browser.find_element(By.NAME, "V2")
    vertice3 = browser.find_element(By.NAME, "V3")

    vertice1.clear()
    vertice1.send_keys("5")
    vertice2.clear()
    vertice2.send_keys("5")
    vertice3.clear()
    vertice3.send_keys("10")

    identify_button = browser.find_element(By.XPATH, "//input[@value='Identificar']")
    identify_button.click()

    try:
        resultado = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Erro')]"))
        )
        assert "Erro" in resultado.text
    except Exception as e:
        pytest.fail(f"The error message did not appear on the page. Error: {str(e)}")
    
def test_identificar_triangulo_zero(browser):
    browser.get("http://www.vanilton.net/triangulo/")

    vertice1 = browser.find_element(By.NAME, "V1")
    vertice2 = browser.find_element(By.NAME, "V2")
    vertice3 = browser.find_element(By.NAME, "V3")

    vertice1.clear()
    vertice1.send_keys("0")
    vertice2.clear()
    vertice2.send_keys("5")
    vertice3.clear()
    vertice3.send_keys("5")

    identify_button = browser.find_element(By.XPATH, "//input[@value='Identificar']")
    identify_button.click()

    try:
        resultado = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Erro')]"))
        )
        assert "Erro" in resultado.text
    except Exception as e:
        pytest.fail(f"The error message did not appear on the page. Error: {str(e)}")


def test_identificar_triangulo_negativo(browser):
    browser.get("http://www.vanilton.net/triangulo/")

    vertice1 = browser.find_element(By.NAME, "V1")
    vertice2 = browser.find_element(By.NAME, "V2")
    vertice3 = browser.find_element(By.NAME, "V3")

    vertice1.clear()
    vertice1.send_keys("-5")
    vertice2.clear()
    vertice2.send_keys("5")
    vertice3.clear()
    vertice3.send_keys("5")

    identify_button = browser.find_element(By.XPATH, "//input[@value='Identificar']")
    identify_button.click()

    try:
        resultado = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Erro')]"))
        )
        assert "Erro" in resultado.text
    except Exception as e:
        pytest.fail(f"The error message did not appear on the page. Error: {str(e)}")