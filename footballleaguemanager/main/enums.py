from django.db import models

class LeagueType(models.IntegerChoices):
    POINTS_BASED = 1, "Pontos corridos"
    KNOCKOUT_CUP = 2, "Copa"