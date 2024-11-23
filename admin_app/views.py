from django.shortcuts import render,redirect,get_object_or_404
from admin_app.models import *
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.db.models import Count
from django.urls import reverse

# Create your views here.

def store_owner_login_required(store_owner_function):
    def check_store_owner(request,*args,**kwrgs):
        if 'store_owner_sess_id' not in request.session:
            return redirect('store_own_login')
        return store_owner_function(request,*args,**kwrgs)
    return check_store_owner

def admin_login_required(admin_fuction):
    def check_admin(request,*args,**kwargs):
        if 'admin_id' not in request.session:
            return redirect('admin_page_login')
        return admin_fuction(request,*args,**kwargs)
    return check_admin

@store_owner_login_required
def index(request):
    store_owner_name=request.session.get('store_owner_sess_name')
    return render(request, 'index.html',{'store_owner_name':store_owner_name})

def store_owner_register(request):
    if request.method=='POST':
        store_owner_name=request.POST['store_ownwer_name']
        store_ownwer_email=request.POST['store_ownwer_email']
        store_ownwer_mobile=request.POST['store_ownwer_mobile']
        store_ownwer_password=request.POST['store_ownwer_password']
        store_ownwer_confirm_password=request.POST['store_ownwer_confirm_password']
        if Store_owner_login.objects.filter(store_ownwer_email=store_ownwer_email).exists():
            return HttpResponse('mail already taken')
        if store_ownwer_password!=store_ownwer_confirm_password:
            return HttpResponse('Password not matches')
        else:
            Store_owner=Store_owner_login(store_ownwer_name=store_owner_name,store_ownwer_email=store_ownwer_email,store_ownwer_mobile=store_ownwer_mobile)
            Store_owner.hash_password(store_ownwer_password)
            Store_owner.save()
    return render(request, 'store_owner_register.html')

def store_owner_login(request):
    if request.method=='POST':
        store_ownwer_email=request.POST['store_ownwer_email']
        store_ownwer_password=request.POST['store_ownwer_password']
        if not Store_owner_login.objects.filter(store_ownwer_email=store_ownwer_email).exists():
            return HttpResponse("email doesnot exists, please create an account")
        Store_owner=Store_owner_login.objects.get(store_ownwer_email=store_ownwer_email)
        if Store_owner.check_password(store_ownwer_password):
            request.session['store_owner_sess_id']=Store_owner.id
            request.session['store_owner_sess_email']=Store_owner.store_ownwer_email
            request.session['store_owner_sess_name']=Store_owner.store_ownwer_name
            if Store.objects.filter(store_ownwer_name_id=request.session['store_owner_sess_id']).exists():
                return redirect('index_page')
            else:
                return redirect('store_register')
        else:
            return HttpResponse("email and password doesnt match")
    return render(request, 'store_owner_login.html')

@store_owner_login_required
def store_owner_logout(request):
    del request.session['store_owner_sess_id']
    del request.session['store_owner_sess_email']
    del request.session['store_owner_sess_name']
    return redirect('store_own_login')

def admin_page_register(request):
    if request.method=='POST':
        admin_name=request.POST['admin_name']
        admin_mail=request.POST['admin_mail']
        admin_password=request.POST['admin_password']
        admin_confirm_password=request.POST['admin_confirm_password']
        if Admin_login.objects.filter(admin_mail=admin_mail).exists():
            return HttpResponse('mail already taken')
        if admin_password!=admin_confirm_password:
            return HttpResponse('Password not matches')
        else:
            admin_login=Admin_login(admin_name=admin_name,admin_mail=admin_mail)
            admin_login.hash_password(admin_password)
            admin_login.save()
    return render(request, 'admin_register.html')

def admin_page_login(request):
    if request.method=='POST':
        admin_mail=request.POST['admin_mail']
        admin_password=request.POST['admin_password']
        if not Admin_login.objects.filter(admin_mail=admin_mail).exists():
            return HttpResponse("email doesnot exists, please create an account")
        admin_login=Admin_login.objects.get(admin_mail=admin_mail)
        if admin_login.check_password(admin_password):
            request.session['admin_id']=admin_login.id
            request.session['admin_mail']=admin_login.admin_mail
            request.session['admin_name']=admin_login.admin_name
            return redirect('admin_index')
        else:
            return HttpResponse("email and password doesnt match")
    return render(request, 'admin_login.html')

@admin_login_required
def admin_page_logout(request):
    del request.session['admin_id']
    del request.session['admin_mail']
    del request.session['admin_name']
    return redirect('admin_page_login')


