from django.shortcuts import render, redirect, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import PipelineList, PipelineResults
from .forms import CreatePipeline
import requests
import json


# render the homepage  
def homepage2(request):
    return render(request, 'base2.html')

# render the homepage  
def homepage(request):
    return render(request, 'base.html')

# render the new create pipeline form
def create_pipeline2(request):
    return render(request, 'create_pipeline2.html')


## show the detailed view of the chosen pipeline object
def detail_view(request, id):
    
    context = {}
    context["data"] = PipelineList.objects.get(id=id)

    ## WHENEVER THE DETAIL VIEW IS SHOWN WE WANT TO UPDATE THE RESULTS FROM API
    # current_pipeline = PipelineResults.objects.get(id=id)
    # unique_api_id = current_pipeline.unique_api_id

    # url = 'https://api.skywatch.co/earthcache/pipelines/{unique_api_id}'
    # recent_results = response.get(url, headers={'x-api-key': 'dd7e14b9-f6c3-45d8-b234-7443a27947ef'}).json()
    # recent_results['data'][0]
         
    return render(request, "post_detail.html", context)


## delete this instance of the model by passing in the object id
def delete_pipeline(request, id):

    # define object we want to delete from the pipeline list by passing in the id
    object_to_delete = PipelineList.objects.get(id=id)
    object_to_delete.delete()

    ## DELETE THE API PIPELINE
    # unique_pipeline_id = object_to_delete.unique_pipeline_id
    # url = 'https://api.skywatch.co/earthcache/pipelines/{unique_pipeline_id}'
    # delete_pipeline = requests.delete('')

    # redirect back to list pipelines - but need a delete validation here
    return redirect('/list_pipelines.html')

## show a list of pipelines for that user
def lists(request):

    # get the user name
    user = str(request.user)

    # filter list of pipelines to only the ones the user has created
    pipeline_list = PipelineList.objects.filter(created_by=user)

    # if the pipeline list is empty, return text
    if len(pipeline_list) == 0:
        context = {'pipeline_list': "You currently have no pipelines"}

    # if not empty, return all pipelines created by user
    else:
        context = {'pipeline_list': pipeline_list}

    # return the list of pipelines
    return render(request, 'list_pipelines.html', context)

## user can create a new pipeline
def create_pipeline(request):
    
    # declare new variable to match the form in forms.py
    form = CreatePipeline()
    context = {'form': form}

    # if the form has been submitted
    if request.method == 'POST':

        # fill in the form variable with users parameters
        form = CreatePipeline(request.POST)

        user = str(request.user)       

        # if the form is valid
        if form.is_valid():

            # add a new id
            pipeline_id = len(PipelineList.objects.filter()) + 1
            #print(f"Pipeline ID: {pipeline_id}")
            
            print("valid")
            form.save()

            # declare current pipeline as the latest created  - latest created by user is probably better too
            current_pipeline = PipelineList.objects.latest('date_created')
            #print(current_pipeline)

            current_pipeline.pipeline_id = pipeline_id
            current_pipeline.created_by = user
            current_pipeline.status = True

            form = CreatePipeline()

            result = "Form submission complete!"
            context = {'form': form, 'result': result}

            # call API
            url = 'https://api.skywatch.co/earthcache/pipelines'

            params = {
                "name": current_pipeline.pipeline_name,
                "interval": "30d",
                "start_date": str(current_pipeline.start_date),
                "output": {
                    "id": "a8fc3dde-a3e8-11e7-9793-ae4260ee3b4b",
                    "format": "geotiff",
                    "mosaic": "off"
                },
                "end_date": str(current_pipeline.end_date),
                "aoi": current_pipeline.AOI,
                "max_cost": 0,
                "min_aoi_coverage_percentage": 50,
                "result_delivery": {
                    "max_latency": "0d",
                    "priorities": [
                    "latest",
                    "highest_resolution",
                    "lowest_cost"
                    ]
                },
                "resolution_low": 30,
                "resolution_high": 10,
                "tags": [
                    {
                    "label": "Texas",
                    "value": "Ranch"
                    },
                    {
                    "label": "Resolution",
                    "value": "10m"
                    }
                ]
                }

            #print(params)
    
            #post_pipeline = requests.post(url,  headers={'x-api-key': 'dd7e14b9-f6c3-45d8-b234-7443a27947ef'}, json=params)
            
            #response = post_pipeline.json()
            
            # UPDATE PIPELINE LISTS OBJECT TO ADD THE UNIQUE ID FROM SKYWATCH
            #unique_api_id = response['data']['id']
            #current_pipeline.unique_api_id = unique_api_id
            current_pipeline.save()
            print(current_pipeline)

            ## CREATE THE RESULTS OBJECT FOR THIS API CALL - but only the id really cause post-detail will call the results API get
            #new_pipeline_result = PipelineResults(unique_pipeline_id=unique_api_id)
            #new_pipeline_result.save()

            ## RENDER THE DETAIL VIEW FOR THIS PIPELINE ONCE SUBMITTED
            id = pipeline_id
            return redirect(reverse('post_detail', args=[ id ]))
    

        else:
            print("not valid")
            form = CreatePipeline()
            result = "Form not valid: please submit another"

            context = {'form': form, 'result': result}
    
    

    # render function to send the form back to index.html
    return render(request, 'create_pipeline.html', context)


