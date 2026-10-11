# Page skeleton and build rules

Read this page when you build the first version. Copy the skeleton, then fill it.

## Build rules

1. **Surface.** Publish as a hosted interactive artifact if the host has one. If not, write one self-contained `.html` file. Do not deliver a Markdown dump or a long chat message. One file: the markup, the styles, and the script together. No external requests except a font or a chart library from a common CDN, and only if you need it.
2. **Start from the skeleton below.** Copy it, then fill it. Keep the fenced blocks (`<!-- TOP -->`, `<!-- BODY -->`, `<!-- EVIDENCE -->`) so that later edits are small patches.
3. **Brand.** If the artifact goes to a person outside the sender's company, and a brand or design system skill is available for that company, apply its colors, fonts, and logo (set `--accent` and `--font`, and put the logo before the banner). For internal work, use the neutral tokens unless the human asks for the brand. If the brand accent is red or green, keep it for the accent only and keep the status colors different from it. Do not redesign the layout unless the human asks.
4. **Phone first.** The recipient opens this from a chat tool or email, frequently on a phone. It must work at a width of 360px with no sideways scroll. Wide tables scroll inside their own container.
5. **Light and dark.** Keep the two themes of the skeleton.
6. **Density.** One screen for layer 1. No block of visible text longer than three sentences in layers 1 and 2; longer content goes into a fold or layer 3.
7. **Charts.** One question for each chart, and the title states the answer ("SMB churn doubled in the quarter"). Label the axes and the units. Use inline SVG or simple CSS bars for small data. A table with fewer than four numbers stays a table or tiles.
8. **Color has meaning.** Green/yellow/red only for status, and always with a word label too. One accent color for the thing that matters most.
9. **Read time.** Show an honest read time in the header ("10 sec top · N min full"). One recipient reads the top and one tab. Thus the number is the words of the top plus the longest tab, without the folds, divided by 200, rounded up. The check script gives this number. If it is more than three minutes, cut or fold.
10. **State.** Keep Review-mode state and check box state in memory. Wrap any `localStorage` call in try/catch.
11. **Print and forward.** The skeleton prints all tabs, opens the folds, and hides the controls. Keep that, because recipients forward a PDF.
12. **Versions.** Show the version in the header meta (V1, V2). Increase it on each publish. The feedback marker reads the version from the header.

## Skeleton

