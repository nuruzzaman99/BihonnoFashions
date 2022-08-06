from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(Products, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == Products.id:
            return True
    return False


@register.filter(name='cart_quantity')
def cart_quantity(Products, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == Products.id:
            return cart.get(id)
    return 0


@register.filter(name='total_price')
def total_price(Products, cart):
    return Products.price * cart_quantity(Products, cart)


@register.filter(name='total_cart_price')
def total_cart_price(Products , cart):
    sum = 0
    for i in Products:
        sum += total_price(i , cart)
    return sum

@register.filter(name='sub_total')
def sub_total(Products , cart):
    sum = 100 + total_cart_price(Products , cart)
    return sum

@register.filter(name='times')
def times(number1 , number2):
    sum = number1 * number2
    return sum