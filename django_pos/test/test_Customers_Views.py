import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client
from customers.models import Customer

@pytest.fixture
def client():
    return Client()

@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='password')

@pytest.fixture
def customer():
    return Customer.objects.create(
        first_name='John',
        last_name='Doe',
        address='123 Main St',
        email='john.doe@example.com',
        phone='1234567890'
    )

@pytest.mark.django_db
def test_customers_list_view(client, user):
    client.login(username='testuser', password='password')
    response = client.get(reverse('customers:customers_list'))
    assert response.status_code == 200
    assert 'customers' in response.context

@pytest.mark.django_db
def test_customers_add_view_get(client, user):
    client.login(username='testuser', password='password')
    response = client.get(reverse('customers:customers_add'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_customers_add_view_post(client, user):
    client.login(username='testuser', password='password')
    data = {
        'first_name': 'Jane',
        'last_name': 'Doe',
        'address': '456 Elm St',
        'email': 'jane.doe@example.com',
        'phone': '0987654321'
    }
    response = client.post(reverse('customers:customers_add'), data)
    assert response.status_code == 302  # Should redirect after successful addition
    assert Customer.objects.filter(email='jane.doe@example.com').exists()

@pytest.mark.django_db
def test_customers_update_view_get(client, user, customer):
    client.login(username='testuser', password='password')
    response = client.get(reverse('customers:customers_update', args=[customer.id]))
    assert response.status_code == 200
    assert 'customer' in response.context

@pytest.mark.django_db
def test_customers_update_view_post(client, user, customer):
    client.login(username='testuser', password='password')
    data = {
        'first_name': 'John',
        'last_name': 'Smith',
        'address': '123 Main St',
        'email': 'john.smith@example.com',
        'phone': '1234567890'
    }
    response = client.post(reverse('customers:customers_update', args=[customer.id]), data)
    assert response.status_code == 302  # Should redirect after successful update
    customer.refresh_from_db()
    assert customer.last_name == 'Smith'
    assert customer.email == 'john.smith@example.com'

@pytest.mark.django_db
def test_customers_delete_view(client, user, customer):
    client.login(username='testuser', password='password')
    response = client.post(reverse('customers:customers_delete', args=[customer.id]))
    assert response.status_code == 302  # Should redirect after successful deletion
    assert not Customer.objects.filter(id=customer.id).exists()
