import xml.etree.ElementTree as ET
import re

tree = ET.parse('publications.xml')

template = r"""
<div class="row">
    <div class="col-md-2" align="center">
        <p class="publabel">{0}</p>
    </div>
    <div class="col-md-10">
        <div class="pub">
            <p><i><b>{1}</b></i><br />
                {2} <br />
                {3}<br />
                <a href="{4}"><i class="fa fa-file-pdf-o fa-lg"
                        aria-hidden="true"></i></a> <br />
            </p>
        </div>
    </div>
</div>
<br />
"""

leon = re.compile("^Shuaiwen (Leon )?Song$")
journals = []
conferences = []
root = tree.getroot()

def get_author_list(author_list):
    authors = map(lambda name: '<b>'+name.text+'</b>' if leon.match(name.text) else name.text, author_list)
    return ", ".join(authors)

def parse_journals(node):
    index = node.find('journal').text
    if node.find('volume') != None:
        index += ', vo. ' + node.find('volume').text
    if node.find('number') != None:
        index += ', no. ' + node.find('number').text
    if node.find('pages') != None:
        index += ', pp. ' + node.find('pages').text
    index += ', ' + node.find('year').text

    return template.format(node.find('journal').text, 
    node.find('title').text, 
    get_author_list(node.findall('author')),
    index,
    node.find('ee').text)

def parse_confs(node):
    return template.format(node.find('booktitle').text, 
    node.find('title').text, 
    get_author_list(node.findall('author')),
    '{0}, pp. {1}, {2}'.format(node.find('booktitle').text, node.find('pages').text, node.find('year').text),
    node.find('ee').text)


for child in root:
    if child.tag == 'r':
        publication = child.getchildren()[0]

        if 'publtype' in publication.attrib and publication.attrib['publtype'] == 'informal':
            continue

        if publication.tag == 'article':
            journals.append(parse_journals(publication))
        elif publication.tag == 'inproceedings':
            conferences.append(parse_confs(publication))
        else:
            raise Exception('Unexpected publication tag: ' + publication.tag)

result = []

result.append('<h3>Refereed Journals</h3>')
result += journals
result.append('<h3>Refereed Conferences and Workshops</h3>')
result += conferences

with open ("temp_publication.html", "w") as out:
    out.writelines(result)