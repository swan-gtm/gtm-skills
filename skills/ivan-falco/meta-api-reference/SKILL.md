---
name: "meta-api-reference"
title: Meta Marketing API reference
description: "Use this skill when working with the Meta Marketing API directly — endpoints, objects, fields, and request patterns for campaigns, ad sets, ads, audiences, and insights."
category: Ads
---

# Meta Marketing API - Complete Reference

## Configuration

- **API Version:** `v22.0`
- **Base URL:** `https://graph.facebook.com/v22.0/`
- **Two tokens in `.env`:**
  - `ADS_MANAGER_ACCESS_TOKEN` - Marketing API (campaign management, insights, reporting)
  - `AD_LIBRARY_ACCESS_TOKEN` - Ad Library API (competitor research)
- **Token expiry:** ~60 days from last refresh (check `.env` comment for date)

---

## Account Hierarchy

```
Ad Account (act_XXXX)
  -> Campaign (objective, budget if CBO, bid strategy)
    -> Ad Set (targeting, budget if ABO, optimization, schedule)
      -> Ad (creative reference, status)
        -> Ad Creative (media, copy, CTA, url_tags)
```

---

## Campaign Schema

**Endpoint:** `POST /{account_id}/campaigns`

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Campaign name |
| `objective` | enum | Marketing objective (ODAX framework) |
| `status` | enum | Campaign status |
| `special_ad_categories` | array | Special category declarations (pass `[]` if none) |

### Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `daily_budget` | int (cents) | Daily budget for CBO (5000 = $50.00) |
| `lifetime_budget` | int (cents) | Lifetime budget for CBO |
| `bid_strategy` | enum | Bidding strategy |
| `buying_type` | enum | Buying type |
| `is_adset_budget_sharing_enabled` | string | `"true"` for CBO, `"false"` for ABO |
| `execution_options` | array | `["validate_only"]` or `["include_recommendations"]` |

### Objective (ODAX Framework)

| Value | Description | Use For |
|-------|-------------|---------|
| `OUTCOME_AWARENESS` | Brand awareness, reach | Top of funnel |
| `OUTCOME_ENGAGEMENT` | Post engagement, video views, page likes | Mid funnel |
| `OUTCOME_TRAFFIC` | Link clicks, landing page views | Mid funnel |
| `OUTCOME_LEADS` | Lead gen forms, conversions (lead) | Bottom of funnel |
| `OUTCOME_SALES` | Conversions (purchase), catalog sales | Bottom of funnel |
| `OUTCOME_APP_PROMOTION` | App installs, app engagement | App campaigns |

Legacy objectives (deprecated for new campaigns, returned by API for old ones): `CONVERSIONS`, `LEAD_GENERATION`, `LINK_CLICKS`, `BRAND_AWARENESS`, `REACH`, `POST_ENGAGEMENT`, `VIDEO_VIEWS`, `MESSAGES`, `APP_INSTALLS`, `PAGE_LIKES`, `EVENT_RESPONSES`, `STORE_VISITS`, `PRODUCT_CATALOG_SALES`

### Bid Strategy

| Value | Description |
|-------|-------------|
| `LOWEST_COST_WITHOUT_CAP` | Lowest cost, no cap (default) |
| `COST_CAP` | Cost cap - set max cost per result |
| `LOWEST_COST_WITH_BID_CAP` | Bid cap - set max bid per auction |
| `LOWEST_COST_WITH_MIN_ROAS` | Min ROAS - target minimum return |

### Special Ad Categories

| Value | Description |
|-------|-------------|
| `CREDIT` | Credit offers |
| `EMPLOYMENT` | Job opportunities |
| `HOUSING` | Housing/real estate |
| `ISSUES_ELECTIONS_POLITICS` | Social issues, elections, politics |
| `FINANCIAL_PRODUCTS_SERVICES` | Financial products |
| `ONLINE_GAMBLING_AND_GAMING` | Gambling/gaming |
| `NONE` | No special category |

### Buying Type

| Value | Description |
|-------|-------------|
| `AUCTION` | Standard auction buying (default, used 99% of the time) |
| `RESERVED` | Reserved/guaranteed delivery (Reach & Frequency) |

### Campaign Status

`ACTIVE`, `PAUSED`, `DELETED`, `ARCHIVED`

### CBO vs ABO

**CBO (Campaign Budget Optimization):**
- Set `daily_budget` or `lifetime_budget` on the **campaign**
- Set `is_adset_budget_sharing_enabled: "true"` on the campaign
- Do NOT set budget on ad sets
- Meta distributes budget across ad sets automatically

