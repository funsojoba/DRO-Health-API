from django.urls import path

from period_cycle_api.views.cycle_view import EstimateCycleView


urlpatterns = [
    path('create-cycles/', EstimateCycleView.as_view())
]
