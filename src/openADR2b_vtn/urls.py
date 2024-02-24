from django.urls import path
from .views import EiRegisterPartyView


urlpatterns = [
    path("EiRegisterParty/", EiRegisterPartyView.as_view(), name="EiRegisterParty_url_path"),
    
]
