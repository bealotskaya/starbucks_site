from django.shortcuts import render


def index(request):
    data= {
        'title': 'Welcome to Starbucks',
        'values': ['Coffe', 'Cocktails', 'Buns']
    }
    return render(request,'main/index.html', data)

def about(request):
    data_a = {
        'title': 'About'
    }
    return render(request,'main/about.html', data_a)

