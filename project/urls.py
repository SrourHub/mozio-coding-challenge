from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from project.application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('providers/', views.provider_list),
    path('providers/<int:id>', views.provider_details),
    path('service_areas/', views.service_area_list),
    path('service_areas/<int:id>', views.service_area_details),
    path('service_areas/contain_polygon/', views.service_areas_that_contain_given_lat_lng)
]

urlpatterns = format_suffix_patterns(urlpatterns)
