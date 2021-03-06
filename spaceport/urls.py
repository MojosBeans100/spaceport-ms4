from django.urls import path
from django.conf.urls import url, include
from . import views
#from . models import PipelineResults

urlpatterns = [
    path('', views.homepage, name='home'),
    path('user_landing_page.html', views.userpage, name='userpage'),
    #path('user_landing_page2.html', views.user_page2, name='userpage2'),
    #path('base2.html', views.homepage2, name='home2'),
    path('models.html', views.model_view, name='models'),
    path('create_pipeline2.html', views.create_pipeline2),
    path('create_pipeline.html', views.create_pipeline, name='create_pipeline'),
    path('list_pipelines.html', views.lists, name='lists'),
    #path('user_landing_page2.html', views.lists, name='lists'),
    path('post_detail/<int:id>', views.detail_view, name='post_detail'),
    #path('post_detail2/<int:id>', views.detail_view, name='post_detail'),
    #path('post_detail2.html', views.post_detail2, name='post_detail2'),
    path('delete_pipeline/<int:id>', views.delete_pipeline, name='delete_pipeline'),
    #path('<id>', views.detail_view, name='detail_view'),
    path('try_api.html', views.try_api),
    path('testing-geoman.html', views.geoman)
]