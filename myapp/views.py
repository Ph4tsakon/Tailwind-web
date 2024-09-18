from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def p1(request):
	return render(request, 'p1.html')

def p2(request):
	return render(request, 'p2.html')

def p3(request):
	return render(request, 'p3.html')

def myself(request):
	return render(request, 'myself.html')