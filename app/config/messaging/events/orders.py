from . import EventBase

# Order entity events
class OrderEvents:
    """
    Customer entity related messaging events
    """
    ORDER_CREATED = 'order-created'
    CONFIRM_ORDER = 'confirm-order'
    ORDER_CONFIRMED = 'order-confirmed'
    CANCEL_ORDER = 'cancel-order'
    ORDER_CANCELLED = 'order-cancelled'
    SHIP_ORDER = 'ship-order'
    ORDER_SHIPPED = 'order-shipped'
    CHECK_ORDER_PRODUCTS_STOCK = 'check-order-products-stock'


class OrderCreatedEvent(EventBase):
    def __init__(self, order_id, products):
        self.order_id = order_id
        self.products = products


class ShipOrderEvent(EventBase):
    def __init__(self, products):
        self.products = products


class CancelOrderEvent(EventBase):
    def __init__(self, order_id):
        self.order_id = order_id


class ConfirmOrderEvent(EventBase):
    def __init__(self, order_id):
        self.order_id = order_id


class OrderShippedEvent(EventBase):
    def __init__(self, order_id):
        self.order_id = order_id
