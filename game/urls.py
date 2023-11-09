from django.urls import path
from .views import GameSettingData

app_name = 'game'

urlpatterns = [
    path('', GameSettingData.as_view())
]