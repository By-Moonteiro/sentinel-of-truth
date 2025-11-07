class News:
    """
    Representa o objeto da notícia.

    Attributes:
        url (str): Link para a notícia.
        status (str): Estado da notícia (ex: "Verdadeiro", "Falso", "Não Checada").
    """

    def __init__(self, url: str, status: str):
        self.url = url
        self.status = status
