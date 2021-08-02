from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Edge(executable_path="./driver/msedgedriver")

def seleccionarChat(nombre: str):
    buscando = True
    while buscando:
        print("buscando chat")
        try:

            elements = browser.find_elements_by_tag_name("span")
            for element in elements:
                if element.text == nombre:
                    print("encontramos al impostor")
                    element.click()
                    buscando = False
                    break
        except:
            print("seguimos buscando")

def enviarMensaje(mensaje: str):
    chatbox = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    chatbox.send_keys(mensaje)
    chatbox.send_keys(Keys.ENTER)


def validaQR():
    try:
        element = browser.find_element_by_tag_name("canvas")
    except:
        return False
    return True

def botWhatsapp():
    browser.get("https://web.whatsapp.com")
    time.sleep(5)
    espera = True
    while espera:
        print("estoy esperando")
        espera = validaQR()
        time.sleep(2)
        if espera == False:
            print("se autentico")
            break

    seleccionarChat("RENP")
    enviarMensaje("te encontreee")

botWhatsapp()

