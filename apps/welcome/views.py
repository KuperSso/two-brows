from django.shortcuts import render, get_list_or_404
from .models import Diplomas, Welcome

def show_welcome_page_view(request):

    return render(request, "welcome/home.html",
                  {"home_info": get_list_or_404(Welcome,)[0],})

def show_my_contact_view(request):  
    return render(request,'welcome/contacts.html')

def diplomas(request):
    return render(request, 'welcome/diplomas.html',
                  {"diplomas": Diplomas.objects.all(), })



def error_404(request, exception):
    return render(request, "errors/404.html", status=404)


def error_500(request, *args, **kwargs):
    return render(request, "errors/500.html", status=500)