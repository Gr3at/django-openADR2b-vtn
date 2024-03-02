from rest_framework.renderers import TemplateHTMLRenderer


class TemplateXMLRenderer(TemplateHTMLRenderer):
    media_type = "application/xml"
    format = "xml"
