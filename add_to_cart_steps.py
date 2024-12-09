from behave import given, when, then
from pages.home_page import HomePage
from pages.cart_page import CartPage

@given('user is on the shopping page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.driver.get('https://react-shopping-cart-67954.firebaseapp.com/')

@when('user adds {count} items with free shipping to cart')
def step_impl(context, count):
    for _ in range(int(count)):
        context.home_page.add_item_to_cart(0)  # Add first item or based on your logic

@then('user should see the items in the cart with correct prices and order')
def step_impl(context):
    cart_page = CartPage(context.driver)
    items = cart_page.get_cart_items()
    # Implement logic to check the cart order and price
    pass
