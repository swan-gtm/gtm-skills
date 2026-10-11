# Check before each publish

Read this page before each publish, also after a small edit.

If you have a shell, save this script as `check.py` and run `python3 check.py out.html source.txt` (the source file is optional). It reports sentences that break the writing rules, the read time, and the numbers that are not in the source. Fix each real finding. A flagged technical term, a proper name, or a noun that ends in -ing can stay. The date of today shows as "not found"; that is correct. The script does not check one-digit numbers ("5 of 6"); check those by eye. If you have no shell, make the same checks by eye.

```python
import re,sys,html
src=open(sys.argv[1],encoding='utf-8').read()
if '{{' in src: print('UNFILLED SLOT: "{{" remains')
vis=re.sub(r'<(script|style)[\s\S]*?</\1>|<!--[\s\S]*?-->','',src)
def txt(s): return html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' | ',s)))
BAD=r"\b(utilize|leverage|facilitate|initiate|robust|seamless|synergy|unlock|supercharge|deep dive|circle back|game.?changer|low-hanging|move the needle|very|really|basically|arguably|prior to|in order to|regarding|going forward|touch base|holistic|streamline|empower|cutting-edge|best-in-class|headwinds?|tailwinds?)\b"
NOUN=r'^(marketing|engineering|pricing|onboarding|hiring|training|billing|reporting|planning|messaging|positioning|forecasting|accounting|testing|meeting|funding|staffing|pending|nothing|something|everything|during|king|ring|string|spring)\b'
n=0
T=re.sub(r'"[^"|]*"|“[^”|]*”','""',txt(vis))                              # quotes are exempt
for s in re.split(r'(?<=[.!?])\s+|\s*\|\s*',T):
    s=s.strip(' .|'); q=s; w=q.split()
    if len(w)<4: continue
    f=[]
    if len(w)>25: f.append('%d words (max 25; 20 for instructions)'%len(w))
    if re.search(r"\b\w+(n['’]t|['’]re|['’]ve|['’]ll)\b|\b(it|that|there|what|let|he|she|who)['’]s\b",q,re.I): f.append('contraction')
    m=re.search(BAD,q,re.I)
    if m: f.append('word: '+m.group(0))
    if re.search(r'\b(is|are|was|were|be|been|being)\s+(\w+ly\s+)?\w+(ed|wn|en)\s+by\b',q,re.I): f.append('passive voice')
    if re.match(r'^[A-Za-z]+ing\b',q) and len(w)>5 and not re.match(NOUN,q,re.I): f.append('starts with -ing (ignore if it is a noun)')
    if re.search(r'\b(soon|asap|next (week|month|quarter)|this week|tomorrow|(by|on|next) (mon|tues|wednes|thurs|fri)day|end of (the )?(week|month))\b',q,re.I): f.append('relative date')
    if f: n+=1; print('- %s\n    %s'%(' · '.join(f),s[:140]))
ev=vis.find('data-block="Evidence"'); body=re.sub(r'<details[\s\S]*?</details>','',vis[:ev] if ev>0 else vis)   # folds do not count
cnt=lambda h: len(re.findall(r"[\w$%€£₪][\w$%.,'’/-]*",txt(h)))
parts=re.split(r'<section[^>]*class="panel"',body); top=cnt(parts[0]); tabs=[cnt(x) for x in parts[1:]] or [0]
words=top+max(tabs); mins=-(-words//200)
print('\n%d finding(s). Top %d words + tabs %s. Top + longest tab: %d words. Header must say "%d min full".%s'%(n,top,tabs,words,mins,' MORE THAN 3 MIN: cut or fold.' if words>600 else ''))
nums=sorted(set(x.strip().rstrip('.,') for x in re.findall(r'[$€£]?\d[\d,.]*\s?(?:%|[KMB]\b|x\b)?',txt(vis))),key=len,reverse=True)
print('Numbers to verify against the source (%d): %s'%(len(nums),' · '.join(x.strip() for x in nums if len(x.strip())>1)))
if len(sys.argv)>2:                                                      # optional: python check.py out.html source.txt
    raw=open(sys.argv[2],encoding='utf-8').read().replace(',','')
    miss=[x for x in nums if len(x)>1 and not re.search(r'(?<![\d.])'+re.escape(re.sub(r'[\s,]','',x))+r'(?![\d])',raw)]
    print('NOT FOUND in the source (must be calculated, assumed, or wrong): '+(' · '.join(miss) or 'none'))
```

Then check with your eyes, or with a screenshot at 360px and at desktop width if you can render the page:

1. The top answers "what is it, and what must I do" in ten seconds.
2. Each number matches the source. Each number that the script does not find in the source has the `calculated` or `assumed` tag, or you correct it.
3. Each action has an owner and a date, or the `not in source` tag.
4. No sideways scroll on a phone. The tabs, the folds, and Review mode work.
5. The Draft banner shows, unless the human gave a signature.

Do not say that you made a check which you could not make.
