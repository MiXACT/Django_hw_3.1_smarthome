from django.urls import path

from measurement.views import SensGetPost, SensModify

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensGetPost.as_view()),
    path('sensors/<int:pk>/', SensModify.as_view())
]
