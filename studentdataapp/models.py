from django.db import models

class studentdata(models.Model):
    student_roll_number=models.IntegerField(unique=True)
    student_first_name=models.CharField(max_length=100)
    student_last_name=models.CharField(max_length=100)
    student_class=models.CharField(max_length=100)
    student_section=models.CharField(max_length=100)
    telugu_marks=models.IntegerField()
    hindi_marks = models.IntegerField()
    english_marks = models.IntegerField()
    mathematics_marks = models.IntegerField()
    scince_marks = models.IntegerField()
    social_marks = models.IntegerField()
