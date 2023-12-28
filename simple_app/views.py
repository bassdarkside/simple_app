from django.shortcuts import render
from .models import Currency


def index(request):
    currency_list = Currency.objects.all()
    get_fields = Currency._meta.get_fields()
    colmn_names = [f.name for f in get_fields]
    context = {
        "currency_list": currency_list,
        "colmn_names": colmn_names,
    }
    return render(request, "simple/index.html", context)
