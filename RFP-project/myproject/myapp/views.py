from django.shortcuts import render
import pickle
import os

# Create your views here.
def index(req):
    res=''
    if req.method=='POST':
        precip=float(req.POST['precip'])
        maxt=float(req.POST['maxt'])
        mint=float(req.POST['mint'])
        wind=float(req.POST['wind'])
        path=os.path.dirname(__file__)
        model=pickle.load(open(os.path.join(path,'rfp.pkl'),'rb'))
        X=[precip,maxt,mint,wind]
        res=str(model.predict([X])[0])
    return render(req,"index.html",{'res':res})