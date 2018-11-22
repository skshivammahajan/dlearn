from django.db import models

# Create your models here.


class NodeInventory(models.Model):
    node_name = models.CharField(max_length = 100)
    node_ip = models.CharField(max_length = 30)
    oss_ip = models.CharField(max_length = 30)
    domain = models.
