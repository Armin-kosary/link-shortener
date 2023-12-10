from django.shortcuts import render
from .forms import GetUserLinkForm
from .models import Link
from django.utils.crypto import get_random_string
# Create your views here.

def home(request):
    form = GetUserLinkForm(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            create_short_link = get_random_string(10)
            while Link.objects.filter(short_link = create_short_link).exists():
                create_short_link = get_random_string(10)
            new_link = Link(
                main_link = form.cleaned_data.get("link"),
                short_link = create_short_link
            )
            new_link.save()
            context = {
                'form' : form,
                'new_link' : create_short_link
            }
            return render(request, 'create_link/home.html', context)
        
    context = {
        'form' : form
    }
    return render(request, 'create_link/home.html', context)