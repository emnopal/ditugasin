import csv

from django.core.exceptions import PermissionDenied
from django.http import HttpResponse

from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d%m%Y%H%M%S") # get current date and time

def download_csv(request, queryset):
    model = queryset.model
    model_fields = model._meta.fields + model._meta.many_to_many
    field_names = [field.name for field in model_fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{dt_string}.csv"'

    writer = csv.writer(response, delimiter=",")
    writer.writerow(field_names)
    for row in queryset:
        values = []
        for field in field_names:
            value = getattr(row, field)
            if callable(value):
                try:
                    value = value() or ''
                except:
                    value = 'Error retrieving value'
            if value is None:
                value = ''
            values.append(value)
        writer.writerow(values)

    return response
