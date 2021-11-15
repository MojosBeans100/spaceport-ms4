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
# def homepage2(request):
#     return render(request, 'base2.html')

def geoman(request):
    return render(request, 'testing-geoman.html')

    # render the homepage  
def post_detail2(request):
    return render(request, 'post_detail2.html')

def model_view(request):

    context = {'all_data': PipelineList.objects.all()}

    return render(request, 'models.html', context)

# render the homepage  
# def user_page2(request):
#     return render(request, 'user_landing_page2.html')


    
# render the homepage  
def userpage(request):
    return render(request, 'user_landing_page.html')



# render the homepage  
def homepage(request):
    return render(request, 'base2.html')

# render the new create pipeline form
def create_pipeline2(request):
    return render(request, 'create_pipeline2.html')


## show the detailed view of the chosen pipeline object
def detail_view(request, id):
    
    context = {}
    context["data"] = PipelineList.objects.get(id=id)

    ## WHENEVER THE DETAIL VIEW IS SHOWN WE WANT TO UPDATE THE RESULTS FROM API

    ## get the relevant pipeline from PipelineList
    # current_pipeline = PipelineList.objects.get(id=id)

    ## get the api unique pipeline id from this pipeline
    # unique_api_id = current_pipeline.unique_api_id

   
        ## if there's an image in the results
        image_found = len(response['data'][i]['results'])

        if image_found > 0:

            ## get the saved pipeline from above
            new_result = PipelineResults.objects.get(api_id=response['data'][i]['pipeline_id'])
            new_result = PipelineResults(
                image_created_at = response['data'][i]['results'][0]['created_at'],
                image_updated_at = response['data'][i]['results'][0]['updated_at'],
                image_preview_url = response['data'][i]['results'][0]['preview_url'],
                image_visual_url = response['data'][i]['results'][0]['visual_url'],
                image_analytics_url = response['data'][i]['results'][0]['analytics_url'],
                image_metadata_url = response['data'][i]['results'][0]['metadata_url'],
                image_size = response['data'][i]['results'][0]['metadata']['size_in_mb'],
                image_valid_pixels_per = response['data'][i]['results'][0]['metadata']['valid_pixels_percentage'],
            )


    # recent_results['data'][0]

    






         
    #return render(request, "post_detail.html", context)
    return render(request, "post_detail.html", context)


