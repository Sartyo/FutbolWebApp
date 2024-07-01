def total_import_shopping_cart(request):
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session["cart"].items():
            total = total + float(value["price"])
    else:
        total = "You must login to make a shipping order"
    return {"total_import_shopping_cart": total}