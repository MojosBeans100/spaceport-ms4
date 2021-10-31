from django.urls import path
from . import views
#from . models import PipelineResults

urlpatterns = [
    path('', views.homepage, name='home'),
    #path('models.html', views.ModelsList.as_view()),
    #path('index.html', views.index),
    path('create_pipeline.html', views.create_pipeline),
    path('list_pipelines.html', views.lists)
    # path('results.html', views.results)
]