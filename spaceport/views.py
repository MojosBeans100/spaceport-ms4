from django.shortcuts import render
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import PipelineList
from .forms import CreatePipeline
import requests
import json


def homepage(request):
    return render(request, 'base.html')

def lists(request):

    user = str(request.user)

    pipeline_list = PipelineList.objects.filter(created_by = user)
    print(pipeline_list)

    if len(pipeline_list) == 0:
        context = {'message': "You currently have no pipelines"}

    else:
        context = {'pipeline_list': pipeline_list}

    return render(request, 'list_pipelines.html', context)

# def create_pipeline(request):
#     return render(request, 'create_pipeline.html')

# class lists(generic.ListView):
#     model = PipelineList()
#     queryset = PipelineResults.objects.order_by('satellite_id')
#     #print(model)
#     template_name = "list_pipelines.html"
#     #paginate_by = 6



def create_pipeline(request):

    
    form = CreatePipeline()
    context = {'form': form}

    if request.method == 'POST':

        form = CreatePipeline(request.POST)

        user = str(request.user)

        print(user)

        #print(form.is_valid())

        # start_date = request.POST['start_date']
        # end_date = request.POST['end_date']
        # pipeline_name = request.POST['pipeline_name']
        # pipeline_des = request.POST['pipeline_des']
        # AOI = request.POST['AOI']
        # output_format = request.POST['output_format']

        # start_date_type = type(request.POST['start_date']) 
        # end_date_type = type(request.POST['end_date'])
        # pipeline_name_type = type(request.POST['pipeline_name'])
        # pipeline_des_type = type(request.POST['pipeline_des'])
        # AOI_type = type(request.POST['AOI'])
        # output_format_type = type(request.POST['output_format'])
    
        # print(f"Start date: {start_date}")
        # print(f"Start date type: {start_date_type}")

        # print(f"End date: {end_date}")
        # print(f"End date type: {end_date_type}")

        # print(f"Pipeline name: {pipeline_name}")
        # print(f"Pipeline name type: {pipeline_name_type}")

        # print(f"Pipeline des: {pipeline_des}")
        # print(f"Pipeline des type: {pipeline_des_type}")

        # print(f"AOI: {AOI}")
        # print(f"AOI type: {AOI_type}")

        # print(f"Output format: {output_format}")
        # print(f"Output format type: {output_format_type}")

        # form_data = {
        #     "start_date": start_date,
        #     "end_date": end_date,
        #     "pipeline name": name,
        # }

        # print(form_data)
        

        if form.is_valid():

            pipeline_id = len(PipelineList.objects.filter()) + 1
            #print(f"Pipeline ID: {pipeline_id}")
            
            print("valid")
            form.save()

            current_pipeline = PipelineList.objects.latest('date_created')
            #print(current_pipeline)

            current_pipeline.pipeline_id = pipeline_id
            current_pipeline.created_by = user
            current_pipeline.status = True

            current_pipeline.save()

            form = CreatePipeline()

            result = "Form submission complete!"
            context = {'form': form, 'result': result}


        else:
            print("not valid")
            form = CreatePipeline()
            result = "Form not valid: please submit another"

            context = {'form': form, 'result': result}
    
    

    # render function to send the form back to index.html
    return render(request, 'create_pipeline.html', context)

   


# def index(request):
#     form = ChooseSatNum()
    
#     # if the form has been posted
#     if request.method == 'POST':
        
#         # fill in the form with the data from the post request
#         form = ChooseSatNum(request.POST)

#         # if the data is valid, save it
#         if form.is_valid():
            
            
#             # call the API
#             try: 

#                 x_api_key = 'dd7e14b9-f6c3-45d8-b234-7443a27947ef'

