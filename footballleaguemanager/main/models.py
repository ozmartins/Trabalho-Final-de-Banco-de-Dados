import uuid
from django.db import models
from .enums import LeagueType;

class League(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    created_at = models.DateField()
    type = models.IntegerField(
        choices=LeagueType.choices,
        default=LeagueType.POINTS_BASED
        )
    has_group_stage = models.BooleanField()
    
    def __str__(self):
        return self.name