#!/usr/bin/env node
// Validates the gtm-skills repo layout and frontmatter. Zero dependencies.
// Run from the repo root: node tools/validate.mjs
// Errors are written one per line, formatted for both humans and agents:
//   <path>: <what is wrong> — <how to fix it>

import fs from 'node:fs';
import path from 'node:path';

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const SKILLS_DIR = path.join(ROOT, 'skills');

const ALLOWED_EXTENSIONS = new Set([
  '.md', '.txt', '.json', '.csv', '.yaml', '.yml', '.py', '.sql', '.docx', '.pdf', '.png',
]);
const KEBAB = /^[a-z0-9][a-z0-9-]*$/;
const FILE_SEGMENT = /^[A-Za-z0-9][A-Za-z0-9._-]*\.[A-Za-z0-9]+$/;
const DIR_SEGMENT = /^[A-Za-z0-9][A-Za-z0-9_-]*$/;
// Categories the site renders (app/lib/skills.ts in gtm-skills-web) — anything else
// merges fine but shows uncategorized, so we catch it here.
const CATEGORIES = new Set([
  'Prospecting', 'Research', 'Positioning', 'Signals', 'ABM', 'Outreach', 'Deals',
  'Events', 'Pricing', 'Reddit', 'AEO', 'RevOps', 'Sales', 'SEO', 'Influencers',
  'Ads', 'Affiliates', 'Newsletters',
]);

// Authors who predate the email requirement (2026-08-07). New submissions hard-fail
// without `email:`; these stay warnings until backfilled. Remove slugs as emails land —
// this list only shrinks.
const EMAIL_GRANDFATHERED = new Set([
  'alex-vacca',
  'amos-bar-joseph',
  'ariel-cohen',
  'austin-hay',
  'bojan-berisavljevic',
  'brad-smith',
  'brianne-thomas',
  'daniel-bustamante',
  'danni-chen',
  'dave-engel',
  'din-arbel',
  'dusan-vystrcil',
  'emilia-korczynska',
  'gal-tamir',
  'huxley-peckham',
  'ido-goldberg',
  'ivan-falco',
  'jeremy-hurst',
  'john-williams',
  'jorge-macias',
  'katya-tarapovskaia',
  'kevin-kd-dorsey',
  'luke-shalom',
  'maja-voje',
  'manny-medina',
  'maxwell-nimmo',
  'omer-levy',
  'pete-mientkiewicz',
  'peter-cools',
  'rutger-katz',
  'ryan-estes',
  'sabahudin-murtic',
  'sam-dunning',
  'sangram-vajre',
  'steve-armenti',
  'thomas-marcelle',
  'tim-yakubson',
  'udi-cohen',
  'victor-moen',
  'yahav-fuchs',
]);

const FORBIDDEN_SKILL_KEYS = [
  'prefix', 'slug', 'author', 'apps', 'authorAvatar', 'authorUrl', 'isDefault', 'isOrgEditable', 'license',
];

const errors = [];
const err = (file, message) => errors.push(`${file}: ${message}`);

const warnings = [];
const warn = (file, message) => warnings.push(`${file}: ${message}`);

const rel = (p) => path.relative(ROOT, p);

// Minimal YAML frontmatter reader: top-level `key: value` pairs, `key: [a, b]`
// inline lists, `key:` + `- item` dash lists, and `key: |` block scalars.
const parseFrontmatter = (raw) => {
  if (!raw.startsWith('---\n')) return null;
  const end = raw.indexOf('\n---', 4);
  if (end === -1) return null;
  const block = raw.slice(4, end);
  const data = {};
  let currentListKey = null;
  for (const line of block.split('\n')) {
    if (!line.trim() || line.trim().startsWith('#')) continue;
    if (/^\s/.test(line)) {
      // Indented: block-scalar content or nested value; count toward the last key's value.
      const trimmed = line.trim();
      if (currentListKey && trimmed.startsWith('- ')) {
        data[currentListKey].push(trimmed.slice(2).trim());
      } else if (data.__lastKey && typeof data[data.__lastKey] === 'string') {
        data[data.__lastKey] += ` ${trimmed}`;
      }
      continue;
    }
    if (line.startsWith('- ') && currentListKey) {
      data[currentListKey].push(line.slice(2).trim());
      continue;
    }
    const match = line.match(/^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.*)$/);
    if (!match) continue;
    const [, key, value] = match;
    currentListKey = null;
    if (value === '' ) {
      data[key] = [];
      currentListKey = key;
    } else if (value === '|' || value === '>') {
      data[key] = '';
      data.__lastKey = key;
      continue;
    } else if (value.startsWith('[') && value.endsWith(']')) {
      data[key] = value.slice(1, -1).split(',').map((s) => s.trim()).filter(Boolean);
    } else {
      data[key] = value.replace(/^["']|["']$/g, '');
    }
    data.__lastKey = key;
  }
  delete data.__lastKey;
  return data;
};

const readFrontmatter = (file) => {
  const raw = fs.readFileSync(file, 'utf8');
  const data = parseFrontmatter(raw);
  if (!data) err(rel(file), 'missing YAML frontmatter — start the file with a --- fenced block');
  return data ?? {};
};

const walkFiles = (dir) => {
  const out = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) out.push(...walkFiles(full));
    else out.push(full);
  }
  return out;
};

