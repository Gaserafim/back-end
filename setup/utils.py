from django.db.models import Avg


def calculate_score_field(model, field, filter_id):
    query = {
        field: filter_id
    }
    return model.objects.filter(**query).aggregate(Avg('score'))['score__avg']
