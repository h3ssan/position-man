from django.db import models

class Position(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Position"
        verbose_name_plural = "Positions"
        ordering = ["-created_at"]


class PositionSubmission(models.Model):
    position = models.ForeignKey(Position, related_name='submissions', on_delete=models.CASCADE)
    candidate = models.ForeignKey('candidate.Candidate', related_name='submissions', on_delete=models.CASCADE)
    resume = models.FileField(upload_to='uploads/resumes/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.candidate.full_name} - {self.position.title}"

    class Meta:
        verbose_name = "Position Submission"
        verbose_name_plural = "Position Submissions"
        ordering = ["-submitted_at"]