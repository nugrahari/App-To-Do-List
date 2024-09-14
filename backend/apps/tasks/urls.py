from django.urls import path, include

urlpatterns = [
    path('api/', include('apps.tasks.api.urls')),  # Pastikan ini sesuai dengan nama aplikasi Anda
]