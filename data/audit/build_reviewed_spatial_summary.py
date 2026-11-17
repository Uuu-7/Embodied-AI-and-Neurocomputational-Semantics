"""Filter the reviewed 120-row S audit and merge exact duplicate words.

Keep rows with numeric S or an explicit user `keep` mark. Duplicates use the
same (language, stripped term); this version requires their mapped English
sense and S to agree. Prefer Hu's existing locked noun record as representative
when identical nominations occur. Source audit is never changed by this script.
"""
import argparse
from collections import Counter, defaultdict
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

parser=argparse.ArgumentParser()
parser.add_argument('--source',required=True)
parser.add_argument('--output',required=True)
args=parser.parse_args()
source=Path(args.source)
output=Path(args.output)
wb=load_workbook(source,read_only=True,data_only=True)
assert wb.sheetnames==['Three-Person S Audit']
sheet=wb.active
headers=[c.value for c in sheet[1]]
assert headers==['Contributor','Candidate ID','Language','Term','Part of speech',
                'Target sense definition (EN)','S depth','S audit status','S source version',
                'Audit note','Native sense ID','Shared English sense ID','English wordnet gloss',
                'Other noun candidate glosses','Root-to-sense path',
                'Cygnet exact-form hits (not S)','User review: keep if S missing']
rows=list(sheet.values)[1:]
assert len(rows)==120
assert all(str(r[16]).strip().lower() in ('','keep','none') for r in rows)
marked=[r for r in rows if str(r[16]).strip().lower()=='keep']
assert all(r[6]=='NA' for r in marked)
selected=[r for r in rows if r[6]!='NA' or str(r[16]).strip().lower()=='keep']
groups=defaultdict(list)
for r in selected:
    groups[(r[2],r[3].strip())].append(r)

priority={'hujinnan':0,'chenfengru':1,'xiayuqi':2}
result=[]
for (language,term),group in groups.items():
    if len(group)>1:
        assert len({(r[6],r[11]) for r in group})==1,(language,term,'conflicting senses or S')
    representative=min(group,key=lambda r:priority[r[0]])
    status='User keep (S missing)' if representative[6]=='NA' else 'Validated S'
    provenance='; '.join(f'{r[0]}:{r[1]}' for r in group)
    result.append((language,term,representative,status,provenance,len(group)))
result.sort(key=lambda x:(0 if x[0]=='ZH' else 1,0 if x[3]=='Validated S' else 1,
                          priority[x[2][0]],int(x[2][1][2:])))

out=Workbook();ws=out.active;ws.title='Reviewed Unique 58'
ws.append(['Index','Language','Term','Part of speech','Target sense definition (EN)',
           'S depth','S-stage retention basis','S audit note','Representative contributor',
           'Original candidate ID','Nomination sources','Merged nomination count',
           'Native sense ID','Shared English sense ID','English wordnet gloss','Root-to-sense path'])
for i,(language,term,r,status,provenance,count) in enumerate(result,1):
    ws.append([i,language,term,r[4],r[5],r[6],status,r[9],r[0],r[1],provenance,
               count,r[10],r[11],r[12],r[14]])
ws.freeze_panes='F2';ws.auto_filter.ref=f'A1:P{ws.max_row}'
for cell in ws[1]:
    cell.font=Font(bold=True,color='FFFFFF')
    cell.fill=PatternFill('solid',fgColor='315A70')
    cell.alignment=Alignment(wrap_text=True,vertical='center')
ws.row_dimensions[1].height=34
for row in ws.iter_rows(min_row=2):
    if row[5].value=='NA':
        row[5].fill=PatternFill('solid',fgColor='FCE8E6')
        row[6].fill=PatternFill('solid',fgColor='FFF2CC')
    row[4].alignment=Alignment(wrap_text=True,vertical='top')
    row[7].alignment=Alignment(wrap_text=True,vertical='top')
    ws.row_dimensions[row[0].row].height=32
for col,width in enumerate([9,9,18,18,55,9,25,65,18,14,42,15,25,27,60,100],1):
    ws.column_dimensions[get_column_letter(col)].width=width
output.parent.mkdir(parents=True,exist_ok=True)
out.save(output)
print('reviewed_keep',len(marked),'selected_before_dedup',len(selected),
      'duplicate_removed',len(selected)-len(result),'result',len(result),
      'language',dict(Counter(x[0] for x in result)),
      'S',dict(Counter(x[3] for x in result)))
