from typing import Dict
from math import ceil


def prepare_order(qty: int):
    """
    This function takes quantity of an order and returns number of boxes and size of boxes
    you need to prepare to pack this order.
    :param qty: The quantity of an order.
    :return: Number and size of boxes you need to pack in the order.
    """
    orders = {}

    small = 0
    medium = 0
    large = 0
    total = 0

    while qty > 0:
        if qty <= 3:
            small += 1
            break
        elif qty <= 6:
            medium += 1
            break
        elif qty <= 9:
            large += 1
            break
        else:
            large += qty // 9
            qty %= 9

    # orders["small"] = small
    # orders["medium"] = medium
    # orders["large"] = large
    #
    # return orders
    return small, medium, large


# i = 10
# print(i, prepare_order(i))

for i in range(1, 101):
    print(i, prepare_order(i))