**ABO (Ad Set Budget Optimization):**
- Set `is_adset_budget_sharing_enabled: "false"` on the campaign
- Set `daily_budget` or `lifetime_budget` on each **ad set**
- Do NOT set budget on the campaign
- Each ad set gets its own independent budget

---

## Ad Set Schema

**Endpoint:** `POST /{account_id}/adsets`

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Ad set name |
| `campaign_id` | string | Parent campaign ID |
| `optimization_goal` | enum | What to optimize for |
| `billing_event` | enum | When to charge |
| `targeting` | JSON object | Targeting specification |
| `status` | enum | Ad set status |
| `daily_budget` or `lifetime_budget` | int (cents) | Budget (ABO only) |

### Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `bid_amount` | int (cents) | Bid amount (required for cost_cap or bid_cap) |
| `bid_strategy` | enum | Overrides campaign bid strategy |
| `start_time` | ISO 8601 | When to start delivering |
| `end_time` | ISO 8601 | When to stop delivering |
| `promoted_object` | JSON object | Pixel/event for conversion optimization |
| `destination_type` | enum | Where the ad sends people |
| `is_dynamic_creative` | bool | Enable dynamic creative |
| `pacing_type` | array | `["standard"]` or `["day_parting"]` |
| `dsa_beneficiary` | string | DSA compliance - beneficiary name (EU) |
| `dsa_payor` | string | DSA compliance - payor name (EU) |
| `targeting_automation` | JSON object | Advantage+ audience settings |

### Optimization Goal (34 values)

**Most commonly used:**

| Value | Use With Objective | Description |
|-------|-------------------|-------------|
| `OFFSITE_CONVERSIONS` | OUTCOME_LEADS, OUTCOME_SALES | Website conversions via pixel |
| `LEAD_GENERATION` | OUTCOME_LEADS | On-platform lead form submissions |
| `LINK_CLICKS` | OUTCOME_TRAFFIC | Link clicks |
| `LANDING_PAGE_VIEWS` | OUTCOME_TRAFFIC | Landing page views (requires pixel) |
| `REACH` | OUTCOME_AWARENESS | Maximum unique reach |
| `IMPRESSIONS` | OUTCOME_AWARENESS | Maximum impressions |
| `AD_RECALL_LIFT` | OUTCOME_AWARENESS | Ad recall optimization |
| `POST_ENGAGEMENT` | OUTCOME_ENGAGEMENT | Post interactions |
| `PAGE_LIKES` | OUTCOME_ENGAGEMENT | Page likes |
| `THRUPLAY` | OUTCOME_ENGAGEMENT | Video views (15s+) |
| `VALUE` | OUTCOME_SALES | Conversion value (ROAS) |
| `APP_INSTALLS` | OUTCOME_APP_PROMOTION | App installs |
| `CONVERSATIONS` | OUTCOME_LEADS | Messaging conversations |
| `QUALITY_LEAD` | OUTCOME_LEADS | Quality leads (CRM-optimized) |

**Full list (additional):** `ADVERTISER_SILOED_VALUE`, `APP_INSTALLS_AND_OFFSITE_CONVERSIONS`, `AUTOMATIC_OBJECTIVE`, `DERIVED_EVENTS`, `ENGAGED_USERS`, `EVENT_RESPONSES`, `IN_APP_VALUE`, `MEANINGFUL_CALL_ATTEMPT`, `MESSAGING_APPOINTMENT_CONVERSION`, `MESSAGING_PURCHASE_CONVERSION`, `NONE`, `PROFILE_AND_PAGE_ENGAGEMENT`, `PROFILE_VISIT`, `QUALITY_CALL`, `REACH`, `REMINDERS_SET`, `SUBSCRIBERS`, `VISIT_INSTAGRAM_PROFILE`

### Billing Event

| Value | Description |
|-------|-------------|
| `IMPRESSIONS` | Charge per impression (most common, used 95%+ of the time) |
| `LINK_CLICKS` | Charge per link click |
| `APP_INSTALLS` | Charge per app install |
| `THRUPLAY` | Charge per video view |
| `CLICKS` | Charge per any click |
| `PAGE_LIKES` | Charge per page like |
| `POST_ENGAGEMENT` | Charge per engagement |

**Full list (additional):** `LISTING_INTERACTION`, `NONE`, `OFFER_CLAIMS`, `PURCHASE`

### Destination Type (most common)

