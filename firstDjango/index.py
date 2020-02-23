from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    params={'name':'Zaid'}
    return render(request,'index.html',params)

def redirect(request):
    textValue= request.GET.get('text','default')
    newTextValue=textValue
    checkValue = request.GET.get('check','off')
    capital = request.GET.get('capital','off')
    punctuation ='''~!@#$%^&*()-_{}[]\|:";'<>?,./'''
    if checkValue=='on':
        newTextValue=''
        for i in textValue:
            if i not in punctuation:
                newTextValue = newTextValue+i
    if capital =='on':
        newTextValue = newTextValue.upper()
    params={'value':newTextValue}
    return render(request,'redirect.html',params)

def bootstrap(request):
    return render(request,'bootstrap.html')