"""Make a one-sheet horizontal C rating form from the reviewed 58-word list.

Only source metadata and formulas are populated. All seven rating cells,
provenance, confidence, and rater cells remain blank for human annotation.
"""
import argparse
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.comments import Comment
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

parser=argparse.ArgumentParser()
parser.add_argument('--source',required=True)
parser.add_argument('--output',required=True)
args=parser.parse_args()
source=Path(args.source)
output=Path(args.output)
original=load_workbook(source,read_only=True,data_only=True)
assert original.sheetnames==['筛选去重结果']
rows=list(original.active.values)
expected=['序号','语言','词汇','词性','目标义（英文）','S','保留依据','S核查说明',
          '代表候选者','原候选ID','同词提名来源','合并提名数','原词网义项ID',
          '共享英语义项ID','英语词网释义','根至义项路径']
assert list(rows[0])==expected
assert len(rows)==59 and len({(r[1],r[2]) for r in rows[1:]})==58

book=Workbook();sheet=book.active;sheet.title='58词C横向评分'
headers=['序号','语言','词汇','词性','目标义（英文）','S','保留依据',
         '视觉 visual','听觉 auditory','触觉 tactile','动作 motor',
         '本体感觉 proprioceptive','内感受 interoceptive','社会 social',
         'C_raw_mean','C_unit','评分依据／来源','置信度','评分者','同词提名来源','共享英语义项ID']
sheet.append(headers)
for i,record in enumerate(rows[1:],2):
    sheet.append([record[0],record[1],record[2],record[3],record[4],record[5],record[6],
                  None,None,None,None,None,None,None,
                  f'=IF(COUNT(H{i}:N{i})=7,AVERAGE(H{i}:N{i}),"")',
                  f'=IF(COUNT(H{i}:N{i})=7,SUM(H{i}:N{i})/14,"")',
                  None,None,None,record[10],record[13]])
sheet.freeze_panes='H2'
sheet.auto_filter.ref=f'A1:U{sheet.max_row}'
sheet.sheet_view.showGridLines=False
for cell in sheet[1]:
    cell.font=Font(bold=True,color='FFFFFF')
    cell.fill=PatternFill('solid',fgColor='315A70')
    cell.alignment=Alignment(wrap_text=True,vertical='center')
sheet.row_dimensions[1].height=42
rubric=('给指定的目标义项逐维评分：0＝该通道不参与目标义；'
       '1＝该通道可直接体现目标义，但依赖语境或处于次要位置；'
       '2＝该通道是识别或实现目标义的典型直接方式。'
       '请填写评分依据／来源；不要为了提高多样性调整分数。')
for col in range(8,15):
    sheet.cell(1,col).comment=Comment(rubric,'项目评分规则')
sheet['O1'].comment=Comment('七维均填 0–2 后自动显示：七维总和 ÷ 7。未评完保持空白。','项目评分规则')
sheet['P1'].comment=Comment('七维均填 0–2 后自动显示：七维总和 ÷ 14。未评完保持空白。','项目评分规则')
score_validation=DataValidation(type='list',formula1='"0,1,2"',allow_blank=True)
score_validation.error='只能填 0、1 或 2';score_validation.errorTitle='C 评分';score_validation.showErrorMessage=True
sheet.add_data_validation(score_validation);score_validation.add(f'H2:N{sheet.max_row}')
confidence_validation=DataValidation(type='list',formula1='"high,medium,low"',allow_blank=True)
sheet.add_data_validation(confidence_validation);confidence_validation.add(f'R2:R{sheet.max_row}')
for row in sheet.iter_rows(min_row=2):
    row[4].alignment=Alignment(wrap_text=True,vertical='top')
    row[16].alignment=Alignment(wrap_text=True,vertical='top')
    for col in range(7,14):
        row[col].fill=PatternFill('solid',fgColor='FFF2CC')
        row[col].alignment=Alignment(horizontal='center',vertical='center')
    if row[5].value=='NA':
        row[5].fill=PatternFill('solid',fgColor='FCE8E6')
    sheet.row_dimensions[row[0].row].height=34
for col,width in enumerate([9,9,18,18,55,9,26,15,15,15,15,22,21,15,17,16,45,15,17,42,26],1):
    sheet.column_dimensions[get_column_letter(col)].width=width
book.calculation.fullCalcOnLoad=True
book.calculation.forceFullCalc=True
output.parent.mkdir(parents=True,exist_ok=True)
book.save(output)
print('rows',sheet.max_row-1,'channels',headers[7:14],'scored_cells',
      sum(sheet.cell(r,c).value is not None for r in range(2,sheet.max_row+1) for c in range(8,15)))