| Value | Description |
|-------|-------------|
| `WEBSITE` | Send to website URL (most common) |
| `ON_AD` | On-ad destination (lead forms, instant experiences) |
| `MESSENGER` | Messenger conversation |
| `WHATSAPP` | WhatsApp conversation |
| `INSTAGRAM_DIRECT` | Instagram DM |
| `APP` | Mobile app |
| `FACEBOOK` | Facebook destination |
| `ON_POST` | On post |
| `ON_VIDEO` | On video |
| `SHOP_AUTOMATIC` | Shop automatic |

**Full list (additional):** `APPLINKS_AUTOMATIC`, `FACEBOOK_LIVE`, `FACEBOOK_PAGE`, `IMAGINE`, `INSTAGRAM_LIVE`, `INSTAGRAM_PROFILE`, `INSTAGRAM_PROFILE_AND_FACEBOOK_PAGE`, `MESSAGING_INSTAGRAM_DIRECT_MESSENGER`, `MESSAGING_INSTAGRAM_DIRECT_MESSENGER_WHATSAPP`, `MESSAGING_INSTAGRAM_DIRECT_WHATSAPP`, `MESSAGING_MESSENGER_WHATSAPP`, `ON_EVENT`, `ON_PAGE`

### Promoted Object

Required for conversion optimization:

```python
# For pixel conversions (OUTCOME_LEADS or OUTCOME_SALES)
'promoted_object': json.dumps({
    'pixel_id': 'YOUR_PIXEL_ID',
    'custom_event_type': 'LEAD'  # or PURCHASE, COMPLETE_REGISTRATION, etc.
})

# For lead gen forms (OUTCOME_LEADS with LEAD_GENERATION goal)
'promoted_object': json.dumps({
    'page_id': 'YOUR_PAGE_ID'
})

# For app installs
'promoted_object': json.dumps({
    'application_id': 'YOUR_APP_ID',
    'object_store_url': 'https://apps.apple.com/...'
})
```

### custom_event_type Values

`LEAD`, `PURCHASE`, `COMPLETE_REGISTRATION`, `ADD_TO_CART`, `ADD_TO_WISHLIST`, `INITIATE_CHECKOUT`, `ADD_PAYMENT_INFO`, `CONTACT`, `CUSTOMIZE_PRODUCT`, `DONATE`, `FIND_LOCATION`, `SCHEDULE`, `START_TRIAL`, `SUBMIT_APPLICATION`, `SUBSCRIBE`, `SEARCH`, `VIEW_CONTENT`, `OTHER`

---

## Targeting Spec

### Complete Structure

```python
targeting = {
    # GEOGRAPHIC (required)
    'geo_locations': {
        'countries': ['US', 'CA', 'GB'],           # ISO country codes
        'country_groups': ['north_america', 'europe'],  # OR use region codes
        'regions': [{'key': '3847'}],               # State/province
        'cities': [{'key': '2430536', 'radius': 10, 'distance_unit': 'mile'}],
        'zips': [{'key': 'US:10001'}],
        'location_types': ['home', 'recent']        # home, recent, travel_in
    },

    # DEMOGRAPHICS
    'age_min': 25,                  # 13-65
    'age_max': 55,                  # 13-65
    'genders': [1],                 # 1=male, 2=female, omit or [0]=all
    'locales': [6],                 # Language codes (6=English)

    # INTEREST/BEHAVIOR TARGETING
    'flexible_spec': [
        {
            'interests': [{'id': '6003107902433', 'name': 'SaaS'}],
            'behaviors': [{'id': '6002714895372', 'name': 'Small business owners'}]
        }
    ],
    # flexible_spec logic:
    #   Within one object: fields are OR'd (interest1 OR behavior1)
    #   Multiple objects in array: OR'd together
    #   Use 'exclusions' for AND NOT logic

    'exclusions': {
        'interests': [{'id': '123', 'name': 'Excluded Interest'}]
    },

    # AUDIENCES
    'custom_audiences': [{'id': 'YOUR_AUDIENCE_ID'}],
    'excluded_custom_audiences': [{'id': 'YOUR_EXCLUDED_AUDIENCE_ID'}],

    # ADVANTAGE+ AUDIENCE
    'targeting_optimization': 'expansion_all',  # Enable Advantage+ expansion

    # PLATFORMS & PLACEMENTS (usually omit for Advantage+ Placements)
    'publisher_platforms': ['facebook', 'instagram', 'audience_network', 'messenger'],
    'device_platforms': ['mobile', 'desktop'],
    'facebook_positions': ['feed', 'story', 'facebook_reels', 'right_hand_column', 'search', 'marketplace', 'video_feeds', 'instream_video', 'profile_feed', 'biz_disco_feed', 'facebook_reels_overlay'],
    'instagram_positions': ['stream', 'story', 'reels', 'profile_reels', 'ig_search', 'explore', 'explore_home', 'profile_feed'],
    'messenger_positions': ['story', 'inbox'],
    'audience_network_positions': ['classic', 'rewarded_video'],

    # CONNECTIONS
    'connections': [{'id': 'YOUR_PAGE_ID'}],           # Connected to page
    'excluded_connections': [{'id': 'YOUR_PAGE_ID'}]   # Not connected to page
}
```