#                 params = {
#                 "name": "High Resolution Sample 2",
#                 "interval": "30d",
#                 "start_date": "2019-12-07",
#                 "output": {
#                     "id": "a8fc3dde-a3e8-11e7-9793-ae4260ee3b4b",
#                     "format": "geotiff",
#                     "mosaic": "off"
#                 },
#                 "end_date": "2019-12-21",
#                 "aoi": {
#                     "type": "Polygon",
#                     "coordinates": [
#                     [
#                         [
#                         -96.3607387799783,
#                         32.5923771291187
#                         ],
#                         [
#                         -96.3607337185765,
#                         32.5923868170991
#                         ],
#                         [
#                         -96.3606253319712,
#                         32.5924923739344
#                         ],
#                         [
#                         -96.3604848886566,
#                         32.5925664011575
#                         ],
#                         [
#                         -96.3603248141178,
#                         32.5926023494186
#                         ],
#                         [
#                         -96.3601592706793,
#                         32.5925970383024
#                         ],
#                         [
#                         -96.3600029045173,
#                         32.5925509376938
#                         ],
#                         [
#                         -96.3574049045173,
#                         32.5913949430461
#                         ],
#                         [
#                         -96.3572573015518,
#                         32.5912996991454
#                         ],
#                         [
#                         -96.3552208146934,
#                         32.5894561296526
#                         ],
#                         [
#                         -96.3537727463132,
#                         32.5920431586138
#                         ],
#                         [
#                         -96.3536626132907,
#                         32.5921749900381
#                         ],
#                         [
#                         -96.3535060223619,
#                         32.5922676368342
#                         ],
#                         [
#                         -96.3533214558468,
#                         32.5923101640973
#                         ],
#                         [
#                         -96.353130698004,
#                         32.5922975524359
#                         ],
#                         [
#                         -96.3523471999923,
#                         32.5921283333776
#                         ],
#                         [
#                         -96.3464009559693,
#                         32.5911851546403
#                         ],
#                         [
#                         -96.3463984221295,
#                         32.5911847476055
#                         ],
#                         [
#                         -96.3427636120308,
#                         32.5905934987997
#                         ],
#                         [
#                         -96.3413194802847,
#                         32.5904909747675
#                         ],
#                         [
#                         -96.3327037320044,
#                         32.5900172659919
#                         ],
#                         [
#                         -96.3325253720148,
#                         32.5899820193623
#                         ],
#                         [
#                         -96.3323702339073,
#                         32.589899921853
#                         ],
#                         [
#                         -96.3322551029996,
#                         32.5897798559711
#                         ],
#                         [
#                         -96.3321924359913,
#                         32.5896348122388
#                         ],
#                         [
#                         -96.3320711003466,
#                         32.5890851868129
#                         ],
#                         [
#                         -96.3317277629942,
#                         32.5887751253808
#                         ],
#                         [
#                         -96.3316428733734,
#                         32.5886747301674
#                         ],
#                         [
#                         -96.331591941204,
#                         32.5885591731414
#                         ],
#                         [
#                         -96.3315784808796,
#                         32.5884364278631
#                         ],
#                         [
#                         -96.3316124038568,
#                         32.5877147943336
#                         ],
#                         [
#                         -96.3305592208909,
#                         32.5868834708082
#                         ],
#                         [
#                         -96.3305114469404,
#                         32.5868407275502
#                         ],
#                         [
#                         -96.3277284469405,
#                         32.584015736996
#                         ],
#                         [
#                         -96.3276437844806,
#                         32.5838983012321
#                         ],
#                         [
#                         -96.3276031184096,
#                         32.5837652371841
#                         ],
#                         [
#                         -96.3276099349048,
#                         32.5836279519809
#                         ],
#                         [
#                         -96.327663649609,
#                         32.5834982146685
#                         ],
#                         [
#                         -96.3277596577258,
#                         32.5833871472831
#                         ],
#                         [
#                         -96.3313634104699,
#                         32.5802955937702
#                         ],
#                         [
#                         -96.3316973496874,
#                         32.5772123438205
#                         ],
#                         [
#                         -96.3317431934068,
#                         32.5770641117137
#                         ],
#                         [
#                         -96.331843239975,
#                         32.5769362146249
#                         ],
#                         [
#                         -96.3339671135089,
#                         32.5750023911045
#                         ],
#                         [
#                         -96.3343207344207,
#                         32.5733199263834
#                         ],
#                         [
#                         -96.3345681049687,
#                         32.5718111702138
#                         ],
#                         [
#                         -96.3299637449795,
#                         32.5731506578839
#                         ],
#                         [
#                         -96.3297675671029,
#                         32.5731761925167
#                         ],
#                         [
#                         -96.3295732226031,
#                         32.5731421268767
#                         ],
#                         [
#                         -96.3267382226031,
#                         32.5721761315635
#                         ],
#                         [
#                         -96.3266011313632,
#                         32.5721088862406
#                         ],
#                         [
#                         -96.3264920948156,
#                         32.5720118002791
#                         ],
#                         [
#                         -96.3264199573205,
#                         32.5718927486008
#                         ],
#                         [
#                         -96.3263905702185,
#                         32.571761387864
#                         ],
#                         [
#                         -96.3260917423249,
#                         32.5659692590568
#                         ],
#                         [
#                         -96.325413813369,
#                         32.5645592829471
#                         ],
#                         [
#                         -96.3253926069185,
#                         32.564506312315
#                         ],
#                         [
#                         -96.3249526069185,
#                         32.563144314187
#                         ],
#                         [
#                         -96.3249332154467,
#                         32.5630093716932
#                         ],
#                         [
#                         -96.324960513474,
#                         32.5628754040964
#                         ],
#                         [
#                         -96.3250322119081,
#                         32.5627536453578
#                         ],
#                         [
#                         -96.3251422984343,
#                         32.5626543056972
#                         ],
#                         [
#                         -96.3295592984343,
#                         32.5596792935384
#                         ],
#                         [
#                         -96.3296334423469,
#                         32.5596371053809
#                         ],
#                         [
#                         -96.3327644423469,
#                         32.5581490986002
#                         ],
#                         [
#                         -96.3328277478905,
#                         32.5581233070197
#                         ],
#                         [
#                         -96.3383137478905,
#                         32.5562382978885
#                         ],
#                         [
#                         -96.3383243259613,
#                         32.556234768945
#                         ],
#                         [
#                         -96.3429575948203,
#                         32.5547350039506
#                         ],
#                         [
#                         -96.3443251884977,
#                         32.5541051637591
#                         ],
#                         [
#                         -96.3455066627244,
#                         32.5531128728725
#                         ],
#                         [
#                         -96.3507030996693,
#                         32.5482217978311
#                         ],
#                         [
#                         -96.350827820296,
#                         32.5481342762133
#                         ],
#                         [
#                         -96.3509771769771,
#                         32.5480807757826
#                         ],
#                         [
#                         -96.3511384894344,
#                         32.5480658387512
#                         ],
#                         [
#                         -96.3512980623531,
#                         32.5480907332816
#                         ],
#                         [
#                         -96.3514423481037,
#                         32.5481533458144
#                         ],
#                         [
#                         -96.3515590969267,
#                         32.5482483605178
#                         ],
#                         [
#                         -96.3534860969267,
#                         32.5503553672458
#                         ],
#                         [
#                         -96.3535796661756,
#                         32.5505105171783
#                         ],
#                         [
#                         -96.3535997499819,
#                         32.5506837380489
#                         ],
#                         [
#                         -96.3533206157359,
#                         32.5533197077269
#                         ],
#                         [
#                         -96.3544086693282,
#                         32.5539131936903
#                         ],
#                         [
#                         -96.3581632559791,
#                         32.5551256283677
#                         ],
#                         [
#                         -96.3582961476875,
#                         32.55518717192
#                         ],
#                         [
#                         -96.358404421026,
#                         32.5552766454897
#                         ],
#                         [
#                         -96.360475421026,
#                         32.5575316527103
#                         ],
#                         [
#                         -96.3605543395135,
#                         32.5576494093759
#                         ],
#                         [
#                         -96.3605901509618,
#                         32.5577812425098
#                         ],
#                         [
#                         -96.3605798828926,
#                         32.5579162094528
#                         ],
#                         [
#                         -96.3599786298113,
#                         32.5603103235637
#                         ],
#                         [
#                         -96.361813351446,
#                         32.5619341103614
#                         ],
#                         [
#                         -96.379154113002,
#                         32.5762042066603
#                         ],
#                         [
#                         -96.3792597444364,
#                         32.5763244543747
#                         ],
#                         [
#                         -96.3793151029373,
#                         32.5764666043633
#                         ],
#                         [
#                         -96.379314563309,
#                         32.5766162121375
#                         ],
#                         [
#                         -96.3792581803853,
#                         32.5767580754622
#                         ],
#                         [
#                         -96.3791516834576,
#                         32.5768777791138
#                         ],
#                         [
#                         -96.3785379649486,
#                         32.5773766710045
#                         ],
#                         [
#                         -96.3720550534858,
#                         32.5829873809385
#                         ],
#                         [
#                         -96.3720467952646,
#                         32.5829943791373
#                         ],
#                         [
#                         -96.3607387799783,
#                         32.5923771291187
#                         ]
#                     ]
#                     ]
#                 },
#                 "max_cost": 0,
#                 "min_aoi_coverage_percentage": 80,
#                 "result_delivery": {
#                     "max_latency": "0d",
#                     "priorities": [
#                     "latest",
#                     "highest_resolution",
#                     "lowest_cost"
#                     ]
#                 },
#                 "resolution_low": 1.5,
#                 "resolution_high": 0.3,
#                 "tags": [
#                     {
#                     "label": "Texas",
#                     "value": "Ranch"
#                     },
#                     {
#                     "label": "Resolution",
#                     "value": "70cm"
#                     }
#                 ]
#                 }

