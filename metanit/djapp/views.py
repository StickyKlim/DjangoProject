import numpy as np
import skfuzzy as fuzz
import plotly.graph_objects as go
from plotly.offline import plot
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from plotly.graph_objs import Scatter
from django.core.mail import send_mail, BadHeaderError
import plotly.graph_objects as go
import io
from django.shortcuts import redirect, render
from .forms import FuzzyForm
    # FuzzyData
from django.views.generic import TemplateView
from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter


def index(request):
    return HttpResponse("Главная страница")

def myform(request):
   if request.method == "POST":
       #temp1
       global temp1_arr, temp2_arr,temp_lo,temp_me,temp_hi,temp2_lo,temp2_me,temp2_hi,range_arr,range_lo,range_me,range_hi,all_arr,all_lo,all_me,all_hi
       temp_low_a = request.POST.get("temp_low_a")
       temp_low_b = request.POST.get("temp_low_b")
       temp_low_c = request.POST.get("temp_low_c")
       temp_mid_a = request.POST.get("temp_mid_a")
       temp_mid_b = request.POST.get("temp_mid_b")
       temp_mid_c = request.POST.get("temp_mid_c")
       temp_hig_a = request.POST.get("temp_hig_a")
       temp_hig_b = request.POST.get("temp_hig_b")
       temp_hig_c = request.POST.get("temp_hig_c")
       spisok1 = [int(temp_low_a), int(temp_low_b), int(temp_low_c)]
       spisok2 = [int(temp_mid_a), int(temp_mid_b), int(temp_mid_c)]
       spisok3 = [int(temp_hig_a), int(temp_hig_b), int(temp_hig_c)]

       temp1_arr = np.arange(0,100,1)

       temp_lo = fuzz.trimf(temp1_arr, spisok1)
       temp_me = fuzz.trimf(temp1_arr, spisok2)
       temp_hi = fuzz.trimf(temp1_arr, spisok3)
       #temp2

       temp2_low_a = request.POST.get("temp2_low_a")
       temp2_low_b = request.POST.get("temp2_low_b")
       temp2_low_c = request.POST.get("temp2_low_c")
       temp2_mid_a = request.POST.get("temp2_mid_a")
       temp2_mid_b = request.POST.get("temp2_mid_b")
       temp2_mid_c = request.POST.get("temp2_mid_c")
       temp2_hig_a = request.POST.get("temp2_hig_a")
       temp2_hig_b = request.POST.get("temp2_hig_b")
       temp2_hig_c = request.POST.get("temp2_hig_c")
       spisok4 = [int(temp2_low_a), int(temp2_low_b), int(temp2_low_c)]
       spisok5 = [int(temp2_mid_a), int(temp2_mid_b), int(temp2_mid_c)]
       spisok6 = [int(temp2_hig_a), int(temp2_hig_b), int(temp2_hig_c)]

       temp2_arr = np.arange(100,300,1)

       temp2_lo = fuzz.trimf(temp2_arr, spisok4)
       temp2_me = fuzz.trimf(temp2_arr, spisok5)
       temp2_hi = fuzz.trimf(temp2_arr, spisok6)

       #range
       range_low_a = request.POST.get("range_low_a")
       range_low_b = request.POST.get("range_low_b")
       range_low_c = request.POST.get("range_low_c")
       range_mid_a = request.POST.get("range_mid_a")
       range_mid_b = request.POST.get("range_mid_b")
       range_mid_c = request.POST.get("range_mid_c")
       range_hig_a = request.POST.get("range_hig_a")
       range_hig_b = request.POST.get("range_hig_b")
       range_hig_c = request.POST.get("range_hig_c")
       spisok7 = [int(range_low_a), int(range_low_b), int(range_low_c)]
       spisok8 = [int(range_mid_a), int(range_mid_b), int(range_mid_c)]
       spisok9 = [int(range_hig_a), int(range_hig_b), int(range_hig_c)]

       range_arr = np.arange(100,500,1)

       range_lo = fuzz.trimf(range_arr, spisok7)
       range_me = fuzz.trimf(range_arr, spisok8)
       range_hi = fuzz.trimf(range_arr, spisok9)

       #result
       all_low_a = request.POST.get("all_low_a")
       all_low_b = request.POST.get("all_low_b")
       all_low_c = request.POST.get("all_low_c")
       all_mid_a = request.POST.get("all_mid_a")
       all_mid_b = request.POST.get("all_mid_b")
       all_mid_c = request.POST.get("all_mid_c")
       all_hig_a = request.POST.get("all_hig_a")
       all_hig_b = request.POST.get("all_hig_b")
       all_hig_c = request.POST.get("all_hig_c")
       spisok10 = [int(all_low_a), int(all_low_b), int(all_low_c)]
       spisok11 = [int(all_mid_a), int(all_mid_b), int(all_mid_c)]
       spisok12 = [int(all_hig_a), int(all_hig_b), int(all_hig_c)]

       all_arr = np.arange(0,400,1)

       all_lo = fuzz.trimf(all_arr, spisok10)
       all_me = fuzz.trimf(all_arr, spisok11)
       all_hi = fuzz.trimf(all_arr, spisok12)

       graphs = []
       graphs.append(
           go.Scatter(x=temp1_arr, y=temp_lo, mode='lines', name='НИЗКАЯ температура платформы'))
       graphs.append(
           go.Scatter(x=temp1_arr, y=temp_me, mode='lines', name='СРЕДНЯЯ температура платформы')
       )
       graphs.append(
           go.Scatter(x=temp1_arr, y=temp_hi, mode='lines', name='ВЫСОКАЯ температура платформы')
       )
       layout = {
         'title': 'Температура платформы',
         'xaxis_title': 'область значений переменной',
         'yaxis_title': 'функция принадлежности',
         'height': 800,
         'width': 800,
       }
       graphs2 = []
       graphs2.append(
           go.Scatter(x=temp2_arr , y=temp2_lo, mode='lines', name='НИЗКАЯ температура пластика'))
       graphs2.append(
           go.Scatter(x=temp2_arr , y=temp2_me, mode='lines', name='СРЕДНЯЯ температура пластика ')
       )
       graphs2.append(
           go.Scatter(x=temp2_arr , y=temp2_hi, mode='lines', name='ВЫСОКАЯ температура пластика')
       )
       layout2 = {
         'title': 'Температура пластика',
         'xaxis_title': 'область значений переменной',
         'yaxis_title': 'функция принадлежности',
         'height': 800,
         'width': 800,
       }
       graphs3 = []
       graphs3.append(
           go.Scatter(x=range_arr  , y=range_lo, mode='lines', name='НИЗКАЯ высота платформы'))
       graphs3.append(
       go.Scatter(x=range_arr , y=range_me, mode='lines', name='СРЕДНЯЯ высота платформы'))
       graphs3.append(
           go.Scatter(x=range_arr , y=range_hi, mode='lines', name='БОЛЬШАЯ высота платформы')
       )
       layout3 = {
         'title': 'Высота платформы',
         'xaxis_title': 'область значений переменной',
         'yaxis_title': 'функция принадлежности',
         'height': 800,
         'width': 800,
       }
       graphs4 = []
       graphs4.append(
           go.Scatter(x=all_arr, y=all_lo, mode='lines', name='НИЗКОЕ качество')
       )
       graphs4.append(
           go.Scatter(x=all_arr, y=all_me, mode='lines', name='СРЕДНЕЕ качество')
       )
       graphs4.append(
         go.Scatter(x=all_arr, y=all_hi, mode='lines', name='ВЫСОКОЕ качество'))
       layout4 = {
         'title': 'Общее качество модели',
         'xaxis_title': 'область значений переменной',
         'yaxis_title': 'функция принадлежности',
         'height': 800,
         'width': 800,
       }
       plot_div = plot({'data': graphs, 'layout': layout},
                      output_type='div')
       plot2_div = plot({'data': graphs2, 'layout': layout2},
                      output_type='div')
       plot3_div = plot({'data': graphs3, 'layout': layout3},
                       output_type='div')
       plot4_div = plot({'data': graphs4, 'layout': layout4},
                       output_type='div')
       temp1 = request.POST.get("temp1")
       temp2 = request.POST.get("temp2")
       range = request.POST.get("range")

       qual_level_lo = fuzz.interp_membership(temp1_arr, temp_lo, temp1)
       qual_level_md = fuzz.interp_membership(temp1_arr, temp_me, temp1)
       qual_level_hi = fuzz.interp_membership(temp1_arr, temp_hi, temp1)

       serv_level_lo = fuzz.interp_membership(temp2_arr, temp2_lo, temp2)
       serv_level_md = fuzz.interp_membership(temp2_arr, temp2_me, temp2)
       serv_level_hi = fuzz.interp_membership(temp2_arr, temp2_hi, temp2)

       tip_level_lo = fuzz.interp_membership(range_arr, range_hi, range)
       tip_level_md = fuzz.interp_membership(range_arr, range_me, range)
       tip_level_hi = fuzz.interp_membership(range_arr, range_lo, range)

       # rule1
       active_rule1 = np.fmax(qual_level_lo, serv_level_lo)
       all_activation_lo = np.fmin(active_rule1, all_lo)

       # rule2
       all_activation_md = np.fmin(serv_level_md, range_me)

       # rule3
       active_rule3 = np.fmax(qual_level_hi, serv_level_hi)
       all_activation_hi = np.fmin(active_rule3, all_hi)
       all0 = np.zeros_like(all_arr)

       # rule4
       active_rule4 = np.fmax(qual_level_lo, tip_level_lo)
       all_activation_lo = np.fmin(active_rule4, all_lo)

       # rule5
       active_rule5 = np.fmax(tip_level_hi, serv_level_hi)
       all_activation_hi = np.fmin(active_rule5, all_hi)
       all0 = np.zeros_like(all_arr)

       # rule6
       active_rule6 = np.fmax(serv_level_lo, tip_level_lo)
       all_activation_lo = np.fmin(active_rule6, all_lo)

       # rule7
       active_rule7 = np.fmax(tip_level_hi, qual_level_hi)
       all_activation_hi = np.fmin(active_rule7, all_hi)
       all0 = np.zeros_like(all_arr)

       # rule8
       all_activation_md = np.fmin(qual_level_md, all_me)

       # rule9
       all_activation_md = np.fmin(tip_level_md, all_me)

       # rule10
       active_rule10 = np.fmin(qual_level_lo, serv_level_lo)
       all_activation_lo = np.fmin(active_rule10, all_lo)

       aggregated = np.fmax(all_activation_lo,
                            np.fmax(all_activation_md, all_activation_hi))

       all = fuzz.defuzz(all_arr, aggregated, 'centroid')
       all_activation = fuzz.interp_membership(all_arr, aggregated, all)
       graphs5 = []
       graphs5.append(
           go.Scatter(x=all_arr, y=all_lo, mode='lines', name='НИЗКОЕ качество'))
       graphs5.append(
           go.Scatter(x=all_arr, y=all_me, mode='lines', name='СРЕДНЕЕ качество')
       )
       graphs5.append(
           go.Scatter(x=all_arr, y=all_hi, mode='lines', name='ВЫСОКОЕ качество')
       )
       graphs5.append(
           go.Scatter(x=all_arr, y=all_activation_lo, mode='lines', name='fill',
                      opacity=0.8, marker_color='orange', fill='tozeroy')
       )
       graphs5.append(
           go.Scatter(x=all_arr, y=all_activation_md, mode='lines', name='fill',
                      opacity=0.8, marker_color='orange', fill='tozeroy')
       )
       graphs5.append(
           go.Scatter(x=all_arr, y=all_activation_hi, mode='lines', name='fill',
                      opacity=0.8, marker_color='orange', fill='tozeroy')
       )
       graphs5.append(
           go.Scatter(x=[all, all], y=[0, all_activation], name='result')
       )
       layout = {
           'title': 'Качество модели',
           'xaxis_title': 'область значений переменной',
           'yaxis_title': 'функция принадлежности',
           'height': 800,
           'width': 800,
       }
       plot_res = plot({'data': graphs5, 'layout': layout},
                       output_type='div')
       return render(request, 'myform.html',context={'plot_div': plot_div,'data1': spisok1, 'data2': spisok2, 'data3': spisok3,
                                                      'plot2_div': plot2_div,   'data4': spisok4, 'data5': spisok5, 'data6': spisok6,
                                                      'plot3_div': plot3_div, 'data7': spisok7, 'data8': spisok8, 'data9': spisok9,
                                                      'plot4_div': plot4_div, 'data10': spisok10, 'data11': spisok11, 'data12': spisok12,'plot_res': plot_res, 'res':all,
                                                     'temp1': temp1, 'temp2': temp2, 'range':range})

   else:
       return render(request, "myform.html", {"form": FuzzyForm()})