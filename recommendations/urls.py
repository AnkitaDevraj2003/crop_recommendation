from django.urls import path 
from recommendations.views import form_recommendation

urlpatterns = [ 
    
    path('recommendation/', form_recommendation)

]