#                 url = 'https://api.skywatch.co/earthcache/pipelines'
#                 #headers: {x_api_key: 'dd7e14b9-f6c3-45d8-b234-7443a27947ef'}
#                 response = requests.get(url, headers={'x-api-key': 'dd7e14b9-f6c3-45d8-b234-7443a27947ef'}, params=params).json()
#                 print(response['data'][0])
#                 #created_at = response['data'][0]['created_at']
#                 #image_url = response['data'][0]['results'][0]['preview_url']
#                 #print(response['data'][0]['results'][0]['preview_url'])
                
#                 #context = {'image_url': image_url}
                
#             # if error from URL
#             except:
#                 print("ERROR")
                
#         # if form is not valid
#         else:
#             print("not valid")
#             context = {'form': form}
    
#     # if the method isn't POST ie is GET
#     else: 
        
#         context = {'form': form}

#     # render function to send the form back to index.html
#     return render(request, 'index.html', context)
 




# def index(request):
#     form = ChooseSatNum()
    
#     # if the form has been posted
#     if request.method == 'POST':
        
#         # fill in the form with the data from the post request
#         form = ChooseSatNum(request.POST)

#         # if the data is valid, save it
#         if form.is_valid():
            
            
#             # call the API
#             try: 

#                 x_api_key = 'dd7e14b9-f6c3-45d8-b234-7443a27947ef'

