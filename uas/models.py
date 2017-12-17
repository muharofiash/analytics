from django.db import models

# Create your models here.
class HeartRate(models.Model):
    unit_id =  models.IntegerField(null=True)
    heart_rate = models.IntegerField(null=True)
    timestamp = models.DateTimeField(null=True)
    sync_time = models.DateTimeField(null=True)
    status = models.CharField(max_length=16, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.unit_id)

class RestingHeartRate(models.Model):
    unit_id = models.IntegerField(null=True)
    rest_heart_rate = models.IntegerField(null=True)
    timestamp = models.DateTimeField(null=True)
    sync_time = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.unit_id)

class StepCalories(models.Model):
    unit_id = models.IntegerField(null=True)
    start_timestamp = models.DateTimeField(null=True)
    stop_timestamp = models.DateTimeField(null=True)
    step = models.IntegerField(null=True)
    total_calories = models.IntegerField(null=True)
    sync_time = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.unit_id)

class Stress(models.Model):
    unit_id = models.IntegerField(null=True)
    stress = models.IntegerField(null=True)
    timestamp = models.DateTimeField(null=True)
    sync_time = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.unit_id)

class RawActivity(models.Model):
    unit_id = models.IntegerField(null=True)
    activity = models.CharField(max_length=32, null=True)
    intensity = models.FloatField(null=True)
    start_timestamp = models.DateTimeField(null=True)
    stop_timestamp = models.DateTimeField(null=True)
    duration = models.FloatField(null=True)
    sync_time = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.unit_id)