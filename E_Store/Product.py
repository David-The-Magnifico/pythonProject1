from E_Store import Product_Category


class Product:
    product_id = ''
    product_name = ''
    product_price = 0.0
    product_desc = ''
    product_type = Product_Category.Product_Category

    def __init__(self, product_type, product_name, product_id, product_price, product_desc):
        self.product_type = product_type
        self.product_desc = product_desc
        self.product_name = product_name
        self.product_price = product_price
        self.product_id = product_id



