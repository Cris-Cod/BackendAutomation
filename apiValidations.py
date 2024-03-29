import requests

reponse = requests.get('http://216.10.245.166/Library/GetBook.php',
             params = {'AuthorName' : 'Rahul Shetty'},)

#print(reponse.text)
#print(type(reponse.text))
#dict_response = json.loads(reponse.text)
#print(dict_response[0]['isbn'])
#print(type(dict_response))
json_response = reponse.json()
#print(json_response)
print(type(json_response))
print(json_response[0]['isbn'])
assert reponse.status_code == 200
print(reponse.headers)
assert reponse.headers['Content-Type'] == 'application/json;charset=UTF-8'
# Retrieve the book details with ISBN KM201
for actualBook in json_response:
    if actualBook['isbn'] == 'KM201':
        print(actualBook)
        break

expectedBook = {'book_name': 'Learn Appium Automation with Java', 'isbn': 'KM201', 'aisle': '227'}
print('actual: ', actualBook)
print('expect: ', expectedBook)
assert actualBook == expectedBook