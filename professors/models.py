from django.db import models
import uuid

class Professor(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)  # duplicates allowed

    def __str__(self):
        return self.name


class Rating(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, db_column="professor_id")
    teaching = models.PositiveSmallIntegerField()
    evaluation = models.PositiveSmallIntegerField()
    behaviour = models.PositiveSmallIntegerField()
    internals = models.PositiveSmallIntegerField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "reviews"  # points to Supabase reviews table
