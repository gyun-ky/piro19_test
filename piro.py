def piro_main(p1, p2, product, order):
    return p1 + p2 + product(product) + order(order)

def product(product):
    return product + 1 

def order(order):
    return order + 1