### Advantage+ Audience (v23.0+)

```python
'targeting_automation': {
    'advantage_audience': 1   # 1 = enabled, 0 = disabled
}
```

When enabled, Meta's AI expands beyond your defined targeting to find high-intent users. You still provide base targeting (geo, age, etc.) but Meta can go beyond it. Defaults to enabled in API v23.0+.

### Geo Targeting Rules

- Use `countries` for individual countries: `['US', 'CA', 'GB']`
- Use `country_groups` for regions: `['north_america', 'europe']`
- Don't list 30+ individual countries when a region covers it
- **Never overlap locations** (e.g., both US and New York City causes error)
- **Exclude Singapore** to avoid regulatory compliance fields

### Interest/Behavior Search

```python
# Search for targeting interests
GET /search?type=adinterest&q=KEYWORD&limit=10000&locale=en_US&access_token=TOKEN

# Response:
# { "data": [{ "id": "6003107902433", "name": "SaaS", "audience_size": 123456, "path": ["..."], "topic": "..." }] }

# Alternative: interest suggestions
GET /search?type=adinterestsuggestion&interest_list=["SaaS"]&access_token=TOKEN
```

API reveals 1000s of interests not shown in Ads Manager's autocomplete (which only shows ~25).

**2026 Note:** Many detailed targeting interests consolidated starting June 2025. Campaigns using interests created before Oct 8, 2025 may stop delivering.

---

## Ad Creative Schema

**Endpoint:** `POST /{account_id}/adcreatives`

### Core Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Creative name |
| `object_story_spec` | JSON object | Main creative content container |
| `url_tags` | string | URL parameters (SET AT CREATION ONLY - cannot update) |
| `instagram_user_id` | string | IG business account ID (set both here AND in object_story_spec) |
| `threads_user_id` | string | Threads profile ID (set at creative level, NOT inside object_story_spec) |
| `asset_feed_spec` | JSON object | For placement customization or dynamic creative |

### object_story_spec - Two Patterns

**Pattern A: Simple ad (link_data)**
```python
'object_story_spec': json.dumps({
    'page_id': 'YOUR_PAGE_ID',
    'instagram_user_id': 'YOUR_IG_USER_ID',
    'link_data': {
        'image_hash': 'HASH',
        'link': 'https://landing-page.com',
        'message': 'Body text',
        'name': 'Headline',
        'description': 'Description',
        'call_to_action': {
            'type': 'SIGN_UP',
            'value': {'link': 'https://landing-page.com'}
        }
    }
})
```

**Pattern B: Placement customization (asset_feed_spec)**
```python
'object_story_spec': json.dumps({
    'page_id': 'YOUR_PAGE_ID',
    'instagram_user_id': 'YOUR_IG_USER_ID'
    # NO link_data - all content goes in asset_feed_spec
})
```

**CRITICAL:** When using `asset_feed_spec`, `object_story_spec` must be MINIMAL (only page_id + instagram_user_id). Including `link_data` causes error.

### link_data Fields

| Field | Type | Description |
|-------|------|-------------|
| `link` | string | Destination URL |
| `message` | string | Ad body text |
| `name` | string | Headline |
| `description` | string | Description under headline |
| `caption` | string | Link caption/domain display |
| `image_hash` | string | Uploaded image hash |
| `picture` | string | Image URL (alternative to image_hash) |
| `call_to_action` | object | CTA button config |
| `child_attachments` | array | Carousel cards (2-10) |
| `multi_share_optimized` | bool | Let Meta show best-performing cards |
| `multi_share_end_card` | bool | Show end card on carousel |

### video_data Fields

```python
'video_data': {
    'video_id': 'VIDEO_ID',           # From video upload (required)
    'image_url': 'THUMBNAIL_URL',      # From /{video_id}/thumbnails (required)
    'title': 'Video title',
    'message': 'Body text',
    'link_description': 'Description',
    'call_to_action': {
        'type': 'LEARN_MORE',
        'value': {'link': 'https://landing.com'}
    }
}
```

### Carousel child_attachments

