from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Services, Record
from .forms import RecordEventForm


def show_available_record_list_view(request): #Веб-сервис, отображающий услуги
    return render(request, "record/record_list.html", {
        "service_cards": enumerate(Services.objects.all()),
    })
  

@login_required
def show_record_detail_view(request, pk):  #Веб-сервис, записывающий текущего пользователя на выбранную запись
    
    selected_record = get_object_or_404(Services, pk=pk)

    if request.method == 'POST':
        form = RecordEventForm(request.POST)

        if form.is_valid():
            event = form.save(commit=False)
            event.service = selected_record
            event.patient = request.user
            event.save()
            return redirect("my_record")

    else:
        form = RecordEventForm()
        
    context = {
        "form": form,
        "service": selected_record
    }
    
    return render(request, "record/record_detail.html", context)

  
@login_required
def show_user_record_list_view(request):  #Веб-сервис, отображающий записи текущего пользователя
  
    context = {
        "confirmed_record": Record.objects.filter(
            patient=request.user, approved=True
        ).select_related("service"),
        "non_confirmed_record": Record.objects.filter(
            patient=request.user, approved=False
        ).select_related("service"),
    }

    return render(request, "record/my_record.html", context)
