from selenium import webdriver
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


#desabilitar modo protegido do Internet Explorer
#cap = DesiredCapabilities().INTERNETEXPLORER
#cap['platform'] = "Win8"
#cap['version'] = "10"
#cap['browserName'] = "internet explorer"
#cap['ignoreProtectedModeSettings'] = True
#cap['IntroduceInstabilityByIgnoringProtectedModeSettings'] = True
#cap['nativeEvents'] = True
#cap['ignoreZoomSetting'] = True
#cap['requireWindowFocus'] = True
#cap['INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS'] = True


exec_path = ("\\\\192.168.252.25\\infocell\\CINFO\\apps\\Python36Homolog2\\Lib\\site-packages\\visagio_robots\\drivers\\IEDriverServer.exe")
input_file =("\\\\192.168.252.25\\infocell\\CINFO\\temp\\parametros_consulta.vic")


driver = webdriver.Ie()
data_atual = datetime.now()
#print(data_atual)
periodoAno = data_atual.strftime('%Y')
#print(periodoAno)
mesAtual = data_atual.strftime('%b')
#print(mesAtual)

if mesAtual == 'Feb': mesAtual = 'Fev'
elif mesAtual == 'Apr': mesAtual = 'Abr'
elif mesAtual == 'May': mesAtual = 'Mai'
elif mesAtual == 'Aug': mesAtual = 'Ago'
elif mesAtual == 'Sep': mesAtual = 'Set'
elif mesAtual == 'Oct': mesAtual = 'Out'
elif mesAtual == 'Dec': mesAtual = 'Dez'

mesAnterior = (data_atual - timedelta(days=30)).strftime('%b')
#print(mesAnterior)

if mesAnterior == 'Feb': mesAnterior = 'Fev'
elif mesAnterior == 'Apr': mesAnterior = 'Abr'
elif mesAnterior == 'May': mesAnterior = 'Mai'
elif mesAnterior == 'Aug': mesAnterior = 'Ago'
elif mesAnterior == 'Sep': mesAnterior = 'Set'
elif mesAnterior == 'Oct': mesAnterior = 'Out'
elif mesAnterior == 'Dec': mesAnterior = 'Dez'


profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2) # custom location
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', '/tmp')
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')


def abreSite(site):
    driver.maximize_window()
    driver.get(site)

    driver.get('http://cid/vic/main.php')
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Consultar").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Base").click()
    time.sleep(3)
    driver.find_element(By.ID, "botao_exp").click()

    file_upload = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "filVic")))
    file_upload.send_keys(input_file)
    driver.find_element(By.XPATH, " / html / body / div[2] / div[2] / form / div[3] / input[1]").click()
    time.sleep(1)
    dropdown = driver.find_element(By.ID, "lstFiltro")
    dropdown.find_element(By.XPATH, "//option[. = 'Ano']").click
    driver.find_element(By.XPATH, "//option[contains(.,\'" + periodoAno + "\')]").click
    driver.find_element(By.CSS_SELECTOR, ".linha_tabela_exportacao:nth-child(2) a:nth-child(1) > img").click()
    driver.find_element(By.ID, "lstFiltro").click()
    dropdown = driver.find_element(By.ID, "lstFiltro")
    dropdown.find_element(By.XPATH, "//option[. = 'Período']").click()
    dropdown = driver.find_element(By.ID, "lstPerOpcoes")
    dropdown.find_element(By.XPATH, "//option[. = '" +  mesAnterior + "']").click()
    dropdown = driver.find_element(By.ID, "lstPerOpcoes")
    dropdown.find_element(By.XPATH, "//option[. = '" + mesAtual + "']").click()
    driver.find_element(By.CSS_SELECTOR, ".linha_tabela_exportacao:nth-child(2) a:nth-child(1) > img").click()
    botaoExportar = driver.find_element(By.ID, "botao_exp2")
    botaoExportar.click()

abreSite('http://cid/vic/main.php')


download_dir = "\\\\172.22.3.126\\Book VIC"  # for linux/*nix, download_dir="/usr/Public"
options = webdriver.ChromeOptions()

profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}], # Disable Chrome's PDF Viewer
               "download.default_directory": download_dir , "download.extensions_to_open": "applications/xls"}
options.add_experimental_option("prefs", profile)
