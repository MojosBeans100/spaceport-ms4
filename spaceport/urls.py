from django.urls import path
from django.conf.urls import url, include
from . import views
#from . models import PipelineResults

urlpatterns = [
    path('base.html', views.homepage, name='home'),
    path('create_pipeline.html', views.create_pipeline),
    #path('<id>', views.detail_view, name='detail_view'),
    path('post_detail/<int:id>', views.detail_view, name='post_detail'),
    path('delete_pipeline/<int:id>', views.delete_pipeline, name='delete_pipeline'),
    path('list_pipelines.html', views.lists)
]