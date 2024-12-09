from behave import given, when, then
from pages.cart_page import CartPage

@given('user has added items to the cart')
def step_impl(context):
    # You can add steps to add items before testing checkout
    pass

@when('user deletes all items from the cart')
def step_impl(context):
    cart_page = CartPage(context.driver)
    cart_page.remove_all_items()

@then('the cart should be empty and total should be reset')
def step_impl(context):
    cart_page = CartPage(context.driver)
    assert len(cart_page.get_cart_items()) == 0
    assert cart_page.get_cart_total() == '0'
