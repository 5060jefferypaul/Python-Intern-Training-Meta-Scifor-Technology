from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('gallery',views.gallery,name='gallery'),
    path('Contact Us',views.ContactUs,name='Contact Us'),
    path('About Us',views.AboutUs,name='About Us'),
    path('Laks',views.Laksha,name='Laks'),
    path('Ooty',views.Ooty,name='Ooty'),
    path('Ladakh',views.Lada,name='Ladakh'),
    path('Laks',views.Laksha,name='Laks'),
    path('Gate',views.Gate,name='Gate'),
    path('Mana',views.Manali,name='Mana'),
    path('Coorg',views.Coorg,name='Coorg'),

]
