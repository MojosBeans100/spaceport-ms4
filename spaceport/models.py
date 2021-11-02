from django.db import models

# Create your models here.

# all pipelines which are created, by any user,
# are listed in this model
class PipelineList(models.Model):

    MY_CHOICES = (
        ('a', 'Hola'),
        ('b', 'Hello'),
        ('c', 'Bonjour'),
        ('d', 'Boas'),
    )

    pipeline_id = models.CharField(max_length=20)              # AUTO unique identifier for this pipeline (auto generated?)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    pipeline_name = models.CharField(max_length=50, unique=True)	        # user's given name for pipeline
    pipeline_des = models.TextField()                                       # user's given description
    created_by = models.CharField(max_length=100, null=True)	            # AUTO user	(username or email?)
    date_created = models.DateTimeField(auto_now=True)                      # AUTO date the pipeline was created (= today()?)
    status = models.BooleanField(default=False)	                            # AUTO pipeline active/not active (default to True when created?)
    AOI = models.JSONField(null=True, blank=True)                                   # area of interest: location co-ordinates (need to be able to control size of this?)
    start_date = models.DateField(null=True)                                         # when pipeline starts capturing images
    end_date = models.DateField(null=True)	                                        # when pipeline ends	DateField or Null	31/12/2021
    freq_number = models.PositiveIntegerField(null=True, blank=True)	   # how frequently images are captured, must be integer
    freq_interval = models.CharField(max_length=20, null=True)            # interval of frequency eg days, weeks, months (user can choose)
    cloud_cover = models.DecimalField(max_digits = 5,decimal_places=2, null=True)      # % cloud cover allowed max
    resolution = models.CharField(max_length=20, null=True)               # picture resolution range eg 7680 × 6876
    output_format = models.CharField(max_length=1, choices=MY_CHOICES,null=True)            # image format type (selected by user) GEOTiff    

# class PipelineResults(models.Model):
#     satellite_id = models.PositiveIntegerField(blank=True, null=True)
#     name = models.CharField(max_length=200, null=True)
#     footprint = models.CharField(max_length=200, null=True)

#     def __str__(self):
#         return self.satellite_id

#     class Meta:
#         verbose_name_plural = 'satellite ids'



# class PipeLineChoice(models.Model):
#     user_sat_num = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     # def __str__(self):
#     #     return self.user_sat_num