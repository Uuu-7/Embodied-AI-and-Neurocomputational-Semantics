"""Rebuild the three candidate S columns and one combined sense audit.

Input: fixed local COW 1.1 and omw-en 2.0 in wn.db (SHA-256
e5e04ab00751fc186f4135826a979b85ed5a690cb49d13a61b47683f94daeda1),
plus Cygnet 2026-05-12 SQLite (SHA-256
12dedc01be32d3735bfde492341b16d1631db02c5df4e0f746f11d9e1a02928f).
Wordnet sources: https://github.com/bond-lab/cow and https://omwn.org/ ;
Cygnet source: https://github.com/omwn/cygnet/releases .

Run with the shared Python environment, --wn-data-dir, --cygnet-db, --repo,
and --output-dir. Copy the three generated CSVs to their contributor folders
and the generated XLSX to data/audit/. The explicit sense locks below are
reviewable decisions; no unlisted synset is assigned an S merely because its
word form was found. Cygnet is only an exact-form coverage cross-check; its
depth is never mixed into the shared English noun graph S.
"""
import argparse
import csv
import os
import sqlite3
from collections import Counter
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--wn-data-dir', required=True)
parser.add_argument('--repo', required=True)
parser.add_argument('--output-dir', required=True)
parser.add_argument('--cygnet-db', required=True)
args = parser.parse_args()
os.environ['WN_DATA_DIR'] = args.wn_data_dir
import wn

ROOT = 'omw-en-00001740-n'
HU = '''
ZH01 cow-00027167-n
ZH02 cow-08521816-n
ZH03 cow-08588294-n
ZH04 cow-13903576-n
ZH05 cow-13903079-n
ZH06 cow-13871452-n
ZH07 cow-08626080-n
ZH08 cow-04059701-n
ZH09 cow-08625462-n
ZH10 cow-08625073-n
ZH11 cow-13827943-n
ZH12 cow-09387222-n
ZH13 cow-05129565-n
ZH14 cow-05084201-n
ZH15 cow-03581531-n
ZH16 cow-13898207-n
ZH17 cow-05075602-n
ZH18 cow-05002822-n
ZH19 cow-05069199-n
ZH20 cow-14420074-n
EN01 omw-en-05085867-n
EN02 omw-en-05129565-n
EN03 omw-en-09379111-n
EN04 omw-en-08512259-n
EN05 omw-en-05085991-n
EN06 omw-en-05089947-n
EN07 omw-en-13828075-n
EN08 omw-en-05077146-n
EN09 omw-en-13887509-n
EN10 omw-en-13873213-n
EN11 omw-en-08624095-n
EN12 omw-en-08588294-n
EN13 omw-en-08613593-n
EN14 omw-en-14419510-n
EN15 omw-en-08560785-n
EN16 omw-en-05079866-n
EN17 omw-en-09387222-n
EN18 omw-en-08641113-n
EN19 omw-en-08521816-n
EN20 omw-en-13871452-n
'''
CHEN = '''
ZH02 cow-13903079-n
ZH18 cow-06196284-n
EN01 omw-en-00027167-n
EN02 omw-en-08512259-n
EN04 omw-en-05085867-n
EN05 omw-en-09387222-n
EN06 omw-en-08521816-n
EN08 omw-en-14419510-n
EN10 omw-en-14002279-n
EN16 omw-en-03839795-n
EN17 omw-en-13935227-n
EN20 omw-en-00282050-n
'''
XIA = '''
ZH03 cow-08588294-n
ZH09 cow-08625462-n
ZH11 cow-08523483-n
ZH12 cow-13903387-n
ZH15 cow-08641113-n
'''

def parse_locks(raw):
    return dict(line.split() for line in raw.strip().splitlines())

LOCKS = {'hujinnan': parse_locks(HU), 'chenfengru': parse_locks(CHEN), 'xiayuqi': parse_locks(XIA)}
english = wn.Wordnet('omw-en:2.0')
chinese = wn.Wordnet('cow:1.1', expand='omw-en:2.0')
repo = Path(args.repo)
outdir = Path(args.output_dir)
outdir.mkdir(parents=True, exist_ok=True)
cygnet=sqlite3.connect(Path(args.cygnet_db).as_uri()+'?mode=ro',uri=True)
cygnet_sql='''select count(distinct sy.rowid) from forms f
 join entries e on e.rowid=f.entry_rowid
 join languages l on l.rowid=e.language_rowid
 join senses se on se.entry_rowid=e.rowid
 join synsets sy on sy.rowid=se.synset_rowid
 where l.code='cmn-Hans' and (f.form=? or f.normalized_form=?)'''
