from django.shortcuts import render
from screens.models import Weight_distribution
import matplotlib.pyplot as plt
import numpy as np


def introduction(request):
    return render(request, 'introduction.html')


def first_screen(request):
    if request.method == 'POST':

        cty = request.POST.get("cty")




        from screens.models import Customer_Type, Juridictional_Risk, List_Matching, Profile_linkage, Product_Service, \
            Transaction_Behavior

        context = {

            'cty': Customer_Type.objects.all(),

            'pds': Product_Service.objects.all(),

            'jdr': Juridictional_Risk.objects.all(),

            'ltm': List_Matching.objects.all(),

            'pfl': Profile_linkage.objects.all(),

            'tsb': Transaction_Behavior.objects.all(),

        }

        return render(request, 'first-screen.html', context)
    else:
        return render(request, 'first-screen.html', context)


def weight_distribution(request):
    context = {
        'wtd': Weight_distribution.objects.all()
    }
    return render(request, 'weight_distribution.html', context)


def score(request):
    return render(request, 'score.html')


def Customer_Type(request):
    from screens.models import Customer_Type
    context = {
        'cty': Customer_Type.objects.all()
    }
    return render(request, 'Customer_Type.html', context)


def Product_Service(request):
    from screens.models import Product_Service
    context = {
        'pds': Product_Service.objects.all()
    }
    return render(request, 'Product_Service.html', context)


def Juridictional_Risk(request):
    from screens.models import Juridictional_Risk
    context = {
        'jdr': Juridictional_Risk.objects.all()
    }
    return render(request, 'Juridictional_Risk.html', context)


def List_Matching(request):
    from screens.models import List_Matching
    context = {
        'ltm': List_Matching.objects.all()
    }
    return render(request, 'List_Matching.html', context)


def Profile_linkage(request):
    from screens.models import Profile_linkage
    context = {
        'pfl': Profile_linkage.objects.all()
    }
    return render(request, 'Profile_linkage.html', context)


def Transaction_Behavior(request):
    from screens.models import Transaction_Behavior
    context = {
        'tsb': Transaction_Behavior.objects.all()
    }
    return render(request, 'Transaction_Behavior.html', context)
