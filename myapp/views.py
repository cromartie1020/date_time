from django.shortcuts import render
from .forms import Date_time_form
def date_time(request):
    form =Date_time_form()
    context={
        "form":form  
    }
    return render(request, 'myapp/form.html', context)


#class JavaScriptCatalog():
#    pass