from selenium.webdriver import ie
from time import sleep


url = 'https://curso-python-selenium.netlify.app/aula_03.html'
brownser = ie()
brownser.get(url)
sleep(1)

a = brownser.find_element_by_tag_name('a')
p = brownser.find_element_by_tag_name('p')

for click in range(1, 11):
    a.click()
    p.text == click



print(f'texto de a:{a.text}')
print(f'texto de p:{p.text}')
