from django import template

register = template.Library()

menu = [
    {"title": "Мои контакты", "view_name": "contacts"},
    {"title": "Услуги", "view_name": "record_list"},
    {"title": "Ваши записи", "view_name": "my_record"},
]   

@register.simple_tag
def get_menu():
    return menu
