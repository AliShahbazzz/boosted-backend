from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
from django.template.loader import render_to_string, get_template
from mysite.settings import BASE_DIR
#from xhtml2pdf import pisa
from django.template import Context
# from wkhtmltopdf.utils import render_pdf_from_template
# import pdfkit

from django.http import HttpResponse
import logging
logger = logging.getLogger('weasyprint')
logger.addHandler(logging.FileHandler(BASE_DIR + '/weasyprint.log'))


def pdf(request, name, resume_number):
    page2active = request.data['page2active']
    achievements = request.data['achievements'].split(",,")
    skills = request.data['skills'].split(",,")
    interests = request.data['interests'].split(",,")
    recommendations = request.data['recommendations'].split(",,")
    intern_description = request.data['intern_description'].split(",,")
    projects = [
        {
            'name': request.data['project_name_1'],
            'start': request.data['project_start_1'],
            'end': request.data['project_end_1'],
            'description': request.data['project_description_1'].split(",,")
        },
        {
            'name': request.data['project_name_2'],
            'start': request.data['project_start_2'],
            'end': request.data['project_end_2'],
            'description': request.data['project_description_2'].split(",,")
        },
        {
            'name': request.data['project_name_3'],
            'start': request.data['project_start_3'],
            'end': request.data['project_end_3'],
            'description': request.data['project_description_3'].split(",,")
        }]
    cerificates = [
        {
            'name': request.data['certificate_name_1'],
            'center': request.data['certifying_center_1'],
            'obtainment': request.data['certificate_obtainment_date_1'],
            'description': request.data['certificate_description_1'].split(",,")
        },
        {
            'name': request.data['certificate_name_2'],
            'center': request.data['certifying_center_2'],
            'obtainment': request.data['certificate_obtainment_date_2'],
            'description': request.data['certificate_description_2'].split(",,")
        },
        {
            'name': request.data['certificate_name_3'],
            'center': request.data['certifying_center_3'],
            'obtainment': request.data['certificate_obtainment_date_3'],
            'description': request.data['certificate_description_3'].split(",,")
        }]
    experiences = [
        {
            'company': request.data['experience_company_1'],
            'position': request.data['experience_position_1'],
            'start': request.data['experience_start_1'],
            'end': request.data['experience_end_1'],
            'description': request.data['experience_description_1'].split(",,")
        },
        {
            'company': request.data['experience_company_2'],
            'position': request.data['experience_position_2'],
            'start': request.data['experience_start_2'],
            'end': request.data['experience_end_2'],
            'description': request.data['experience_description_2'].split(",,")
        },
        {
            'company': request.data['experience_company_3'],
            'position': request.data['experience_position_3'],
            'start': request.data['experience_start_3'],
            'end': request.data['experience_end_3'],
            'description': request.data['experience_description_3'].split(",,")
        },
        {
            'company': request.data['experience_company_4'],
            'position': request.data['experience_position_4'],
            'start': request.data['experience_start_4'],
            'end': request.data['experience_end_4'],
            'description': request.data['experience_description_4'].split(",,")
        },
        {
            'company': request.data['experience_company_5'],
            'position': request.data['experience_position_5'],
            'start': request.data['experience_start_5'],
            'end': request.data['experience_end_5'],
            'description': request.data['experience_description_5'].split(",,")
        }]
    htmlobj = render_to_string(
        'resume' + resume_number + '/resume' + resume_number + '.html', {'data': request.data,
                                                                         'achievements': achievements,
                                                                         'skills': skills,
                                                                         'interests': interests,
                                                                         'intern_description': intern_description,
                                                                         'recommendations': recommendations,
                                                                         'projects': projects,
                                                                         'certificates': cerificates,
                                                                         'experiences': experiences,
                                                                         'page2active': page2active})

    htmlObject = HTML(string=htmlobj, base_url=request.build_absolute_uri())
    # cssStyle = CSS(BASE_DIR+'/templates/resume' +
    #                resume_number + '/resume' + resume_number + '.css')
    font_config = FontConfiguration()

    pdfCreatePath = BASE_DIR+'/media/resumes/' + name + \
        '_' + resume_number + '_' + 'Resume.pdf'
    pdfURL = 'media/resumes/' + \
        name + '_' + resume_number + '_' + 'Resume.pdf'

    htmlObject.write_pdf(
        pdfCreatePath,
        # stylesheets=[cssStyle],
        font_config=font_config)

    # response = HttpResponse(pdfURL, content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="ResumeFile.pdf"'

    return pdfURL


def png(request, name, resume_number):
    achievements = request.data['achievements'].split(",,")
    skills = request.data['skills'].split(",,")
    interests = request.data['interests'].split(",,")
    recommendations = request.data['recommendations'].split(",,")
    intern_description = request.data['intern_description'].split(",,")
    experiences = [
        {
            'company': request.data['experience_company_1'],
            'position': request.data['experience_position_1'],
            'start': request.data['experience_start_1'],
            'end': request.data['experience_end_1'],
            'description': request.data['experience_description_1'].split(",,")
        },
        {
            'company': request.data['experience_company_2'],
            'position': request.data['experience_position_2'],
            'start': request.data['experience_start_2'],
            'end': request.data['experience_end_2'],
            'description': request.data['experience_description_2'].split(",,")
        }, ]
    htmlobj = render_to_string(
        'resume' + resume_number + '/resume' + resume_number + '.html', {'data': request.data,
                                                                         'achievements': achievements,
                                                                         'skills': skills,
                                                                         'interests': interests,
                                                                         'intern_description': intern_description,
                                                                         'experiences': experiences,
                                                                         'page2active': 'false'})
    htmlObject = HTML(string=htmlobj, base_url=request.build_absolute_uri())
    # cssStyle = CSS(BASE_DIR+'/templates/resume' +
    #                resume_number + '/resume' + resume_number + '.css')
    font_config = FontConfiguration()
    pngCreatePath = BASE_DIR+'/media/thumbnails/' + name + \
        '_' + resume_number + '_' + 'Resume.png'
    pngURL = 'media/thumbnails/' + \
        name + '_' + resume_number + '_' + 'Resume.png'

    htmlObject.write_png(
        pngCreatePath,
        resolution=50,
        # stylesheets=[cssStyle],
        font_config=font_config)

    return pngURL
