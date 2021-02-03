from django.shortcuts import render
from property.models import Property, Category
from agents.models import Agent

# Create your views here.
def home(request):
    category_list = Category.objects.all()
    property_list = Property.objects.all()
    agents_list = Agent.objects.all()
    template = 'home/home.html'
    context = {
        'category_list': category_list,
        'property_list_home': property_list,
        'agents_list_home': agents_list
    }

    return render(request, template, context)
