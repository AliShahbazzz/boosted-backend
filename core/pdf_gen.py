from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
from django.template.loader import render_to_string
from mysite.settings import BASE_DIR


def pdf(request, name, resume_number):
    page2active = request.data['page2active']
    htmlobj = render_to_string(
        'resume' + resume_number + '/resume' + resume_number + '.html', {'data': request.data, 'page2active': page2active})
    htmlObject = HTML(string=htmlobj)
    cssStyle = CSS(BASE_DIR+'/templates/resume' +
                   resume_number + '/resume' + resume_number + '.css')
    font_config = FontConfiguration()

    pdfCreatePath = BASE_DIR+'/media/resumes/' + name + \
        '_' + resume_number + '_' + 'Resume.pdf'
    pdfURL = 'http://localhost:8000/media/resumes/' + \
        name + '_' + resume_number + '_' + 'Resume.pdf'

    htmlObject.write_pdf(
        pdfCreatePath,
        stylesheets=[cssStyle],
        font_config=font_config)

    return pdfURL


def png(request, name, resume_number):
    htmlobj = render_to_string(
        'resume' + resume_number + '/resume' + resume_number + '.html', {'data': request.data, 'page2active': 'false'})
    htmlObject = HTML(string=htmlobj)
    cssStyle = CSS(BASE_DIR+'/templates/resume' +
                   resume_number + '/resume' + resume_number + '.css')
    font_config = FontConfiguration()
    pngCreatePath = BASE_DIR+'/media/thumbnails/' + name + \
        '_' + resume_number + '_' + 'Resume.png'
    pngURL = 'http://localhost:8000/media/thumbnails/' + \
        name + '_' + resume_number + '_' + 'Resume.png'

    htmlObject.write_png(
        pngCreatePath,
        resolution=60,
        stylesheets=[cssStyle],
        font_config=font_config)

    return pngURL
