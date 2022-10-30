from django.urls import path
from siteapp.views import (home,disclaimer,termsConditions,codeOfEthics)
urlpatterns = [
    path('',home.as_view(),name='home'),
    path('disclaimer',disclaimer,name='disclaimer'),
    path('termscondition',termsConditions,name='termscondition'),
path('codeofethics',codeOfEthics,name='codeofethics'),
]