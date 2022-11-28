from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.db import connection


# Create your views here.

def listing(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM restaurant")
    restaurantlist = dictfetchall(cursor)

    context = {
        "restaurantlist": restaurantlist
    }

    # Message according medicines Role #
    context['heading'] = "Restaurant Details";
    return render(request, 'restaurant-details.html', context)

def lists(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM restaurant")
    restaurantlist = dictfetchall(cursor)

    context = {
        "restaurantlist": restaurantlist
    }

    # Message according medicines Role #
    context['heading'] = "Restaurant Details";
    return render(request, 'restaurant-list.html', context)

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def getData(id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM restaurant WHERE restaurant_id = " + id)
    dataList = dictfetchall(cursor)
    return dataList[0];

def update(request, restaurantId):
    context = {
        "fn": "update",
        "restaurantDetails": getData(restaurantId),
        "heading": 'Update Restaurant',
    }
    if (request.method == "POST"):
        cursor = connection.cursor()
        cursor.execute("""
                   UPDATE restaurant
                   SET restaurant_name=%s, restaurant_description=%s WHERE restaurant_id = %s
                """, (
            request.POST['restaurant_name'],
            request.POST['restaurant_description'],
            restaurantId
        ))
        context["restaurantDetails"] =  getData(restaurantId)
        messages.add_message(request, messages.INFO, "Restaurant updated succesfully !!!")
        return redirect('restaurant-listing')
    else:
        return render(request, 'restaurant.html', context)


def add(request):
    context = {
        "fn": "add",
        "heading": 'Add Restaurant'
    };
    if (request.method == "POST"):
        cursor = connection.cursor()
        cursor.execute("""
		   INSERT INTO restaurant
		   SET restaurant_name=%s, restaurant_description=%s
		""", (
            request.POST['restaurant_name'],
            request.POST['restaurant_description']))
        return redirect('restaurant-listing')
    return render(request, 'restaurant.html', context)

def delete(request, id):
    cursor = connection.cursor()
    sql = 'DELETE FROM restaurant WHERE restaurant_id=' + id
    cursor.execute(sql)
    messages.add_message(request, messages.INFO, "Restaurant Deleted succesfully !!!")
    return redirect('restaurant-listing')
