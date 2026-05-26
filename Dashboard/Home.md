---
cssclasses:
  - vault-home
---

# Home

> [!quick-actions]-
> - [New Note](obsidian://new)
> - [Search Vault](obsidian://search)
> - [Graph View](obsidian://show-graph)
> - [[Dashboard|Main Dashboard]]
> - [[Deep Learning/CheatSheet|Deep Learning Cheat Sheet]]
> - [[Prompts/Prep Doc|Prep Doc]]

## Overview

```dataviewjs
const pages = dv.pages().where(p => p.file.path !== dv.current().file.path);
const inFolder = (name) => pages.where(p => p.file.folder.includes(name)).length;
const updated = pages.where(p => p.file.mtime >= dv.date("today").minus({ days: 7 })).length;

dv.table(
  ["Vault", "Notes", "Updated this week", "Deep Learning", "Infinitune"],
  [["Obsidian Vault", pages.length, updated, inFolder("Deep Learning"), inFolder("Infinitune")]]
);
```

## Workspaces

| Deep Learning | Infinitune | Interview Prep | Prompts |
| --- | --- | --- | --- |
| [[Deep Learning/Transformers|Transformers]] | [[Infinitune/1. Project Overview/Project Readme|Project Readme]] | [[Interview Prep/Basic CS Questions|Basic CS]] | [[Prompts/Resume Tailoring|Resume Tailoring]] |
| [[Deep Learning/Attention|Attention]] | [[Infinitune/4. Architecture & Code Deep-Dive/1. System Architecture|System Architecture]] | [[Interview Prep/Basic DS Questions|Basic DS]] | [[Prompts/Cover Letters|Cover Letters]] |
| [[Deep Learning/Backpropagation|Backpropagation]] | [[Infinitune/4. Architecture & Code Deep-Dive/2. Code Walkthrough|Code Walkthrough]] | [[Interview Prep/Behavioral Interview Questions|Behavioral]] | [[Prompts/Job Application Question Answers|Application Answers]] |
| [[Deep Learning/Convolutional Neural Network (CNN)|CNN]] | [[Infinitune/5. Interview Preparation Guide/Interview Q&A|Interview Q&A]] | [[Infinitune/5. Interview Preparation Guide/Project Talking Points|Project Talking Points]] | [[Prompts/AI ML DS Cold Email|AI/ML/DS Email]] |
| [[Deep Learning/Variational Auto Encoders|VAE]] | [[Infinitune/6. Future Work & Research/Future Improvements|Future Work]] | [[Prompts/Prep Doc|Prep Doc]] | [[Prompts/Cheatsheet Generation|Cheatsheet Generation]] |
| [[Deep Learning/CheatSheet|Cheat Sheet]] | [[Infinitune/2. Summaries/1. Short Summary (1-Min)|1-Min Summary]] | [[LeetCode/355. Design Twitter|Design Twitter]] | [[Prompts/SDE Cold Email|SDE Email]] |

## Continue

```dataview
TABLE WITHOUT ID
  file.link AS Note,
  file.folder AS Area,
  dateformat(file.mtime, "MMM d") AS Updated
FROM ""
WHERE file.name != this.file.name
  AND file.ext = "md"
SORT file.mtime DESC
LIMIT 8
```

## Saved Searches

| Search | Query |
| --- | --- |
| [Deep Learning](obsidian://search?query=path%3A%22Deep%20Learning%22) | Notes in the Deep Learning workspace |
| [Infinitune Architecture](obsidian://search?query=path%3A%22Infinitune%22%20architecture%20OR%20%22code%20walkthrough%22) | Architecture and implementation notes |
| [Interview Prep](obsidian://search?query=path%3A%22Interview%20Prep%22%20OR%20path%3A%22Infinitune%2F5.%20Interview%20Preparation%20Guide%22) | Behavioral, CS, DS, and project prep |
| [Job Prompts](obsidian://search?query=path%3A%22Prompts%22%20resume%20OR%20cover%20OR%20application%20OR%20email) | Resume, cover letter, application, and outreach prompts |
| [Transformers Stack](obsidian://search?query=Transformers%20OR%20Attention%20OR%20LoRA%20OR%20QLoRA) | Transformers, attention, LoRA, and QLoRA |

## Study Path

| Step | Open |
| --- | --- |
| Fundamentals | [[Deep Learning/Pre-requisites|Pre-requisites]] |
| Neural networks | [[Deep Learning/Backpropagation|Backpropagation]] |
| Sequence models | [[Deep Learning/Recurrent Neural Networks|RNNs]] and [[Deep Learning/Long Short Term Memory Networks (LSTM)|LSTM]] |
| Attention | [[Deep Learning/Attention|Attention]] |
| Transformers | [[Deep Learning/Transformers|Transformers]] |
| Project explanation | [[Infinitune/2. Summaries/2. Medium Summary (5-Min)|Infinitune 5-Min Summary]] |

> [!activity]- Vault Activity
> ```contributionGraph
> title: Note Contributions
> graphType: month-track
> dateRangeValue: 3
> dateRangeType: LATEST_MONTH
> startOfWeek: 0
> showCellRuleIndicators: false
> titleStyle:
>   textAlign: center
>   fontSize: 14px
>   fontWeight: normal
> dataSource:
>   type: PAGE
>   value: ""
>   dateField:
>     type: FILE_MTIME
>   filters: []
>   countField:
>     type: DEFAULT
> fillTheScreen: false
> enableMainContainerShadow: false
> cellStyleRules: []
> ```

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
