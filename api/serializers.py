from rest_framework import serializers
from django.db.models import fields
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        many = True
        fields = ["name", "category", "subcategory", "amount"]
