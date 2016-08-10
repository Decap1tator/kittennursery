from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
        return dictionary.get(key)
#example {{ mydict:get_item:item.name }}