```python
'child_attachments': [
    {
        'link': 'https://product1.com',
        'name': 'Card 1 Headline',
        'description': 'Card 1 description',
        'image_hash': 'IMAGE_HASH_1',
        'call_to_action': {
            'type': 'SHOP_NOW',
            'value': {'link': 'https://product1.com'}
        }
    },
    {
        'link': 'https://product2.com',
        'name': 'Card 2 Headline',
        'description': 'Card 2 description',
        'image_hash': 'IMAGE_HASH_2'
    }
    # 2-10 cards total, each card needs image_hash + link at minimum
]
```

### CTA Types (Complete List)

**Most commonly used in B2B:**

| Value | Description |
|-------|-------------|
| `SIGN_UP` | Sign up |
| `LEARN_MORE` | Learn more |
| `DOWNLOAD` | Download |
| `SUBSCRIBE` | Subscribe |
| `APPLY_NOW` | Apply now |
| `GET_QUOTE` | Get quote |
| `CONTACT_US` | Contact us |
| `BOOK_NOW` | Book now |
| `REGISTER_NOW` | Register now |
| `SHOP_NOW` | Shop now |
| `MESSAGE_PAGE` | Send message |

**Full list by category:**

Commerce: `BUY_NOW`, `BUY_TICKETS`, `ORDER_NOW`, `SELL_NOW`, `GET_OFFER`, `ADD_TO_CART`, `PURCHASE_GIFT_CARDS`, `PAY_TO_ACCESS`

Information: `SEE_MENU`, `GET_SHOWTIMES`, `GET_DIRECTIONS`

App: `INSTALL_APP`, `INSTALL_MOBILE_APP`, `USE_APP`, `USE_MOBILE_APP`, `GET_MOBILE_APP`, `PLAY_GAME`, `UPDATE_APP`

Engagement: `BOOK_TRAVEL`, `REQUEST_TIME`, `SEND_INVITES`, `REFER_FRIENDS`, `OPEN_MESSENGER_EXT`, `INSTAGRAM_MESSAGE`, `CALL`, `CALL_NOW`, `CALL_ME`

Media: `WATCH_VIDEO`, `WATCH_MORE`, `LISTEN_MUSIC`, `LISTEN_NOW`, `GO_LIVE`, `RECORD_NOW`

Social: `LIKE_PAGE`, `VIEW_INSTAGRAM_PROFILE`, `INTERESTED`, `SAVE`, `SEND_TIP`, `DONATE`, `DONATE_NOW`, `EVENT_RSVP`, `VOTE_NOW`

Other: `OPEN_LINK`, `NO_BUTTON`, `BET_NOW`, `PRE_REGISTER`, `GET_EVENT_TICKETS`, `SEARCH_MORE`

### url_tags

- Set on creative at **creation time only** - cannot update, must recreate creative
- Standard format: `utm_source=meta&utm_medium=paid-social&utm_campaign={{adset.name}}&utm_content={{ad.name}}`
- Dynamic params: `{{campaign.name}}`, `{{campaign.id}}`, `{{adset.name}}`, `{{adset.id}}`, `{{ad.name}}`, `{{ad.id}}`, `{{placement}}`, `{{site_source_name}}`

---

## Ad Schema

**Endpoint:** `POST /{account_id}/ads`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | Ad name |
| `adset_id` | string | Yes | Parent ad set ID |
| `creative` | JSON object | Yes | `{"creative_id": "CREATIVE_ID"}` |
| `status` | enum | Yes | `PAUSED` (NEVER set to ACTIVE) |
| `tracking_specs` | JSON array | No | Additional conversion tracking |

---

## Custom Audience Schema

**Endpoint:** `POST /{account_id}/customaudiences`

### Customer List Upload

```python
# Step 1: Create audience
'name': 'My Customer List',
'subtype': 'CUSTOM',
'customer_file_source': 'USER_PROVIDED_ONLY'

# Step 2: Add users via /{audience_id}/users
'schema': ['EMAIL', 'FN', 'LN'],   # or 'PHONE', 'MOBILE_ADVERTISER_ID', 'UID'
'data': [
    ['sha256_hashed_email', 'sha256_hashed_firstname', 'sha256_hashed_lastname'],
    # ... up to 10,000 per batch
]
```

All PII fields must be SHA-256 hashed before sending. Normalize: lowercase, trim whitespace, E.164 format for phones.

### Website Custom Audience

```python
'name': 'Website Visitors - Last 30 Days',
'subtype': 'WEBSITE',
'rule': json.dumps({
    'inclusions': {
        'operator': 'or',
        'rules': [{'event_sources': [{'id': 'YOUR_PIXEL_ID', 'type': 'pixel'}], 'retention_seconds': 2592000}]
    }
})
```