def try_api(request):

    #url = 'https://api.skywatch.co/earthcache/pipelines'
    #url = 'https://api.skywatch.co/earthcache/pipelines/3752f093-bbd6-4555-8aea-e75423dbc41f'
    #url = 'https://api.skywatch.co/earthcache/pipelines/3752f093-bbd6-4555-8aea-e75423dbc41f/interval_results'
    #url = 'https://api.skywatch.co/earthcache/pipelines/ca93c8a4-3813-11ec-9d9b-fa9d951a5380/interval_results'

    # params = {
    #     "name": "LUCY 8",
    #     "interval": "30d",
    #     "start_date": "2019-12-01",
    #     "output": {
    #         "id": "a8fc3dde-a3e8-11e7-9793-ae4260ee3b4b",
    #         "format": "geotiff",
    #         "mosaic": "off"
    #     },
    #     "end_date": "2019-12-30",
    #     "aoi": {
    #     "type": "Polygon",
    #     "coordinates": [
    #       [
    #         [
    #           -3.326883316040039,
    #           48.8207109168586
    #         ],
    #         [
    #           -3.333578109741211,
    #           48.82116301419633
    #         ],
    #         [
    #           -3.335294723510742,
    #           48.81347680485208
    #         ],
    #         [
    #           -3.3187294006347656,
    #           48.81268551051467
    #         ],
    #         [
    #           -3.3164119720458984,
    #           48.819467628153056
    #         ],
    #         [
    #           -3.326883316040039,
    #           48.8207109168586
    #         ]
    #       ]
    #     ]
    #   },
    #     "max_cost": 0,
    #     "min_aoi_coverage_percentage": 80,
    #     "result_delivery": {
    #         "max_latency": "0d",
    #         "priorities": [
    #         "latest",
    #         "highest_resolution",
    #         "lowest_cost"
    #         ]
    #     },
    #     "resolution_low": 30,
    #     "resolution_high": 10,
    #     "tags": [
    #         {
    #         "label": "Texas",
    #         "value": "Ranch"
    #         },
    #         {
    #         "label": "Resolution",
    #         "value": "10m"
    #         }
    #     ]
    #     }

    response = {"data": {"id": "37b57b48-3fa9-11ec-8e41-9a623311d0d3", "name": "Test10", "start_date": "2021-11-15", "end_date": "2021-11-18", "aoi": {"type": "Polygon", "coordinates": [[[2.286872863769531, 48.83602344356167], [2.4008560180664062, 48.83602344356167], [2.4008560180664062, 48.89271247049609], [2.286872863769531, 48.89271247049609], [2.286872863769531, 48.83602344356167]]]}, "area_km2": 52.67503533722846, "cloud_cover_percentage": 100, "min_aoi_coverage_percentage": 50, "interval": "30d", "resolution_low": 30, "resolution_high": 10, "output": {"id": "a8fc3dde-a3e8-11e7-9793-ae4260ee3b4b", "format": "geotiff", "mosaic": "off"}, "status": "pending", "tags": [{"label": "Texas", "value": "Ranch"}, {"label": "Resolution", "value": "10m"}], "created_at": "2021-11-07T09:00:55.729062Z", "updated_at": "2021-11-07T09:00:55.729062Z", "max_cost": 0, "result_delivery": {"max_latency": "0d", "priorities": ["latest", "highest_resolution", "lowest_cost"]}}}
    
    #response = requests.get(url,  headers={'x-api-key': 'dd7e14b9-f6c3-45d8-b234-7443a27947ef'}).json()

    print(response)
    print(response['data']['id'])

    # print(response['data'][0])

    return render(request, 'results.html')