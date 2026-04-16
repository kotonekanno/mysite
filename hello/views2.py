from django import forms
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

class MyForm(forms.Form):
     name = forms.CharField(label = '名前')
     age = forms.IntegerField(label = '年齢')

@csrf_exempt
def form(request):
    params = { 'form': None, 'result': '' } 
    if request.method == 'POST':
       name = request.POST['name'] 
       age = request.POST['age']
       params['form'] = MyForm(request.POST)
       if int(age) >= 20:
            params['result'] = name + 'さんは20歳以上です'
       else:
            params['result'] = name + 'さんは20歳未満です'
    else: 
       params['form'] = MyForm() 
       params['result'] = '入力された名前, 年齢を表示' 
 
    return render(request, 'form.html', params)
