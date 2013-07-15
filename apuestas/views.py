from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

def index(request):
	context = Context({

		})
	return render(request, 'apuestas/index.html', context)

def usuario(request, usuario_id):
	return HttpResponse('Usuario_id' + usuario_id)	