---
cssclasses:
  - vault-home
  - hide-properties
---

```dataviewjs
const pages = dv.pages().where(p => p.file.path !== dv.current().file.path && p.file.ext === "md");

const safe = (value) => String(value ?? "")
  .replace(/&/g, "&amp;")
  .replace(/</g, "&lt;")
  .replace(/>/g, "&gt;")
  .replace(/"/g, "&quot;");

const notePath = (path) => String(path).replace(/\.md$/, "");
const link = (path, label, extra = "") =>
  `<a class="internal-link" data-href="${safe(notePath(path))}" href="${safe(notePath(path))}" style="${extra}">${safe(label)}</a>`;

const inArea = (page, area) => {
  const path = String(page.file.path ?? "").replaceAll("\\", "/");
  const folder = String(page.file.folder ?? "").replaceAll("\\", "/");
  return path.startsWith(`${area}/`) || path.includes(`/${area}/`) || folder === area || folder.endsWith(`/${area}`) || folder.includes(`/${area}/`);
};
const areaPages = (area) => pages.where(p => inArea(p, area));
const count = (area) => areaPages(area).length;
const modifiedWithin = (days) => pages.where(p => p.file.mtime >= dv.date("today").minus({ days })).length;
const recent = pages.sort(p => p.file.mtime, "desc").limit(8).array();
const newest = (area) => areaPages(area).sort(p => p.file.mtime, "desc").array()[0];
const areaName = (page) => {
  const path = String(page.file.path ?? "").replaceAll("\\", "/");
  for (const area of ["Deep Learning", "Infinitune", "Interview Prep", "Prompts", "LeetCode", "Tutorials"]) {
    if (path.startsWith(`${area}/`) || path.includes(`/${area}/`)) return area;
  }
  return "Root";
};

const s = {
  wrap: "max-width:1120px;margin:0 auto 40px auto;font-family:var(--font-interface);",
  hero: "display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:22px;align-items:end;margin:22px 0 16px 0;padding:28px;border:1px solid var(--background-modifier-border);border-radius:12px;background:linear-gradient(135deg,rgba(91,141,239,.16),transparent 45%),var(--background-secondary);",
  kicker: "display:inline-block;margin-bottom:10px;color:var(--interactive-accent);font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;",
  h1: "margin:0 0 10px 0;color:var(--text-normal);font-size:46px;line-height:1;font-weight:850;letter-spacing:0;",
  heroText: "margin:0;color:var(--text-muted);font-size:16px;line-height:1.5;max-width:680px;",
  actions: "display:flex;flex-wrap:wrap;justify-content:flex-end;gap:8px;",
  action: "display:inline-flex;align-items:center;min-height:34px;padding:7px 11px;border:1px solid var(--background-modifier-border);border-radius:8px;background:var(--background-primary);color:var(--text-normal);font-size:14px;font-weight:700;text-decoration:none;",
  stats: "display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin:0 0 24px 0;",
  stat: "padding:16px;border:1px solid var(--background-modifier-border);border-radius:10px;background:var(--background-secondary);",
  statNum: "display:block;color:var(--text-normal);font-size:28px;line-height:1;font-weight:850;",
  statLabel: "display:block;margin-top:6px;color:var(--text-muted);font-size:12px;font-weight:750;letter-spacing:.04em;text-transform:uppercase;",
  sectionHead: "display:flex;align-items:end;justify-content:space-between;gap:18px;margin:24px 0 12px 0;",
  h2: "margin:0;color:var(--text-normal);font-size:20px;line-height:1.2;font-weight:800;",
  sectionText: "margin:0;color:var(--text-muted);font-size:14px;line-height:1.4;max-width:520px;",
  grid: "display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px;",
  card: "position:relative;padding:18px;border:1px solid var(--background-modifier-border);border-radius:10px;background:var(--background-secondary);overflow:hidden;",
  topBar: "position:absolute;left:0;right:0;top:0;height:3px;background:var(--interactive-accent);opacity:.9;",
  cardHead: "display:flex;align-items:flex-start;justify-content:space-between;gap:14px;margin-bottom:13px;",
  h3: "margin:0 0 6px 0;color:var(--text-normal);font-size:16px;line-height:1.2;font-weight:800;",
  desc: "margin:0;color:var(--text-muted);font-size:13px;line-height:1.4;",
  badge: "min-width:34px;padding:5px 8px;border:1px solid var(--background-modifier-border);border-radius:999px;color:var(--text-muted);text-align:center;font-size:12px;font-weight:800;",
  linkList: "display:grid;grid-template-columns:1fr;gap:7px;",
  cardLink: "display:block;padding:7px 9px;border:1px solid var(--background-modifier-border);border-radius:7px;background:var(--background-primary);color:var(--text-normal);font-size:14px;line-height:1.25;text-decoration:none;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;",
  twoCol: "display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px;margin-top:18px;",
  panel: "padding:18px;border:1px solid var(--background-modifier-border);border-radius:10px;background:var(--background-secondary);",
  continueGrid: "display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:8px;",
  continueCard: "display:block;padding:11px;border:1px solid var(--background-modifier-border);border-radius:8px;background:var(--background-primary);color:var(--text-normal);text-decoration:none;",
  small: "display:block;color:var(--text-muted);font-size:12px;line-height:1.2;",
  strongLine: "display:block;margin:4px 0;color:var(--text-normal);font-size:14px;line-height:1.25;font-weight:750;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;",
  recentList: "display:grid;gap:6px;",
  recentRow: "display:grid;grid-template-columns:minmax(0,1.3fr) minmax(90px,.75fr) 54px;gap:10px;align-items:center;padding:7px 9px;border:1px solid var(--background-modifier-border);border-radius:8px;background:var(--background-primary);color:var(--text-normal);font-size:14px;text-decoration:none;",
  recentName: "overflow:hidden;text-overflow:ellipsis;white-space:nowrap;",
  recentMeta: "overflow:hidden;color:var(--text-muted);font-size:12px;text-overflow:ellipsis;white-space:nowrap;",
  recentTime: "color:var(--text-muted);font-size:12px;text-align:right;",
  searchGrid: "display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:10px;",
  queryCard: "padding:12px;border:1px solid var(--background-modifier-border);border-radius:10px;background:var(--background-secondary);",
  queryTitle: "display:block;color:var(--text-normal);font-size:14px;font-weight:800;",
  queryText: "display:block;margin-top:6px;padding:6px;border-radius:6px;background:var(--background-primary);color:var(--text-muted);font-family:var(--font-monospace);font-size:11px;line-height:1.25;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;",
  path: "display:flex;flex-wrap:wrap;gap:8px;padding:14px;border:1px solid var(--background-modifier-border);border-radius:10px;background:var(--background-secondary);"
};

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
  <article style="${s.card}">
    <div style="${s.topBar}"></div>
    <div style="${s.cardHead}">
      <div>
        <h3 style="${s.h3}">${safe(space.title)}</h3>
        <p style="${s.desc}">${safe(space.description)}</p>
      </div>
      <strong style="${s.badge}">${space.noteCount}</strong>
    </div>
    <div style="${s.linkList}">
      ${space.links.map(([path, label]) => link(path, label, s.cardLink)).join("")}
    </div>
  </article>
`).join("");

