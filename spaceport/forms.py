from django.forms import ModelForm, DateInput
from .models import PipelineList



# class CreatePipeline(ModelForm):
#     class Meta:
#         model = PipelineList
#         fields = '__all__'


# class ChooseSatNum(ModelForm):
#     class Meta:
#         model = PipeLineChoice
#         fields = '__all__'


class CreatePipeline(ModelForm):
    class Meta:
        model = PipelineList
        fields = ['pipeline_name', 'pipeline_des', 'AOI', 'start_date', 'end_date','output_format']  
        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'end_date': DateInput(attrs={'type': 'date'}),
        }