// --- Repo-level rules ---------------------------------------------------------

if (fs.existsSync(path.join(ROOT, 'SKILL.md'))) {
  err('SKILL.md', 'a SKILL.md at the repo root makes `npx skills` treat this as a single-skill repo and hides the whole library — remove it');
}
if (!fs.existsSync(SKILLS_DIR)) {
  err('skills/', 'directory is missing');
  report();
}

// --- Author directories -------------------------------------------------------

const authorSlugs = new Set();
const skillSlugOwners = new Map(); // skill slug -> author slug

for (const entry of fs.readdirSync(SKILLS_DIR, { withFileTypes: true })) {
  if (!entry.isDirectory()) {
    err(rel(path.join(SKILLS_DIR, entry.name)), 'loose file directly under skills/ — skills live in skills/<author>/<skill>/');
    continue;
  }
  if (entry.name.startsWith('.')) continue; // system space (skills/.system/), validated separately below
  const authorDir = path.join(SKILLS_DIR, entry.name);
  const authorSlug = entry.name;

  if (!KEBAB.test(authorSlug)) {
    err(rel(authorDir), `author directory "${authorSlug}" is not kebab-case (lowercase letters, digits, hyphens)`);
  }
  authorSlugs.add(authorSlug);

  const authorMd = path.join(authorDir, 'author.md');
  if (!fs.existsSync(authorMd)) {
    err(rel(authorDir), 'missing author.md — create it from templates/author.md (your profile lives at the root of your directory)');
  } else {
    const fm = readFrontmatter(authorMd);
    if (!fm.name) err(rel(authorMd), 'frontmatter is missing `name:` (the author\'s full name)');
    if (fm.slug) err(rel(authorMd), 'remove `slug:` — the directory name is the slug');
    if (!fm.linkedinUrl) {
      err(rel(authorMd), 'frontmatter is missing `linkedinUrl:` — the person\'s own LinkedIn profile is the primary identity check');
    } else if (!/linkedin\.com\/in\//.test(fm.linkedinUrl)) {
      err(rel(authorMd), '`linkedinUrl:` must be a personal profile (linkedin.com/in/<handle>), not a company or product page');
    }
    if (!fm.companyDomain) {
      err(rel(authorMd), 'frontmatter is missing `companyDomain:` — it powers your company page and logo on gtmskills.com (a personal site\'s domain works too)');
    } else if (!/^[a-z0-9][a-z0-9.-]*\.[a-z]{2,}$/.test(fm.companyDomain)) {
      err(rel(authorMd), `\`companyDomain: ${fm.companyDomain}\` should be a bare domain like acme.com — no protocol, no path`);
    }
    if (!fm.email) {
      if (EMAIL_GRANDFATHERED.has(authorSlug)) {
        warn(rel(authorMd), 'no `email:` (grandfathered) — backfill so maintainers can send acceptance/rejection and review mail');
      } else {
        err(rel(authorMd), 'frontmatter is missing `email:` — required; maintainers use it for acceptance, rejection, and review questions. Use a work address you\'re comfortable having public');
      }
    }
    if (!fm.avatarUrl) warn(rel(authorMd), 'no `avatarUrl:` — maintainers will take your LinkedIn photo and re-host it (submitting means you\'re OK with that)');
  }
  if (fs.existsSync(path.join(authorDir, 'SKILL.md'))) {
    err(rel(path.join(authorDir, 'SKILL.md')), 'SKILL.md directly in an author directory — each skill needs its own folder: skills/<author>/<skill>/SKILL.md');
  }

  for (const child of fs.readdirSync(authorDir, { withFileTypes: true })) {
    if (!child.isDirectory()) {
      if (child.name !== 'author.md') {
        err(rel(path.join(authorDir, child.name)), 'unexpected loose file in an author directory — only author.md and skill folders belong here');
      }
      continue;
    }
    validateSkillDir(path.join(authorDir, child.name), authorSlug);
  }
}

