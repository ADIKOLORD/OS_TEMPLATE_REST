from rest_framework.viewsets import ModelViewSet
# for get permissions
from rest_framework import permissions

# for get filters
from rest_framework import filters

# import your own models in (models, serializers).py
from theonlyapp.models import MyModel
from theonlyapp.serializers import MyModelSerializer


class MyModelAPIViewSet(ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

    permission_classes = [permissions.AllowAny]

    # you should add this to INSTALLED APPS
    # 'django_filters'
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['price', 'pub_date']











#####################################--QR CODE--#########################################
"""
from django.shortcuts import render
import qrcode
import qrcode.image.svg
from io import BytesIO
def index(request):
    context = {}
    if request.method == "POST":
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(request.POST.get("qr_text",""), image_factory=factory, box_size=20)
        stream = BytesIO()
        img.save(stream)
        context["svg"] = stream.getvalue().decode()

    return render(request, "qrcode.html", context=context)
"""
