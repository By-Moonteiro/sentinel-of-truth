import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils.json_handler import save_date, load_date
from src.utils.config import DADOS

dic = {
    "nome": "Wagner", 
    "idade": 21
}

save_date(dic, DADOS)