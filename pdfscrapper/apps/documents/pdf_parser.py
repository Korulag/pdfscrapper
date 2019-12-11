from PyPDF2 import PdfFileReader

ANNOTATIONS_KEY = '/Annots'
URI_KEY = '/URI'
ANK_KEY = '/A'


def extract_hyperlinks(pdf_file):
    hyperlinks = set()
    pdf_reader = PdfFileReader(pdf_file)
    pages = pdf_reader.getNumPages()
    for page in range(pages):
        page_part = pdf_reader.getPage(page)
        page_object = page_part.getObject()
        if ANNOTATIONS_KEY in page_object.keys():
            ann = page_object[ANNOTATIONS_KEY]
            for a in ann:
                u = a.getObject()
                if URI_KEY in u[ANK_KEY].keys():
                    hyperlinks.add(unicode(u[ANK_KEY][URI_KEY]))
    return list(hyperlinks)
