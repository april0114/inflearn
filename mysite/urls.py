# """
# URL configuration for mysite project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('', HomeView.as_view(), name ='home'),
#     path('blog/', include(blog.urls)),
#     path('api/', include(api.urls)),
#     path('admin/', admin.site.urls),
#     #drf
#     path('api-auth/', include('rest_framework.urls')),


# ]

# urlpatterns += static(setting.MEDIA_URL, document_root = setting.MEDIA_ROOT)

from django.urls import path, include
from django.contrib import admin


# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('api2/', include('api2.urls')),
    path('', include('api.urls')),
    path('blog/', include('blog.urls'))


]