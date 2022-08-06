from django import template
from Account.models import Customer

register = template.Library()

@register.filter(name='is_customer')
def is_customer(customer):
    if Customer.objects.filter(email = customer):
        return True
    return False