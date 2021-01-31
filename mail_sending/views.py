from django.http import JsonResponse
from django.shortcuts import render
from .forms import ContactModelForm


def contact(request):

    form = ContactModelForm()

    if request.is_ajax():
        form = ContactModelForm(request.POST)
        print(request.POST)
        if form.is_valid():

            form.save()
            return JsonResponse({
                'message': 'success'
            })

    return render(request, 'index.html', {'form': form})
