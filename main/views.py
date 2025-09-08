from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406437376',
        'name': 'Chevinka Queen Cilia Sidabutar',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)