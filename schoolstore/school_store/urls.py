from . import views
from django.urls import path
app_name='school_store'
urlpatterns = [

    path('',views.demo,name='demo'),
    path('register/', views.register, name='register'),
    path('login/',views.login,name='login'),
    path('new_page/',views.new_page,name='new_page'),
    # path('form/',views.form,name='form'),
    path('order/', views.order_view, name='order'),
    path('logout/', views.logout,name='logout'),

    path('form/add/', views.form_create_view, name='form_add'),
    path('<int:pk>/', views.form_update_view, name='form_change'),

    path('ajax/load_courses', views.load_courses, name='ajax_load_courses'),  # AJAX

]