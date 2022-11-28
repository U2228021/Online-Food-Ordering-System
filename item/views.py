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
    cursor.execute("SELECT * FROM item")
    itemlist = dictfetchall(cursor)

    context = {
        "itemlist": itemlist
    }

    # Message according medicines Role #
    context['heading'] = "Item Details";
    return render(request, 'item-details.html', context)

def lists(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM item")
    itemlist = dictfetchall(cursor)

    context = {
        "itemlist": itemlist
    }

    # Message according medicines Role #
    context['heading'] = "Item Details";
    return render(request, 'item-list.html', context)

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def getData(id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM item WHERE item_id = " + id)
    dataList = dictfetchall(cursor)
    return dataList[0];

def update(request, itemId):
    context = {
        "fn": "update",
        "itemDetails": getData(itemId),
        "heading": 'Update Item',
    }
    if (request.method == "POST"):
        cursor = connection.cursor()
        cursor.execute("""
                   UPDATE item
                   SET item_name=%s, item_description=%s WHERE item_id = %s
                """, (
            request.POST['item_name'],
            request.POST['item_description'],
            itemId
        ))
        context["itemDetails"] =  getData(itemId)
        messages.add_message(request, messages.INFO, "Item updated succesfully !!!")
        return redirect('item-listing')
    else:
        return render(request, 'item.html', context)


def add(request):
    context = {
        "fn": "add",
        "heading": 'Add Item'
    };
    if (request.method == "POST"):
        cursor = connection.cursor()
        cursor.execute("""
		   INSERT INTO item
		   SET item_name=%s, item_description=%s
		""", (
            request.POST['item_name'],
            request.POST['item_description']))
        messages.add_message(request, messages.INFO, "We got your request. Thanks for it !!!")
        return redirect('item-add')
    return render(request, 'item.html', context)

def delete(request, id):
    cursor = connection.cursor()
    sql = 'DELETE FROM item WHERE item_id=' + id
    cursor.execute(sql)
    messages.add_message(request, messages.INFO, "Item Deleted succesfully !!!")
    return redirect('item-listing')
