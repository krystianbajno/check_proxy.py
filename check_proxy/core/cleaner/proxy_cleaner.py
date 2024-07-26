
import re
from check_proxy.core.classifiers.classifier_enum import ClassifierEnum
from check_proxy.core.classifiers.proxy_classifier import classify_proxy


def clean_proxies(proxy_lines):
    cleaned = []
    for proxy in proxy_lines:
        classification = classify_proxy(proxy)
        
        if classification == ClassifierEnum.VMESS:
            cleaned.append(proxy)
        else:
            pattern = re.compile(r'\d+\.\d+\.\d+\.\d+:\d+')
            matches = pattern.findall(proxy)
            for match in matches:
               cleaned.append(match)
                
    return cleaned
            