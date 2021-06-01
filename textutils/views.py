from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def Analyze(request):

    djText = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    removenum = request.GET.get('removenum', 'off')
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djText:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'Analyze.html', params)

    elif fullcaps == 'on':
        analyzed = ""
        for char in djText:
            analyzed = analyzed+char.upper()

        parmas = {'purpose': 'Caps Lock', 'analyzed_text': analyzed}
        return render(request, "Analyze.html", parmas)

    elif newlineremover == 'on':
        analyzed = ""
        for char in djText:
            if char != '\n':
                analyzed = analyzed+char

        parmas = {'purpose': 'New Lines', 'analyzed_text': analyzed}
        return render(request, "Analyze.html", parmas)
    elif extraspaceremover == 'on':
        analyzed = ""
        for index,char in enumerate(djText):
            if not(djText[index]==" " and djText[index+1]==" "):
                analyzed = analyzed+char

        parmas = {'purpose': 'Remove Extra Spaces', 'analyzed_text': analyzed}
        return render(request, "Analyze.html", parmas)
    elif removenum == 'on':
        analyzed = ""
        num='''12345678910[]'''
        for char in djText:
            if char not in num:
                analyzed=analyzed+char
            

        parmas = {'purpose': 'Remove Nums', 'analyzed_text': analyzed}
        return render(request, "Analyze.html", parmas)
    elif djText=='':
        params={'purpose':'error','analyzed_text': 'Please Write Some Text to See Magic'}
        return render(request, "Analyze.html", params)
    else:
        return HttpResponse("Error")
