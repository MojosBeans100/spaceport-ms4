from django.contrib import admin

# Register your models here.
from .models import PipelineList, PipelineResults

@admin.register(PipelineList)
class PipelineListAdmin(admin.ModelAdmin):
    list_display = ('pipeline_name', 'pipeline_des', 'AOI','start_date', 'end_date', 'date_created')


@admin.register(PipelineResults)
class PipelineResultsAdmin(admin.ModelAdmin):
    list_display = ('results_status', 'unique_pipeline_id')


