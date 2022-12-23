from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ItemSerializer
from .models import Item
from rest_framework import serializers, status
from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        # Read
        "all_items": "/items",
        "Search by Category": "items/?category=category_name",
        "Search by Subcategory": "items/?subcategory=subcategory_name",
        # Create
        "Add": "/create",
        # Update
        "Update": "item/update/id",
        # Delete
        "Delete": "item/delete/id",
    }

    return Response(api_urls)


@api_view(["GET"])
def getItem(request, id):
    item = get_object_or_404(Item, pk=id)

    if item:
        data = ItemSerializer(item).data
        return Response(data, status=status.HTTP_200_OK)

    return Response(
        {"message": f"Item does not exists with id : {id}"},
        status=status.HTTP_404_NOT_FOUND,
    )


@api_view(["GET"])
def getAllItems(request):

    if request.query_params:
        items = Item.objects.filter(**request.query_params.dict())
    else:
        items = Item.objects.all()

    if items:
        data = ItemSerializer(items, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response({"message": "No data found!"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def addItem(request):
    item = ItemSerializer(data=request.data)

    if Item.objects.filter(**request.data).exists():
        raise serializers.ValidationError("This data already exists!!")

    if item.is_valid():
        item.save()
        return Response(item.data, status=status.HTTP_201_CREATED)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["PATCH"])
def updateItem(request, id):
    item = Item.objects.get(pk=id)
    data = ItemSerializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data, status=status.HTTP_201_CREATED)

    if not item:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE"])
def deleteItem(request, id):
    try:
        item = Item.objects.get(pk=id)

        if item:
            item.delete()
            return Response(
                {"message": f"Succesfully Delete item with {id}"},
                status=status.HTTP_204_NO_CONTENT,
            )
    except:
        return Response(
            {"message": f"Item does not exists with id : {id}"},
            status=status.HTTP_404_NOT_FOUND,
        )
