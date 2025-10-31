class News:
    """
    Representa uma notícia.

    Attributes:
        url (str): Link para a notícia.
        status (str): Estado da notícia (ex: "Verdadeiro", "Falso", "Não Checada").
    """

    def __init__(self, url: str, status: str = "Não Checada"):
        self.url = url
        self.status = status

    def to_list(self):
        return [[self.url], [self.status]]
            
