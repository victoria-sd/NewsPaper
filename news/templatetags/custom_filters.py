from django import template


register = template.Library()

BAD_WORDS = ['Top', 'Interesting']

@register.filter()
def censor(value):

   if not isinstance(value, str):
        raise ValueError("Значение должно быть строкой")

   for word in BAD_WORDS:
      value = value.replace(word, '*' * len(word))
   return (value)