### Lookalike Audience

```python
'name': '1% Lookalike - US - Customer List',
'subtype': 'LOOKALIKE',
'origin_audience_id': 'SOURCE_AUDIENCE_ID',   # min 100 members, recommended 1000-5000
'lookalike_spec': json.dumps({
    'ratio': 0.01,          # 1% similarity (0.01 to 0.20)
    'country': 'US',        # Single country per lookalike
    'starting_ratio': 0.00  # Optional: for tiered lookalikes (e.g., 1-2% tier)
})
```

**Tiered pattern:** Create 0-1% (ratio=0.01), then 1-2% (ratio=0.02, starting_ratio=0.01), then 2-3% (ratio=0.03, starting_ratio=0.02).

**2026 Note:** `lookalike_spec` is MANDATORY for creating new lookalike audiences (since Jan 6, 2026).

---

## Reach Estimation

**Endpoint:** `GET /{account_id}/reachestimate`

```python
params = {
    'access_token': token,
    'currency': 'USD',
    'optimize_for': 'OFFSITE_CONVERSIONS',
    'targeting_spec': json.dumps({
        'geo_locations': {'countries': ['US']},
        'age_min': 25,
        'age_max': 55
    })
}
```

Returns estimated audience size as a range, estimated daily results, and bid estimates.

---

## Insights / Reporting

**Endpoint:** `GET /{object_id}/insights` (works at account, campaign, ad set, or ad level)

### Core Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `fields` | string | Comma-separated metrics |
| `date_preset` | enum | Predefined date range |
| `time_range` | JSON | Custom date range `{"since":"2026-01-01","until":"2026-01-31"}` |
| `level` | enum | `campaign`, `adset`, `ad` (breakdown level) |
| `breakdowns` | string | Comma-separated delivery breakdowns |
| `action_breakdowns` | string | Comma-separated action breakdowns |
| `time_increment` | int or string | 1-90 (days), `"monthly"`, `"all_days"` |
| `limit` | int | Results per page (default 25) |
| `filtering` | JSON array | Filter conditions |

### Date Presets

`today`, `yesterday`, `last_3d`, `last_7d`, `last_14d`, `last_28d`, `last_30d`, `last_90d`, `this_week_mon_today`, `this_week_sun_today`, `last_week_mon_sun`, `last_week_sun_sat`, `this_month`, `last_month`, `this_quarter`, `last_quarter`, `this_year`, `last_year`, `maximum`, `lifetime`

### Common Metrics

`spend`, `impressions`, `clicks`, `reach`, `frequency`, `ctr`, `cpc`, `cpm`, `actions`, `cost_per_action_type`, `action_values`, `conversions`, `cost_per_conversion`, `conversion_values`, `purchase_roas`

### Delivery Breakdowns

| Breakdown | Description |
|-----------|-------------|
| `age` | Age ranges |
| `gender` | Gender |
| `country` | Country |
| `region` | Region/state |
| `dma` | DMA (US only) |
| `publisher_platform` | Facebook, Instagram, etc. |
| `platform_position` | Feed, stories, reels, etc. |
| `device_platform` | Mobile, desktop |
| `impression_device` | Device type |
| `frequency_value` | Frequency distribution |
| `hourly_stats_aggregated_by_advertiser_time_zone` | Hour of day (advertiser TZ) |
| `hourly_stats_aggregated_by_audience_time_zone` | Hour of day (audience TZ) |
| `product_id` | Product catalog ID |

**Dynamic creative breakdowns:** `ad_format_asset`, `body_asset`, `call_to_action_asset`, `description_asset`, `image_asset`, `link_url_asset`, `title_asset`, `video_asset`

**CRITICAL:** Cannot combine delivery breakdowns and action_breakdowns in the same request. Request them separately.

### Action Breakdowns

| Breakdown | Description |
|-----------|-------------|
| `action_type` | Type of action (lead, purchase, etc.) |
| `action_device` | Device where action occurred |
| `action_destination` | Where action led to |

### action_type Values

**Most commonly used:**

