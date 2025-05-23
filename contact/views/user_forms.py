from django.shortcuts import render
from contact.forms import RegisterForm

from contact.models import Contact

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )