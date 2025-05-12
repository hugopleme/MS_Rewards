from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

opcaoNavegador = Options()
opcaoNavegador.add_argument("--start-maximized")

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options = opcaoNavegador)

# url = "https://www.bing.com"
# # for i in range(0, 30):
# #     driver.get(url)
# #     time.sleep(3)
# #
# #     caixaBusca = driver.find_element(By.XPATH, "//textarea[(@class='sb_form_q sb_form_ta')]")
# #     caixaBusca.send_keys(str(i))
# #     caixaBusca.send_keys(Keys.RETURN)
# #     time.sleep(3)

url = "https://rewards.bing.com/"
time.sleep(3)

missaoDiaria = driver.find_elements(By.XPATH, "//a[(@class='ds-card-sec ng-scope')]")[:3]

for missoes in missaoDiaria:
    missoes.send_keys(Keys.RETURN)


driver.close()