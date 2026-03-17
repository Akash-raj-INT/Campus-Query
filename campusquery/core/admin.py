from django.contrib import admin
from .models import Answer, Comment, MentorProfile, Note, Question

admin.site.register(Note)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comment)
admin.site.register(MentorProfile)
