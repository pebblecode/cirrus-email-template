from pkg_resources import resource_string


buyer_template = resource_string(__name__, 'assets/inoket-order-buyer.html')
supplier_template = resource_string(__name__, 'assets/inoket-order-seller.html')
