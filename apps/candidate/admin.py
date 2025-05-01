from django.contrib import admin

from .models import Candidate, Language, CandidateLanguage, Country

class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "code")
    search_fields = ("name", "code")
    ordering = ("name",)

admin.site.register(Country, CountryAdmin)

class CandidateLanguageInline(admin.TabularInline):
    model = CandidateLanguage
    extra = 1  # Number of empty forms to display


class CandidateAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone_number", "country", "created_at")
    search_fields = ("full_name", "email", "phone_number")
    list_filter = ("created_at", "country")
    ordering = ("-created_at",)
    inlines = [CandidateLanguageInline]  # Add inline for CandidateLanguage

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related("candidatelanguage_set__language")


admin.site.register(Candidate, CandidateAdmin)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ("name", "name_in_native_language")
    search_fields = ("name", "name_in_native_language")
    ordering = ("name",)
    list_per_page = 20


admin.site.register(Language, LanguageAdmin)