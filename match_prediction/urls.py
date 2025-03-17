from django.contrib import admin
from django.urls import path, include
from users.views import home_view  # import your home view
from users import views 

   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # root URL now shows home_view
    path('users/', include('users.urls')), 
    path('live/', views.live_view, name='live'), # adjust if your app name is different
]
