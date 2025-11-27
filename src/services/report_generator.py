from src.utils.config import REPORT
from ..repository.abstract_repository import AbstractNewsRepository


class ReportService:
    """
    Obtêm todos os dados e gera o relatório.

    Responsável por gerar o .txt com todos os dados específicos.
    """

    def __init__(self, repository: AbstractNewsRepository):
        self.repository = repository

    def percent_calculation(self) -> tuple[float, float, float]:
        """
        Calcula a porcentagem de cada status em relação ao total.

        Returns:
            tuple: Tupla com a porcentagem das notícias com status individualmente.
        """
        total = self.repository.qtd_news_register()
        true_news = self.repository.qtd_news_status_each("Verdadeiro")
        false_news = self.repository.qtd_news_status_each("Falso")
        unverified_news = self.repository.qtd_news_status_each("Não Checado")

        if total > 0:  # <- Evita divisão por 0
            percent_true = (true_news / total) * 100
            percent_false = (false_news / total) * 100
            percent_unverified = (unverified_news / total) * 100

        else:
            return 0.0, 0.0, 0.0

        return percent_true, percent_false, percent_unverified

    def report_generation(self) -> None:
        """
        Gera o relatório com todos os dados formatados em uma tabela.
        """
        try:
            # Pega o percentual de cada status
            (percent_true, percent_false, percent_unverified) = (
                self.percent_calculation()
            )

            # Pega o total de notícia de cada status
            true = self.repository.qtd_news_status_each("Verdadeiro")
            false = self.repository.qtd_news_status_each("Falso")
            unverified = self.repository.qtd_news_status_each("Não Checado")

            # Pega o total de notícias gerais
            total = self.repository.qtd_news_register()

            with open(  # <- Cria/Escreve o relatório
                REPORT, "w", encoding="utf-8"
            ) as report:
                report.write(
                    "╔═════════════════════════════════════════════════════════╗\n"
                )
                report.write(
                    "║                        RELATÓRIO                        ║\n"
                )
                report.write(
                    "╠═════════════════════════════════════════════════════════╣\n"
                )
                report.write(f" Total de Notícias Cadastradas: {total}\n")
                report.write("\n")
                report.write(" Distribuição por Status: \n")
                report.write("\n")
                report.write(
                    f"  -> Notícias Verdadeiras: {true} ({percent_true:.1f}%)\n"
                )
                report.write(f"  -> Notícias Falsas: {false} ({percent_false:.1f}%)\n")
                report.write(
                    f"  -> Notícias Não Checadas: {unverified} ({percent_unverified:.1f}%)\n"
                )
                report.write(
                    "╚═════════════════════════════════════════════════════════╝\n"
                )
            print("Relatório gerado com sucesso!")

        except (FileNotFoundError, PermissionError) as e:
            print(f"Erro ao gerar o arquivo do relatório: {e}")
