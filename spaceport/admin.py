from django.contrib import admin

# Register your models here.
from .models import PipelineList

@admin.register(PipelineList)
class PipelineListAdmin(admin.ModelAdmin):
    list_display = ('pipeline_name', 'pipeline_des', 'AOI','start_date', 'end_date','date_created')





# @admin.register(PipeLineChoice)
# class PipeLineChoiceAdmin(admin.ModelAdmin):
#     list_display = ('user_sat_num', 'created_at')    


# @admin.register(PipelineResults)
# class PipeLineChoiceAdmin(admin.ModelAdmin):
#     list_display = ('satellite_id', 'name','footprint')    
