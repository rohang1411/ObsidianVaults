---
cssclass: dashboard
---

<style>
/* Dashboard++ Core Styling Clone (TfTHacker / Nicole van der Hoeven) */
/* Natively integrated so you don't need snippets! */

.dashboard {
    --db-column-count: 3;
    --db-card-bg: var(--background-secondary);
    --db-card-radius: 12px;
    --db-header-height: auto;
}

/* Adjust column count on smaller screens */
@media screen and (max-width: 1000px) {
    .dashboard { --db-column-count: 2; }
}
@media screen and (max-width: 600px) {
    .dashboard { --db-column-count: 1; }
}

/* Base Dashboard Grid Layout */
.dashboard .markdown-preview-view > div > div > ul {
    display: grid !important;
    grid-template-columns: repeat(var(--db-column-count), 1fr);
    grid-gap: 20px;
    padding: 0;
    margin: 0;
    list-style: none !important;
}

/* The actual "Cards" (Top-level List Items) */
.dashboard .markdown-preview-view > div > div > ul > li {
    background-color: var(--db-card-bg);
    border-radius: var(--db-card-radius);
    padding: 24px;
    border: 1px solid var(--background-modifier-border);
    display: flex;
    flex-direction: column;
    margin: 0;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
}

.dashboard .markdown-preview-view > div > div > ul > li:hover {
    box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
    border-color: var(--interactive-accent);
}

/* Removing the bullet point from the top-level cards */
.dashboard .markdown-preview-view > div > div > ul > li::before {
    display: none !important;
}

/* Card Titles (The first line of the top level list item) */
/* We target the direct text node/strong tag inside the li */
.dashboard .markdown-preview-view > div > div > ul > li > strong,
.dashboard .markdown-preview-view > div > div > ul > li > a.internal-link,
.dashboard .markdown-preview-view > div > div > ul > li > p {
    font-size: 1.4em !important;
    font-weight: 700 !important;
    margin-bottom: 12px !important;
    color: var(--text-normal);
    display: block;
    border-bottom: 2px solid var(--background-modifier-border);
    padding-bottom: 8px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.dashboard .markdown-preview-view > div > div > ul > li > strong {
    color: var(--interactive-accent);
}

/* The inner lists inside the cards (The actual links) */
.dashboard .markdown-preview-view > div > div > ul > li > ul {
    padding-left: 0;
    margin-top: 10px;
    list-style: none !important;
    display: flex;
    flex-direction: column;
    gap: 8px;
}

/* Inner list items */
.dashboard .markdown-preview-view > div > div > ul > li > ul > li {
    margin: 0;
    padding: 0;
}

/* Hide bullet points on inner links */
.dashboard .markdown-preview-view > div > div > ul > li > ul > li::before {
    content: '' !important;
    display: none !important;
}

/* Styling the Internal Links directly */
.dashboard .markdown-preview-view > div > div > ul > li > ul > li a {
    display: flex;
    align-items: center;
    padding: 8px 12px;
    background-color: var(--background-primary);
    border-radius: 8px;
    text-decoration: none !important;
    color: var(--text-normal);
    font-weight: 500;
    transition: all 0.2s ease;
    border: 1px solid var(--background-modifier-border);
}

.dashboard .markdown-preview-view > div > div > ul > li > ul > li a:hover {
    background-color: var(--interactive-accent);
    color: var(--text-on-accent, white) !important;
    transform: translateX(4px);
    border-color: var(--interactive-accent);
}

/* Add small bullet icon inside the link button */
.dashboard .markdown-preview-view > div > div > ul > li > ul > li a::before {
    content: "•";
    margin-right: 8px;
    font-size: 1.2em;
    color: var(--text-muted);
    transition: color 0.2s;
}

.dashboard .markdown-preview-view > div > div > ul > li > ul > li a:hover::before {
    color: rgba(255,255,255,0.7);
}

/* Hide the main H1 page title for a cleaner dashboard look */
.dashboard .markdown-preview-view h1.page-title {
    display: none !important;
}
</style>

# Obsidian Dashboard++

- **🧠 Deep Learning**
    - [[Deep Learning/Transformers|Transformers]]
    - [[Deep Learning/Convolutional Neural Network (CNN)|Convolutional Neural Networks]]
    - [[Deep Learning/Long Short Term Memory Networks (LSTM)|LSTMs]]
    - [[Deep Learning/GAN|Generative Adversarial Nets]]
    - [[Deep Learning/Variational Auto Encoders|Variational Auto Encoders]]
    - [[Deep Learning/CheatSheet|Theory CheatSheet]]

- **🎵 Infinitune**
    - [[Infinitune/1. Project Overview/1. Project Overview|1. Project Overview]]
    - [[Infinitune/3. Core Concepts & Technologies/3. Core Concepts & Technologies|3. Core Concepts]]
    - [[Infinitune/4. Architecture & Code Deep-Dive/4. Architecture & Code Deep-Dive|4. Architecture Dive]]
    - [[Infinitune/5. Interview Preparation Guide/5. Interview Preparation Guide|5. Interview Prep]]
    - [[Infinitune/Flowchart.canvas|Architecture Flowchart]]

- **⚡ Quick Links**
    - [➕ Create New Note](obsidian://new)
    - [🔍 Search Workspace](obsidian://search)
    - [🕸️ View Graph](obsidian://show-graph)
    - [[README|Vault Readme]]
