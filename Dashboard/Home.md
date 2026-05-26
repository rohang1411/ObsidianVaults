---
cssclasses:
  - vault-home
---

```dataviewjs
const pages = dv.pages().where(p => p.file.path !== dv.current().file.path && p.file.ext === "md");

const safe = (value) => String(value ?? "")
  .replace(/&/g, "&amp;")
  .replace(/</g, "&lt;")
  .replace(/>/g, "&gt;")
  .replace(/"/g, "&quot;");

const notePath = (path) => String(path).replace(/\.md$/, "");
const wiki = (path, label) =>
  `<a class="internal-link" data-href="${safe(notePath(path))}" href="${safe(notePath(path))}">${safe(label)}</a>`;
const openSearch = (label, query) =>
  `<a class="vault-search-card" href="obsidian://search?query=${encodeURIComponent(query)}">
    <span>${safe(label)}</span>
    <small>${safe(query)}</small>
  </a>`;
const inArea = (page, area) => {
  const path = String(page.file.path ?? "").replaceAll("\\", "/");
  const folder = String(page.file.folder ?? "").replaceAll("\\", "/");
  return path.startsWith(`${area}/`) || path.includes(`/${area}/`) || folder === area || folder.endsWith(`/${area}`) || folder.includes(`/${area}/`);
};
const areaPages = (area) => pages.where(p => inArea(p, area));
const count = (area) => areaPages(area).length;
const modifiedWithin = (days) => pages.where(p => p.file.mtime >= dv.date("today").minus({ days })).length;
const areaName = (page) => {
  const path = String(page.file.path ?? "").replaceAll("\\", "/");
  for (const area of ["Deep Learning", "Infinitune", "Interview Prep", "Prompts", "LeetCode", "Tutorials"]) {
    if (path.startsWith(`${area}/`) || path.includes(`/${area}/`)) return area;
  }
  return "Root";
};
const recent = pages.sort(p => p.file.mtime, "desc").limit(8).array();

const workspaces = [
  {
    title: "Deep Learning",
    noteCount: count("Deep Learning"),
    description: "Concepts, architectures, math, and revision material.",
    links: [
      ["Deep Learning/Transformers", "Transformers"],
      ["Deep Learning/Attention", "Attention"],
      ["Deep Learning/Backpropagation", "Backpropagation"],
      ["Deep Learning/CheatSheet", "Cheat Sheet"]
    ]
  },
  {
    title: "Infinitune",
    noteCount: count("Infinitune"),
    description: "Project overview, architecture, implementation, and interviews.",
    links: [
      ["Infinitune/1. Project Overview/Project Readme", "Project Readme"],
      ["Infinitune/4. Architecture & Code Deep-Dive/1. System Architecture", "Architecture"],
      ["Infinitune/4. Architecture & Code Deep-Dive/2. Code Walkthrough", "Code Walkthrough"],
      ["Infinitune/5. Interview Preparation Guide/Interview Q&A", "Interview Q&A"]
    ]
  },
  {
    title: "Interview Prep",
    noteCount: count("Interview Prep"),
    description: "Behavioral, CS, DS, and project talking points.",
    links: [
      ["Interview Prep/Basic CS Questions", "Basic CS"],
      ["Interview Prep/Basic DS Questions", "Basic DS"],
      ["Interview Prep/Behavioral Interview Questions", "Behavioral"],
      ["Infinitune/5. Interview Preparation Guide/Project Talking Points", "Project Talking Points"]
    ]
  },
  {
    title: "Prompts",
    noteCount: count("Prompts"),
    description: "Reusable systems for applications, outreach, and study.",
    links: [
      ["Prompts/Resume Tailoring", "Resume Tailoring"],
      ["Prompts/Cover Letters", "Cover Letters"],
      ["Prompts/Job Application Question Answers", "Application Answers"],
      ["Prompts/Cheatsheet Generation", "Cheatsheet Generation"]
    ]
  },
  {
    title: "Coding Practice",
    noteCount: count("LeetCode"),
    description: "Problem solving and fundamentals for technical interviews.",
    links: [
      ["LeetCode/355. Design Twitter", "Design Twitter"],
      ["Interview Prep/Basic CS Questions", "CS Fundamentals"],
      ["Interview Prep/Basic DS Questions", "DS Fundamentals"]
    ]
  },
  {
    title: "Vault Utilities",
    noteCount: count("Tutorials") + 1,
    description: "Dashboards, setup notes, and project maps.",
    links: [
      ["Dashboard", "Main Dashboard"],
      ["Tutorials/Obsidian Setup Tutorial", "Obsidian Setup"],
      ["README", "Vault README"]
    ]
  }
];

const workspaceCards = workspaces.map(space => `
  <article class="vault-card">
    <div class="vault-card-head">
      <div>
        <h3>${safe(space.title)}</h3>
        <p>${safe(space.description)}</p>
      </div>
      <strong>${space.noteCount}</strong>
    </div>
    <div class="vault-link-list">
      ${space.links.map(([path, label]) => wiki(path, label)).join("")}
    </div>
  </article>
`).join("");

const recentRows = recent.map(page => `
  <a class="vault-recent-row internal-link" data-href="${safe(notePath(page.file.path))}" href="${safe(notePath(page.file.path))}">
    <span>${safe(page.file.name)}</span>
    <small>${safe(areaName(page))}</small>
    <time>${page.file.mtime.toFormat("MMM d")}</time>
  </a>
