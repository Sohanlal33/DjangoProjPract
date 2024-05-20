from django.urls import path
from testapp import views
urlpatterns = [
    path('hello',views.greetings),
    path('about',views.about),
    path('contact',views.contact),

]