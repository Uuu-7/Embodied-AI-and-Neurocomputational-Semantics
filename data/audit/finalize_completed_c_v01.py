"""Restore four moved columns and publish English C ratings and summaries.

Input is the user's completed workbook preserved at commit 0ebba51. The
original values are checked against the 58-word S result before transformation.
"""
import argparse
from collections import Counter
from pathlib import Path
from statistics import mean

from openpyxl import Workbook, load_workbook
from openpyxl.comments import Comment
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

p=argparse.ArgumentParser()
p.add_argument('--completed',required=True)
p.add_argument('--source-58',required=True)
p.add_argument('--output',required=True)
a=p.parse_args()
raw=load_workbook(a.completed,data_only=False)
ws=raw.active
original=list(ws.values)
assert len(original)>=59
assert [ws.cell(1,c).value for c in (24,25,26,27)]==['词性','目标义（英文）','S','保留依据']
assert all(ws.cell(1,c).value is None for c in (4,5,6,7,23))
source=list(load_workbook(a.source_58,read_only=True,data_only=True).active.values)
assert len(source)==59

decisions={'keep':'keep','有相似':'Similar alternative','没位置了':'No remaining slot',
           '改为delete':'Delete (revised)',None:None}
retention={'有效 S':'Validated S','用户标记 keep（S 缺失）':'User keep (S missing)'}
records=[]
for rownum in range(2,60):
    r=[ws.cell(rownum,col).value for col in range(1,28)]
    src=source[rownum-1]
    assert (r[0],r[1],r[2],r[23],r[24],r[25])==tuple(src[:6]),rownum
    scores=r[7:14]
    assert len(scores)==7 and all(type(v) is int and 0<=v<=2 for v in scores),rownum
    assert r[16] in decisions,(rownum,r[16])
    assert r[26] in retention
    assert retention[r[26]]==src[6]
    assert {v.strip() for v in r[20].replace('；',';').split(';')}=={v.strip() for v in src[10].split(';')}
    assert r[21]==src[13]
    records.append(dict(index=r[0],language=r[1],term=r[2],pos=r[23],definition=r[24],
                        S=r[25],retention=retention[r[26]],scores=scores,decision=decisions[r[16]],
                        original_decision=r[16],evidence=r[17],confidence=r[18],rater=r[19],
                        nominations=src[10],english_sense=r[21],c_mean=sum(scores)/7,
                        c_unit=sum(scores)/14))
assert len(records)==58
assert Counter(r['decision'] for r in records)=={'keep':40,'Similar alternative':10,
                                                'No remaining slot':1,'Delete (revised)':1,None:6}
selected=[r for r in records if r['decision']=='keep']
assert len(selected)==40 and Counter(r['language'] for r in selected)=={'ZH':20,'EN':20}

book=Workbook();main=book.active;main.title='C Ratings 58'
header=['Index','Language','Term','Part of speech','Target sense definition (EN)','S depth',
        'S-stage retention basis','Visual','Auditory','Tactile','Motor','Proprioceptive',
        'Interoceptive','Social','C raw mean','C unit','Selection decision',
        'Rating evidence or source','Confidence','Rater','Nomination sources',
        'Shared English sense ID']
main.append(header)
rubric=('Score the specified target sense on each channel: 0 = the channel does not '
       'contribute; 1 = it can directly instantiate the sense but is context-dependent '
       'or secondary; 2 = it is a characteristic direct way to identify or enact the sense.')
for col in range(8,15):
    main.cell(1,col).comment=Comment(rubric,'Project scoring guide')
main['O1'].comment=Comment('Mean of the seven channel scores when all seven are filled.','Method')
main['P1'].comment=Comment('Sum of the seven channel scores divided by 14.','Method')
for i,r in enumerate(records,2):
    main.append([r['index'],r['language'],r['term'],r['pos'],r['definition'],r['S'],
                 r['retention'],*r['scores'],f'=IF(COUNT(H{i}:N{i})=7,AVERAGE(H{i}:N{i}),"")',
                 f'=IF(COUNT(H{i}:N{i})=7,SUM(H{i}:N{i})/14,"")',r['decision'],
                 r['evidence'],r['confidence'],r['rater'],r['nominations'],r['english_sense']])
    if r['S']=='NA':main.cell(i,6).fill=PatternFill('solid',fgColor='FCE8E6')
    if r['decision']=='keep':main.cell(i,17).fill=PatternFill('solid',fgColor='D9EAD3')
    main.row_dimensions[i].height=32
main.freeze_panes='H2';main.auto_filter.ref='A1:V59';main.sheet_view.showGridLines=False
score_dv=DataValidation(type='list',formula1='"0,1,2"',allow_blank=True)
main.add_data_validation(score_dv);score_dv.add('H2:N59')
confidence_dv=DataValidation(type='list',formula1='"high,medium,low"',allow_blank=True)
main.add_data_validation(confidence_dv);confidence_dv.add('S2:S59')
for col,width in enumerate([9,10,18,19,58,11,25,12,12,12,12,19,19,12,15,14,24,45,16,16,45,27],1):
    main.column_dimensions[get_column_letter(col)].width=width
