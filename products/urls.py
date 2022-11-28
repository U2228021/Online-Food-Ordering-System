from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.products, name="products"),
    url(r'^filters/(?P<typeID>\w{0,50})/$', views.product_filter, name="product_filter"),
    url(r'^product-listing$', views.productlisting, name="productlisting"),
    url(r'^payment$', views.payment, name="payment"),
    url(r'^cart_listing$', views.cart_listing, name="cart_listing"),
    url(r'^order-listing$', views.orderlisting, name="orderlisting"),
    url(r'^order-items/(?P<orderID>\w{0,50})/$', views.order_items, name="order_items"),
    url(r'^order-edit/(?P<orderID>\w{0,50})/$', views.order_edit, name="order_edit"),
    url(r'^order-cancel/(?P<orderID>\w{0,50})/$', views.cancel_order, name="cancel_order"),
    url(r'^add$', views.add, name="add"),
    url(r'^product-details/(?P<productId>\w{0,50})/$', views.product_details, name="product_details"),
    url(r'^update/(?P<productId>\w{0,50})/$', views.update, name="update"),
    url(r'^cart-delete/(?P<itemId>\w{0,50})/$', views.delete_item, name="delete_item"),
    url(r'^delete/(?P<prodId>\w{0,50})/$', views.delete, name="delete"),
    url(r'^stock$', views.stock, name="stock"),
    url(r'^deletestock/(?P<id>\w{0,50})/$', views.deletestock, name="deletestock"),
    url(r'^order$', views.order, name="order"),
    url(r'^restaurantlisting$', views.restaurantlisting, name="restaurantlisting"),
    url(r'^addrestaurant$', views.addrestaurant, name="addrestaurant"),
    url(r'^deleterestaurant/(?P<id>\w{0,50})/$', views.deleterestaurant, name="deleterestaurant"),
]