const continueItems = [
  ["Deep Learning", newest("Deep Learning")],
  ["Infinitune", newest("Infinitune")],
  ["Interview Prep", newest("Interview Prep")],
  ["Prompts", newest("Prompts")]
].filter(([, page]) => page).map(([label, page]) => `
  <a class="internal-link" data-href="${safe(notePath(page.file.path))}" href="${safe(notePath(page.file.path))}" style="${s.continueCard}">
    <small style="${s.small}">${safe(label)}</small>
    <span style="${s.strongLine}">${safe(page.file.name)}</span>
    <time style="${s.small}">${page.file.mtime.toFormat("MMM d, yyyy")}</time>
  </a>
`).join("");

const recentRows = recent.map(page => `
  <a class="internal-link" data-href="${safe(notePath(page.file.path))}" href="${safe(notePath(page.file.path))}" style="${s.recentRow}">
    <span style="${s.recentName}">${safe(page.file.name)}</span>
    <small style="${s.recentMeta}">${safe(areaName(page))}</small>
    <time style="${s.recentTime}">${page.file.mtime.toFormat("MMM d")}</time>
  </a>
`).join("");

const queryCard = (title, query) => `
  <div style="${s.queryCard}">
    <span style="${s.queryTitle}">${safe(title)}</span>
    <code style="${s.queryText}">${safe(query)}</code>
  </div>
`;

