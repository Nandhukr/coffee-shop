from django.shortcuts import render
from .models import MenuItem
from .models import Event
from django.http import JsonResponse
from nan.forms import ContactForm
from django.views.generic import View,FormView,CreateView,TemplateView,ListView,DetailView



class IndexView(ListView):
    template_name="index.html"
    context_object_name="Menu"
    model=MenuItem

def menu(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})



def events(request):
    upcoming_events = Event.objects.filter(date__gte=datetime.date.today())
    return render(request, 'events.html', {'upcoming_events': upcoming_events})




def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            return JsonResponse({'message': 'Thank you for your message! We will get back to you soon.'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return render(request, 'contact.html')
