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
        csv = csv + ",".join(self.headers)
        
        csv = csv + "\n"

        for line in self.lines:
            csv = csv + ",".join(line)
            csv = csv + "\n"

        return csv
    
    @staticmethod
    def create_report():
        return CSVProxyReport()