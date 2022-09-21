from django.shortcuts import render
from .forms import HomeForm
from django.http import HttpResponseRedirect
from .models import HomeApp

# Create your views here.



def homeView(request):
    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            form.save()
        
    return render(request, 'homeApp/homeForm.html', {'form': HomeForm})