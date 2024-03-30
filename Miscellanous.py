import requests


#http://rahulshettyacademy.com
#'visit-month'
cookie = {'visit-month' : 'February'}
response = requests.get('http://rahulshettyacademy.com', allow_redirects=False, cookies=cookie, timeout=1)
print(response.history)
print(response.status_code)


se = requests.session()
se.cookies.update({'visit-month' : 'February'})
res = se.get('https://httpbin.org/cookies', cookies={'visit-year' : '2024'})
print(res.text)

#Attachment

url = 'https://petstore.swagger.io/v2/pet/9843217/uploadImage'
files = {'file' : open('/home/criscodx/Downloads/api.png', 'rb')}
r = requests.post(url, files= files)
print(r.status_code)
print(r.text)