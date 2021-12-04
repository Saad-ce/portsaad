from django.shortcuts import render,HttpResponse
import joblib
# Create your views here.
def index(request):
    return render(request,"index.html")

def contact(request):
    return render(request,"contact.html")

def portfoliodetails(request):
    return render(request,"portfolio-details.html")

def blogsingle(request):
    return render(request,"blog-single.html")
def heartpredictor(request):
    return render(request,"heartpredictor.html")
def resultheart(request):
    cls = joblib.load("finals.sav")
    lis = []
    lis2 = []

    lis2.append(request.GET['Name'])

    lis.append(request.GET['age'])
    lis.append(request.GET['sex'])

    lis.append(request.GET['cp'])

    lis.append(request.GET['trestbps'])
    lis.append(request.GET['chol'])
    lis.append(request.GET['fbs'])

    lis.append(request.GET['restecg'])
    lis.append(request.GET['thalach'])
    lis.append(request.GET['exang'])
    lis.append(request.GET['oldpeak'])
    lis.append(request.GET['slope'])
    lis.append(request.GET['ca'])
    lis.append(request.GET['thal'])

    print(lis)
    print(lis2)
    ans = cls.predict([lis])
    str2 = " "
    ans3 = str2.join(lis2)
    return render(request, "result-heart.html", {"ans": ans, "ans3": ans3})
