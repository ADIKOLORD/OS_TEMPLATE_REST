from rest_framework.serializers import ModelSerializer

from theonlyapp.models import MyModel, Category, Cart


class MyModelSerializer(ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

