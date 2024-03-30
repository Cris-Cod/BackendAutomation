import requests
import configparser
from payloads import *
from utilities.configurations import *
from utilities.resources import *

config = getConfig()
url = config['API']['endPoint'] + ApiResources.addBook
header = {'Content-Type': 'application/json'}
query = "select * from Books"
addBook_response = requests.post(url, json=buildPayloadFromBD(query), headers= header,)

print(addBook_response.json())
response_json = addBook_response.json()
print(type(response_json))

bookId = response_json['ID']

#Delete Book

resonse_deleteBook = requests.post('http://216.10.245.166/Library/DeleteBook.php',
              json={'ID': bookId},
              headers={'Content-Type': 'application/json'},)

assert resonse_deleteBook.status_code == 200
resonse_deleteBook.json()
res_json = resonse_deleteBook.json()
print(res_json['msg'])
assert res_json['msg'] == 'book is successfully deleted'


#Authentication
se = requests.session()
se.auth = auth=('eee-eee', getPassword())
url = 'https://api.github.com/user'
gitHub_response = se.get(url)

print(gitHub_response.status_code)

url2 = 'https://api.github.com/user/repos'
reponse2 = requests.get(url2, auth=('eee-eee', getPassword()))
print(reponse2.status_code)