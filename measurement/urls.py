from django.urls import path

from measurement.views import sensors

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', sensors)
]
