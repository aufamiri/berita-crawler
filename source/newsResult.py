class NewsResult:
    def __init__(self, url, title, content, valid=True):
        self.url = url
        self.title = title.strip()
        self.content = content.strip()
        self.valid = valid