`).join("");

const continueItems = [
  ["Deep Learning", areaPages("Deep Learning").sort(p => p.file.mtime, "desc").array()[0]],
  ["Infinitune", areaPages("Infinitune").sort(p => p.file.mtime, "desc").array()[0]],
  ["Interview Prep", areaPages("Interview Prep").sort(p => p.file.mtime, "desc").array()[0]],
  ["Prompts", areaPages("Prompts").sort(p => p.file.mtime, "desc").array()[0]]
].filter(([, page]) => page).map(([label, page]) => `
  <a class="vault-continue-card internal-link" data-href="${safe(notePath(page.file.path))}" href="${safe(notePath(page.file.path))}">
    <small>${safe(label)}</small>
    <span>${safe(page.file.name)}</span>
    <time>${page.file.mtime.toFormat("MMM d, yyyy")}</time>
  </a>
`).join("");

const root = dv.el("div", "", { cls: "vault-dashboard" });
root.innerHTML = `
  <section class="vault-hero">
    <div>
      <span class="vault-kicker">Home</span>
      <h1>Rohan's Vault</h1>
      <p>Fast access to learning, interview prep, project knowledge, prompts, and coding practice.</p>
    </div>
    <div class="vault-actions">
      <a href="obsidian://new">New Note</a>
      <a href="obsidian://search">Search</a>
      <a href="obsidian://show-graph">Graph</a>
      ${wiki("Deep Learning/CheatSheet", "Cheat Sheet")}
      ${wiki("Prompts/Prep Doc", "Prep Doc")}
    </div>
  </section>

  <section class="vault-stats" aria-label="Vault stats">
    <div><strong>${pages.length}</strong><span>Total notes</span></div>
    <div><strong>${modifiedWithin(7)}</strong><span>Updated this week</span></div>
    <div><strong>${count("Deep Learning")}</strong><span>Deep Learning</span></div>
    <div><strong>${count("Infinitune")}</strong><span>Infinitune</span></div>
  </section>

  <div class="vault-section-head">
    <h2>Workspaces</h2>
    <p>Primary launch points for the areas you use most.</p>
  </div>
  <section class="vault-card-grid">${workspaceCards}</section>

  <section class="vault-two-column">
    <div class="vault-panel">
      <div class="vault-section-head compact">
        <h2>Continue Working</h2>
        <p>Newest note from each major area.</p>
      </div>
      <div class="vault-continue-grid">${continueItems}</div>
    </div>
    <div class="vault-panel">
      <div class="vault-section-head compact">
        <h2>Recently Updated</h2>
        <p>Your latest edits across the vault.</p>
      </div>
      <div class="vault-recent-list">${recentRows}</div>
    </div>
  </section>

  <div class="vault-section-head">
    <h2>Saved Searches</h2>
    <p>Open targeted searches only when you need the result list.</p>
  </div>
  <section class="vault-search-grid">
    ${openSearch("Deep Learning", 'path:"Deep Learning"')}
    ${openSearch("Infinitune Architecture", 'path:"Infinitune" architecture OR "code walkthrough"')}
    ${openSearch("Interview Prep", 'path:"Interview Prep" OR path:"Infinitune/5. Interview Preparation Guide"')}
    ${openSearch("Job Prompts", 'path:"Prompts" resume OR cover OR application OR email')}
    ${openSearch("Transformers Stack", 'Transformers OR Attention OR LoRA OR QLoRA')}
  </section>

  <div class="vault-section-head">
    <h2>Study Path</h2>
    <p>A quick sequence for revision and project explanation practice.</p>
  </div>
  <section class="vault-study-path">
    ${wiki("Deep Learning/Pre-requisites", "Prerequisites")}
    ${wiki("Deep Learning/Backpropagation", "Backpropagation")}
    ${wiki("Deep Learning/Attention", "Attention")}
    ${wiki("Deep Learning/Transformers", "Transformers")}
    ${wiki("Infinitune/2. Summaries/2. Medium Summary (5-Min)", "Infinitune 5-Min")}
  </section>
`;
```

## Vault Activity

```contributionGraph
title: Note Contributions
graphType: month-track
dateRangeValue: 3
dateRangeType: LATEST_MONTH
startOfWeek: 0
showCellRuleIndicators: false
titleStyle:
  textAlign: center
  fontSize: 14px
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

> [!database]- Browse Vault Database
> ```base
> filters:
>   and:
>     - file.ext == "md"
> properties:
>   file.name:
>     displayName: Note
>   file.folder:
>     displayName: Area
>   file.mtime:
>     displayName: Updated
> views:
>   - type: table
>     name: Recent Notes
>     limit: 20
>     order:
>       - file.name
>       - file.folder
>       - file.mtime
>   - type: table
>     name: Deep Learning
>     filters:
>       and:
>         - 'file.inFolder("Deep Learning")'
>     order:
>       - file.name
>       - file.mtime
>   - type: table
>     name: Infinitune
>     filters:
>       and:
>         - 'file.inFolder("Infinitune")'
>     order:
>       - file.name
>       - file.folder
>       - file.mtime
> ```

> [!map]- Infinitune Project Map
> ![[Infinitune/Flowchart.canvas]]
