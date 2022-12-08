from django.urls import path
from . import views
from django.views.i18n import JavaScriptCatalog
urlpatterns=[
    path('', views.date_time, name='date_time'),
    path('jsi18n',JavaScriptCatalog.as_view(), name='js-catlog')

]