@admin_login_required
def admin_index(request):
    admin_name=request.session['admin_name']
    return render(request, 'admin_index.html',{'admin_name':admin_name})

@store_owner_login_required
def store_register(request):
    stowner_name=request.session.get('store_owner_sess_name')
    store_owner_id=request.session.get('store_owner_sess_id')
    store_owner=Store_owner_login.objects.all()
    states=State.objects.all()
    cities=City.objects.all()
    if request.method=='POST':
        store_ownwer_name_id=request.POST['store_ownwer_name']
        store_ownwer_name=Store_owner_login.objects.get(id=store_ownwer_name_id)
        store_name=request.POST['store_name']
        store_location=request.POST['store_location']
        store_description=request.POST['store_description']
        city=City.objects.get(id=request.POST['city'],state_id=request.POST['state'])
        zip_code=request.POST['zip_code']
        latitude=request.POST['latitude']
        longitude=request.POST['longitude']
        store_number=request.POST['store_number']
        store_image=request.FILES['store_image']
        Store.objects.create(store_ownwer_name=store_ownwer_name,store_name=store_name,store_location=store_location,store_description=store_description,city=city,zip_code=zip_code,latitude=latitude,longitude=longitude,store_number=store_number,store_image=store_image)
        return redirect('index_page')
    context={'store_owner':store_owner,'states':states,'cities':cities,'stowner_name':stowner_name,'store_owner_id':store_owner_id}
    return render(request,'store_register.html',context)
    
def noti(request):
    return render(request, 'notification.html')

@admin_login_required
def admin_page_category(request):
    admin_name=request.session['admin_name']
    product_types=Product_Type.objects.all()
    categories=Category.objects.all()
    if request.method=='POST':
        product_type=Product_Type.objects.get(id=request.POST['product_type'])
        category=request.POST['category']
        category_image=request.FILES['category_image']
        Category.objects.create(product_type=product_type,category=category,category_image=category_image)
    return render(request, 'category.html',{'product_types':product_types,'categories':categories,'admin_name':admin_name})

@admin_login_required
def admin_page_type_of_product(request):
    admin_name=request.session['admin_name']
    product_types=Product_Type.objects.all()
    if request.method=='POST':
        product_type=request.POST['product_type']
        Product_Type.objects.create(product_type=product_type)
        # try:
        #     Product_Type.objects.create(product_type=product_type, product_type_image=product_type_image)
        #     print("Product created successfully!")
        # except Exception as e:
        #     print("Error creating product:", e)
    return render(request, 'type_of_product.html',{'product_types':product_types,'admin_name':admin_name})

@admin_login_required
def admin_page_cut_type(request):
    admin_name=request.session['admin_name']
    cut_types=Cut_type.objects.all()
    if request.method=='POST':
        cut_type=request.POST['cut_type']
        cut_image=request.FILES['cut_image']
        Cut_type.objects.create(cut_type=cut_type,cut_image=cut_image)
    return render(request, 'cut_type.html',{'cut_types':cut_types,'admin_name':admin_name})

@admin_login_required
def admin_page_store_owner_list(request):
    admin_name=request.session['admin_name']
    store_owners_list=Store_owner_login.objects.annotate(store_count=Count('store'))
    return render(request,'store_owner_list.html',{'store_owners_list':store_owners_list,'admin_name':admin_name})

@admin_login_required
def store_owner_action(request,id):
    store_owner_action=get_object_or_404(Store_owner_login,id=id)
    store_owner_action.owner_is_suspicious = not store_owner_action.owner_is_suspicious 
    store_owner_action.save()
    return redirect('admin_page_store_owner_list')

@admin_login_required
def admin_page_stores_list(request):
    admin_name=request.session['admin_name']
    stores_list=Store.objects.all()
    return render(request,'stores_list.html',{'stores_list':stores_list,'admin_name':admin_name})

@admin_login_required
def store_action(request,id):
    store_action = get_object_or_404(Store, id=id)    
    store_action.store_is_suspicious = not store_action.store_is_suspicious
    store_action.save()
    return redirect('admin_page_stores_list')

@store_owner_login_required
def is_todaycatch(request,id):
    is_todaycatch=get_object_or_404(Store_products,id=id)
    is_todaycatch.is_todays_catch= not is_todaycatch.is_todays_catch
    is_todaycatch.save()
    return redirect(reverse('storeowner_managestocks', args=[is_todaycatch.store_name.id]))

@store_owner_login_required
def is_available(request,id):
    is_available=get_object_or_404(Store_products,id=id)
    is_available.is_available=not is_available.is_available
    is_available.save()
    return redirect(reverse('storeowner_managestocks',args=[is_available.store_name.id]))

