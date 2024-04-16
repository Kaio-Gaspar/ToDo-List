from openpyxl import Workbook
import os
from datetime import datetime

now = datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

wb = Workbook()

def make_wb():
    if not os.path.exists('logs'):
        os.mkdir('logs')
    wb.save(os.path.join('logs', f'log_{timestamp}.xlsx'))

make_wb()
