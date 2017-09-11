from django.shortcuts import render
from StudentProfiler.models import Faculty,Students
from django.http import HttpResponseRedirect
# Create your views here.
from fusioncharts import FusionCharts

def index(req):
    if req.method=="POST":
        username=req.POST.get('user')
        password=req.POST.get('pass')
        user=Faculty.objects.filter(username=username)
        if user.count()==1:
            if user[0].check_password(password):
               req.session['user']=username
               return HttpResponseRedirect("/selection/")
            else:
               return render(req,"login.html",{"error":"invalid Username or Password"})
        else:
            return render(req,"login.html",{"error":"invalid Username or Password"})
    return render(req,"login.html")

def newlogin(req):
    if req.method=='POST':
        #use create_user for hashing or else pass will be stored in plain text
        user=Faculty.objects.create_user(username=req.POST.get('username'),password=req.POST.get('password'),email=req.POST.get('email'),first_name=req.POST.get('fname'),last_name=req.POST.get('lname'))
        user.save()
        return render(req,"newlogin.html",{'success':'Registration Successful!'})
    return render(req,"newlogin.html")

def selection(req):
    try:
        if req.session['user']:
           return render(req,"selection.html",{"user":req.session['user']})
    except:
           #print("except")
           return HttpResponseRedirect("/")

def marks(req):
  try:
    if req.session['user']:  
     if req.method=='GET':
        div=req.GET.get('class')
        year=req.GET.get('batch-year')
        subject=req.GET.get('subject')
        uids=list()
        for i in range(60):
            if i<=8:
                uids.append(year[2:]+"-"+"CMPN"+div+"0"+str(i+1)+"-"+str(int(year)+4))
            else:
                uids.append(year[2:]+"-"+"CMPN"+div+str(i+1)+"-"+str(int(year)+4))
        return render(req,"marks.html",{"subject":subject,"uids":uids,"user":req.session['user']})
  except:
      return HttpResponseRedirect("/")


def chart(request):
    if request.method=="GET":
        subject=request.GET.get('subject')
        year=request.GET.get('batch-year')
        div=request.GET.get('class')
        year=year[2:]
        uid=year+"-"+"CMPN"+div
        dataSource={}
        graph={}
        dataSource['chart']={"caption":"Performance Of Students","subCaption":"By CMPN B","xAxisName":"Category","yAxisName":"Percentage","numberPrefix":"","theme":"zune"}
        count=Students.objects.all().count()
        l=Students.objects.filter(category="low",UID__contains=uid,subject=subject).count()
        graph['low']="{0:.2f}".format(l/(count*1.0)*100)
        m=Students.objects.filter(category="medium",UID__contains=uid,subject=subject).count()
        graph['medium']="{0:.2f}".format(m/(count*1.0)*100)
        h=Students.objects.filter(category="high",UID__contains=uid,subject=subject).count()
        graph['high']="{0:.2f}".format(h/(count*1.0)*100)


        dataSource['data'] = []
        # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
        for key in graph:
            data = {}
            data['label'] = key #label for bar i.e low.medium,high
            data['value'] = graph[key]  #percentage value
            dataSource['data'].append(data)
        column2D = FusionCharts("column2D", "ex1" , "800", "650", "chart-1", "json", dataSource)
        return render(request, 'graph.html', {'output': column2D.render()})


def logout(req):
    del req.session['user']
    return HttpResponseRedirect("/")
