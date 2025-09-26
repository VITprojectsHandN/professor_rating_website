import uuid
from django.db import models

class Professor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # match Supabase UUID
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "professors"  # must match Supabase table name

    def save(self, *args, **kwargs):
        self.name = self.name.title()  # Ensure name is always Title Case
        super().save(*args, **kwargs)


class Rating(models.Model):
    professor = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        db_column="professor_id"
    )
    teaching = models.PositiveSmallIntegerField()
    evaluation = models.PositiveSmallIntegerField()
    behaviour = models.PositiveSmallIntegerField()
    internals = models.PositiveSmallIntegerField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "reviews"  # must match Supabase table name
