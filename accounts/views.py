from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Seja bem-vindo ao app de contas!")

def login(request):
    return HttpResponse("Pagina de Login do app de contas")

def register(request):
    return HttpResponse("Pagina de Cadastro do app de contas")