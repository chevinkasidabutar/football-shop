from django.shortcuts import render

def show_main(request):
    context = {
        'store' : 'BolaBale store',
        'name': 'Chevinka Queen Cilia Sidabutar',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)