| action_type | Description |
|-------------|-------------|
| `lead` | On-platform lead form submission |
| `link_click` | Link click |
| `landing_page_view` | Landing page view |
| `post_engagement` | Post interaction |
| `video_view` | Video view |
| `page_engagement` | Page interaction |
| `onsite_conversion.lead_grouped` | Grouped on-platform lead events |
| `offsite_conversion.fb_pixel_lead` | Pixel lead event |
| `offsite_conversion.fb_pixel_purchase` | Pixel purchase event |
| `offsite_conversion.fb_pixel_add_to_cart` | Pixel add to cart |
| `offsite_conversion.fb_pixel_initiate_checkout` | Pixel checkout initiated |
| `offsite_conversion.fb_pixel_complete_registration` | Pixel registration |
| `offsite_conversion.fb_pixel_view_content` | Pixel content view |
| `offsite_conversion.fb_pixel_custom` | Pixel custom conversion |
| `omni_purchase` | Cross-channel purchase |
| `omni_add_to_cart` | Cross-channel add to cart |

### Extracting Conversions from Actions

```python
actions = row.get('actions', [])
leads = sum(int(a['value']) for a in actions if a['action_type'] == 'lead')
pixel_leads = sum(int(a['value']) for a in actions if a['action_type'] == 'offsite_conversion.fb_pixel_lead')
```

### Async Reports (Large Datasets)

For large date ranges or complex breakdowns:

```python
# Request async report
params['async'] = True
r = requests.get(url, params=params)
report_id = r.json()['report_run_id']

# Poll for completion
status_url = f'https://graph.facebook.com/v22.0/{report_id}'
r = requests.get(status_url, params={'access_token': token})
# Check async_status: "Job Completed", "Job Running", etc.

# Download results
results_url = f'https://graph.facebook.com/v22.0/{report_id}/insights'
r = requests.get(results_url, params={'access_token': token})
```

### Data Retention (2026)

- Unique-count fields: 13 months historical data
- Frequency breakdowns: 6 months
- Hourly breakdowns: 13 months
- Over 100 metrics deprecated (including unique_actions)

---

## Attribution Settings (2026)

### attribution_spec

```python
'attribution_spec': json.dumps([
    {'event_type': 'CLICK_THROUGH', 'window_days': 7},
    {'event_type': 'VIEW_THROUGH', 'window_days': 1}
])
```

### Available Windows (After Jan 12, 2026)

| Click-Through | View-Through |
|--------------|--------------|
| 1 day | 1 day |
| 7 days (default) | ~~7 days~~ REMOVED |
| | ~~28 days~~ REMOVED |

Default: 7-day click + 1-day view (7d_click / 1d_view).

**Impact:** 7-day and 28-day view-through windows were removed January 12, 2026. Historical reports using those windows no longer return data.

---

## Conversions API (CAPI) - Server-Side Events

**Endpoint:** `POST /{pixel_id}/events`

### Event Structure

```python
{
    'data': [
        {
            'event_name': 'Lead',               # Standard event name
            'event_time': 1709568234,            # Unix timestamp
            'event_id': 'unique-event-12345',    # For deduplication with pixel
            'action_source': 'website',          # website, app, offline, etc.
            'event_source_url': 'https://site.com/page',
            'user_data': {
                'em': ['sha256_hashed_email'],   # MUST be hashed
                'ph': ['sha256_hashed_phone'],   # MUST be hashed, E.164 format
                'fn': ['sha256_hashed_first'],   # MUST be hashed, lowercase
                'ln': ['sha256_hashed_last'],    # MUST be hashed, lowercase
                'fbp': 'fb.1.123.456',           # NOT hashed (browser cookie)
                'fbc': 'fb.1.123.456',           # NOT hashed (click cookie)
                'external_id': ['sha256_hashed_id'],
                'client_ip_address': '1.2.3.4',
                'client_user_agent': 'Mozilla/5.0...'
            },
            'custom_data': {
                'value': 99.99,                  # Required for Purchase
                'currency': 'USD',               # Required for Purchase
                'content_ids': ['product123'],
                'content_type': 'product',
                'order_id': 'order-456'
            }
        }
    ],
    'access_token': token
}
```

### Standard Event Names

`Purchase`, `Lead`, `ViewContent`, `AddToCart`, `InitiateCheckout`, `CompleteRegistration`, `AddPaymentInfo`, `AddToWishlist`, `Contact`, `FindLocation`, `Schedule`, `Search`, `StartTrial`, `SubmitApplication`, `Subscribe`, `CustomizeProduct`, `Donate`

### Deduplication

- Both Pixel and CAPI must send identical `event_name` + `event_id`
- Meta auto-deduplicates matching events
- Without deduplication, conversions counted twice
- Generate `event_id` on server, pass to both Pixel and CAPI

### user_data Hashing Rules

