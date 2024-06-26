import pytest
from django.db.utils import IntegrityError
from customers.models import Customer

@pytest.mark.django_db
def test_customer_str():
    customer = Customer(first_name="John", last_name="Doe")
    assert str(customer) == "John Doe"

@pytest.mark.django_db
def test_customer_get_full_name():
    customer = Customer(first_name="John", last_name="Doe")
    assert customer.get_full_name() == "John Doe"

@pytest.mark.django_db
def test_customer_to_select2():
    customer = Customer.objects.create(first_name="John", last_name="Doe")
    select2_output = customer.to_select2()
    assert select2_output == {"label": "John Doe", "value": customer.id}

@pytest.mark.django_db
def test_customer_creation():
    customer = Customer.objects.create(
        first_name="John",
        last_name="Doe",
        address="123 Main St",
        email="john.doe@example.com",
        phone="1234567890"
    )
    assert customer.first_name == "John"
    assert customer.last_name == "Doe"
    assert customer.address == "123 Main St"
    assert customer.email == "john.doe@example.com"
    assert customer.phone == "1234567890"

@pytest.mark.django_db
def test_customer_blank_fields():
    customer = Customer.objects.create(first_name="John")
    assert customer.last_name is None
    assert customer.address is None
    assert customer.email is None
    assert customer.phone is None


