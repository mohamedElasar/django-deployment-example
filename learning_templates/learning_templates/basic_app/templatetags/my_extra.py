from django import template

register = template.library()

@registr.filter(name='cut')
def cut(value,arg):
    return value.replace(arg,'')


# register.filter('cut',cut)
