# from django.urls import path
# from todolist import views
# urlpatterns = [
#     path('',views.home,name="home"),
#     path('readdata/',views.Read_Data,name="readdata"),
#     path('readdata/<int:id>/',views.Request_Data,name="requestdata")
# ]

from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.home, name="home"),
    path('readdata/', views.Read_Data, name="readdata"),
    path('requestdata/<int:task_id>/', views.Request_Data, name="requestdata"),
    path('deletedata/<int:task_id>/',views.Delete_Data,name='deletedata'),
    path('edit/<int:task_id>/',views.Updata_Data,name="update_data")
]