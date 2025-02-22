from django.contrib import admin
from .models import *
from django.db.models import Sum 
# Register your models here.
admin.site.register(Recipe)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(StudentId)
admin.site.register(Subject)



class SubjectMarksAdmin(admin.ModelAdmin):
    list_display=['student','subject','marks']
admin.site.register(SubjectMarks,SubjectMarksAdmin)





class ReportCardAdmin(admin.ModelAdmin):
    list_display=['student','student_rank','total_marks','date_of_report_card_generation']
    ordering=['-student_rank']
    def total_marks(self,obj):
        subject_marks=SubjectMarks.objects.filter(student=obj.student)
        return (subject_marks.aggregate(marks=Sum('marks')))['marks']
        return 0

admin.site.register(ReportCard,ReportCardAdmin)