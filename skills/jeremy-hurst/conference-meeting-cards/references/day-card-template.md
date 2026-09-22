---
title: "Day-card template"
description: (reference)
---

# Day-card template

One self-contained HTML file per calendar day. Copy the whole block and fill every `{{...}}` slot. The tokens inside this template are per-render fill slots (event, date, company, attendee, bullet text), not setup placeholders from the skill's placeholder block. Then remove the HTML comments and any bullet with nothing true to say, and save it to your output folder. The stylesheet is inline on purpose so the file opens on a phone with no dependencies beyond the two web fonts (swap them for your own from your design tokens).

Print behavior is built in: one meeting per page, card backgrounds print, the sticky bar and jump links are hidden.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{EVENT_NAME}} - {{WEEKDAY_DATE}} meeting cards</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap');
  :root{--ink:#1c1a18;--ink-soft:#4a4640;--bg:#f0ece6;--card:#faf7f3;--cream:#ede8e2;--cream-2:#ddd7cf;--grey:#b8b5b0;--grey-2:#8a8681;--rule:#e2dbd2;--accent:#c0392b;--accent-2:#e05a47;}
  *{box-sizing:border-box;}
  html,body{margin:0;padding:0;}
  body{background:var(--bg);color:var(--ink);font-family:-apple-system,"Inter",Segoe UI,Roboto,sans-serif;line-height:1.45;padding:0;}
  .topbar{position:sticky;top:0;z-index:10;background:var(--bg);border-bottom:1px solid var(--rule);padding:12px 16px 10px;}
  .eyebrow{font-family:"Space Grotesk",Georgia,serif;text-transform:uppercase;letter-spacing:.14em;font-size:11px;font-weight:600;color:var(--accent);margin:0 0 4px;}
  h1{font-family:"Space Grotesk",Georgia,serif;font-size:clamp(22px,5vw,32px);font-weight:700;margin:0;letter-spacing:-.02em;}
  .meta{font-size:13px;color:var(--grey-2);margin:4px 0 10px;}
  .jumps{display:flex;flex-wrap:wrap;gap:8px;}
  .jumps a{font-size:12px;font-weight:600;color:var(--ink);text-decoration:none;background:var(--card);border:1px solid var(--rule);border-radius:99px;padding:6px 10px;}
  .wrap{max-width:640px;margin:0 auto;padding:16px 16px 48px;}
  .meeting{background:var(--card);border:1px solid var(--rule);border-radius:16px;padding:18px 16px 16px;margin:0 0 18px;}
  .time{font-family:"Space Grotesk",Georgia,serif;font-size:12px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--accent);margin:0 0 6px;}
  .chip{display:inline-block;font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:.06em;padding:3px 8px;border-radius:99px;color:#fff;background:linear-gradient(135deg,var(--accent),var(--accent-2));margin:0 0 8px;}
  h2{font-family:"Space Grotesk",Georgia,serif;font-size:clamp(24px,6vw,30px);font-weight:700;margin:0 0 4px;letter-spacing:-.02em;}
  .gen{font-size:12px;color:var(--grey-2);margin:0 0 16px;}
  .people{display:flex;flex-wrap:wrap;gap:12px;margin:0 0 16px;}
  .person{width:148px;text-align:center;background:var(--cream);border:1px solid var(--rule);border-radius:12px;padding:12px 10px 10px;}
  .avatar{width:64px;height:64px;border-radius:50%;margin:0 auto 8px;object-fit:cover;display:block;background:var(--cream-2);box-shadow:0 0 0 1px var(--rule);}
  .avatar-fallback{width:64px;height:64px;border-radius:50%;margin:0 auto 8px;display:flex;align-items:center;justify-content:center;font-family:"Space Grotesk",Georgia,serif;font-weight:600;font-size:18px;color:var(--grey-2);background:var(--cream-2);box-shadow:0 0 0 1px var(--rule);}
  .name{font-weight:700;font-size:14px;margin:0 0 2px;letter-spacing:-.01em;}
  .name a{color:var(--ink);text-decoration:none;}
  .name a:hover{color:var(--accent);}
  .title{font-size:12px;color:var(--ink-soft);margin:0 0 6px;}
  .li{font-size:11px;color:var(--accent);word-break:break-all;text-decoration:none;}
  .context{margin:0;padding:0 0 0 18px;}
  .context li{font-size:15px;color:var(--ink);margin:0 0 8px;padding:0;}
  .context li:last-child{margin:0;}
  .label{font-weight:700;color:var(--ink-soft);}
  footer.page{font-size:12px;color:var(--grey-2);padding:8px 16px 32px;max-width:640px;margin:0 auto;}
  @media print{
    body{background:#fff;padding:0;}
    .topbar{position:static;border:none;}
    .jumps{display:none;}
    .meeting{page-break-after:always;break-after:page;border:1px solid var(--rule);box-shadow:none;margin:0 0 12px;}
    .meeting:last-of-type{page-break-after:auto;}
  }
</style>
</head>
<body>
  <div class="topbar">
    <p class="eyebrow">{{EVENT_NAME}} · walking cards</p>
    <h1>{{WEEKDAY_DATE}}</h1>
    <p class="meta">{{DAY_LABEL}} · {{MEETING_COUNT}} meetings · {{TIMES_NOTE}}</p>
    <nav class="jumps">
      <a href="#m-{{company-slug}}">{{Company}}</a>
      <!-- one jump link per meeting, in day order -->
    </nav>
  </div>
  <div class="wrap">

    <!-- Repeat one <article> per meeting, chronological (or list order if times are TBD) -->
    <article class="meeting" id="m-{{company-slug}}">
      <p class="time">{{TIME_OR_TBD}}{{ · LOCATION, only if known}}</p>
      <h2>{{Company}}</h2>
      <p class="gen">Generated {{GENERATED_DATE}}</p>
      <div class="people">
        <!-- Attendee with a photo -->
        <div class="person">
          <img class="avatar" src="{{PHOTO_URL}}" alt="">
          <p class="name"><a href="https://www.linkedin.com/in/{{handle}}">{{Full Name}}</a></p>
          <p class="title">{{Title}}</p>
          <a class="li" href="https://www.linkedin.com/in/{{handle}}">linkedin.com/in/{{handle}}</a>
        </div>
        <!-- Attendee whose enrichment failed: initials, no invented title, verify flag -->
        <div class="person">
          <div class="avatar-fallback">{{AB}}</div>
          <p class="name"><a href="https://www.linkedin.com/in/{{handle}}">{{Full Name}}</a></p>
          <p class="title">verify details</p>
          <a class="li" href="https://www.linkedin.com/in/{{handle}}">linkedin.com/in/{{handle}}</a>
        </div>
      </div>
      <ul class="context">
        <!-- At most {{MAX_BULLETS}} bullets, each under {{BULLET_CHAR_CAP}} characters, fixed order, skip any bullet with nothing true to say -->
        <li><span class="label">What they do.</span> {{One plain-English sentence.}}</li>
        <li><span class="label">Amount.</span> {{CRM amount + close date, or a labeled ACV estimate, or "No open deal."}}</li>
        <li><span class="label">Stage.</span> {{Stage label}}. Next: {{next step}}.</li>
        <li><span class="label">Use cases.</span> {{Only if there is an active deal.}}</li>
        <li><span class="label">People.</span> {{Champion / budget / blocker for this conversation.}}</li>
        <li><span class="label">Relationship.</span> {{Only if meaningful.}}</li>
        <!-- Optional 7th, only for a real key risk -->
        <li><span class="label">Risk.</span> {{From the latest forecast note.}}</li>
      </ul>
    </article>

  </div>
  <footer class="page">{{EVENT_NAME}} · {{WEEKDAY_DATE}} · print with backgrounds on for one card per page</footer>
</body>
</html>
```
