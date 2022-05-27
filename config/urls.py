from django.contrib import admin
from django.urls import path, include

''
# for swagger setting
from .swagger import swagger_urlpatterns

# end swagger setting
''
# for get router to ModelViewSet
from rest_framework.routers import DefaultRouter

# end import
''
# for media setting
from django.conf.urls.static import static

from . import settings

# end media setting
''
# import class for View in views.py
from theonlyapp.views import MyModelAPIViewSet

# end import
''
# TO ADMIN PANEL TITLE
admin.site.site_header = 'Наша Админка'
admin.site.index_title = 'Админ Ади'
# END ADMIN PANEL TITLE


router = DefaultRouter()
router.register('mymodel', MyModelAPIViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))

]
# add media urls to urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# add to main urlpatterns swagger_urls
urlpatterns += swagger_urlpatterns
# end adding