combined=[]
for person in ('chenfengru','hujinnan','xiayuqi'):
    source=repo/'candidates'/person/'candidate_pool_zh20_en20_v01.csv'
    with source.open(encoding='utf-8-sig', newline='') as f:
        reader=csv.DictReader(f)
        fields=reader.fieldnames
        rows=list(reader)
    assert len(rows)==40 and len(LOCKS[person])==sum(r['candidate_id'] in LOCKS[person] for r in rows)
    for row in rows:
        key=row['candidate_id']
        lex=chinese if row['language']=='ZH' else english
        all_synsets=lex.synsets(row['term'])
        noun_synsets=[s for s in all_synsets if s.pos=='n']
        audit={
            'contributor':person,
            **row,
            'database_version':'cow:1.1 + omw-en:2.0' if row['language']=='ZH' else 'omw-en:2.0',
            'native_sense_id':'', 'shared_english_sense_id':'', 'source_gloss_en':'',
            'direct_parent':'', 'root_to_sense_path':'', 'S_status':'', 'S_audit_note':'',
            'cygnet_exact_form_hits':'', 'other_noun_glosses':'',
            '用户审阅（无S词保留请填keep）':'',
        }
        if row['language']=='ZH':
            audit['cygnet_exact_form_hits']=str(cygnet.execute(cygnet_sql,(row['term'],row['term'])).fetchone()[0])
        audit['other_noun_glosses']=' | '.join((
            (next((x.definition() for x in english.synsets(ili=s.ili) if x.pos=='n'),s.definition()) or '')
            for s in noun_synsets[:4]
        ))
        if key in LOCKS[person]:
            sid=LOCKS[person][key]
            native=lex.synset(sid)
            assert native.pos=='n' and any(s.id==sid for s in noun_synsets),(person,key,row['term'],sid)
            matches=[s for s in english.synsets(ili=native.ili) if s.pos=='n']
            assert len(matches)==1,(person,key,sid)
            shared=matches[0]
            paths=[p for p in shared.hypernym_paths() if p and p[-1].id==ROOT]
            assert paths,(person,key,sid)
            path=min(paths,key=lambda p:(len(p),[s.id for s in p]))
            row['S_score']=str(len(path))
            audit['native_sense_id']=native.id
            audit['shared_english_sense_id']=shared.id
            audit['source_gloss_en']=shared.definition()
            audit['direct_parent']=path[0].id
            audit['root_to_sense_path']=' > '.join([s.id for s in reversed(path)]+[shared.id])
            audit['S_status']='verified_shared_noun_depth'
            if person=='hujinnan':
                audit['S_audit_note']='Sense lock from prior Spatial_Relations_estimates.xlsx, independently recomputed from fixed database.'
            elif person=='chenfengru' and key in ('ZH18','EN17','EN20'):
                audit['S_audit_note']='Database depth is valid for the target abstract/metaphorical sense; spatial-scope decision remains separate.'
            else:
                audit['S_audit_note']='Target sense matched; shortest hypernym path to entity; S is edge count.'
        else:
            row['S_score']='NA'
            if person=='xiayuqi' and key in ('ZH05','ZH06'):
                audit['S_status']='spatial_sense_no_shared_english_path'
                audit['S_audit_note']='COW has a Chinese spatial noun synset (cow-8000...), but no omw-en shared ILI/path; do not mix native COW depth with shared graph.'
            elif row['part_of_speech'] not in ('noun','locative_noun'):
                audit['S_status']='target_pos_not_comparable_with_noun_root'
                audit['S_audit_note']='Target is verb, relation, adjective, adposition, idiom, or mixed POS; noun entity-root depth is not comparable.'
            elif not all_synsets:
                audit['S_status']='lexeme_not_found_in_primary_wordnet'
                audit['S_audit_note']='Exact written form absent from fixed COW/OMW wordnet.'
            elif not noun_synsets:
                audit['S_status']='target_noun_sense_not_found'
                audit['S_audit_note']='Written form found, but no matching noun synset in fixed COW/OMW wordnet.'
            else:
                audit['S_status']='target_sense_not_found'
                audit['S_audit_note']='Word/noun found, but none of its mapped English glosses matches the specified target sense closely enough.'
        audit['S_score']=row['S_score']
        combined.append(audit)
    dest=outdir/f'{person}_candidate_pool_zh20_en20_v01.csv'
    with dest.open('w',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=fields,quoting=csv.QUOTE_ALL,lineterminator='\r\n')
        writer.writeheader();writer.writerows(rows)

