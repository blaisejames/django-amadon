from django.shortcuts import render, HttpResponse, redirect

def index(request):
    context = {
        "count": request.session.get('count', 0),
        "total": request.session.get('total', 0),
        "grand_total": request.session.get("grand_total", 0),
        "product_data": [ 
            { "id": 0, "item": "Dojo Tshirt", "price": 19.99 },
            { "id": 1, "item": "Dojo Sweater", "price": 29.99 },
            { "id": 2, "item": "Dojo Cup", "price": 4.95 },
            { "id": 3, "item": "Algorithm Book", "price": 19.99},
        ],
    }
    request.session['cart'] = context
    return render(request, 'amadon/index.html', context)

def buy(request):
    if request.method == "GET":
        return render(request, "amadon/add.html")
    elif request.method == "POST":
        id = int(request.POST['id'])
        quantity = int(request.POST['quantity'])
        price = request.session['cart']['product_data'][id]['price']
        request.session.modified = True
        request.session['cart']['count'] = request.session['cart']['count'] + quantity
        request.session['cart']['total'] = quantity * price
        print request.session['cart']['total']
        request.session['cart']['grand_total'] = request.session['cart']['grand_total'] + request.session['cart']['total']
        print request.session['cart']
        return redirect("checkout")
        
def checkout(request):
    print request.session['cart']
    return render(request,'amadon/checkout.html')

def clear(request):
    try:
        for key in request.session.keys():
            del request.session[key]
    except KeyError:
        pass
    return redirect('index')