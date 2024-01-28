from django.urls import path 
from question.views import index,index2,index3,question_list,question_details,question_details_template

#from question import views

urlpatterns=[
    path('index',index),
    path('index2',index2),
    path('index3',index3),
    path('question_list',question_list),
    path('question/<int:question_id>',question_details),
    path('question-temp/<int:question_id>',question_details_template)
    
]