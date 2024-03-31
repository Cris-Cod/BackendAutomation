import requests
from behave import *

from utilities.configurations import getPassword
from utilities.resources import ApiResources


@given('I have github auth credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = auth = ('xxx', getPassword())


@when('I hit getRepo API of github')
def step_impl(context):
    context.reponse2 = context.se.get(ApiResources.githubRepo)


@then('status code of response should be {statusCode:d}')
def step_impl(context, statusCode):
    print(context.reponse2.status_code)
    assert context.reponse2.status_code == statusCode