@admin_login_required
def admin_page_store_products(request):
    admin_name=request.session['admin_name']
    store_products = Store_products.objects.prefetch_related('store_product_cutprice_set').all()
    # store_count=Store_product_cutPrice.objects.annotate(count=Count('cut_type'))
    return render(request,'store_products_list.html',{'store_products':store_products,'admin_name':admin_name})

@store_owner_login_required
def storeowner_managestore(request):
    store_owner=request.session['store_owner_sess_id']
    store_owner_name=request.session['store_owner_sess_name']
    stores_list=Store.objects.filter(store_ownwer_name=store_owner)
    return render(request,'storeowner_managestore.html',{'stores_list':stores_list,'store_owner':store_owner,'store_owner_name':store_owner_name})

@store_owner_login_required
def delete_my_store(request,id):
    Store.objects.filter(id=id).delete()
    return redirect('storeowner_managestore')


@store_owner_login_required
def storeowner_manageproducts(request,id):
    store_owner=request.session['store_owner_sess_id']
    store_owner_name=request.session['store_owner_sess_name']
    stores_list=Store.objects.filter(id=id)
    categories=Category.objects.all()
    cut_type=Cut_type.objects.all()
    added_store_products=Store_products.objects.filter(store_name_id=id).prefetch_related('store_product_cutprice_set')
    if request.method=='POST':
        store_name=Store.objects.get(id=request.POST['store_name'])
        product_name=request.POST['product_name']
        category=Category.objects.get(id=request.POST['category'])
        mrp=request.POST['mrp']
        product_image=request.FILES['product_image']
        product_available_quantity=request.POST['product_available_quantity']
        
        store_products=Store_products(store_name=store_name,product_name=product_name,category=category,mrp=mrp,product_image=product_image,product_available_quantity=product_available_quantity)
        store_products.save()

        cut_type_ids=request.POST.getlist('cut_type')  
        cut_type_prices=request.POST.getlist('cut_type_price')  
        is_default_prices=request.POST.getlist('is_default_price') 

        
        for i in range(len(cut_type_ids)):
            if cut_type_ids[i]:  # Ensure cut type is selected
                cut_type_instance = Cut_type.objects.get(id=cut_type_ids[i])
                product_price = cut_type_prices[i]
                is_default = True if is_default_prices[i] == '1'   else False
            print(store_name,mrp,product_image,cut_type_instance,is_default)
                
            store_product_cutprice=Store_product_cutPrice(product_name=store_products,cut_type=cut_type_instance,product_price=product_price,is_default_cutprice=is_default) 
            store_product_cutprice.save()

    context={'stores_list':stores_list,'store_owner_name':store_owner_name,'categories':categories,'cut_type':cut_type,'added_store_products':added_store_products,'store_id': id}
    return render(request,'storeowner_manageproducts.html',context)

@store_owner_login_required
def display_stores_4owner(request):
    store_owner_name=request.session.get('store_owner_sess_name')
    store_owner_id=request.session.get('store_owner_sess_id')
    owners_store=Store.objects.filter(store_ownwer_name=store_owner_id)
    context={'store_owner_name':store_owner_name,'owners_store':owners_store}
    return render(request, 'display_stores4owner.html',context)

@store_owner_login_required
def storeowner_managestocks(request,id):
    store_owner=request.session['store_owner_sess_id']
    store_owner_name=request.session['store_owner_sess_name']
    stores_list=Store.objects.filter(id=id)
    categories=Category.objects.all()
    cut_type=Cut_type.objects.all()
    added_store_products=Store_products.objects.filter(store_name_id=id).prefetch_related('store_product_cutprice_set')
    
    context={'stores_list':stores_list,'store_owner_name':store_owner_name,'categories':categories,'cut_type':cut_type,'added_store_products':added_store_products,'store_id': id}
    return render(request,'storeowner_managestocks.html',context)

@store_owner_login_required
def delete_stock(request,id):
    stores=Store_products.objects.get(id=id)
    stores_id=stores.store_name_id
    stores.delete()
    # return redirect(reverse('storeowner_managestocks',args=[stores_id]))
    return redirect('storeowner_managestocks',id=stores_id)

@admin_login_required
def delete_prod_type(request,id):
    Product_Type.objects.get(id=id).delete()
    return redirect('admin_page_type_of_product')

@admin_login_required
def delete_cat_type(request,id):
    Category.objects.get(id=id).delete()
    return redirect('admin_page_category')

@admin_login_required
def delete_cut_type(request,id):
    Cut_type.objects.get(id=id).delete()
    return redirect('admin_page_cut_type')