---
editor-width: 100
banner: "![[IMAGE_FILE_NAME.PNG/JPG/WHATEVER]]"
cssclasses:
  - hide-properties
---

```dataviewjs
// === CONFIG ===
const dailyFolder = "00 - Daily/";
const weeklyFolder = "01 - Weekly/";
const dateFormat = "yyyy-MM-dd";
const weekFormat = "kkkk-'W'WW";

// === BUILD PATHS ===
const today = dv.date("today");
const dailyPath = `${dailyFolder}${today.toFormat(dateFormat)}`;
const weeklyPath = `${weeklyFolder}${today.toFormat(weekFormat)}`;

// === BUTTONS ===
let content = "";
content += `<a class="internal-link elegant-btn ready" href="${dailyPath}">📅 Today</a>`;
content += `<a class="internal-link elegant-btn ready" href="${weeklyPath}">🗓️ This Week</a>`;

// === OUTPUT ===
dv.el("div", `<div class="breadcrumbs-wrapper">${content}</div>`);
```

```search-bar
show recent files
```

```contributionGraph
title: Note Contributions
graphType: month-track
dateRangeValue: 1
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

---

![[Academic Library.base]]

```dataviewjs
// Create container
let container = dv.el("div", "", {cls: "tag-cloud-container"});

// Get all pages
let pages = dv.pages();

// Flatten all tags across all pages
let allTags = [];
for (let page of pages) {
    if (page.file.tags) {
        allTags.push(...page.file.tags);
    }
}

// Count occurrences of each tag
let tagCounts = allTags.reduce((acc, tag) => {
    acc[tag] = (acc[tag] || 0) + 1;
    return acc;
}, {});

// 🔹 Sort tags alphabetically
let sortedTags = Object.keys(tagCounts).sort((a, b) => a.localeCompare(b));

// Render each tag as clickable link
for (let tag of sortedTags) {
    let count = tagCounts[tag];
    let link = dv.el(
        "a",
        `${tag} (${count})`,
        {
            href: `obsidian://search?query=${encodeURIComponent(tag)}`,
            cls: "tag-chip"
        }
    );
    link.style.margin = "2px"; // add spacing
    container.appendChild(link);
}

```
<div style="height: 25px;"></div>

---
<div style="height: 25px;"></div>
<iframe src="https://jandee.vercel.app/mermo-code" width="100%" height="275px"></iframe>