function validateSkillDir(skillDir, authorSlug) {
  const skillSlug = path.basename(skillDir);

  if (skillSlug === 'author') {
    err(rel(skillDir), '"author" is a reserved name — rename the skill folder');
    return;
  }
  if (!KEBAB.test(skillSlug)) {
    err(rel(skillDir), `skill folder "${skillSlug}" is not kebab-case`);
  }
  if (skillSlugOwners.has(skillSlug)) {
    err(rel(skillDir), `slug "${skillSlug}" already exists under skills/${skillSlugOwners.get(skillSlug)}/ — skill slugs are globally unique; pick another name`);
  } else {
    skillSlugOwners.set(skillSlug, authorSlug);
  }

  const skillMd = path.join(skillDir, 'SKILL.md');
  if (!fs.existsSync(skillMd)) {
    err(rel(skillDir), 'missing SKILL.md — every skill folder needs one; start from templates/skill/SKILL.md');
    return;
  }
  const fm = readFrontmatter(skillMd);
  if (!fm.name) err(rel(skillMd), 'frontmatter is missing `name:` — required by npx skills; must equal the folder name');
  else if (fm.name !== skillSlug) {
    err(rel(skillMd), `\`name: ${fm.name}\` must equal the folder name "${skillSlug}" — one identity, nothing to drift`);
  }
  if (!fm.title) err(rel(skillMd), 'frontmatter is missing `title:` (the human display name)');
  if (!fm.description) err(rel(skillMd), 'frontmatter is missing `description:` — required by npx skills and by the library router');
  if (!fm.category) {
    err(rel(skillMd), 'frontmatter is missing `category:` — pick one the site already renders (see the list in tools/validate.mjs)');
  } else if (!CATEGORIES.has(fm.category)) {
    err(rel(skillMd), `\`category: ${fm.category}\` isn't one the site renders — it would publish uncategorized. Known: ${[...CATEGORIES].join(', ')}`);
  }
  for (const key of FORBIDDEN_SKILL_KEYS) {
    if (key in fm) err(rel(skillMd), `remove \`${key}:\` — ${key === 'prefix' || key === 'isDefault' || key === 'isOrgEditable' ? 'Swan lifecycle flags are decided in the database, never in this repo' : 'this field is no longer part of the spec'}`);
  }
  for (const contributor of fm.contributors ?? []) {
    if (!fs.existsSync(path.join(SKILLS_DIR, contributor, 'author.md'))) {
      err(rel(skillMd), `contributor "${contributor}" has no profile — every contributor slug must match an existing skills/<slug>/author.md`);
    }
  }

  for (const file of walkFiles(skillDir)) {
    const relToSkill = path.relative(skillDir, file);
    const segments = relToSkill.split(path.sep);
    const fileName = segments.at(-1);
    if (!ALLOWED_EXTENSIONS.has(path.extname(fileName).toLowerCase())) {
      err(rel(file), `extension "${path.extname(fileName)}" is not allowed — permitted: ${[...ALLOWED_EXTENSIONS].join(' ')}`);
    }
    if (!FILE_SEGMENT.test(fileName)) {
      err(rel(file), 'file name must start with an alphanumeric and contain only letters, digits, dot, underscore, hyphen, with an extension');
    }
    for (const dir of segments.slice(0, -1)) {
      if (dir === 'prev-versions') err(rel(file), '"prev-versions" is a reserved directory name inside a skill');
      if (!DIR_SEGMENT.test(dir)) err(rel(file), `directory segment "${dir}" must be alphanumeric with underscores/hyphens and no dots`);
    }
  }
}

// System space: skills/.system/<name>/SKILL.md — internal-only skills (e.g. submit-skill).
const systemDir = path.join(SKILLS_DIR, '.system');
if (fs.existsSync(systemDir)) {
  for (const entry of fs.readdirSync(systemDir, { withFileTypes: true })) {
    if (!entry.isDirectory()) continue;
    const skillMd = path.join(systemDir, entry.name, 'SKILL.md');
    if (!fs.existsSync(skillMd)) {
      err(rel(path.join(systemDir, entry.name)), 'missing SKILL.md');
      continue;
    }
    const fm = readFrontmatter(skillMd);
    if (!fm.name || !fm.description) err(rel(skillMd), 'system skills still need `name:` and `description:`');
  }
}

function report() {
  for (const w of warnings) console.warn(`warn — ${w}`);
  if (errors.length) {
    console.error(`${errors.length} problem${errors.length === 1 ? '' : 's'} found:\n`);
    for (const line of errors) console.error(`  ${line}`);
    process.exit(1);
  }
  console.log(`ok — ${skillSlugOwners.size} skills across ${authorSlugs.size} creators, all checks passed`);
  process.exit(0);
}

report();
