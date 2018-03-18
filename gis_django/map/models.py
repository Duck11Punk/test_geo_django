from django.contrib.gis.db import models



class Map(models.Model):
    
    productivi = models.IntegerField()
    mpoly = models.MultiPolygonField()
    

    def __str__(self):
        return str(self.productivi)