from django.http import Httpresponse



def saludar (request):
    return HttpResponse ("hola mundo!") 

def segunda_vista (request):
    return HttpResponse ("ya entendi parece ser simple")

    
