from django.shortcuts import render, redirect
from create_link.models import Link
# Create your views here.

def RedirectLink(request, ShortLink):
    link = Link.objects.get(short_link = ShortLink)
    get_main_link = link.main_link
    return redirect(get_main_link)