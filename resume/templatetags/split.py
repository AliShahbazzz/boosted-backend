from django import template

register = template.Library()


@register.filter(name='split')
def split(value, key):
    """
        Returns the value turned into a list.
    """
    return value.split(key)


@register.filter(name='get_range')
def get_range(value):
    return range(0, value, 1)


@register.filter(name='join_var')
def join_var(value, key):
    k = str(key)
    return k.join(value)


@register.filter(name='get_project')
def get_project(data):
    arr = [
        {
            'name': data['project_name_1'],
            'start': data['project_start_1'],
            'end': data['project_end_1'],
            'description': data['project_description_1']
        },
        {
            'name': data['project_name_2'],
            'start': data['project_start_2'],
            'end': data['project_end_2'],
            'description': data['project_description_2']
        },
        {
            'name': data['project_name_3'],
            'start': data['project_start_3'],
            'end': data['project_end_3'],
            'description': data['project_description_3']
        }]
    return arr


@register.filter(name='get_certificate')
def get_certificate(data):
    arr = [
        {
            'name': data['certificate_name_1'],
            'center': data['certifying_center_1'],
            'obtainment': data['certificate_obtainment_date_1'],
            'description': data['certificate_description_1']
        },
        {
            'name': data['certificate_name_2'],
            'center': data['certifying_center_2'],
            'obtainment': data['certificate_obtainment_date_2'],
            'description': data['certificate_description_2']
        },
        {
            'name': data['certificate_name_3'],
            'center': data['certifying_center_3'],
            'obtainment': data['certificate_obtainment_date_3'],
            'description': data['certificate_description_3']
        }]
    return arr


@register.filter(name='get_experience')
def get_experience(data):
    arr = [
        {
            'company': data['experience_company_1'],
            'position': data['experience_position_1'],
            'start': data['experience_start_1'],
            'end': data['experience_end_1'],
            'description': data['experience_description_1']
        },
        {
            'company': data['experience_company_2'],
            'position': data['experience_position_2'],
            'start': data['experience_start_2'],
            'end': data['experience_end_2'],
            'description': data['experience_description_2']
        },
        {
            'company': data['experience_company_3'],
            'position': data['experience_position_3'],
            'start': data['experience_start_3'],
            'end': data['experience_end_3'],
            'description': data['experience_description_3']
        },
        {
            'company': data['experience_company_4'],
            'position': data['experience_position_4'],
            'start': data['experience_start_4'],
            'end': data['experience_end_4'],
            'description': data['experience_description_4']
        }]
    return arr
