from django.urls import path, include

urlpatterns = [
    path('customers/', include(('src.api.customers.urls', 'customers'), namespace='customers')),
]