# def update_pipeline():
#     get api_id from PipelineList
#     GET from API url
#     update PipelineList: status, num_results
#     update PipelineResults


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

    active_list =  PipelineList.objects.filter(created_by=user).filter(status=1)
    complete_list = PipelineList.objects.filter(created_by=user).filter(status=0)
    # in_progress_list = PipelineList.objects.filter(created_by=user).filter(status='in_progress')


    #print(active_list)
    context = {
            'active_list': active_list,
            'complete_list':complete_list,
            #'progress': in_progress_list,
            }

    # # if the pipeline list is empty, return text
    # if len(pipeline_list) == 0:
    #     context = {'pipeline_list': "You currently have no pipelines"}

    # # if not empty, return all pipelines created by user
    # else:
    #     context = {'pipeline_list': pipeline_list}
    #     

    # return the list of pipelines
    #return render(request, 'user_landing_page2.html', context)
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
            current_pipeline = PipelineList.objects.filter(created_by=user).latest('date_created')
            #print(current_pipeline)

            current_pipeline.pipeline_id = pipeline_id
            current_pipeline.created_by = user
            current_pipeline.status = True
            # current_pipeline.status = Active

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
    
            post_pipeline = requests.post(url,  headers={'x-api-key': 'dd7e14b9-f6c3-45d8-b234-7443a27947ef'}, json=params)
            
            response = post_pipeline.json()
            
            # UPDATE PIPELINE LISTS OBJECT TO ADD THE UNIQUE ID FROM SKYWATCH
            api_id = response['data'][0]['pipeline_id']
            current_pipeline.api_id = api_id
            current_pipeline.save()
            #print(current_pipeline)

            ## CREATE THE RESULTS OBJECT FOR THIS API CALL - but only the id really cause post-detail will call the results API get
            pipeline_result = PipelineResults(api_id=api_id)
            pipeline_result.save()


            ## feed this api id into GET response
            # url = 'https://api.skywatch.co/earthcache/pipelines/{unique_api_id}'
            # recent_results = response.get(url, headers={'x-api-key': 'dd7e14b9-f6c3-45d8-b234-7443a27947ef'}).json()

            for i in recent_results['data']:
                new_result = PipelineResult(
                    api_id = response['data'][i]['pipeline_id'],
                    created_at = response['data'][i]['created_at'],
                    updated_at = response['data'][i]['updated_at'],
                    api_pipeline_id = response['data'][i]['pipeline_id'],
                    output_id = response['data'][i]['output_id'],
                    status = response['data'][i]['status'],
                    message = response['data'][i]['message'],
                    interval_start_date = response['data'][i]['interval']['start_date'],
                    interval_end_date = response['data'][i]['interval']['start_date'],
                    cost = response['data'][i]['total_interval_cost'],
                    scene_height = response['data'][i]['overall_metadata']['scene_height'],
                    scene_width = response['data'][i]['overall_metadata']['scene_width'],
                    filled_area = response['data'][i]['overall_metadata']['filled_area_km2'],
                    aoi_area_per = response['data'][i]['overall_metadata']['filled_area_percentage_of_aoi'],
                    cloud_cover_per = response['data'][i]['overall_metadata']['cloud_cover_percentage'],
                    aoi_cloud_cover_per = response['data'][i]['overall_metadata']['cloud_cover_percentage_of_aoi'],
                    visible_area = response['data'][i]['overall_metadata']['visible_area_km2'],
                    visible_area_per = response['data'][i]['overall_metadata']['visible_area_percentage'],
                    aoi_visible_area_per = response['data'][i]['overall_metadata']['visible_area_percentage_of_aoi'],
            )

            new_result.save()

            ## RENDER THE DETAIL VIEW FOR THIS PIPELINE ONCE SUBMITTED
            #id = pipeline_id
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
    #url = 'https://api.skywatch.co/earthcache/pipelines/0d1865c0-3fb4-11ec-90e2-de2f2f2b54f2/interval_results'
    url = 'https://api.skywatch.co/earthcache/pipelines/ca93c8a4-3813-11ec-9d9b-fa9d951a5380/interval_results'

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

    ##response = {"data": {"id": "37b57b48-3fa9-11ec-8e41-9a623311d0d3", "name": "Test10", "start_date": "2021-11-15", "end_date": "2021-11-18", "aoi": {"type": "Polygon", "coordinates": [[[2.286872863769531, 48.83602344356167], [2.4008560180664062, 48.83602344356167], [2.4008560180664062, 48.89271247049609], [2.286872863769531, 48.89271247049609], [2.286872863769531, 48.83602344356167]]]}, "area_km2": 52.67503533722846, "cloud_cover_percentage": 100, "min_aoi_coverage_percentage": 50, "interval": "30d", "resolution_low": 30, "resolution_high": 10, "output": {"id": "a8fc3dde-a3e8-11e7-9793-ae4260ee3b4b", "format": "geotiff", "mosaic": "off"}, "status": "pending", "tags": [{"label": "Texas", "value": "Ranch"}, {"label": "Resolution", "value": "10m"}], "created_at": "2021-11-07T09:00:55.729062Z", "updated_at": "2021-11-07T09:00:55.729062Z", "max_cost": 0, "result_delivery": {"max_latency": "0d", "priorities": ["latest", "highest_resolution", "lowest_cost"]}}}
    
    #response = requests.get(url,  headers={'x-api-key': 'dd7e14b9-f6c3-45d8-b234-7443a27947ef'}).json()

    #print(response)

    print(dparser("Today is January 1, 2047 at 8:21:00AM", fuzzy_with_tokens=True))

    ## INTETRVAL RESULTS

    # number of intervals
    #print(len(response['data']))

    # for i in response['data']:
    #     print(response['data'][i]['status'])

    #print(response['data'][0]['status'])


    # number of results for first interval
    #print(len(response['data'][0]['results']))

    # first result image
    #print(response['data'][0]['results'][0]['preview_url'])

    # first image satellite source
    #print(response['data'][0]['results'][0]['metadata']['source'])

    # first image cloud cover %
    #print(response['data'][0]['results'][0]['metadata']['cloud_cover_percentage'])

    # pipeline status
    #print(response['data'][0]['status'])

    # print(response['data'][0])
    #print(response['data'][0])

    return render(request, 'results.html')