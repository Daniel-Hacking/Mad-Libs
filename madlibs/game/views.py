from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Attributes
from .forms import AttributesForm

# Create your views here.


def home(request):
    Attributes.objects.all().delete()
    return render (request, 'home/index.html')

def stories(request, storyid):

    attributes = Attributes.objects.all()
    context = {
        'attributes': attributes
    }
    return render(request, 'stories/' + str(storyid) + '.html', context)

def attribute_form(request, storyid):
    
    ##Attributes.objects.all().delete()

    form = AttributesForm(request.POST or None) 

    if form.is_valid():
        form.save()
        return redirect(reverse(stories, kwargs={'storyid':storyid}))
        ##return render(request, 'stories/' + str(storyid) + '.html')
    else:
        return render(request, 'home/attribute_form.html', {'form': form})