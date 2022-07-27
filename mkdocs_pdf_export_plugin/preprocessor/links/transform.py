import os

# from .util import is_doc, normalize_href
from .util import is_doc, normalize_href, abs_asset_href, get_xref_href

# # normalize href to #foo/bar/section:id
# def transform_href(href: str, rel_url: str):
#     head, tail = os.path.split(href)

#     num_hashtags = tail.count('#')

#     if tail.startswith('#'):
#         head, section = os.path.split(rel_url)
#         section = os.path.splitext(section)[0]
#         id = tail[1:]
#     elif num_hashtags is 1:
#         section, ext = tuple(os.path.splitext(tail))
#         id = str.split(ext, '#')[1]
        
#         if head == '..':
#             href = normalize_href(href, rel_url)
#             return '#{}:{}'.format(href, id)

#     elif num_hashtags is 0:
#         if not is_doc(href):
#             return href

#         href = normalize_href(href, rel_url)
#         return '#{}:'.format(href)

#     if head != '':
#         head += '/'

#     return '#{}{}:{}'.format(head, section, id)

# # normalize id to foo/bar/section:id
# def transform_id(id: str, rel_url: str):
#     head, tail = os.path.split(rel_url)
#     section, _ = os.path.splitext(tail)

#     if len(head) > 0:
#         head += '/'

#     return '{}{}:{}'.format(head, section, id)

# normalize href to #foo/bar/section:id
def transform_href(href: str, rel_url: str, base_url: str, output_dir: str):

    # print('---')
    # print('Link in: "{}". baseurl:"{}". rel_url:"{}"'.format(href, base_url, rel_url))
    if href.count('#') is 1:

        path, anchor = href.split('#')

        if path is '':
            # print('Building xref. Path:{}, base_url:{}'.format(path,base_url))
            xref = rel_url.strip('/')
        else:
            xref = get_xref_href(path.strip('/'), base_url, output_dir)

        out = '#{}:{}'.format(xref, anchor)

    else:
        xref = get_xref_href(href, base_url, output_dir)

        out = '#{}:'.format(xref)

    # print('Link out: "{}"'.format(out))
    return out


# normalize id to foo/bar/section:id
def transform_id(id: str, rel_url: str):
    head, tail = os.path.split(rel_url)
    section, _ = os.path.splitext(tail)

    if len(head) > 0:
        head += '/'

    return '{}{}:{}'.format(head, section, id)