from  django.urls import path

from api.v1.dashboard.user.view import RegisterApi
from api.v1.sayt.category.view import CategoryView
from api.v1.sayt.product.view import ProductView

urlpatterns=[
    path("sayt/ctg/",CategoryView.as_view(),name='api_ctg_list'),
    path("sayt/ctg/<int:pk>/",CategoryView.as_view(),name='api_ctg_one'),
    path("sayt/pro/", ProductView.as_view(),name='api_pro-list'),
    path("sayt/pro/<int:pk>/", ProductView.as_view(),name='api_pro_one'),
    path("dashboard/register/", RegisterApi.as_view(),name='api_dashboard_register'),
    # path("dashboard/login/", RegisterApi.as_view(),name='api_dashboard_'),
]
