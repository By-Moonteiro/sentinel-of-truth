from ..utils.json_handler import Handler
from .manager import ManageNews

class ReportNews:
    def __init__(self):
        self.loaded_news = Handler.load_date()

    def percent_calculation(self):

        true, false, unverified = self.qtd_news_status_each

        percent_true = (true / self.qtd_news_register()) * 100
        percent_false = (false / self.qtd_news_register()) * 100
        percent_unverified = (unverified / self.qtd_news_register()) * 100

        return percent_true, percent_false, percent_unverified

    def qtd_news_register(self):

        # Total de notícias
        total_news = len(self.loaded_news)

        return total_news
    
    def qtd_news_status_each(self):

        # Total de notícias por status
        true_news = len(ManageNews.search_status_news("Verdadeiro"))
        false_news = len(ManageNews.search_status_news("Falso"))
        unverified_news = len(ManageNews.search_status_news("Não Checado"))

        return true_news, false_news, unverified_news

    def report_generation(self):

        percent_true, percent_false, percent_unverified = self.percent_calculation
        true, false, unverified = self.qtd_news_status_each()


        with open(Dados, "w", encoding="utf-8") as report:
            report.write("\n╔══════════════════════════════════════════════════════════════╗")
            report.write("║                           RELATÓRIO                          ║")
            report.write("╠══════════════════════════════════════════════════════════════╣")
            report.write(f"║ Total de Notícias Cadastradas: {self.qtd_news_register()}   ║")
            report.write("║                                                              ║")
            report.write("║ Distribuição por Status:                                     ║")
            report.write("║                                                              ║")
            report.write(f"║  -> Verdadeiras: {true} ({percent_true:.1f}%)               ║")
            report.write(f"║  -> Falsas: {false} ({percent_false:.1f}%)                  ║")
            report.write(f"║  -> Não Checadas: {unverified} ({percent_unverified:.1f}%)  ║")
            report.write("╚══════════════════════════════════════════════════════════════╝")