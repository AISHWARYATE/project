from pickle import FALSE
from tkinter.messagebox import YES
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm,trollingForm,productForm
from django.contrib.auth import authenticate, login
from .forms import CityForm,AddBoat,addfishermen
from .models import City,products,trolling,cart,boat,fishermen
from django.contrib import messages
import urllib,json
import requests
import folium

# Create your views here.


def index(request):
    return render(request, 'index.html')

def home(request):

    return render(request, 'homepage.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('employee')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request,'admin.html')


def customer(request):
    return render(request,'customer.html')


def employee(request):
    return render(request,'employee.html')

def tr_view(request):
    # trl=[]
    troll=trolling.objects.all().values()
    print(troll)
    for i in troll:
        test=i.values()
        for j in test:
            print(j)
            # trl.append(j)
            # print(trl)
    return render(request,'trollingview.html',{'j':j})

def troling(request):
    if request.method=='POST':
        fm=trollingForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('adminpage')
    else:
        fm=trollingForm()
        return render(request,'wear.html',{'fm':fm})





def product(request):
    return render(request,'product.html')

def admin_all_prdct_view(request):
    return render(request,'ad_view_all_fishes.html')

def cust_all_prdct_view(request):
    return render(request,'cust_view_all_fishes.html')


def product_add(request):
    if request.user.is_superuser or request.user.is_employee:
        if request.method == 'POST':
            fom= productForm(request.POST,request.FILES)
            print(fom)
            if fom.is_valid():
                instance = fom.save()
                instance.user = request.user
                instance.save()
                return redirect('product_view')
        else:
            fom = productForm()
        return render(request,'addproductss.html',{'fm':fom})


def product_view(request):
    ab=products.objects.all() 
    return render(request,'fish_prdt.html',{'ab':ab})


def logout(request):
    return render(request,'homepage.html')

def admin_view_product(request):
    ac=products.objects.all() 
    return render(request,'admin_product.html',{'ac':ac})

def cust_view_product(request):
    ad=products.objects.all() 
    return render(request,'cust_view_all_products.html',{'ad':ad})

def cartview(request,id):
        fm=products.objects.filter(prod_id=id).first()
        return render(request,'viewcart.html',{'fm':fm})


# def carts(request):
#     one_objs = cart.objects.all().prefetch_related('many_set')
#     print(one_objs)
#     return render(request,'viewcart.html')



# def carts(request):
#     books = cart.objects.all()
#     return render(request,'viewcart.html',{'books':books})

 
def carts(request):
    if request.method == "POST":
        product_name=request.POST.get('prod_name')
        product_cost=request.POST.get('product_cost')
        quantity=request.POST.get('quantity')
        print(product_name,product_cost,quantity)
        total = float(product_cost) * float(quantity)
        # total_price=request.POST['price']
        add=cart(products_name=product_name,products_cost=total,quantity=quantity)
        add.save()

        data=cart.objects.all()
        return render(request,'cart.html',{'data':data})
    return render(request,'viewcart.html')


def payment(request,id):
        fmn=cart.objects.filter(cart_id=id).first()
        return render(request,'payment.html',{'fmn':fmn})


def boatdetails(request):
     if request.method == 'POST':
          fom= AddBoat(request.POST,request.FILES)
          if fom.is_valid():
               fom.save()
          
               return redirect('home')
     else:
          fom = AddBoat()
     return render(request,'addboat.html',{'fom':fom})




def viewboat(request):
     Data = boat.objects.all()
     print(Data)
     return render(request,"viewboat.html",{'Data':Data})   


def delete(request,myid):
     item = boat.objects.get(id=myid)
     item.delete()
     messages.info(request,'delete successfully')
     return redirect('viewboat')

def edit(request,myid):
     boat_item = boat.objects.get(id= myid)
     boat_list = boat.objects.all()
     context = {
          'boat_item':boat_item,
          'boat_list':boat_list
     }
     return render(request,'edit.html',context)


def update(request,myid):
     item= boat.objects.get(id= myid)
     item.boat_no = request.POST['boat_no']
     item.boat_name =request.POST['boat_name']
     item.no_of_fishermen =request.POST['no_of_fishermen']
     item.boat_length =request.POST['boat_length']
     item.upload_photo =request.POST['upload_photo']

     item.save()
     messages.info(request,"Item Updated Successfully")
     return redirect('viewboat')
 



READ_API_KEY='7QLYL32DYARK6URL'
CHANNEL_ID='1806212'

def ms(request):
   # wp = urllib.request.urlopen("http://example.com")
   

    conn = urllib.request.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                           % (CHANNEL_ID,READ_API_KEY))

    response = conn.read()
    #print ("http status code=%s" % (conn.getcode()))
    data=json.loads(response)
    print(data['field1'])
    lattitude=(data['field1'][0:9])
    print( lattitude)
    longittude=(data['field1'][10:19])
    print(longittude)
    temp=int(data['field1'][20:22])
    if(temp>=30):
         a="sunny"
     
    elif(temp<30 and temp>=25):
         a="cloudy"
    else:
         a="cools"
    print(a)     
    print(temp)
    hum=(data['field1'][23:25])
    print(hum)
    status=(data['field1'][26:27])
    print(status)

    context={'temp':temp,
    'a':a,
    'hum':hum,}

    return render(request,"weather.html",{'context':context})
    
    #print (data['field2'])
