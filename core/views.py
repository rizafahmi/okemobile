from django.shortcuts import render_to_response
from django.template import RequestContext
import xml.etree.ElementTree as etree
from django.conf import settings
import os.path

def get_breaking(xml_url):
    import urllib2
    f = urllib2.urlopen(xml_url)
    #f = open(xml_url)
    #xml = f.read()

    #tree = etree.parse(xml)
    tree = etree.fromstring(f.read())

    root_xml = tree.getroot()
    # print root_xml[1]
    xml_dict = []
    for x in root_xml[1].findall('news')[:settings.NUM_OF_BREAKING]:

        # http://services.okezone.com/raw/detail/2011/11/18/195/531253
        url = x[6].text[31:]
        #print url

        xml_dict.append({
            'channel_id': x[0].attrib['id'],
            'date_published': x[1].text,
            'title': x[2].text,
            'subtitle': x[3].text,
            'summary': x[4].text,
            'thumbnail': x[5].text,
            'xml_url': x[6].text,
            'url': url
        })


    return xml_dict

def get_headline(xml_url):
    f = open(xml_url)

    tree = etree.parse(f)

    root_xml = tree.getroot()
    # print root_xml[1]
    xml_dict = []
    for x in root_xml[1].findall('news')[:settings.NUM_OF_HEADLINE]:
        url = x[6].text[31:]
        xml_dict.append({
            'channel_id': x[0].attrib['id'],
            'date_published': x[1].text,
            'title': x[2].text,
            'subtitle': x[3].text,
            'summary': x[4].text,
            'thumbnail': x[5].text,
            'xml_url': x[6].text,
            'url': url,
        })


    return xml_dict

def get_popular(xml_url):
    f = open(xml_url)

    tree = etree.parse(f)

    root_xml = tree.getroot()
    # print root_xml[1]
    xml_dict = []
    for x in root_xml[0].findall('news')[:settings.NUM_OF_POPULAR]:
        url = x[4].text[31:]
        xml_dict.append({
            'channel_id': x[0].attrib['id'],
            'date_published': x[1].text,
            'title': x[2].text,
            'hits': x[3].text,
            'xml_url': x[4].text,
            'url': url,
        })


    return xml_dict

def get_detail(xml_url):
    f = open(xml_url)

    tree = etree.parse(f)

    root_xml = tree.getroot()

    xml_dict = {}
    for x in root_xml[1].findall('news'):

        xml_dict = {
            'channel_id': x[0].attrib['id'],
            'date_published': x[1].text,
            'title': x[5].text,
            'subtitle': x[3].text,
            'summary': x[7].text,
            'thumbnail': x[11].text,
            'caption': x[12].text,
            'weburl': x[9].text,
            'content': x[8].text,
            'reporter': x[2].text,
            'institution': x[4].text,
        }


    return xml_dict

def home(request):

    data = {}
    data['breaking'] = get_breaking(settings.XML_URL + 'breaking')
    data['headline'] = get_headline(settings.XML_URL + 'headline')
    data['popular'] = get_popular(settings.XML_URL + 'popular')

    return render_to_response('core/index.html', data,
            context_instance = RequestContext(request))

def kanal(request, kanal):

    data = {}
    data['breaking'] = get_breaking(settings.XML_URL + '/breaking.xml')
    data['headline'] = get_headline(settings.XML_URL + '/breaking.xml')
    data['popular'] = get_popular(settings.XML_URL + '/popular.xml')
    data['kanal'] = kanal

    return render_to_response('core/kanal.html', data,
            context_instance = RequestContext(request))

def detail(request, url):

    data = {}
    data['detail'] = get_detail(settings.XML_URL + '/detail.xml')
    #print data
    return render_to_response('core/detail.html', data,
            context_instance = RequestContext(request))