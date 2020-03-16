from ..repositories import customers_repository
from ..models.customers_db.Customer import CustomerSchema

async def order_created_cb(message):
    print(" [x] %r:%r" % (message.delivery.routing_key, message.body))
    await message.channel.basic_ack(message.delivery.delivery_tag)


def get(email):
    try:
        customer = customers_repository.get_customer(email)
        return CustomerSchema().dump(customer), 200
    except ValueError as error:
        return f'Customer {email} not found', 404


def post(body):
    try:
        new_customer = customers_repository.add_customer(CustomerSchema().load(body, partial=True))
        return CustomerSchema().dump(new_customer), 201
    except ValueError as error:
        return f'Error creating customer', 500
    

def put(body):
    try:
        updated_customer = customers_repository.update_customer(CustomerSchema().load(body, partial=True))
        return CustomerSchema().dump(updated_customer), 200
    except ValueError as error:
        return f'Customer not found', 404


def delete(email):
    try:
        customers_repository.delete_customer(email)
        return 204
    except ValueError as error:
        return f'Customer {email} not found', 404

