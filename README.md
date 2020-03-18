## AMQP events
In this proof of concept, all queues are declared in the default AMQP exchange. The default AMQP exchange is a direct exchange in which messages are delivered to the queue with a name equal to the routing key of the message. Each queue is automatically bound to the default exchange with a routing key equal to the queue name.
| producers (services) | queue / routing key | body | listeners (services) | description |
| -------------------- | ------------------- | ---- | -------------------- | ----------- |
| `orders` | `order-created` | `Order` | `customers` | Dispatched after `Order` is created (status `pending`) |
| `customers` | `check-order-products-stock` | `Order.products` | `products` | Dispatched if `Customer` has no pending invoices |
| `customers` | `cancel-order` | `Order.order_id` | `orders` | Dispatched if `Customer` has pending invoices |
| `products` | `confirm-order` | `Order.order_id` | `orders` | Dispatched after checking products are in stock |
| `products` | `cancel-order` | `Order.order_id` | `orders` | Dispatched when lack of products stock |
| `orders` | `order-confirmed` | `Order.client_id` | `notifications` | Dispatched after order status is `confirmed` |
| `orders` | `ship-order` | `List[OrderProduct]` | `products` | Dispatched after order status is `confirmed` |
| `orders` | `order-cancelled` | `Order.client_id` | `notifications` | Dispatched after order status is `cancelled` |
| `products` | `order-shipped` | `Order.order_id` | `orders` | Dispatched after product stock is updated |
| `orders` | `order-shipped-notify` | `Order.client_id` | `notifications` | Dispatched after order status is `shipped` |
