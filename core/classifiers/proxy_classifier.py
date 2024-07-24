import functools

from core.classifiers.classifier_config import classifier_config

def classify_proxies_by_type(proxies):
    classified_proxies = {}
    
    for entry in classifier_config:
        __split_by(entry["classifier"], proxies, classified_proxies, entry["class"])
        
    return classified_proxies

def get_len_classified_proxies_total(classified_proxies):
    return functools.reduce(lambda acc, key: acc + len(classified_proxies[key]), classified_proxies.keys(), 0)

def get_proxies_by_class(classified_proxies, proxy_class):
    return classified_proxies.get(proxy_class)

def get_len_of_proxy_class(classified_proxies, proxy_class):
    return len(classified_proxies.get(proxy_class))

def __split_by(callback, in_array, classified_proxies, key):
    if not classified_proxies.get(key):
        classified_proxies[key] = []
        
    for item in in_array:
        if callback(item): classified_proxies[key].append(item)