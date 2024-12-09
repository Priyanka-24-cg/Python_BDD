from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # Filter elements
    FILTER_XS = (By.CSS_SELECTOR, "input[value='XS']")
    FILTER_S = (By.CSS_SELECTOR, "input[value='S']")
    FILTER_M = (By.CSS_SELECTOR, "input[value='M']")

    # Add to cart button
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.add-to-cart")

    def select_size_filter(self, size):
        if size == 'XS':
            self.driver.find_element(*self.FILTER_XS).click()
        elif size == 'S':
            self.driver.find_element(*self.FILTER_S).click()
        elif size == 'M':
            self.driver.find_element(*self.FILTER_M).click()

    def add_item_to_cart(self, item_index):
        # You can implement this to add specific items based on index or name
        items = self.driver.find_elements(By.CSS_SELECTOR, ".product")
        items[item_index].find_element(*self.ADD_TO_CART_BUTTON).click()
