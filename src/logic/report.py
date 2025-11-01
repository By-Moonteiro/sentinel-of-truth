from src.utils.json_handler import Handler
from .manager import ManageNews
from src.utils.config import REPORT

class ReportNews:
    def __init__(self):
        self.loaded_news = Handler.load_date()

    def percent_calculation(self):

        try:
            true, false, unverified = self.qtd_news_status_each()
            total = self.qtd_news_register()

            if total == 0: # Verifica divisões por 0
                return 0, 0, 0

            percent_true = (true / total) * 100
            percent_false = (false / total) * 100
            percent_unverified = (unverified / total) * 100

            return percent_true, percent_false, percent_unverified
        
        except Exception as e:

            print(f"Erro no calculo de porcentagem: {e}")

            return 0.0, 0.0, 0.0

    def qtd_news_register(self):

        try:
            # Total de notícias gerais
            total_news = len(self.loaded_news)

            return total_news
        
        except Exception as e:

            print(f"Erro ao carregar o total de noticias: {e}")

            return 0
    
    def qtd_news_status_each(self):

        try:
            # Total de notícias por status
            true_news = len(ManageNews.search_status_news("Verdadeiro"))
            false_news = len(ManageNews.search_status_news("Falso"))
            unverified_news = len(ManageNews.search_status_news("Não Checado"))

            return true_news, false_news, unverified_news
        
        except Exception as e: # <- Verifica o erro

            print(f"Erro ao contar notícias: {e}")

            return 0, 0, 0 # <- Retorna valor seguro

    def report_generation(self):
            
            percent_true, percent_false, percent_unverified = self.percent_calculation()
            true, false, unverified = self.qtd_news_status_each()
            total = self.qtd_news_register()

            with open(REPORT, "w", encoding="utf-8") as report:
                report.write("╔══════════════════════════════════════════════════════════════╗\n")
                report.write("║                           RELATÓRIO                          ║\n")
                report.write("╠══════════════════════════════════════════════════════════════╣\n")
                report.write(f"║ Total de Notícias Cadastradas: {total}                             ║\n")
                report.write("║                                                              ║\n")
                report.write("║ Distribuição por Status:                                     ║\n")
                report.write("║                                                              ║\n")
                report.write(f"║  -> Verdadeiras: {true} ({percent_true:.1f}%)                                    ║\n")
                report.write(f"║  -> Falsas: {false} ({percent_false:.1f}%)                                         ║\n")
                report.write(f"║  -> Não Checadas: {unverified} ({percent_unverified:.1f}%)                                   ║\n")
                report.write("╚══════════════════════════════════════════════════════════════╝\n")