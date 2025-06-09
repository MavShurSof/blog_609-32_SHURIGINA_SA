from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    data = {"header":"Homepage", "message":"Welcome to my website!"}
    return render(request, 'articles/article_list.html', context=data)


def about(request):
    header = "About Us"
    staff = ['Jhon Nichols', 'Jhon Rogers', 'Timothy Smith']
    director = {"name": "David Lee", "img": '/director.png'}
    address = ('20 W 34th St.', 'New York', 'NY 10001', 'USA')
    data = {"header": header, "staff": staff, "director": director, "address": address}
    return render(request, 'about.html', data)