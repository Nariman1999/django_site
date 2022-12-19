from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.index3, name='index3'),
    path('novosti/', views.novosti, name='novosti'),
    path('novosti/<int:pk>', views.detail_novosti, name='detail_novosti'),
    path('document/', views.document, name='document'),
    path('dohod/', views.dohod, name='dohod'),
    path('rashods/', views.rashods, name='rashods'),

] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)