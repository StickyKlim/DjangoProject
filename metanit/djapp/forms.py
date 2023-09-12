from django import forms

class FuzzyForm(forms.Form):
     # Система управления настройками 3d принтера
     # температруа платформы
     temp_low_a = forms.IntegerField(label="температура платформы низкая (а):", initial= 5, min_value=1, max_value=100, required= True)
     temp_low_b = forms.IntegerField(label="температура платформы низкая (b):", initial= 15, min_value=10, max_value=100, required= True)
     temp_low_c = forms.IntegerField(label="температура платформы низкая (c):", initial= 35, min_value=10, max_value=100, required= True)

     temp_mid_a = forms.IntegerField(label="температура платформы средняя (a):", initial= 28, min_value=10, max_value=100, required= True)
     temp_mid_b = forms.IntegerField(label="температура платформы средняя (b):", initial= 40, min_value=20, max_value=100, required= True)
     temp_mid_c = forms.IntegerField(label="температура платформы средняя (c):", initial= 50, min_value=20, max_value=100, required= True)

     temp_hig_a = forms.IntegerField(label="температура платформы высокая (a):", initial= 43, min_value=30, max_value=100, required= True)
     temp_hig_b = forms.IntegerField(label="температура платформы высокая (b):", initial= 70, min_value=30, max_value=100, required= True)
     temp_hig_c = forms.IntegerField(label="температура платформы высокая (c):", initial= 100, min_value=30, max_value=100, required= True)
    # температура пластика
     temp2_low_a = forms.IntegerField(label="температура пластика низкая (а):", initial=100, min_value=100, max_value=210, required=True)
     temp2_low_b = forms.IntegerField(label="температура пластика низкая (b):",  initial=113, min_value=100, max_value=210, required=True)
     temp2_low_c = forms.IntegerField(label="температура пластика низкая (c):", initial=160, min_value=100, max_value=210, required=True)
     temp2_mid_a = forms.IntegerField(label="температура пластика средняя (а):", initial=135, min_value=100, max_value=300,required=True)
     temp2_mid_b = forms.IntegerField(label="температура пластика средняя (b):", initial=185, min_value=100, max_value=300,required=True)
     temp2_mid_c = forms.IntegerField(label="температура пластика средняя (c):", initial=215, min_value=100, max_value=300,required=True)
     temp2_hig_a = forms.IntegerField(label="температура пластика высокая (а):", initial=207, min_value=200, max_value=300,required=True)
     temp2_hig_b = forms.IntegerField(label="температура пластика высокая (b):", initial=289, min_value=210, max_value=300,required=True)
     temp2_hig_c = forms.IntegerField(label="температура пластика высокая (c):", initial=300, min_value=210, max_value=300,required=True)
     #Расстояние между платформой и экструдером
     range_low_a= forms.IntegerField(label="расстояние малое (а):", initial=100, min_value=100, max_value=500,   required=True)
     range_low_b= forms.IntegerField(label="расстояние малое (b):", initial=110, min_value=100, max_value=500,   required=True)
     range_low_c= forms.IntegerField(label="расстояние малое (c):", initial=203, min_value=100, max_value=500,   required=True)
     range_mid_a= forms.IntegerField(label="расстояние среднее (а):", initial=189, min_value=100, max_value=500,   required=True)
     range_mid_b= forms.IntegerField(label="расстояние среднее (b):", initial=220, min_value=100, max_value=500,   required=True)
     range_mid_c= forms.IntegerField(label="расстояние среднее (c):", initial=340, min_value=100, max_value=500,   required=True)
     range_hig_a= forms.IntegerField(label="расстояние большое (а):", initial=334, min_value=300, max_value=500,   required=True)
     range_hig_b= forms.IntegerField(label="расстояние большое (b):", initial=450, min_value=300, max_value=500,   required=True)
     range_hig_c= forms.IntegerField(label="расстояние большое (c):", initial=500, min_value=300, max_value=500,   required=True)
     #Уровень модели
     all_low_a = forms.IntegerField(label="Качество модели низкое (a):", initial=0, min_value=0, max_value=400,   required=True)
     all_low_b = forms.IntegerField(label="Качество модели низкое (b):", initial=3, min_value=0, max_value=400,   required=True)
     all_low_c = forms.IntegerField(label="Качество модели низкое (c):", initial=180, min_value=0, max_value=400,   required=True)
     all_mid_a = forms.IntegerField(label="Качество модели среднее (a):", initial=160, min_value=0, max_value=400, required=True)
     all_mid_b = forms.IntegerField(label="Качество модели среднее (b):",  initial=197, min_value=0, max_value=400, required=True)
     all_mid_c = forms.IntegerField(label="Качество модели среднее (c):",  initial=225, min_value=0, max_value=400, required=True)
     all_hig_a = forms.IntegerField(label="Качество модели высокое (a):", initial=205, min_value=200, max_value=400,required=True)
     all_hig_b = forms.IntegerField(label="Качество модели высокое (b):", initial=300, min_value=200, max_value=400,required=True)
     all_hig_c = forms.IntegerField(label="Качество модели высокое (c):", initial=400, min_value=200, max_value=400,required=True)

     temp1=forms.IntegerField(label="Температура платформы", initial= 30, min_value=10, max_value=50, required= True)
     temp2=forms.IntegerField(label="Температура пластика", initial=210, min_value=100, max_value=300, required=True)
     range=forms.IntegerField(label="Расстояние", initial=300, min_value=100, max_value=500,   required=True)