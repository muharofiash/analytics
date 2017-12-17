from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^detail/(?P<unit_id>\d+)/', views.hr_detail, name='detail')
]
