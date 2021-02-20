from django.urls import path

from . import views


urlpatterns = [
    # ex: /polls/
    path('index', views.index, name='index'),
    path('<int:IdKaf>/', views.DisInKaf, name='dics'),
    path('tests/<int:Idpredm>/',views.TestInKaf,name='tests'),
    path('testir/<int:Idtest>/',views.Questions,name='testid'),
    path('results/<str:questions_id>',views.vote,name='gety')



    ]