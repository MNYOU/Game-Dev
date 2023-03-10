from django.urls import path

from .views import *

urlpatterns = [
    path('', home),
    path('base', base),
    path('list/<int:vacancy_id>', vacancies),
    path('last', last_vacancies),
    path('relevance/', relevance),
    path('geography', geography)
]