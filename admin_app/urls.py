from django.urls import path
from admin_app import views

urlpatterns = [
                # store owner urls
                path('index',views.index,name='index_page'),
                path('store-owner-register',views.store_owner_register,name='store_owner_register'),
                path('store-register',views.store_register,name='store_register'),
                path('',views.store_owner_login,name='store_own_login'),
                path('store-owner-manage-store',views.storeowner_managestore,name='storeowner_managestore'),
                path('store-owner-manage-products/<int:id>',views.storeowner_manageproducts,name='storeowner_manageproducts'),
                path('store-owner-manage-stocks/<int:id>',views.storeowner_managestocks,name='storeowner_managestocks'),
                path('display-stores',views.display_stores_4owner,name='display_stores_4owner'),
                path('store-owner-logout',views.store_owner_logout,name='store_owner_logout'),
                path('noti',views.noti,name='noti'),
                path('store_action/<int:id>',views.store_action,name='store_action'),
                path('is_todaycatch/<int:id>',views.is_todaycatch,name='is_todaycatch'),
                path('is_available/<int:id>',views.is_available,name='is_available'),
                path('delete_my_store/<int:id>',views.delete_my_store,name='delete_my_store'),
                path('delete_stock/<int:id>',views.delete_stock,name='delete_stock'),
                path('store_owner_action/<int:id>',views.store_owner_action,name='store_owner_action'),

                #admin urls
                path('adminpage/admin-index',views.admin_index,name='admin_index'),
                path('adminpage/admin_register',views.admin_page_register,name='admin_page_register'),
                path('adminpage/admin_login',views.admin_page_login,name='admin_page_login'),
                path('admin-page-logout',views.admin_page_logout,name='admin_page_logout'),
                path('adminpage/category',views.admin_page_category,name='admin_page_category'),
                path('adminpage/product-type',views.admin_page_type_of_product,name='admin_page_type_of_product'),
                path('adminpage/cut-type',views.admin_page_cut_type,name='admin_page_cut_type'),
                path('adminpage/store-owner-list',views.admin_page_store_owner_list,name='admin_page_store_owner_list'),
                path('adminpage/store-products-list',views.admin_page_store_products,name='admin_page_store_products'),
                path('adminpage/stores-list',views.admin_page_stores_list,name='admin_page_stores_list'),
                path('adminpage/product-type/<int:id>',views.delete_prod_type,name='delete_prod_type'),
                path('adminpage/cate/<int:id>',views.delete_cat_type,name='delete_cat_type'),
                path('adminpage/ca/<int:id>',views.delete_cat_type,name='delete_cat_type'),
]