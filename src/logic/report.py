from src.utils.config import REPORT
from .manager import ManageNews

manager = ManageNews()


class ReportNews:
    """
    Obtêm todos os dados do relatório.

    Responsável por achar o total de noticias, a quantidade por status + a porcentagem dos status, e exibir tudo

    Attributes:
        dict: Dicionario com as noticias carregadas
    """

    def connection(self) -> dict:
        """
        Carrega a conexão do SQLite.
        """
        return ManageNews._conectar()

    def percent_calculation(self) -> float:
        """
        Calcula a porcentagem de cada status.

        Returns:
            float: Porcentagem das notícias com status verdadeiro/falso/não verificado individualmente.
        """
        total = self.qtd_news_register()
        true_news = self.qtd_news_status_each("Verdadeiro")
        false_news = self.qtd_news_status_each("Falso")
        unverified_news = self.qtd_news_status_each("Não Checado")

        if total > 0: # <- Evita divisão por 0
            
            percent_true = (true_news / total) * 100
            percent_false = (false_news / total) * 100
            percent_unverified = (unverified_news / total) * 100

        else:
            return 0.0, 0.0, 0.0
            
        return percent_true, percent_false, percent_unverified

    def qtd_news_register(self) -> int:
        """
        Obtêm o total de notícias cadastradas.

        Returns:
            total_news(int): Total de notícias.
        """
        with self.connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM noticias")
            
            return cursor.fetchone()[0]


    def qtd_news_status_each(self, status: str) -> int:
        """
        Obtêm o total de notícias por status.

        Returns:
            int: Total de notícias verdadeiras, falsas e não checadas.
        """
        with self.connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT COUNT(*) FROM noticias WHERE status = ?",
                (status,)
            )
            return cursor.fetchone()[0]
        


    def report_generation(self) -> None:
        """
        Gera o relatório com todos os dados formatados em uma tabela.
        """

        # Pega o percentual de cada status
        (percent_true, 
         percent_false, 
         percent_unverified
         ) = self.percent_calculation()   

        # Pega o total de notícia de cada status
        true = self.qtd_news_status_each("Verdadeiro")
        false = self.qtd_news_status_each("Falso")
        unverified = self.qtd_news_status_each("Não Checado")

        # Pega o total de notícias gerais
        total = self.qtd_news_register()
        

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
