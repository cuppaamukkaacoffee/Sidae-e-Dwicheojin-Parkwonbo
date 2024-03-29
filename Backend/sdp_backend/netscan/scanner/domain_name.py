import tldextract


def get_domain_name(url):
    url_comps = tldextract.extract(url)
    domain_name = "{}.{}".format(url_comps.domain, url_comps.suffix)
    return domain_name
