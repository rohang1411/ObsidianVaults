---
banner: "https://images.unsplash.com/photo-1550684848-fac1c5b4e853?q=80&w=2070&auto=format&fit=crop"
banner_y: 0.53
cssclasses:
  - notion-dashboard
  - vault-home
---

# Rohan's Vault
Deep learning, interview prep, project notes, prompts, and coding practice in one command center.

> [!quick-actions]-
> - [New Note](obsidian://new)
> - [Search Vault](obsidian://search)
> - [Graph View](obsidian://show-graph)
> - [[Dashboard|Main Dashboard]]
> - [[Deep Learning/CheatSheet|Deep Learning Cheat Sheet]]
> - [[Prompts/Prep Doc|Prep Doc]]

```dataviewjs
const pages = dv.pages().where(p => p.file.path !== dv.current().file.path);
const totalNotes = pages.length;
const updatedThisWeek = pages.where(p => p.file.mtime >= dv.date("today").minus({ days: 7 })).length;
const projectNotes = pages.where(p => p.file.folder.startsWith("Infinitune")).length;
const deepLearningNotes = pages.where(p => p.file.folder.startsWith("Deep Learning")).length;

dv.el("div", `
<div class="home-stats">
  <div><span>${totalNotes}</span><small>Total notes</small></div>
  <div><span>${updatedThisWeek}</span><small>Updated this week</small></div>
  <div><span>${deepLearningNotes}</span><small>Deep learning</small></div>
  <div><span>${projectNotes}</span><small>Infinitune</small></div>
</div>
`);
```

## Focus Areas

- ### Deep Learning
  Core ML concepts, neural networks, math foundations, and architecture notes.
  - [[Deep Learning/Transformers|Transformers]]
  - [[Deep Learning/Attention|Attention]]
  - [[Deep Learning/Backpropagation|Backpropagation]]
  - [[Deep Learning/Convolutional Neural Network (CNN)|Convolutional Neural Networks]]
  - [[Deep Learning/Variational Auto Encoders|Variational Auto Encoders]]
  - [[Deep Learning/CheatSheet|Cheat Sheet]]

- ### Infinitune
  Architecture, implementation notes, summaries, interview material, and future work.
  - [[Infinitune/1. Project Overview/Project Readme|Project Readme]]
  - [[Infinitune/2. Summaries/1. Short Summary (1-Min)|1-Min Summary]]
  - [[Infinitune/4. Architecture & Code Deep-Dive/1. System Architecture|System Architecture]]
  - [[Infinitune/4. Architecture & Code Deep-Dive/2. Code Walkthrough|Code Walkthrough]]
  - [[Infinitune/5. Interview Preparation Guide/Interview Q&A|Interview Q&A]]
  - [[Infinitune/6. Future Work & Research/Future Improvements|Future Improvements]]

- ### Interview Prep
  Fast access to CS, DS, behavioral, and project talking points.
  - [[Interview Prep/Basic CS Questions|Basic CS Questions]]
  - [[Interview Prep/Basic DS Questions|Basic DS Questions]]
  - [[Interview Prep/Behavioral Interview Questions|Behavioral Questions]]
  - [[Infinitune/5. Interview Preparation Guide/Project Talking Points|Infinitune Talking Points]]

- ### Prompts
  Reusable job-search, application, outreach, and study prompts.
  - [[Prompts/Resume Tailoring|Resume Tailoring]]
  - [[Prompts/Cover Letters|Cover Letters]]
  - [[Prompts/Job Application Question Answers|Application Answers]]
  - [[Prompts/AI ML DS Cold Email|AI/ML/DS Cold Email]]
  - [[Prompts/SDE Cold Email|SDE Cold Email]]
  - [[Prompts/Cheatsheet Generation|Cheatsheet Generation]]

- ### Coding Practice
  Data structures, systems thinking, and implementation practice.
  - [[LeetCode/355. Design Twitter|355. Design Twitter]]
  - [[Interview Prep/Basic CS Questions|CS Fundamentals]]
  - [[Interview Prep/Basic DS Questions|DS Fundamentals]]

- ### Vault Utilities
  Setup notes, dashboards, and visual maps.
  - [[Tutorials/Obsidian Setup Tutorial|Obsidian Setup Tutorial]]
  - [[Dashboard|Main Dashboard]]
  - [[README|Vault README]]

## Recently Updated

```dataview
TABLE WITHOUT ID
  file.link AS Note,
  file.folder AS Area,
  dateformat(file.mtime, "MMM d, yyyy") AS Updated
FROM ""
WHERE file.name != this.file.name
SORT file.mtime DESC
LIMIT 12
```

## Study Queue

```dataview
LIST
FROM "Deep Learning" OR "Infinitune"
WHERE contains(file.name, "Transformers")
   OR contains(file.name, "Attention")
   OR contains(file.name, "QLoRA")
   OR contains(file.name, "LoRA")
   OR contains(file.name, "Perplexity")
SORT file.name ASC
```

## Vault Base

```base
filters:
  and:
    - file.ext == "md"
properties:
  file.name:
    displayName: Note
  file.folder:
    displayName: Area
  file.mtime:
    displayName: Updated
views:
  - type: table
    name: Recent Notes
    limit: 20
    order:
      - file.name
      - file.folder
      - file.mtime
  - type: table
    name: Deep Learning
    filters:
      and:
        - 'file.inFolder("Deep Learning")'
    order:
      - file.name
      - file.mtime
  - type: table
    name: Infinitune
    filters:
      and:
        - 'file.inFolder("Infinitune")'
    order:
      - file.name
      - file.folder
      - file.mtime
```

## Search Console

```search-bar
show recent files
```

```query
path:"Deep Learning" OR path:"Infinitune" OR path:"Interview Prep"
```

## Contribution Graph

```contributionGraph
title: Note Contributions
graphType: month-track
dateRangeValue: 3
dateRangeType: LATEST_MONTH
startOfWeek: 0
showCellRuleIndicators: true
titleStyle:
  textAlign: center
  fontSize: 15px
  fontWeight: normal
dataSource:
  type: PAGE
  value: ""
  dateField:
    type: FILE_MTIME
  filters: []
  countField:
    type: DEFAULT
fillTheScreen: false
enableMainContainerShadow: false
cellStyleRules: []
```

## Tag Cloud

```dataviewjs
let tags = {};
for (let page of dv.pages()) {
  for (let tag of page.file.tags ?? []) {
    tags[tag] = (tags[tag] ?? 0) + 1;
  }
}

let entries = Object.entries(tags).sort((a, b) => a[0].localeCompare(b[0]));
if (!entries.length) {
  dv.paragraph("No tags found yet.");
} else {
  let html = entries.map(([tag, count]) =>
    `<a class="tag-chip" href="obsidian://search?query=${encodeURIComponent(tag)}">${tag} <span>${count}</span></a>`
  ).join("");
  dv.el("div", html, { cls: "tag-cloud-container" });
}
```

## System Architecture Map

![[Infinitune/Flowchart.canvas]]
