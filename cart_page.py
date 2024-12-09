from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    # Cart elements
    CART_ITEM_LIST = (By.CSS_SELECTOR, ".cart-item")
    CART_TOTAL = (By.CSS_SELECTOR, ".total-price")
    REMOVE_ITEM_BUTTON = (By.CSS_SELECTOR, ".remove-item")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".checkout")

    def get_cart_items(self):
        return self.driver.find_elements(*self.CART_ITEM_LIST)

    def get_cart_total(self):
        return self.driver.find_element(*self.CART_TOTAL).text

    def remove_all_items(self):
        items = self.get_cart_items()
        for item in items:
            item.find_element(*self.REMOVE_ITEM_BUTTON).click()

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
