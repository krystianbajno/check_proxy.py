class ProxyChecker:
    UNTAMPERED_PROXY_PATTERN = [
        "<HTML><HEAD><TITLE>Success</TITLE></HEAD><BODY>Success</BODY></HTML>",
        "<HTML><HEAD><TITLE>Success</TITLE></HEAD><BODY>Success</BODY></HTML>\n"
    ]

    INTERROGATOR_URL = "https://captive.apple.com/"
    
    def __init__(self, on_proxy_found, on_check):
        self.on_proxy_found = on_proxy_found
        self.on_check = on_check

    def is_response_not_tampered(self, response):
        tampered = True

        for pattern in self.UNTAMPERED_PROXY_PATTERN:
            print(response.text)
            if pattern == response.text:
                tampered = False

        return not tampered