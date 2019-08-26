from django import template

register = template.Library()

@register.filter(name='zip')
def zip_lists(a, b):
  return zip(a, b)

@register.filter(name='cal_percentage')
def cal_percentage(new, old):
  per = (new-old)/old
  return int(per*100)

@register.filter(name='cal_page')
def cal_page(page_number, no_of_pro):
  per = (page_number-1)*no_of_pro
  return int(per+1)

@register.filter(name='multiply')
def cal_percentage(num1, num2):
  return num1*num2