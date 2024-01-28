from django.shortcuts import render

from django.http import HttpResponse

import json

from question.models import Question

# Create your views here.

def index(request):
    json_obj=json.dumps({'msg':'I  Am Good boy'})
    return HttpResponse(json_obj)

def index2(request):
    python_obj=json.loads('{"USER":"json.loads"}')
    return HttpResponse(python_obj)
def index3(request):
    html_obj='''
    <html>
    <head></head>
    <body align="center">
    <font size=30>
    <b>HELLO RAM</b>
    </font>
    
    </body>
    </html>
    
    '''
    return HttpResponse(html_obj)

def question_list(request):
    question = Question.objects.all()
    question_list=[]
    for question in question:
        question_list.append(question.question)
    context={'question':question_list}
    print(context)
    return render(request,"question/question_list.html",context)

def question_details(request, question_id):
    question=Question.objects.get(id=question_id)
    question_dict={
        'question':question.question,
        'category':question.category,
        'added_date':str(question.added_date)
    }
    json_obj = json.dumps(question_dict)
    return HttpResponse(json_obj)


def question_details_template(request, question_id):
    question=Question.objects.get(id=question_id)
    context={
        'question':question.question,
        'category':question.category,
        'marks':question.mark,
        'added_date':str(question.added_date)
   }
   
    print(context)
    return render(request,"question/question_detail.html",context)

