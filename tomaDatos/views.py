from django.shortcuts import render
from django.http import HttpResponse
from tomaDatos.forms import formSintomas
from tomaDatos.models import Sintomas

# Create your views here.

def tomaDatos(request):
    consejos = [  "Informa a tu médico de familia tu tempuratura" , 
                "Estás en estado febril, informa a tu médico de familia" , 
                "Evita tomar cosas frías" , 
                "Toma agua al clima y recuerda taparte al toser" , 
                "Trata de no realizar actividades que te agiten" , 
                "Llama a emergencia" , 
                "Quédate en casa, te cuidas y cuidas a los demás" 
                ]
    consejos2 = []
    if request.method == "POST":
        formulario = formSintomas(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            
            registro = Sintomas.objects.create(
                temperatura = info['temperatura'],
                dolorGarganta = info['dolorGarganta'],
                tos = info['tos'],
                senGusto = info['senGusto'],
                senOlfato = info['senOlfato'],
                respiracion = info['respiracion'],
            )
            
            if (info['temperatura'] <= 34.5) and (info['temperatura'] < 38):
                consejos2.append(consejos[0])
            if info['temperatura'] >= 38:
                consejos2.append(consejos[1])
            if info['dolorGarganta'] >= 3:
                consejos2.append(consejos[2])
            if info['tos'] >= 3:
                consejos2.append(consejos[3])
            if (info['respiracion']>=2) and (info['respiracion']<4):
                consejos2.append(consejos[4])
            if info['respiracion']>=4:
                consejos2.append(consejos[5])
            
            contexto = {
                "consejos":consejos2
            }
                
            
            return render(request,"gracias.html",contexto)
        
    else: 
        formulario = formSintomas()
        
    contexto = {
        "formulario":formulario
    }
    
    return render(request,"formulario.html",contexto)