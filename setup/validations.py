from django.core.exceptions import ValidationError


'''Valida se a data da publicação de alguma entidade, é maior que o ano de 1900.'''
def validate_publication_date(value):
    if value < 1900 or value > 9999:
        raise ValidationError(
            f"Insira um ano válido, a partir de 1900."
        )
