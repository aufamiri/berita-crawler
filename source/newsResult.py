class NewsResult:
    def __init__(self, url, title, content, valid=True):
        self.url = url
        self.title = title
        self.content = content
        self.valid = valid