#                 url = 'https://api.skywatch.co/earthcache/pipelines/3752f093-bbd6-4555-8aea-e75423dbc41f/interval_results'
#                 #headers: {x_api_key: 'dd7e14b9-f6c3-45d8-b234-7443a27947ef'}
#                 response = requests.get(url, headers={'x-api-key': 'dd7e14b9-f6c3-45d8-b234-7443a27947ef'}).json()

#                 #created_at = response['data'][0]['created_at']
#                 image_url = response['data'][0]['results'][0]['preview_url']
#                 print(response['data'][0]['results'][0]['preview_url'])
                
#                 context = {'image_url': image_url}
                
#             # if error from URL
#             except:
#                 print("ERROR")
                
#         # if form is not valid
#         else:
#             print("not valid")
#             context = {'form': form}
    
#     # if the method isn't POST ie is GET
#     else: 
        
#         context = {'form': form}

#     # render function to send the form back to index.html
#     return render(request, 'index.html', context)



# def index(request):
#     form = ChooseSatNum()
    
#     # if the form has been posted
#     if request.method == 'POST':
        
#         # fill in the form with the data from the post request
#         form = ChooseSatNum(request.POST)

#         # if the data is valid, save it
#         if form.is_valid():
#             print("valid")
#             form.save()
#             satellite_id = PipeLineChoice.objects.latest('created_at').user_sat_num
            
#             # call the API
#             try: 
#                 url = 'https://api.spectator.earth/satellite/{satellite_id}'.format(satellite_id = satellite_id)
#                 response = requests.get(url).json()
#                 data = {
#                     "satellite_id": satellite_id,
#                     "id": response['id'],
#                     "satellite_name": response['properties']['name'],
#                     "avg_footprint_width": response['properties']['sensors'][0]['avg_footprint_width'],
#                 }

#                 #print(data["satellite_name"])

#                 # save the data to the pipeline results model
#                 satellite_id = data["id"]
#                 name = data["satellite_name"]
#                 footprint = data["avg_footprint_width"]

#                 # create a new object and save to model
#                 PipelineResults.objects.create(satellite_id=satellite_id, name=name, footprint=footprint)
               
#                 # create the context to send back to the HTML
#                 context = {'form': form, 'satellite_data': data}
                
#             # if error from URL
#             except:
#                 print("ERROR")
#                 error_message = f"No satellites found for Sat Num {satellite_id}"
#                 context = {'form': form, 'satellite_data': "No satellites found", "error_msg": error_message}
            
#         # if form is not valid
#         else:
#             print("not valid")
#             context = {'form': form}
    
#     # if the method isn't POST ie is GET
#     else: 
        
#         context = {'form': form}

#     # render function to send the form back to index.html
#     return render(request, 'index.html', context)




# def index(request):

#     satellite_id = 2

#     url = 'https://api.spectator.earth/satellite/{satellite_id}'.format(satellite_id = satellite_id)
        
#     response = requests.get(url).json()
        
#     data = {
#         "id": response['id'],
#         "satellite_name": response['properties']['name'],
#         "avg_footprint_width": response['properties']['sensors'][0]['avg_footprint_width'],
#     }

#     print(data)

#     #print(satellite_data)

#     context = { 'satellite_info' : data}

#     return render(request, 'index.html', context)