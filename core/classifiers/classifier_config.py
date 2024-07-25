from core.classifiers.classifier_enum import ClassifierEnum


classifier_config = [
    {
        "class": ClassifierEnum.VMESS,
        "classifier": lambda proxy: "vmess" in proxy
    },
    {
        "class": ClassifierEnum.SOCKS,
        "classifier": lambda proxy: "vmess" not in proxy
    }
]
