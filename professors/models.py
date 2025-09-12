from django.db import models


class Professor(models.Model):
    id = models.UUIDField(primary_key=True)  # matches Supabase uuid
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "teachers"  # use Supabase "teachers" table

    def __str__(self):
        return self.name


class Rating(models.Model):
    professor = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        db_column="professor_id"  # must match Supabase column
    )
    teaching = models.PositiveSmallIntegerField()
    evaluation = models.PositiveSmallIntegerField()
    behaviour = models.PositiveSmallIntegerField()
    internals = models.PositiveSmallIntegerField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "reviews"  # use Supabase "reviews" table



    