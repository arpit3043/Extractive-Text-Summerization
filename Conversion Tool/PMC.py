import sys
import argparse
import requests
import lxml.html

from urllib.parse import quote as urlquote

NCBI_BASE_URL = 'https://www.ncbi.nlm.nih.gov'
NCBI_SEARCH_PATH = 'pubmed/?term='
NCBI_DEFAULT_SEARCH_TERM = 'notch'
NCBI_SEARCH_RESULT_TITLE_A_XPATH = '//p[@class="title"]/a'

if __name__ == '__main__':

    # argparse tutorial: https://docs.python.org/3/howto/argparse.html
    parser = argparse.ArgumentParser(
        description='Search PubMed ({}) for given term(s) and return a list '
                    'of URLs and titles from the first page of search '
                    'results'.format(NCBI_BASE_URL))

    # accept a list of terms; if none specified, use 'notch' as default
    parser.add_argument(
        'term', nargs='*', metavar='TERM', default=[NCBI_DEFAULT_SEARCH_TERM],
        help="The search term; multiple are allowed [default: '{}']"
             .format(NCBI_DEFAULT_SEARCH_TERM)
    )

    # store input arguments in 'args' object; arguments are accessed as
    # properties on this object, e.g., 'args.terms'
    args = parser.parse_args()

    # take all terms and join them with spaces, then URL-encode that string
    terms = urlquote(' '.join(args.term))
    query_url = NCBI_BASE_URL + '/' + NCBI_SEARCH_PATH + 'Femur Fracture'

    with requests.Session() as s:
        response = s.get(query_url)
        assert response.ok

        # suppress this in the output by redirecting stderr to /dev/null,
        # e.g., './pm-article-finder.py notch 2>/dev/null'
        print('# ' + query_url, file=sys.stderr)

        # see: https://stackoverflow.com/a/15622069
        html = lxml.html.fromstring(response.content)
        anchors = html.xpath(NCBI_SEARCH_RESULT_TITLE_A_XPATH)

        # for each <a> tag found within <p class="title">, print the document
        # URL, a tab, then the text content of the <a> (the document title)
        for anchor in anchors:
            print(NCBI_BASE_URL + anchor.attrib['href'], end='')  # no EOL
            # text_content() method strips all inner tags (like <b></b>)
            print("\t", anchor.text_content())