#urllib.request.urlopen("https://api.thingspeak.com/update?api_key=907TEK5GBX5K2PDB&field1=100")




def status(request):
     import datetime

     x = datetime.datetime.now()

     y=str(x)
     date=y[:10]
     time=y[10:]
     print(date )
     print(time)
     wp = urllib.request.urlopen("http://example.com")
     conn = urllib.request.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                           % (CHANNEL_ID,READ_API_KEY))
     response = conn.read()
     #print ("http status code=%s" % (conn.getcode()))
     data=json.loads(response)
     print(data['field1'])
    
     status=int(data['field1'][26:27])
     print(status)
     if(status==1):
          b="Danger Zone"
         
     else:
          b="Safe Zone"

     context={'b':b,'date':date}
     return render(request,"status.html",{'context':context})
    
    #print (data['field2'])
#urllib.request.urlopen("https://api.thingspeak.com/update?api_key=907TEK5GBX5K2PDB&field1=100")




def climate(request):
    cities = City.objects.all()
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=5e060a563266435156fbb7e9254be676'
    if request.method == 'POST':
        form = CityForm(request.POST) 
        form.save()   
    form = CityForm() 
    weather_data = []
    for city in cities:
        print(city)
        city_weather = requests.get(url.format(city)).json()      
        print (city_weather)
        weather ={
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
    weather_data.append(weather) 
    print(city_weather)
    return render(request, 'climate.html',{'weather_data' : weather_data,'form':form})



def map(request):
       conn = urllib.request.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                           % (CHANNEL_ID,READ_API_KEY))
       response = conn.read()
       data=json.loads(response)
       print(data['field1'])
       lattitude=(data['field1'][0:9])
       print( lattitude)
       longittude=(data['field1'][10:19])
       print(longittude)
       m = folium.Map(location=[lattitude,longittude],zoom_start=7)
       folium.Marker(location=[lattitude,longittude],tooltip='click for more',popup='kabani').add_to(m)
       m = m._repr_html_()
       context ={
            'm':m
            }
       return render(request,'map.html',context)

    

# def delete_cart(request,id):
#      item = cart.objects.get(cart_id=id)
#      item.delete()
#      messages.info(request,'payment success')
#      return redirect('customer')


def fishermendetails(request):
    if request.method=='POST':
        fd=addfishermen(request.POST)
        if fd.is_valid():
            fd.save()
            return redirect('employee')
    else:
         fd=addfishermen()
         return render(request,'fishermen.html',{'fd':fd})



def adminviewfishermen(request):
    dat=fishermen.objects.all()
    return render(request,'adminviewfishermen.html',{'ad':dat})
