from django.contrib import admin

from .models import Position, PositionSubmission


class PositionAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at")
    search_fields = ("title",)
    list_filter = ("created_at", "updated_at")
    ordering = ("-created_at",)
    date_hierarchy = "created_at"

admin.site.register(Position, PositionAdmin)

class PositionSubmissionAdmin(admin.ModelAdmin):
    list_display = ("candidate", "position", "submitted_at")
    search_fields = ("position__title", "candidate__full_name")
    list_filter = ("submitted_at",)
    ordering = ("-submitted_at",)
    date_hierarchy = "submitted_at"

admin.site.register(PositionSubmission, PositionSubmissionAdmin)