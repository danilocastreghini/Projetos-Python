import http.client
import mimetypes
import json
import csv

dataPuxada=input('dataPuxada:')
queryType=int(input('queryType:'))
conn = http.client.HTTPSConnection("sappoprd.ambevdevs.com.br")
payload = ''
headers = {
  'Authorization': 'Basic VVNSX0NJRzpAbWIzdkBjaWc=',
  'Cookie': 'saplb_*=(J2EE4474220)4474250; JSESSIONID=dz9X1hOihZFmKbzIoiOF1N78XovHcQGKRUQA_SAPTo2TlUA6zPG6n4Z-awyQ5cQ0'
}

conn.request("GET", "/RESTAdapter/v1/CIG/getPreSaleResults?dataPuxada="+dataPuxada+"&queryType=" + str(queryType), payload, headers)
res = conn.getresponse()
data = res.read()
dados = data.decode("utf-8")
print(dados)

# open a file for writing
cig_data = open('d:/GV2C/cig_'+dataPuxada+'_'+ str(queryType) +'.csv', 'w', newline='')

# create the csv writer object
csvwriter = csv.writer(cig_data, delimiter=';')

strDados = str(dados)

jDados = json.loads(strDados)
rows = jDados['queryResult']['row']
#print(rows)

count = 0
for r in rows:
  if count == 0:
    header = r.keys()
    csvwriter.writerow(header)
    count += 1

  #print(r)
  csvwriter.writerow(r.values())

#print(data.decode("utf-8"))
cig_data.close()
input('Pressione qualquer tecla para sair')
