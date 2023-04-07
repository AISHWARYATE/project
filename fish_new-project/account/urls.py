from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('index', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('employee/', views.employee, name='employee'),
    path('wear',views.troling,name='wear'),
    path('product/',views.product,name='product') ,
    path('product_add/',views.product_add,name='product_add') ,
    path('product_view/',views.product_view,name='product_view') ,
    path('tr_view/',views.tr_view,name='tr_view') ,
    path('logout/',views.logout,name='logout') ,
    path('admin_view_product',views.admin_view_product,name='admin_view_product') ,
    path('admin_all_prdct_view',views.admin_all_prdct_view,name='admin_all_prdct_view') ,
    path('cust_all_prdct_view',views.cust_all_prdct_view,name='cust_all_prdct_view') ,
    path('cust_view_product/',views.cust_view_product,name='cust_view_product') ,
    path('cust_view_product/<int:id>',views.cartview,name='cart') ,
    path('carts/',views.carts,name='carts') ,
    path('carts/<int:id>',views.payment,name='payment') ,
    path('boatdetails',views.boatdetails,name='boatdetails'),
    path('viewboat',views.viewboat,name='viewboat'),
    path('delete/<int:myid>/', views.delete, name="delete"),
    path('edit/<int:myid>/', views.edit, name="edit"),
    path('update/<int:myid>/', views.update, name="update"),
    path('main',views.ms,name='main'),
    path('status',views.status,name='status'),
    path('climate',views.climate,name='climate'),
    path('map/',views.map,name='map'),
    path('fishermen',views.fishermendetails,name='fishermen'),
    path('adminviewfishermen',views.adminviewfishermen,name='adminviewfishermen'),

    # path('delete_cart/<int:id>/', views.delete_cart, name="delete_cart"),#the path for our index view
]
