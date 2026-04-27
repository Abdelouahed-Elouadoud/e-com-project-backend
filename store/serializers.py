from rest_framework import serializers
from .models import Custumer , Collection , Product , Reviews

class CustomerSerializer(serializers.ModelSerializer):
    #name = serializers.CharField(source='first_name')
    first_name = serializers.CharField(source='user.first_name')
    email = serializers.EmailField(source='user.email')

    class Meta:
        model = Custumer
        fields = ['id','first_name' ,'email', 'phone']


class CollectionSerializer(serializers.ModelSerializer):
    class Meta :
        model = Collection
        fields =['id','titre']


class ProductSerializer(serializers.ModelSerializer):
    collection = CollectionSerializer(read_only=True)
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'description',
            'unit_price',
            'inventory',
            'last_update',
            'collection',
            'slug'
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta :
        model=Reviews
        fields=['id','date','name','description','product']
        