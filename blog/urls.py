from django.urls import path
from . import views


urlpatterns =[

     path('',views.Welcome,name="welcome"),

     path('post/',views.Posts,name="posts"),

     path('Specifi_Post/<str:title>/',views.Specific_Post,name="Specifi_Post"),
     path('Specific_category/<str:category>/',views.Specific_Category,name="Specific_category"),
     path('Specific_Author/<str:author>/',views.Specific_Author,name="Specific_Author"),
     path('create/',views.Create,name="create"),
     path('update/',views.Update,name="update"),
     path('delete/',views.Delete,name="delete"),
     path('add_comment/<int:id>/',views.add_comment,name="add_comment"),
     path('update_comment/<int:id>/',views.update_comment,name="update_comment"),
     path('delete_comment/<int:id>/',views.delete_comment,name="delete_comment"),

]