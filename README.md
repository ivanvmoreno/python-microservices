## AMQP events
In this proof of concept, all queues are declared in the default AMQP exchange.
| producers (services) | queue / routing key | listeners (services) | description |
| -------- | ----- | --------- | ------------ |
| `orders` | `order-created` | `customers` | Dispatched after `Order` is created (status `pending`) |
| `customers` | `check-order-products-stock` | `products` | Dispatched if `Customer` has no pending invoices |
| `customers` | `cancel-order` | `orders` | Dispatched if `Customer` has pending invoices |
| `products` | `confirm-order` | `orders` | Dispatched after checking products are in stock |
| `products` | `cancel-order` | `orders` | Dispatched when lack of products stock |
| `orders` | `order-confirmed` | `notifications` | Dispatched after order status is `confirmed` |
| `orders` | `ship-order` | `products` | Dispatched after order status is `confirmed` |
| `orders` | `order-cancelled` | `notifications` | Dispatched after order status is `cancelled` |
| `products` | `order-shipped` | `orders` `notifications` | Dispatched after product stock is updated |
