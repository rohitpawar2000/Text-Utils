from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    rohit={'name':'rohit','surname':'pawar'}
    return render(request,'index.html',rohit)

def analyze(request):
    text=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','default')
    charcount=request.POST.get('charcount','default')
    newline=request.POST.get('newline','default')
    uppercase=request.POST.get('uppercase','default')
    lowercase=request.POST.get('lowercase','default')

    if(removepunc=="on"):
        punc='''/?<>,;:'"!@$%&*#'''
        analyze=""


        for char in text:
            if char not in punc:
                 analyze=analyze+char

        dict={'purpose':'Remove Punctuations','sentence':'your sentence after removing punctuations is :','text':analyze}

        # return render(request,'analyze.html',dict)
        text=analyze

    if(charcount=="on"):
        count=0
        analyze=""

        for char in text:
            if char==" " or char == "  ":
                pass
            else:
                count=count+1

        dict = {'purpose': 'Count Characters', 'sentence': 'your character count is :',
            'text': count}

        analyze=str(count)
        text=analyze
        # return render(request, 'analyze.html', dict)

    if(newline=="on"):

        analyze=""
        for char in text:
            if char != "\n" and char != "\r":
                analyze=analyze+char
        dict = {'purpose': 'Your ', 'sentence': 'your sentece after removing new line is :',
            'text': analyze}

        text=analyze
        # return render(request, 'analyze.html', dict)

    if(uppercase=="on"):
        djtext=upper=text.upper()


        dict = {'purpose': 'uppercase sentence', 'sentence': 'your sentece after uppercasing each character is :',
                'text': djtext}

        text=djtext
        # return render(request, 'analyze.html', dict)


    if (lowercase == "on"):
        djtext = text.lower()

        dict = {'purpose': 'uppercase sentence', 'sentence': 'your sentece after uppercasing each character is :',
                'text': djtext}
        text=djtext

        # return render(request, 'analyze.html', dict)

    if (removepunc != "on" and newline!="on" and uppercase!="on" and lowercase != "on"):
        return HttpResponse("please select given option ")


    return render(request,'analyze.html',dict)






def contact(request):
    return HttpResponse("this is contact page")