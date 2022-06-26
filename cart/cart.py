from store.models import Product


class Cart:
    """
    A base Cart class, providing some default behaviors that
    can be inherited or overridden, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = request.session['cart'] = {}
        self.cart = cart

    def add(self, product_id):
        """
        Adding and updating the users basket session data
        """
        product_id = str(product_id)
        if product_id in self.cart:
            self.cart[product_id] += 1
        else:
            self.cart[product_id] = 1
        self.save()


    def remove(self, product_id):
        """
        Adding and updating the users basket session data
        """

        product_id = str(product_id)

        if self.cart[product_id] == 1:
            self.delete(product_id)
        else:
            self.cart[product_id] -= 1
        self.save()


    def delete(self, product_id):
        """
        Delete item from session data
        """
        product_id = str(product_id)
        del self.cart[product_id]
        self.save()

    def __len__(self):
        """
        Count the total quantity of items
        """
        return sum((qty for qty in self.cart.values()))

    def __iter__(self):
        """
        Collect the product_id in the session data to query the database
        and return products
        """

        for product_id, qty in self.cart.items():
            product = Product.objects.get(id=product_id)
            price = product.price * qty
            item = {"product": product, "qty": qty, "price": price}
            yield item

    def get_total_price(self):
        total_price = 0
        for product_id, qty in self.cart.items():
            product = Product.objects.get(id=product_id)
            total_price += product.price * qty
        return total_price

    def clear(self):
        # Remove basket from session
        del self.session['cart']
        self.save()

    def save(self):
        self.session.modified = True
