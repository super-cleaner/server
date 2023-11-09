from django.urls import path
from . import views
app_name = 'record'

urlpatterns = [
    path("",views.main),
    path("check",views.check),
    path("result/<int:game_id>",views.result),
]

