from django.shortcuts import render, get_object_or_404, \
    HttpResponseRedirect, redirect

from django.contrib import messages

from product.models import Product, Subcategory, Order
from product.forms import OrderForm


def index(request):
    context = {
        'products': Product.objects.filter(on_the_main=True)
    }

    return render(request, 'product/index.html', context)


def subcategory_product(request, id):
    context = {
        'subcategory': get_object_or_404(Subcategory, id=id)
    }
    return render(request, 'product/subcategory-product.html', context)


def product_details(request, id):
    context = {
        'product': get_object_or_404(Product, id=id),
    }
    return render(request, 'product/product-details.html', context)


def add_product_to_session(request, p_id):
    request.session.modified = True
    if 'products' not in request.session:
        request.session['products'] = []
    if p_id not in request.session['products']:
        request.session['products'].append(p_id)
        messages.info(request, 'Added to cart!')
    else:
        messages.info(request, 'Already exists!')


def delete_product_from_session(request, id):
    request.session.modified = True
    if id in request.session['products']:
        print(request.session['products'])
        request.session['products'].remove(str(id))
        print(request.session['products'])
        return HttpResponseRedirect('/cart')


def cart(request):
    if request.method == 'POST':
        next_page = request.POST.get('next', '/')
        print(next_page)
        p_id = request.POST.get('product_id')
        add_product_to_session(request, p_id)
        # show all elements in session
        # for key, value in request.session.items():
        #     print('{} => {}'.format(key, value))
        return HttpResponseRedirect(next_page)
    else:
        if request.session.get('products'):
            products = Product.objects.filter(
                id__in=request.session['products']
            )
            total_price, total_count = 0, 0
            for item in products:
                total_price = item.price + total_price
                total_count += 1
            return render(request, 'product/cart.html',
                          {'products': products,
                           'total_price': total_price,
                           'total_count': total_count})
        else:
            return render(request, 'product/cart.html')


def make_order(request):
    products = ''
    try:
        products = Product.objects.filter(
            id__in=request.session['products']
        )
    except KeyError:
        request.session['products'] = []
    total_price, total_count = 0, 0
    for item in products:
        total_price = item.price + total_price
        total_count += 1
    form = OrderForm(request.POST)
    if request.method == "POST":
        # create a form instance:

        if request.session['products']:
            if form.is_valid():
                name = request.POST.get('name')
                email = request.POST.get('email')
                products = Product.objects.filter(
                    id__in=request.session['products']
                ).values('id')
                q = Order(name_user=name, email_user=email, product_ids=products,
                          total_price=total_price, total_count=total_count)
                q.save()

                messages.info(request, 'we took the order')
                # clear the session
                request.session.flush()
                return HttpResponseRedirect('/')
        else:
            messages.info(request, 'cart is empty')
    else:
        form = OrderForm()
    return render(request, 'product/cart.html', {'form': form,
                                                 'products': products,
                                                 'total_price': total_price,
                                                 'total_count': total_count})
