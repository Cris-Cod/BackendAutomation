import requests
from behave import *

from payloads import *
from utilities.configurations import getConfig
from utilities.resources import ApiResources


@given('the book details which needs to be added to Library')
def step_impl(context):
    config = getConfig()
    context.url = config['API']['endPoint'] + ApiResources.addBook
    context.header = {'Content-Type': 'application/json'}
    context.payload = addBookPayload('oiu', 114)

@when('we execute the Addbook PostAPI method')
def step_impl(context):
    context.addBook_response = requests.post(context.url, json=context.payload, headers=context.header, )


@then('book is successfully added')
def step_impl(context):
    print(context.addBook_response.json())
    response_json = context.addBook_response.json()
    print(type(response_json))
    context.bookId = response_json['ID']
    print(context.bookId)
    assert response_json['Msg'] == 'successfully added'


@given('the book details which {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    config = getConfig()
    context.url = config['API']['endPoint'] + ApiResources.addBook
    context.header = {'Content-Type': 'application/json'}
    context.payload = addBookPayload(isbn, aisle)
