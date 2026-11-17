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
assert original.sheetnames==['Reviewed Unique 58']
rows=list(original.active.values)
expected=['Index','Language','Term','Part of speech','Target sense definition (EN)',
          'S depth','S-stage retention basis','S audit note','Representative contributor',
          'Original candidate ID','Nomination sources','Merged nomination count',
          'Native sense ID','Shared English sense ID','English wordnet gloss','Root-to-sense path']
assert list(rows[0])==expected
assert len(rows)==59 and len({(r[1],r[2]) for r in rows[1:]})==58

book=Workbook();sheet=book.active;sheet.title='C Rating Template 58'
headers=['Index','Language','Term','Part of speech','Target sense definition (EN)',
         'S depth','S-stage retention basis','Visual','Auditory','Tactile','Motor',
         'Proprioceptive','Interoceptive','Social','C raw mean','C unit',
         'Rating evidence or source','Confidence','Rater','Nomination sources','Shared English sense ID']
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
rubric=('Rate the specified target sense: 0 = the channel does not contribute; '
       '1 = it can directly instantiate the sense but is context-dependent or secondary; '
       '2 = it is a characteristic direct way to identify or enact the sense. '
       'Record evidence and do not alter scores to force diversity.')
for col in range(8,15):
    sheet.cell(1,col).comment=Comment(rubric,'Project scoring guide')
sheet['O1'].comment=Comment('After all seven scores are filled: sum of scores / 7.','Method')
sheet['P1'].comment=Comment('After all seven scores are filled: sum of scores / 14.','Method')
score_validation=DataValidation(type='list',formula1='"0,1,2"',allow_blank=True)
score_validation.error='Enter 0, 1, or 2.';score_validation.errorTitle='C rating';score_validation.showErrorMessage=True
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
