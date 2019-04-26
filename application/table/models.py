from django.db import models
from app.settings import BASE_DIR


class Table(models.Model):
    field_name = models.CharField(max_length=50)
    field_width = models.IntegerField()
    field_number = models.IntegerField()


class CSVFile(models.Model):
    path = models.FilePathField(path=BASE_DIR)

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path
        self.save()

