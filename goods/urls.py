from django.urls import include, path
# from .views import booking
# from .views import update_booking
from goods import views

app_name='goods'

urlpatterns = [
    path('search/', views.catalog, name='search'),
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),
    # path('booking/<int:product_id>/', booking, name='booking'),
    # path('booking/update/<int:display_id>/', update_booking, name='update_booking'),
    # path('update-booking/', update_booking, name='update_booking_url'),
    
]