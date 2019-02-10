from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):

    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()
    i=0
    new=""
    for word in wordlist:
        text=word[i]
        new=new+text.upper()
        text==""
    



    wordlength=len(wordlist)
    i = 0
    for word in wordlist:
        for char in word:
            i+=1

    avg = i/wordlength

    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'avgword':avg,'first':new})

def about(request):
   
    return render(request,'about.html')


    
    