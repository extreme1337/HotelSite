from django.shortcuts import render
from property.models import Property, Category
from django.db.models import Count
from agents.models import Agent

# Create your views here.
def home(request):
    category_list = Category.objects.annotate(property_count=Count('property')).values('category_name', 'property_count', 'image')

    property_list = Property.objects.all()
    agents_list = Agent.objects.all()
    template = 'home/home.html'
    context = {
        'category_list_home': category_list,
        'property_list_home': property_list,
        'agents_list_home': agents_list
    }

    return render(request, template, context)
