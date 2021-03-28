
import unittest 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

#Abrir navegador

class Iniciar_usuario(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'Documentos\chromedriver')
	

	def test_IniciarSesion_(self):
		driver=self.driver
		driver.get("https://www.lineru.com/")
		numerodedocumento= "1110544278"
		contraseña= "1234567"
		#Selectores
		boton_inicio_sesion ='body > app-root > app-init > shared-init-header > header > div > div > div > nav > a > span'
		selector_usuario='#mat-input-33'
		selector_contraseña='#mat-input-34'
		boton_login= 'body > app-root > app-auth-login > div > div.container > div > div > div.card.shadow-with-hover.p-3.p-lg-4.p-xl-5.mb-5.ml-0.ml-md-2 > div > form > div:nth-child(3) > button'
		#Acciones
		driver.find_element_bt_css_selector(boton_inicio_sesion).click()
		driver.find_element_bt_css_selector(selector_usuario).send_kesy(numerodedocumento)
		driver.find_element_bt_css_selector(selector_usuario).send_kesy(contraseña)
		driver.find_element_bt_css_selector(boton_login).click()
		time.sleep(10)

	def tearDown(self):
		self.driver.close()
if __name__ == '__main__':
	unittest.main()
	




