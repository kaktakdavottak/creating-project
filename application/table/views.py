import csv
import os

from django.shortcuts import render
from django.views import View
from .models import Table, CSVFile


class TableView(View):

    def get(self, request):
        with open(CSVFile.objects.all()[0].get_path(), 'rt') as csv_file:
            header = []
            table = []
            table_reader = csv.reader(csv_file, delimiter=';')
            for table_row in table_reader:
                if not header:
                    header = {idx: value for idx, value in enumerate(table_row)}
                else:
                    row = {header.get(idx) or 'col{:03d}'.format(idx): value
                           for idx, value in enumerate(table_row)}
                    table.append(row)

            result = render(request,
                            'table.html',
                            {'columns': Table.objects.order_by("field_number"),
                             'table': table,
                             'csv_file': os.path.basename(CSVFile.objects.all()[0].get_path())})
        return result
