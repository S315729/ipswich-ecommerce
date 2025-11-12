from django.test import TestCase, Client
from django.contrib.auth.models import User
from products.models import Category, Product
from cart.models import Cart, CartItem
from orders.models import Order, OrderItem


class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Test Category',
            description='Test Description'
        )
        self.product = Product.objects.create(
            name='Test Product',
            category=self.category,
            description='Test product description',
            price=99.99,
            stock=10
        )

    def test_product_creation(self):
        """Test that product is created correctly"""
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.price, 99.99)
        self.assertEqual(self.product.stock, 10)
        self.assertTrue(self.product.available)

    def test_product_slug_generation(self):
        """Test that slug is auto-generated"""
        self.assertEqual(self.product.slug, 'test-product')

    def test_is_in_stock(self):
        """Test stock checking method"""
        self.assertTrue(self.product.is_in_stock())
        self.product.stock = 0
        self.assertFalse(self.product.is_in_stock())


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Electronics',
            description='Electronic devices'
        )

    def test_category_creation(self):
        """Test that category is created correctly"""
        self.assertEqual(self.category.name, 'Electronics')
        self.assertEqual(str(self.category), 'Electronics')

    def test_category_slug_generation(self):
        """Test that slug is auto-generated"""
        self.assertEqual(self.category.slug, 'electronics')


class CartModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.category = Category.objects.create(name='Test Category')
        self.product1 = Product.objects.create(
            name='Product 1',
            category=self.category,
            description='Description 1',
            price=50.00,
            stock=10
        )
        self.product2 = Product.objects.create(
            name='Product 2',
            category=self.category,
            description='Description 2',
            price=75.00,
            stock=5
        )
        self.cart = Cart.objects.create(user=self.user)

    def test_cart_creation(self):
        """Test that cart is created correctly"""
        self.assertEqual(self.cart.user, self.user)
        self.assertEqual(str(self.cart), f'Cart for {self.user.username}')

    def test_add_to_cart(self):
        """Test adding items to cart"""
        CartItem.objects.create(
            cart=self.cart,
            product=self.product1,
            quantity=2
        )
        self.assertEqual(self.cart.items.count(), 1)
        self.assertEqual(self.cart.get_total_items(), 2)

    def test_cart_total_price(self):
        """Test cart total price calculation"""
        CartItem.objects.create(cart=self.cart, product=self.product1, quantity=2)
        CartItem.objects.create(cart=self.cart, product=self.product2, quantity=1)
        expected_total = (50.00 * 2) + (75.00 * 1)
        self.assertEqual(float(self.cart.get_total_price()), expected_total)


class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            name='Test Product',
            category=self.category,
            description='Test Description',
            price=100.00,
            stock=10
        )
        self.order = Order.objects.create(
            user=self.user,
            first_name='John',
            last_name='Doe',
            email='john@example.com',
            address='123 Test St',
            city='Test City',
            postal_code='12345',
            country='Test Country',
            phone='1234567890',
            total_amount=100.00
        )

    def test_order_creation(self):
        """Test that order is created correctly"""
        self.assertEqual(self.order.user, self.user)
        self.assertEqual(self.order.status, 'pending')
        self.assertEqual(float(self.order.total_amount), 100.00)

    def test_order_item_creation(self):
        """Test adding items to order"""
        order_item = OrderItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=2,
            price=self.product.price
        )
        self.assertEqual(self.order.items.count(), 1)
        self.assertEqual(float(order_item.get_total_price()), 200.00)


class ProductViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            name='Test Product',
            category=self.category,
            description='Test Description',
            price=99.99,
            stock=10,
            available=True
        )

    def test_product_list_view(self):
        """Test product list page loads correctly"""
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Product')
        self.assertTemplateUsed(response, 'products/product_list.html')

    def test_product_detail_view(self):
        """Test product detail page loads correctly"""
        response = self.client.get(f'/products/{self.product.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Product')
        self.assertTemplateUsed(response, 'products/product_detail.html')


class CartViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            name='Test Product',
            category=self.category,
            description='Test Description',
            price=99.99,
            stock=10
        )

    def test_cart_detail_view(self):
        """Test cart page loads correctly"""
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart_detail.html')

    def test_add_to_cart(self):
        """Test adding product to cart"""
        response = self.client.post(f'/cart/add/{self.product.id}/', {
            'quantity': 2
        })
        self.assertEqual(response.status_code, 302)  # Redirect after adding


class OrderViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')

    def test_order_list_view(self):
        """Test order list page loads correctly"""
        response = self.client.get('/orders/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/order_list.html')

    def test_create_order_requires_login(self):
        """Test that creating order requires authentication"""
        self.client.logout()
        response = self.client.get('/orders/create/')
        self.assertEqual(response.status_code, 302)  # Redirect to login