for row in main.iter_rows(min_row=2):
    row[4].alignment=Alignment(wrap_text=True,vertical='top')
    row[16].alignment=Alignment(wrap_text=True,vertical='top')

summary=book.create_sheet('Evaluation Summary')
summary.append(['Metric','Value','Interpretation'])
metrics=[
    ('Candidates rated',len(records),'All 58 retained after the S-stage screen were rated on all seven channels.'),
    ('Complete seven-channel profiles',sum(all(type(v) is int for v in r['scores']) for r in records),''),
    ('Marked keep',len(selected),'User selection; 20 Chinese and 20 English.'),
    ('Keep: Chinese',sum(r['language']=='ZH' for r in selected),''),
    ('Keep: English',sum(r['language']=='EN' for r in selected),''),
    ('Similar alternative',sum(r['decision']=='Similar alternative' for r in records),'Not marked keep.'),
    ('No remaining slot',sum(r['decision']=='No remaining slot' for r in records),'Not marked keep.'),
    ('Delete (revised)',sum(r['decision']=='Delete (revised)' for r in records),'Changed from an earlier S-stage keep.'),
    ('No decision mark',sum(r['decision'] is None for r in records),'Unmarked; not counted among the selected 40.'),
    ('Selected 40 with numeric S',sum(r['S']!='NA' for r in selected),''),
    ('Selected 40 with S = NA',sum(r['S']=='NA' for r in selected),'Explicitly retained at the S stage.'),
    ('All 58: mean C raw',mean(r['c_mean'] for r in records),'Mean of seven 0–2 scores per term, then mean across terms.'),
    ('Selected 40: mean C raw',mean(r['c_mean'] for r in selected),''),
    ('Selected 40: min C raw',min(r['c_mean'] for r in selected),''),
    ('Selected 40: max C raw',max(r['c_mean'] for r in selected),''),
    ('Selected 40: mean C unit',mean(r['c_unit'] for r in selected),'C unit = sum of seven scores / 14.'),
]
for metric in metrics:summary.append(metric)
summary.append([])
summary.append(['Channel','All 58 mean','Selected 40 mean','Selected 40 score 0','Selected 40 score 1','Selected 40 score 2'])
channels=['Visual','Auditory','Tactile','Motor','Proprioceptive','Interoceptive','Social']
for col,label in enumerate(channels):
    counts=Counter(r['scores'][col] for r in selected)
    summary.append([label,mean(r['scores'][col] for r in records),
                    mean(r['scores'][col] for r in selected),counts[0],counts[1],counts[2]])
summary.append([])
summary.append(['Interpretation','These ratings and selection marks were completed by one user; no independent consensus or C × S quadrant analysis is claimed.'])
summary.freeze_panes='B2';summary.column_dimensions['A'].width=34
summary.column_dimensions['B'].width=22;summary.column_dimensions['C'].width=74
for col in ('D','E','F'):summary.column_dimensions[col].width=23
for row in summary:
    for cell in row:cell.alignment=Alignment(wrap_text=True,vertical='top')

chosen=book.create_sheet('User Selected 40')
chosen.append(['Language','Term','Part of speech','Target sense definition (EN)','S depth',
               'Visual','Auditory','Tactile','Motor','Proprioceptive','Interoceptive','Social',
               'C raw mean','C unit','Selection decision','Nomination sources','Shared English sense ID'])
for r in selected:
    chosen.append([r['language'],r['term'],r['pos'],r['definition'],r['S'],*r['scores'],
                   r['c_mean'],r['c_unit'],r['decision'],r['nominations'],r['english_sense']])
chosen.freeze_panes='F2';chosen.auto_filter.ref='A1:Q41';chosen.sheet_view.showGridLines=False
for col,width in enumerate([10,18,20,58,11,12,12,12,12,19,19,12,17,14,22,44,27],1):
    chosen.column_dimensions[get_column_letter(col)].width=width
for sheet in book:
    for cell in sheet[1]:
        cell.font=Font(bold=True,color='FFFFFF')
        cell.fill=PatternFill('solid',fgColor='315A70')
        cell.alignment=Alignment(wrap_text=True,vertical='center')
    sheet.row_dimensions[1].height=38
book.calculation.fullCalcOnLoad=True;book.calculation.forceFullCalc=True
output=Path(a.output);output.parent.mkdir(parents=True,exist_ok=True)
book.save(output)
print('rated',len(records),'keep',len(selected),'selected_language',dict(Counter(r['language'] for r in selected)),
      'selected_S_NA',sum(r['S']=='NA' for r in selected),'mean_C_raw_selected',mean(r['c_mean'] for r in selected))
