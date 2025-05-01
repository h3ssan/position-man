from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=255)
    name_in_native_language = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"

class Candidate(models.Model):
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=16, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.full_name

class CandidateLanguage(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    proficiency_level = models.CharField(max_length=64, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('native', 'Native'),
    ])

    def __str__(self):
        return f"{self.candidate.full_name} - {self.language.name} ({self.proficiency_level})"