assert len(combined)==120
assert all(r['S_score']=='NA' or r['root_to_sense_path'].count(' > ')==int(r['S_score']) for r in combined)
columns=['contributor','candidate_id','language','term','pinyin','part_of_speech','target_sense_definition_en',
         'subfamily','image_schema_candidate','channels_to_review','metaphorical_extension_or_scope',
         'individual_lexical_source_verified','C_score','S_score','review_status','database_version',
         'native_sense_id','shared_english_sense_id','source_gloss_en','direct_parent','root_to_sense_path',
         'S_status','S_audit_note','cygnet_exact_form_hits','other_noun_glosses','用户审阅（无S词保留请填keep）']
with (outdir/'candidate_S_combined_v01.csv').open('w',encoding='utf-8-sig',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=columns)
    writer.writeheader();writer.writerows(combined)

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

status_zh={
    'verified_shared_noun_depth':'有效 S',
    'target_pos_not_comparable_with_noun_root':'目标词性与名词根深度不可比较',
    'lexeme_not_found_in_primary_wordnet':'主词网未查到目标词形',
    'target_sense_not_found':'查到词形，但没有对应目标义项',
    'spatial_sense_no_shared_english_path':'查到空间义项，但没有共享英语上位路径',
    'target_noun_sense_not_found':'查到词形，但没有目标名词义项',
}
note_zh={
    'verified_shared_noun_depth':'匹配目标名词义项；S 为至 entity 根的最短 hypernym 边数。',
    'target_pos_not_comparable_with_noun_root':'目标义项不是可比的名词义项；保留 NA，不能借用同形名词的层级。',
    'lexeme_not_found_in_primary_wordnet':'COW／OMW 固定版本未命中该完整词形。',
    'target_sense_not_found':'词形命中，但现有义项与表中的目标定义不符。',
    'spatial_sense_no_shared_english_path':'COW 有中文空间名词义项，但不能映射到本表统一使用的英语 entity 上位图。',
    'target_noun_sense_not_found':'词形命中，但没有可匹配的目标名词义项。',
}
wb=Workbook();ws=wb.active;ws.title='三人S汇总'
headers=['候选者','编号','语言','词','词性','目标义（英文）','S','S核查状态','S来源版本','中文说明',
         '原词网义项ID','共享英语义项ID','英语词网释义','其他名词候选释义','根至义项路径',
         'Cygnet词形命中数（不参与S）','用户审阅：无S词保留请填keep']
ws.append(headers)
for r in combined:
    note=note_zh[r['S_status']]
    if r['contributor']=='chenfengru' and r['candidate_id'] in ('ZH18','EN17','EN20'):
        note+=' 当前目标义偏抽象或隐喻，空间定义域仍需团队确认。'
    ws.append([r['contributor'],r['candidate_id'],r['language'],r['term'],r['part_of_speech'],
               r['target_sense_definition_en'],int(r['S_score']) if r['S_score']!='NA' else 'NA',
               status_zh[r['S_status']],r['database_version'],note,r['native_sense_id'],r['shared_english_sense_id'],
               r['source_gloss_en'],r['other_noun_glosses'] if r['S_score']=='NA' else '',
               r['root_to_sense_path'],int(r['cygnet_exact_form_hits']) if r['cygnet_exact_form_hits'] else '',
               ''])
ws.freeze_panes='G2';ws.auto_filter.ref=f'A1:Q{ws.max_row}'
for cell in ws[1]:
    cell.font=Font(bold=True,color='FFFFFF')
    cell.fill=PatternFill('solid',fgColor='315A70')
    cell.alignment=Alignment(wrap_text=True,vertical='center')
ws.row_dimensions[1].height=38
for row in ws.iter_rows(min_row=2):
    row[5].alignment=Alignment(wrap_text=True,vertical='top')
    row[9].alignment=Alignment(wrap_text=True,vertical='top')
    row[13].alignment=Alignment(wrap_text=True,vertical='top')
    row[16].fill=PatternFill('solid',fgColor='FFF2CC')
    if row[6].value=='NA':
        row[6].fill=PatternFill('solid',fgColor='FCE8E6')
    ws.row_dimensions[row[0].row].height=32
for idx,width in enumerate([16,9,8,18,18,52,9,35,30,65,24,25,55,55,90,26,37],1):
    ws.column_dimensions[get_column_letter(idx)].width=width
dv=DataValidation(type='list',formula1='"keep"',allow_blank=True)
dv.error='只填写 keep，或保持空白';dv.errorTitle='审阅标记';dv.showErrorMessage=True
ws.add_data_validation(dv);dv.add('Q2:Q121')
wb.save(outdir/'candidate_S_combined_v01.xlsx')
for person in LOCKS:
    subset=[r for r in combined if r['contributor']==person]
    print(person,'valid',sum(r['S_score']!='NA' for r in subset),'NA',sum(r['S_score']=='NA' for r in subset))
print('statuses',dict(Counter(r['S_status'] for r in combined)))
