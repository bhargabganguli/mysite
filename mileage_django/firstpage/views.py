from django.shortcuts import render
#from django.shortcuts import render_to_response
from django.http import HttpResponse
#we will import pandas
import pandas as pd
import numpy as np



def index(request):
    
    return render(request, 'index.html', {'imp':False})


#this is user defined function to load the csv data into a  dataframe(name=csv)

#from django.views.decorators.cache import cache_control
#@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def result(request):
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_absolute_error as mae
    if request.method == "POST":
        global file
        file = request.FILES["myFile"]
        csv=pd.read_csv(file)
        print(csv)
        size=csv.shape
        global x
        x=csv.iloc[:,:]
        global t
        t=x.dtypes
        print(t)
        cont=x.select_dtypes(include=[np.number])
        disc=x.select_dtypes(exclude=[np.number])
        context={'rows':size[0],'columns':size[1], 'col_name':cont.columns,'data':csv}
        return render(request, "mmm.html",context)
    else:   
        return render(request, "index.html")

def saturation(request):
    return render(request, 'mmm.html', {'x':"uri"})

def imp_features(request):
    return render(request, 'mmm.html',{'x':"uri"})
    
def area_plot(request):
    return render(request, 'mmm.html',{'x':uri,'y':"uri2"})    
       
##this is user defined function to go to the upload html page where is the upload button of csv file
def upload(request):
    return render(request, "upload.html")


def viewdb(request):
    return render(request, 'index.html')

def predictMPG(request):
    context={'scoreval':"scoreval",'summary':"reg summary"}
    return render(request, 'result.html',context)

def boxplot(request):
  import matplotlib.pyplot as plt
  from io import StringIO
  from io import BytesIO
  import base64
  import urllib
  c1=request.POST.get('column1')
  c2=request.POST.get('column2')
  #d=request.POST.get('dataset')
  #csv=pd.read_csv(file)
  #d=request.session.get('data')
  #plt.hist(csv.c1,csv.c2)
  fig=plt.figure()
  plt.boxplot(x[c1])
  plt.xlabel(c1)
  plt.ylabel(c1)
  
  imgdata=StringIO()
  fig.savefig(imgdata, format='svg')
  imgdata.seek(0)
  
  uri = imgdata.getvalue()
  #buffer.close()
  
  
  context={'something2':True , 'graph2':uri}
  return render(request, 'result.html',context)


def scatterplot(request):
    import matplotlib.pyplot as plt
    from io import StringIO
    from io import BytesIO
    import base64
    import urllib
    c1=request.POST.get('column1')
    c2=request.POST.get('column2')
    fig=plt.figure()
    plt.scatter(x[c1],x[c2])
    plt.xlabel(c1)
    plt.ylabel(c2)
    imgdata=StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    
    
    
    uri = imgdata.getvalue()
    #buffer.close()
    
    context={'something2':True , 'graph2':uri}
    return render(request, 'result.html',context)

def histogram(request):
    import matplotlib.pyplot as plt
    from io import StringIO
    from io import BytesIO
    import base64
    import urllib
    c1=request.POST.get('column1')
    
    fig=plt.figure()
    plt.hist(x[c1])
    plt.xlabel(c1)
    plt.ylabel("frequency")
    imgdata=StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    
    
    
    uri = imgdata.getvalue()
    #buffer.close()
    
    context={'something2':True , 'graph2':uri}
    return render(request, 'result.html',context)


def carry(request):
    return render(request, 'mmm.html',{'x':uri,'y':uri2,'z':uri3,'carry':True})  

def optimise(request):

    return render(request, 'result.html', {'scoreval':x_data.shape, 'summary':data2})
