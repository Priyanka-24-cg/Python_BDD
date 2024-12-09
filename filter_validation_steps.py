from behave import given, when, then
from pages.home_page import HomePage

@given('user is on the shopping page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.driver.get('https://react-shopping-cart-67954.firebaseapp.com/')

@when('user selects size {size} filter')
def step_impl(context, size):
    context.home_page.select_size_filter(size)

@then('the displayed items should be filtered to {size} size')
def step_impl(context, size):
    # Implement logic to verify filtered items
    pass
