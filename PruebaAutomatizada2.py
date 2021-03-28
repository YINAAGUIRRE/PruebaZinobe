
import unittest 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

#Abrir navegador

class Crear_usuario(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'Documentos\chromedriver')
	

	def test_IniciarSesion_(self):
		driver=self.driver
		driver.get("https://www.lineru.com/")
		primernombre= "Yina"
		numerodedocumento= "1110544278"
		numerocelular= "3144572042"
		correo="paoaguirre@gmail.com"
		contraseña="123456"
		#Selectores
		boton_inicio_sesion ='body > app-root > app-init > shared-init-header > header > div > div > div > nav > a > span'
		boton_crear ='body > app-root > app-auth-login > auth-header > header > div.nav-buttons.ng-star-inserted > div > button'
		selector_primernombre = '#mat-input-46'
		selector_tipocedula = '#mat-select-4 > div > div.mat-select-value.ng-tns-c83-92 > span > span'
		selector_numerodedocumento ='#mat-input-47'
		selector_numerocelular = '#mat-input-48'
		selector_correo= '#mat-input-49'
		selector_contraseña='#mat-input-50'
		selector_autorización = 'body > app-root > app-auth-register > div > div.container > div > div > div.card.shadow-with-hover.p-3.p-lg-4.p-xl-5.my-5.ml-0.ml-md-2 > div > form > div.col.pl-0.pl-lg-5.pr-0.pr-lg-5 > div > app-checkbox:nth-child(1) > div > div.ng-dirty.ng-valid.ng-touched > div > label'
		selector_autorización2= 'body > app-root > app-auth-register > div > div.container > div > div > div.card.shadow-with-hover.p-3.p-lg-4.p-xl-5.my-5.ml-0.ml-md-2 > div > form > div.col.pl-0.pl-lg-5.pr-0.pr-lg-5 > div > app-checkbox:nth-child(2) > div > div.ng-dirty.ng-touched.ng-valid > div > label'
		boton_login= 'body > app-root > app-auth-register > div > div.container > div > div > div.card.shadow-with-hover.p-3.p-lg-4.p-xl-5.my-5.ml-0.ml-md-2 > div > form > div.margin-form > button'
		#Acciones
		driver.find_element_bt_css_selector(boton_inicio_sesion).click()
		driver.find_element_bt_css_selector(boton_crear).click()
		driver.find_element_bt_css_selector(selector_primernombre).send_kesy(primernombre)
		driver.find_element_bt_css_selector(selector_tipocedula).click()
		driver.find_element_bt_css_selector(selector_numerodedocumento).send_keys(numerodedocumento)
		driver.find_element_bt_css_selector(selector_numerocelular).send_kesy(numerocelular)
		driver.find_element_bt_css_selector(selector_correo).send_keys(correo)
		driver.find_element_bt_css_selector(selector_contraseña).send_keys(contraseña)
		dirver.find_element_bt_css_selector(selector_autorización).click()
		driver.find_element_bt_css_selector(selector_autorización2).click()
		driver.find_element_bt_css_selector(boton_login).click()
		time.sleep(10)

	def tearDown(self):
		self.driver.close()
		
if __name__ == '__main__':
	unittest.main()
	




