---
name: "ads-measurement-scorecard"
title: Ads measurement scorecard
description: Use this skill when setting up paid media measurement — the scorecard of leading vs vanity metrics and the dashboard that keeps reporting honest.
category: Ads
---

# Measurement Scorecard & Dashboard Setup

## Why Measurement Matters

- You can't fix what you can't see
- If it takes 6+ reports and 30+ minutes to answer basic questions, that level of speed won't let you scale

## Measurement Scorecard

Score 1-3 on each question (don't lie, be honest):

### Dashboards & Reporting

**Q1: Do you have one dashboard where you can see overall blended pipeline performance?**

Blended = paid + organic

- **1** = no dashboard created
- **2** = limited dashboard (can improve)
- **3** = reliable dashboard used regularly

**Q2: Do you have dashboards where you can see channel performance?**

(spend/pacing/conversions)

- **1** = no channel dashboard created
- **2** = limited dashboard (needs work)
- **3** = reliable dashboard used regularly

### Conversion Tracking

**Q3: Are you tracking conversions from the ad channels?**

- **1** = no conversion tracking set up
- **2** = tracking via pixel conversions
- **3** = tracking via offline conversions

### Web Analytics

**Q4: Do you have a web analytics tool implemented?**

(e.g. Google Analytics 4, Adobe Analytics)

- **1** = no web analytics tool implemented
- **2** = yes but haven't configured it
- **3** = yes and consistently using it for insights

### Attribution

**Q5: Do you have an organizationally agreed upon attribution process to understand what is working?**

- **1** = not really
- **2** = everyone has an 'idea' but it isn't documented
- **3** = it's clearly documented and agreed upon as a team (no bias)

## Scoring Interpretation

- **Score < 6** = below average. Consider pausing campaigns until visibility is in place.
- **Score 6-13** = average. Room for improvement (most fall here).
- **Score 13-15** = above average. Strong confidence in measuring success.

Focus on improving items scored lowest first.

## Program Visibility Dashboard Setup

### Build an Automated Dashboard

Build an automated paid media dashboard in Google Sheets.

## Building the Paid Media Dashboard (Technical Setup)

The dashboard needs to combine ad spend data with CRM data (source of truth).

### Ad Spend Data Structure (per channel tab)

- Column A: Date
- Column B: Total cost
- One tab per channel (Google Ads, LinkedIn, Facebook, etc.)

### CRM Data Structure

- Column A: Create date (when the event happened)
- Column B: Lead source (paid vs organic)
- Column C: Lead source detail (which channel - Google, LinkedIn, etc.)

### Recommended Data Connectors

**For ad spend:**
- Dataslayer ($99/month, auto-refresh hourly) or Supermetrics

**For CRM (Salesforce):**
- Salesforce Connector by Google (free, Google Workspace)

**For CRM (HubSpot):**
- HubSpot App Marketplace workflow --> push to Google Sheets

### Formula Setup

- Leads, SQOs, SAOs, Pipeline, Closed Won, Revenue use SUMIFS and COUNTIFS functions
- Each function distinguishes channels based on the name in the Lead Source Detail field
- Make sure the Lead Source Detail field matches the channel name used in the formulas

### Dashboard Capabilities

- Filter by any date range (dynamic start/end date)
- Individual channel performance (spend, leads, CPL, through full lifecycle to revenue)
- Blended performance (paid + organic combined)
- Blended cost per opportunity to measure overall program health

### Important Notes

If lifecycle stage labels differ (e.g., "meetings" instead of "SQLs"), customize the field labels. If advertising on additional channels, insert new rows and import data accordingly.

If not comfortable with sheets, loop in your marketing operations team or hire on Upwork/Fiverr.