const root = dv.el("div", "", { cls: "vault-dashboard" });
root.innerHTML = `
  <div style="${s.wrap}">
    <section style="${s.hero}">
      <div>
        <span style="${s.kicker}">Home</span>
        <h1 style="${s.h1}">Rohan's Vault</h1>
        <p style="${s.heroText}">Fast access to learning, interview prep, project knowledge, prompts, and coding practice.</p>
      </div>
      <div style="${s.actions}">
        ${link("Dashboard", "Main Dashboard", s.action)}
        ${link("Deep Learning/CheatSheet", "Cheat Sheet", s.action)}
        ${link("Prompts/Prep Doc", "Prep Doc", s.action)}
        ${link("Infinitune/2. Summaries/1. Short Summary (1-Min)", "Infinitune Summary", s.action)}
      </div>
    </section>

    <section style="${s.stats}">
      <div style="${s.stat}"><strong style="${s.statNum}">${pages.length}</strong><span style="${s.statLabel}">Total notes</span></div>
      <div style="${s.stat}"><strong style="${s.statNum}">${modifiedWithin(7)}</strong><span style="${s.statLabel}">Updated this week</span></div>
      <div style="${s.stat}"><strong style="${s.statNum}">${count("Deep Learning")}</strong><span style="${s.statLabel}">Deep Learning</span></div>
      <div style="${s.stat}"><strong style="${s.statNum}">${count("Infinitune")}</strong><span style="${s.statLabel}">Infinitune</span></div>
    </section>

    <div style="${s.sectionHead}">
      <h2 style="${s.h2}">Workspaces</h2>
      <p style="${s.sectionText}">Primary launch points for the areas you use most.</p>
    </div>
    <section style="${s.grid}">${workspaceCards}</section>

    <section style="${s.twoCol}">
      <div style="${s.panel}">
        <div style="margin-bottom:12px;">
          <h2 style="${s.h2}">Continue Working</h2>
          <p style="${s.sectionText}">Newest note from each major area.</p>
        </div>
        <div style="${s.continueGrid}">${continueItems}</div>
      </div>
      <div style="${s.panel}">
        <div style="margin-bottom:12px;">
          <h2 style="${s.h2}">Recently Updated</h2>
          <p style="${s.sectionText}">Your latest edits across the vault.</p>
        </div>
        <div style="${s.recentList}">${recentRows}</div>
      </div>
    </section>

    <div style="${s.sectionHead}">
      <h2 style="${s.h2}">Saved Search Queries</h2>
      <p style="${s.sectionText}">Copy one into Obsidian search when you need a focused result set.</p>
    </div>
    <section style="${s.searchGrid}">
      ${queryCard("Deep Learning", 'path:"Deep Learning"')}
      ${queryCard("Infinitune Architecture", 'path:"Infinitune" architecture OR "code walkthrough"')}
      ${queryCard("Interview Prep", 'path:"Interview Prep" OR path:"Infinitune/5. Interview Preparation Guide"')}
      ${queryCard("Job Prompts", 'path:"Prompts" resume OR cover OR application OR email')}
      ${queryCard("Transformers Stack", 'Transformers OR Attention OR LoRA OR QLoRA')}
    </section>

    <div style="${s.sectionHead}">
      <h2 style="${s.h2}">Study Path</h2>
      <p style="${s.sectionText}">A quick sequence for revision and project explanation practice.</p>
    </div>
    <section style="${s.path}">
      ${link("Deep Learning/Pre-requisites", "Prerequisites", s.action)}
      ${link("Deep Learning/Backpropagation", "Backpropagation", s.action)}
      ${link("Deep Learning/Attention", "Attention", s.action)}
      ${link("Deep Learning/Transformers", "Transformers", s.action)}
      ${link("Infinitune/2. Summaries/2. Medium Summary (5-Min)", "Infinitune 5-Min", s.action)}
    </section>
  </div>
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
