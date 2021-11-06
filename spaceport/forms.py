from django.forms import ModelForm, DateInput
from .models import PipelineList

class CreatePipeline(ModelForm):
    class Meta:
        model = PipelineList

        fields = ['id','pipeline_name', 'pipeline_des', 'AOI', 'start_date', 'end_date','output_format']  
        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'end_date': DateInput(attrs={'type': 'date'}),
        }

        labels = {
            'pipeline_name': "Pipeline Name",
            'pipeline_dec': "Add some detail to describe your pipeline",
        }