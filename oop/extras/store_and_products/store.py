class Store:
    def __init__(self, name, product_list = []):
        self.name = name
        self.product_list = product_list
    
    def add_product(self, new_product):
        self.product_list.append(new_product)
        return self
    
    def sell_product(self, id):
        self.product_list[id].print_info
        self.product_list.pop(id)
        return self