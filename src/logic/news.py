class News:
    """
    Cria o objeto da notícia.

    Attributes:
        url(str): Url da notícia
        status(str): Status da notícia
    """    
    def __init__(self, url: str, status: str) -> None:
        """Atributos da notícia"""
        self.url = url
        self.status = status

