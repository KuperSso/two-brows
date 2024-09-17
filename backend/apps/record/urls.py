from django.urls import path
from .views import (show_available_record_list_view,
                    show_record_detail_view,
                    show_user_record_list_view)
                    

urlpatterns = [
    path("", show_available_record_list_view, name="record_list"),
    path("<uuid:pk>/", show_record_detail_view, name="record_detail"),
    path("your_record/", show_user_record_list_view, name="my_record"),
]