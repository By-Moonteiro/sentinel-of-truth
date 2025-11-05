from src.utils.json_handler import Handler
from src.utils.config import REPORT
from .manager import ManageNews

handler = Handler()
manager = ManageNews()


class ReportNews:
    """
    Obtêm todos os dados do relatório.

    Responsável por achar o total de noticias, a quantidade por status + a porcentagem dos status, e exibir tudo

    Attributes:
        dict: Dicionario com as noticias carregadas
    """

    def __init__(self) -> dict:
        """
        Carrega todas as notícias salvas.
        """
        self.loaded_news = handler.load_date()

    def percent_calculation(self) -> float:
        """
        Calcula a porcentagem de cada status.

        Returns:
            float: Porcentagem das notícias com status verdadeiro/falso/não verificado individualmente.
        """
        try:
            true, false, unverified = self.qtd_news_status_each()
            total = self.qtd_news_register()

            if total == 0:  # Verifica divisões por 0
                return 0, 0, 0

            percent_true = (true / total) * 100
            percent_false = (false / total) * 100
            percent_unverified = (unverified / total) * 100

            return percent_true, percent_false, percent_unverified

        except Exception as e:
            print(f"Erro no calculo de porcentagem: {e}")

            return 0.0, 0.0, 0.0

    def qtd_news_register(self) -> int:
        """
        Obtêm o total de notícias cadastradas.

        Returns:
            total_news(int): Total de notícias.
        """
        try:
            # Total de notícias gerais
            total_news = len(self.loaded_news)

            return total_news

        except Exception as e:
            print(f"Erro ao carregar o total de noticias: {e}")

            return 0

    def qtd_news_status_each(self) -> int:
        """
        Obtêm o total de notícias por status.

        Returns:
            int: Total de notícias verdadeiras, falsas e não checadas.
        """
        try:
            # Pega o total de notícias por status

            true_news = len(manager.search_status_news("Verdadeiro"))
            false_news = len(manager.search_status_news("Falso"))
            unverified_news = len(manager.search_status_news("Não Checado"))

            return true_news, false_news, unverified_news

        except Exception as e:  # <- Verifica o erro
            print(f"Erro ao contar notícias: {e}")

            return 0, 0, 0  # <- Retorna valor seguro

    def report_generation(self) -> None:
        """
        Gera o relatório com todos os dados formatados em uma tabela.
        """

        (  # Pega o percentual de cada status
            percent_true,
            percent_false,
            percent_unverified,
        ) = self.percent_calculation()

        (  # Pega o total de notícia de cada status
            true,
            false,
            unverified,
        ) = self.qtd_news_status_each()

        total = self.qtd_news_register()  # <- Pega o total de notícias gerais

        with open(
            REPORT, "w", encoding="utf-8"
        ) as report:  # <- Cria/Escreve o relatório
            report.write(
                "╔═════════════════════════════════════════════════════════════════════╗\n"
            )
            report.write(
                "║                              RELATÓRIO                              ║\n"
            )
            report.write(
                "╠═════════════════════════════════════════════════════════════════════╣\n"
            )
            report.write(
                f"║ Total de Notícias Cadastradas: {total}                                    ║\n"
            )
            report.write(
                "║                                                                     ║\n"
            )
            report.write(
                "║ Distribuição por Status:                                            ║\n"
            )
            report.write(
                "║                                                                     ║\n"
            )
            report.write(
                f"║  -> Notícias Verdadeiras: {true} ({percent_true:.1f}%)                                  ║\n"
            )
            report.write(
                f"║  -> Notícias Falsas: {false} ({percent_false:.1f}%)                                       ║\n"
            )
            report.write(
                f"║  -> Notícias Não Checadas: {unverified} ({percent_unverified:.1f}%)                                 ║\n"
            )
            report.write(
                "╚═════════════════════════════════════════════════════════════════════╝\n"
            )