| Field | Hash? | Notes |
|-------|-------|-------|
| `em` (email) | SHA-256 | Normalize to lowercase first |
| `ph` (phone) | SHA-256 | E.164 format, no spaces/dashes |
| `fn` (first name) | SHA-256 | Lowercase |
| `ln` (last name) | SHA-256 | Lowercase |
| `external_id` | SHA-256 | Your customer ID |
| `fbp` | **NO** | Browser cookie, send raw |
| `fbc` | **NO** | Click cookie, send raw |
| `client_ip_address` | **NO** | Send raw |
| `client_user_agent` | **NO** | Send raw |

**CRITICAL:** Hashing `fbp` or `fbc` breaks matching entirely.

---

## Image Upload

**Endpoint:** `POST /{account_id}/adimages`

### Requirements

- Format: JPG or PNG
- Max size: 30MB
- Recommended: 1080x1080px minimum
- Aspect ratios: 1:1 (feed), 4:5 (feed), 9:16 (stories/reels)

### Response

```json
{
  "images": {
    "filename.jpg": {
      "hash": "a1b2c3d4e5f6...",
      "url": "https://scontent.xx.fbcdn.net/...",
      "height": 1080,
      "width": 1080
    }
  }
}
```

---

## Video Upload

**Endpoint:** `POST /{account_id}/advideos`

### Requirements

- Format: MP4, MOV (H.264 codec recommended)
- Max size: 4GB
- Feed: 1s to 240 minutes, aspect 4:5 or 1:1
- Stories/Reels: 1-60s (15s recommended), aspect 9:16
- Thumbnail REQUIRED for ad creation - fetch from `GET /{video_id}/thumbnails`

### Chunked Upload (for files >100MB)

Three phases:
1. `upload_phase=start` + `file_size` -> returns `upload_session_id`
2. `upload_phase=transfer` + `upload_session_id` + `start_offset` + `video_file_chunk` (loop)
3. `upload_phase=finish` + `upload_session_id` + `title` -> returns video ID

---

## Pagination

```python
data = r.json()
results = data.get('data', [])

while 'paging' in data and 'next' in data['paging']:
    r = requests.get(data['paging']['next'])
    data = r.json()
    results.extend(data.get('data', []))
```

---

## CRUD Operations

### Create

```python
r = requests.post(f'https://graph.facebook.com/v22.0/{parent_id}/{edge}', data={...})
# edge: campaigns, adsets, ads, adcreatives, adimages, advideos, customaudiences
```

### Read

```python
r = requests.get(f'https://graph.facebook.com/v22.0/{object_id}', params={
    'fields': 'field1,field2,...',
    'access_token': token
})
```

### Update

```python
r = requests.post(f'https://graph.facebook.com/v22.0/{object_id}', data={
    'name': 'New Name',
    'status': 'PAUSED',
    'access_token': token
})
```

### Delete

```python
r = requests.delete(f'https://graph.facebook.com/v22.0/{object_id}', params={
    'access_token': token
})
```

---

## Key Gotchas & Rules

1. **Always Python, never curl** - token contains characters that get mangled by shell interpolation
2. **Always load token from `.env`** via `dotenv` - never paste tokens into commands
3. **Budgets in cents** - 5000 = $50.00
4. **`is_adset_budget_sharing_enabled` is a string** - `"true"` / `"false"`, not boolean
5. **To update URLs, copy, or any creative content** - POST to the AD (not the creative) with inline `creative` JSON containing the full spec with changes. `url_tags` can also be changed this way.
6. **Instagram account in TWO places** - both top-level `instagram_user_id` and inside `object_story_spec`
7. **Minimal `object_story_spec` with `asset_feed_spec`** - only page_id + instagram_user_id, no link_data
8. **`optimization_type: PLACEMENT`** for different images per placement, `REGULAR` for dynamic creative
9. **`REGULAR` limits to 1 ad per ad set** - use `PLACEMENT` when you need multiple ads
10. **Video thumbnails required** - fetch from `/{video_id}/thumbnails` after upload
11. **Files >100MB fail single upload** - always use chunked upload for large videos
12. **Exclude Singapore** from targeting to avoid regulatory compliance fields
13. **Custom Audience TOS** - Error 1359208 requires re-accepting terms in Ads Manager UI (API cannot detect this)
14. **Empty `data: []` = no activity** in that period, not an error
15. **Cannot combine delivery + action breakdowns** in same insights request
16. **Ad copy formatting** - always use `\n\n` between paragraphs, `\n` within lists
17. **Threads profile identity** - set `threads_user_id` at the creative level (NOT inside `object_story_spec`). To find the Threads profile ID, check an existing working creative: `GET /{creative_id}?fields=threads_user_id`. The Threads profile is tied to the Instagram account, not the Facebook Page directly.
