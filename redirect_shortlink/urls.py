from django.urls import path
from .views import RedirectLink
urlpatterns = [
    path('<ShortLink>', RedirectLink, name='redirector')
]
