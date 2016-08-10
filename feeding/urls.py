from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'submit_updates',views.submit_updates,name='submit_updates'),
    url(r'^update',views.update, name='update'),
    url(r'^$', views.feeding_schedule, name='schedule'),
]
