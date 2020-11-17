from django.shortcuts import render
from django.http import HttpResponse
from tomaDatos.forms import formSintomas
from tomaDatos.models import Sintomas
import pandas as pd

# Create your views here.

def tomaDatos(request):
    consejos = [  "Informa a tu médico de familia tu temperatura" , 
                "Estás en estado febril, toma algún antipilectico, toma una ducha e informa a tu médico de familia" , 
                "Evita tomar cosas frías" , 
                "Toma agua al clima y recuerda taparte al toser" , 
                "Trata de no realizar actividades que te agiten" , 
                "Llama a emergencias, tu respiracion esta complicandose" , 
                "Quédate en casa, te cuidas y cuidas a los demás" ,
                "Haste una revisión de tu garganta y ante cualquier cosa inusual informa a tu médico de familia",
                "Toma antigripales y mucho liquido",
                "Llamar a la eps  y pide indicaciones",
                "Llama a emergencias, algo malo puede estar pasando",
                "Tu temperatura esta mas baja de lo normal",
                "Tomar hidratante con suero oral y liquidos",
                "Usa solución salida para descongestionar tu nariz y informa a tu médico",
                "Usa analgésico como acetaminofen cada 6 horas",
                "Usa analgésico como acetaminofen cada 6 horas y reporta a tu eps o médico",
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
                dolorPecho = info['dolorPecho'],
            )
            
            if (info['temperatura'] >= 34.5) and (info['temperatura'] < 38):
                consejos2.append(consejos[0])
            if info['temperatura'] >= 38:
                consejos2.append(consejos[1])
            if info['dolorGarganta'] == 3:
                consejos2.append(consejos[2])
            if info['tos'] >= 3:
                consejos2.append(consejos[3])
            if (info['respiracion']>=2) and (info['respiracion']<4):
                consejos2.append(consejos[4])
            if info['respiracion']>=4:
                consejos2.append(consejos[5])
            if info['dolorGarganta'] >= 4:
                consejos2.append(consejos[7])
            if (info['senGusto'] == 'No') or (info['senOlfato'] == 'No'):
                consejos2.append(consejos[8])
            if (info['dolorPecho'] < 4) and (info['dolorPecho'] >= 2):
                consejos2.append(consejos[9])
            if info['dolorPecho'] >= 4:
                consejos2.append(consejos[10])
            if info['temperatura'] < 32:
                consejos2.append(consejos[11])
            if info['diarrea'] == 'Si':
                consejos2.append(consejos[12])
            if info['secrecion'] == 'Si':
                consejos2.append(consejos[13])
            if (info['dolorEspalda'] == 'Si') or (info['dolorCabeza'] == 'Si') or ((info['malestar'] > 1) and (info['malestar']<=3)):
                consejos2.append(consejos[14])
            if info['malestar'] > 3:
                consejos2.append(consejos[15])
            if info['resultado'] != '':
                Sintomas2 = [
                    info['temperatura'],
                    info['dolorGarganta'],
                    info['tos'],
                    info['senGusto'],
                    info['senOlfato'],
                    info['respiracion'],
                    info['dolorPecho'],
                    info['diarrea'],
                    info['dolorCabeza'],
                    info['dolorEspalda'],
                    info['malestar'],
                    info['secrecion'],
                    info['resultado']
                ]
                guardarCSV(Sintomas2)
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


def guardarCSV(Sintomas = []):
    print(Sintomas)
    data = {'temperatura': Sintomas[0],
            'dolorGarganta': Sintomas[1],
            'tos':Sintomas[2],
            'senGusto':Sintomas[3],
            'senOlfato':Sintomas[4],
            'respiracion':Sintomas[5],
            'dolorPecho':Sintomas[6],
            'diarrea':Sintomas[7],
            'dolorCabeza':Sintomas[8],
            'dolorEspalda':Sintomas[9],
            'malestar':Sintomas[10],
            'secrecion':Sintomas[11],
            'resultado':Sintomas[12]
            }

    #df = pd.DataFrame(data, columns = ['temperatura', 'dolorGarganta', 'tos', 'senGusto', 'senOlfato','respiracion','dolorPecho','diarrea','dolorCabeza','dolorEspalda','malestar','secrecion','resultado'],index=[0])
    #df.to_csv('sintomas.csv')
    df2 = pd.read_csv('sintomas.csv', index_col=0)
    n = len(df2.index)
    df2.loc[n] = Sintomas
    #df2 = df2.append(Sintomas)
    #print(df2)
    df2.to_csv('sintomas.csv')
    
