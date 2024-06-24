from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from .models import Customer


@login_required(login_url="/accounts/login/")
def customers_list_view(request):
    context = {
        "active_icon": "customers",
        "customers": Customer.objects.all()
    }
    return render(request, "customers/customers.html", context=context)


@login_required(login_url="/accounts/login/")
def customers_add_view(request):
    context = {
        "active_icon": "customers",
    }

    if request.method == 'POST':
        # Save the POST arguments
        data = request.POST

        attributes = {
            "first_name": data['first_name'],
            "last_name": data['last_name'],
            "address": data['address'],
            "email": data['email'],
            "phone": data['phone'],
        }

        # Check if a customer with the same attributes exists
        if Customer.objects.filter(**attributes).exists():
            messages.error(request, 'Customer already exists!',
                           extra_tags="warning")
            return redirect('customers:customers_add')

        try:
            # Create the customer
            new_customer = Customer.objects.create(**attributes)

            # If it doesn't exist save it
            new_customer.save()

            messages.success(request, 'Customer: ' + attributes["first_name"] + " " +
                             attributes["last_name"] + ' created successfully!', extra_tags="success")
            return redirect('customers:customers_list')
        except Exception as e:
            messages.success(
                request, 'There was an error during the creation!', extra_tags="danger")
            print(e)
            return redirect('customers:customers_add')

    return render(request, "customers/customers_add.html", context=context)


@login_required(login_url="/accounts/login/")
def customers_update_view(request, customer_id):
    try:
        customer = get_object_or_404(Customer, id=customer_id)

        if request.method == 'POST':
            data = request.POST

            # Update the customer attributes
            customer.first_name = data['first_name']
            customer.last_name = data['last_name']
            customer.address = data['address']
            customer.email = data['email']
            customer.phone = data['phone']
            customer.save()

            messages.success(request, 'Customer: ' + customer.get_full_name() + ' updated successfully!', extra_tags="success")
            return redirect('customers:customers_list')

    except Customer.DoesNotExist:
        messages.error(request, 'Customer not found!', extra_tags="danger")
        return redirect('customers:customers_list')
    except Exception as e:
        messages.error(request, 'Error updating customer: ' + str(e), extra_tags="danger")
        return redirect('customers:customers_list')

    context = {
        "active_icon": "customers",
        "customer": customer,
    }

    return render(request, "customers/customers_update.html", context=context)

@login_required(login_url="/accounts/login/")
def customers_delete_view(request, customer_id):
    """
    Args:
        request:
        customer_id : The customer's ID that will be deleted
    """
    try:
        # Get the customer to delete
        customer = Customer.objects.get(id=customer_id)
        customer.delete()
        messages.success(request, '¡Customer: ' + customer.get_full_name() +
                         ' deleted!', extra_tags="success")
        return redirect('customers:customers_list')
    except Exception as e:
        messages.success(
            request, 'There was an error during the elimination!', extra_tags="danger")
        print(e)
        return redirect('customers:customers_list')
