import store
import products

store = store.Store("tea_store")
chai = products.Product("chai", 5, "tea")
chamomile = products.Product("chamomile", 4, "tea")
mug = products.Product("mug", 10, "mugs")

store.add_product(chai).add_product(chamomile).add_product(mug)
chai.update_price(10, False).print_info()
store.sell_product(2)
print(store.product_list)