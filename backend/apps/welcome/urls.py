from django.urls import path
from .views import (show_welcome_page_view,
                    show_my_contact_view, diplomas)

urlpatterns = [
    path("", show_welcome_page_view, name="home"),
    path("contacts/", show_my_contact_view, name="contacts"),
    path("diplomas/", diplomas, name="diplomas"),

]
