class CSVProxyReport:
    def __init__(self):
        self.headers = []
        self.lines = []

    def append_line(self, line):
        self.lines.append(line)

    def set_headers(self, headers):
        self.headers = headers

    def get_report_view(self):
        csv = ""
        for header in self.headers:
            csv = csv + header

        csv = csv + "\n"

        for line in self.lines:
            csv = csv + ",".join(line)
            csv = csv + "\n"

        return csv
    
    @staticmethod
    def create_report():
        return CSVProxyReport()