```html
<!doctype html><html lang="en" dir="ltr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{{SHORT_TITLE}}</title>
<style>
:root{--bg:#f7f6f3;--card:#fff;--ink:#17171a;--mute:#6b6b76;--line:#e4e2dc;--accent:#2b50ff;--ok:#16794c;--warn:#a15c00;--bad:#b3261e;--r:14px;--font:system-ui,-apple-system,Segoe UI,Inter,sans-serif}
@media(prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#121214;--card:#1c1c20;--ink:#f1f1f3;--mute:#a0a0ac;--line:#2e2e35;--accent:#8ea2ff;--ok:#5fd39b;--warn:#f0b35a;--bad:#ff8a80}}
:root[data-theme=dark]{--bg:#121214;--card:#1c1c20;--ink:#f1f1f3;--mute:#a0a0ac;--line:#2e2e35;--accent:#8ea2ff;--ok:#5fd39b;--warn:#f0b35a;--bad:#ff8a80}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.5 var(--font)}
main{max-width:920px;margin:0 auto;padding:16px}
.banner{font-size:13px;padding:6px 12px;border-radius:99px;display:inline-block;border:1px solid var(--warn);color:var(--warn)}
.banner.signed{border-color:var(--ok);color:var(--ok)}
.meta{color:var(--mute);font-size:13px;margin:8px 0 16px}
.top{background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:20px}
.verdict{font-size:clamp(22px,4.5vw,32px);line-height:1.2;font-weight:700;margin:0 0 12px;text-wrap:balance}
.ask{border-inline-start:4px solid var(--accent);padding:8px 12px;margin:12px 0;font-weight:600}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin-top:14px}
.tile{border:1px solid var(--line);border-radius:10px;padding:12px}.tile b{display:block;font-size:26px;font-variant-numeric:tabular-nums}.tile span{font-size:13px;color:var(--mute)}
.tabs{display:flex;gap:6px;margin:20px 0 10px;flex-wrap:wrap;align-items:center}body.review .tabs::after{content:attr(data-hint);font-size:12px;color:var(--mute)}.tabs button{border:1px solid var(--line);background:none;color:var(--ink);padding:8px 14px;border-radius:99px;font:inherit;cursor:pointer;white-space:nowrap}.tabs button[aria-selected=true]{background:var(--ink);color:var(--bg)}
.block{background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:16px;margin:10px 0;position:relative}
.block h3{margin:0 0 8px;font-size:17px}
.tag{font-size:11px;text-transform:uppercase;letter-spacing:.04em;border:1px solid var(--line);border-radius:6px;padding:1px 6px;color:var(--mute);white-space:nowrap}
.tag.ok{color:var(--ok);border-color:var(--ok)}.tag.warn{color:var(--warn);border-color:var(--warn)}.tag.bad{color:var(--bad);border-color:var(--bad)}
.scroll{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:14px}th,td{text-align:start;padding:8px;border-bottom:1px solid var(--line);vertical-align:top}th{color:var(--mute);font-weight:600;white-space:nowrap}table.sort th{cursor:pointer}table.sort th::after{content:' ↕';opacity:.5}.scroll table.wide{min-width:560px}
details{border-top:1px solid var(--line);padding:10px 0}summary{cursor:pointer;font-weight:600}
.rv{display:none;gap:6px;margin-top:10px;flex-wrap:wrap}body.review .rv{display:flex}.rv button,.rv input{font:inherit;font-size:13px;padding:4px 10px;border-radius:8px;border:1px solid var(--line);background:none;color:var(--ink)}.rv button.on{background:var(--accent);color:var(--bg);border-color:var(--accent)}.rv input{flex:1;min-width:140px}
.bar{display:flex;gap:8px;justify-content:flex-end;margin:16px 0}.bar button{font:inherit;padding:8px 14px;border-radius:99px;border:1px solid var(--line);background:var(--card);color:var(--ink);cursor:pointer}
/* shape components: use the ones you need, delete the others */
.opts{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:10px}.opt{border:1px solid var(--line);border-radius:10px;padding:14px}.opt.pick{border:2px solid var(--accent)}.opt dt{font-size:12px;color:var(--mute);margin-top:8px}.opt dd{margin:0}
.bars{display:grid;gap:8px}.barrow{display:grid;grid-template-columns:minmax(90px,30%) 1fr auto;gap:8px;align-items:center;font-size:14px}.barrow i{display:block;height:14px;border-radius:4px;background:var(--accent);min-width:2px}.barrow i.plan{background:var(--line)}
.chips{display:flex;gap:6px;flex-wrap:wrap;margin:8px 0}.chips button{font:inherit;font-size:13px;padding:4px 12px;border-radius:99px;border:1px solid var(--line);background:none;color:var(--ink);cursor:pointer}.chips button.on{background:var(--accent);color:var(--bg);border-color:var(--accent)}
.row{display:flex;gap:10px;padding:10px 0;border-top:1px solid var(--line);flex-wrap:wrap}.row input[type=checkbox]{width:18px;height:18px;margin-top:3px}.row>div{flex:1;min-width:200px}.row small{display:block;color:var(--mute)}.row .rv{flex-basis:100%}
.tl{border-inline-start:2px solid var(--line);margin-inline-start:6px;padding-inline-start:16px}.tl>div{position:relative;padding:6px 0}.tl>div::before{content:'';position:absolute;inset-inline-start:-22px;top:13px;width:10px;height:10px;border-radius:50%;background:var(--accent)}
.cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px}.steps>div{border:1px solid var(--line);border-radius:10px;padding:10px;font-size:14px;margin-bottom:22px;position:relative}.steps>div:not(:last-child)::after{content:'↓';position:absolute;bottom:-22px;left:50%;color:var(--mute)}.steps>div.new{border-color:var(--accent)}.steps>div.gone{border-style:dashed;color:var(--mute)}.steps small{display:block;color:var(--mute)}
code{font-size:.9em;overflow-wrap:anywhere}
.panel[data-title]::before{content:attr(data-title);display:none;font-size:20px;font-weight:700;margin:18px 0 6px}
@media print{*{-webkit-print-color-adjust:exact;print-color-adjust:exact}.panel[hidden]{display:block!important}.panel[data-title]::before{display:block}.tabs,.bar,.rv,.chips{display:none!important}.block{break-inside:avoid}}
[hidden]{display:none!important}
</style></head><body><main>
<span class="banner" id="banner">Draft, not signed</span>
<div class="meta"><bdi>{{SENDER}} → {{RECIPIENT}}</bdi> · <bdi>{{DATE}}</bdi> · <bdi>V1</bdi> · <bdi>10 sec top</bdi> · <bdi>{{N}} min full</bdi></div>

<!-- TOP:start -->
<section class="top" data-block="Top">
  <h1 class="verdict">{{VERDICT: one sentence, the answer}}</h1>
  <div class="ask">{{ASK: what the recipient must do, and by when}}</div>
  <div class="tiles">
    <div class="tile"><b>{{NUMBER}}</b><span>{{label · comparison}}</span></div>
  </div>
</section>
<!-- TOP:end -->

<!-- BODY:start  (tabs are optional; a maximum of four) -->
<nav class="tabs" role="tablist" data-hint="Review each tab">
  <button role="tab" aria-selected="true" data-tab="t1">{{Tab 1}}</button>
  <button role="tab" aria-selected="false" data-tab="t2">{{Tab 2}}</button>
</nav>
<section id="t1" class="panel" data-title="{{Tab 1}}">
  <article class="block" data-block="{{Block name}}">
    <h3>{{Heading that states the point}} <span class="tag ok">{{status}}</span></h3>
    <p>{{One to three STE sentences.}}</p>
    <details><summary>Detail</summary>{{depth}}</details>
  </article>
  <!-- Component patterns. Copy the ones that the shape needs.
  Options:   div.opts > div.opt (add .pick to the recommended one) > h4 + dl(dt label, dd value)
  Bars:      div.bars > div.barrow > span label + i style="width:NN%" + b value   (i.plan = target bar)
  Actions:   div.row[data-block][data-owner] > input checkbox + div(b owner + text + small date)
  Filter:    div.chips[data-filter="data-owner"] > button.on (the first button shows all) + one button for each value (script filters .row)
  Timeline:  div.tl > div(b date or phase + text + span.tag status)
  Table:     div.scroll > table (add class="sort" and a thead/tbody when a sort helps the reader; add class="wide" for five or more columns)
  Conflict:  div.tile > b "A or B" + span(label + span.tag.warn conflict + the two sources)
  Diagram:   div.cols > div(h4 "Before") + div(h4 "After"); each has div.steps > div (add .new or .gone) with text + small detail.
             For a system map, use inline SVG that uses var(--ink), var(--line), var(--accent)
  -->
</section>
<section id="t2" class="panel" data-title="{{Tab 2}}" hidden></section>
<!-- BODY:end -->

<!-- EVIDENCE:start -->
<section class="block" data-block="Evidence">
  <h3>Evidence</h3>
  <details><summary>Sources</summary>{{source name · date}}</details>
  <details><summary>Assumptions and gaps</summary>{{assumed / unverified / conflict / not in source}}</details>
  <details><summary>Method and calculations</summary>{{how each derived number was calculated}}</details>
  <details><summary>Cut</summary>{{content the human removed, kept here}}</details>
</section>
<!-- EVIDENCE:end -->

<div class="bar" id="bar">
  <button id="rvToggle">Review mode</button>
  <button id="rvCopy" hidden>Copy feedback</button>
</div>
</main>
<script>
(function(){
  var L={keep:'Keep',cut:'Cut',fix:'Fix',up:'Move up',note:'Note (optional)',review:'Review mode',exit:'Exit review',copy:'Copy feedback',copied:'Copied. Paste it in chat',none:'No changes. Ready to sign.'}; // translate these for other languages
  // Tabs
  var tabs=[].slice.call(document.querySelectorAll('.tabs button'));
  tabs.forEach(function(b){b.onclick=function(){tabs.forEach(function(x){x.setAttribute('aria-selected',x===b);var p=document.getElementById(x.dataset.tab);if(p)p.hidden=x!==b;});};});
  // Sortable tables: click a header
  document.querySelectorAll('table.sort th').forEach(function(th){th.onclick=function(){var t=th.closest('table'),i=[].indexOf.call(th.parentNode.children,th),rows=[].slice.call(t.tBodies[0].rows),d=th.dataset.d=th.dataset.d==='1'?'-1':'1';rows.sort(function(a,b){var x=a.cells[i].textContent.trim(),y=b.cells[i].textContent.trim(),nx=parseFloat(x.replace(/[^0-9.\-]/g,'')),ny=parseFloat(y.replace(/[^0-9.\-]/g,''));return((isNaN(nx)||isNaN(ny))?x.localeCompare(y):nx-ny)*d;}).forEach(function(r){t.tBodies[0].appendChild(r);});};});
  // Filter chips: <div class="chips" data-filter="data-owner"><button class="on">All</button><button>Dana</button></div>
  document.querySelectorAll('.chips[data-filter]').forEach(function(c){var a=c.dataset.filter,bs=[].slice.call(c.querySelectorAll('button'));bs.forEach(function(b){b.onclick=function(){bs.forEach(function(x){x.classList.toggle('on',x===b);});var v=b.textContent.trim(),all=b===bs[0];(c.closest('.block')||document).querySelectorAll('['+a+']').forEach(function(r){r.hidden=!(all||r.getAttribute(a)===v);});};});});
  window.addEventListener('beforeprint',function(){document.querySelectorAll('details').forEach(function(d){d.open=true;});});
  // Review mode (skipped when the signed version has no #bar): Keep / Cut / Fix + note on every [data-block], then Copy feedback
  var tg=document.getElementById('rvToggle'),cp=document.getElementById('rvCopy');if(!tg)return;
  var state={};
  document.querySelectorAll('[data-block]').forEach(function(el){
    var name=el.dataset.block,box=document.createElement('div');box.className='rv';
    (name==='Top'||name==='Evidence'?[L.keep,L.fix]:[L.keep,L.cut,L.fix,L.up]).forEach(function(v){var b=document.createElement('button');b.textContent=v;b.onclick=function(){state[name]=state[name]||{};state[name].v=v;[].forEach.call(box.querySelectorAll('button'),function(x){x.classList.toggle('on',x===b);});};box.appendChild(b);});
    var i=document.createElement('input');i.placeholder=L.note;i.oninput=function(){state[name]=state[name]||{};state[name].n=i.value;};box.appendChild(i);el.appendChild(box);
  });
  tg.onclick=function(){var on=document.body.classList.toggle('review');cp.hidden=!on;tg.textContent=on?L.exit:L.review;};
  cp.onclick=function(){
    var meta=((document.querySelector('.meta')||{}).textContent||'').trim(),ver=(meta.match(/\bV(\d+)\b/)||[0,'1'])[1];
    var lines=['[lawyer-five-year-old · review v'+ver+']',document.title+' · '+meta];
    Object.keys(state).forEach(function(k){var s=state[k];if(s.v||s.n)lines.push(k+' | '+(s.v||'Note')+(s.n?' | '+s.n:''));});
    if(lines.length===2)lines.push(L.none);
    var txt=lines.join('\n');
    function done(){cp.textContent=L.copied;setTimeout(function(){cp.textContent=L.copy;},2500);}
    function fallback(){var ta=document.createElement('textarea');ta.value=txt;document.body.appendChild(ta);ta.select();try{document.execCommand('copy');}catch(e){}ta.remove();done();}
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(txt).then(done,fallback);}else{fallback();}
  };
})();
</script></body></html>
```

Fill rules:
- `data-block` names are short and unique; they are the identity in the feedback text.
- Replace the body blocks with the components of the selected shape (tiles, tables, timeline, comparison columns, SVG diagram, check boxes). Keep the classes and tokens.
- `data-title` on each panel is the tab name. It prints as a heading.
- If the body has one view, delete the `nav.tabs` element and the second panel. For a third or fourth tab, add a button and a `section.panel` with the same id pattern.
- Delete the component CSS and the script parts that you do not use.
- Signed version: set the banner to `class="banner signed"` with the text `Signed by NAME, DATE`, and delete the `#bar` element. The script then adds no review controls.
- Filter chips filter the rows in their own `.block`. Put the chips and the rows in the same block.
- No `{{` can remain in a published file.
