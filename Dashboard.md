---
banner: "https://images.unsplash.com/photo-1550684848-fac1c5b4e853?q=80&w=2070&auto=format&fit=crop"
banner_y: 0.53
cssclasses:
  - dashboard
---

<style>
/* === ADVANCED DASHBOARD++ CARDS === */
/* Built robustly to handle Banners plugin extra nested divs */

.dashboard {
    --db-column-count: 3;
    --db-card-bg: var(--background-secondary);
    --db-card-bg-hover: var(--background-secondary-alt);
    --db-card-radius: 16px;
    --db-accent: var(--interactive-accent);
}

/* Responsive Grid */
@media screen and (max-width: 1100px) {
    .dashboard { --db-column-count: 2; }
}
@media screen and (max-width: 650px) {
    .dashboard { --db-column-count: 1; }
}

/* Hide Page Title to let Banners shine */
.dashboard .markdown-preview-view h1.page-title,
.dashboard .markdown-source-view.mod-cm6 .cm-scroller .cm-sizer .cm-heading.cm-heading-1 {
    display: none !important;
}

/* 
    THE GRID CONTAINER (Top-Level Lists)
    Using :not(ul ul) grabs ONLY the outermost lists regardless of plugin wrappers
*/
.dashboard .markdown-preview-view ul:not(ul ul) {
    display: grid !important;
    grid-template-columns: repeat(var(--db-column-count), 1fr);
    gap: 24px;
    padding: 20px 0;
    margin: 0;
    list-style: none !important;
}

/* The Cards (Top-Level List Items) */
.dashboard .markdown-preview-view ul:not(ul ul) > li {
    background-color: var(--db-card-bg);
    border-radius: var(--db-card-radius);
    padding: 28px 24px 24px 24px;
    border: 1px solid var(--background-modifier-border);
    display: flex;
    flex-direction: column;
    margin: 0;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
    position: relative;
    overflow: hidden;
}

/* Hover effect on the Card */
.dashboard .markdown-preview-view ul:not(ul ul) > li:hover {
    transform: translateY(-6px);
    box-shadow: 0 12px 25px rgba(0, 0, 0, 0.15);
    border-color: var(--db-accent);
}

/* Color Accent Bar at top of Card */
.dashboard .markdown-preview-view ul:not(ul ul) > li::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: var(--db-accent);
    opacity: 0.8;
}

/* Remove main bullet point icon from Cards */
.dashboard .markdown-preview-view ul:not(ul ul) > li::before {
    display: none !important;
}

/* Card Headers (The Project Name) */
.dashboard .markdown-preview-view ul:not(ul ul) > li > strong,
.dashboard .markdown-preview-view ul:not(ul ul) > li > a.internal-link,
.dashboard .markdown-preview-view ul:not(ul ul) > li > p {
    font-size: 1.5em !important;
    font-weight: 800 !important;
    margin: 0 0 20px 0 !important;
    color: var(--text-normal);
    display: block;
    border-bottom: 2px solid var(--background-modifier-border-hover);
    padding-bottom: 12px;
    letter-spacing: -0.5px;
}

/* The inner Lists (Links container) */
.dashboard .markdown-preview-view ul ul {
    padding-left: 0;
    margin-top: 0;
    list-style: none !important;
    display: flex;
    flex-direction: column;
    gap: 10px;
}

/* Remove inner bullet points */
.dashboard .markdown-preview-view ul ul > li::before {
    display: none !important;
}

.dashboard .markdown-preview-view ul ul > li {
    margin: 0;
    padding: 0;
}

/* Card Button Links */
.dashboard .markdown-preview-view ul ul > li a {
    display: flex;
    align-items: center;
    padding: 10px 14px;
    background-color: var(--background-primary);
    border-radius: 10px;
    text-decoration: none !important;
    color: var(--text-normal);
    font-weight: 600;
    transition: all 0.2s ease;
    border: 1px solid var(--background-modifier-border);
}

/* Link Button Hover */
.dashboard .markdown-preview-view ul ul > li a:hover {
    background-color: var(--db-accent);
    color: var(--text-on-accent, white) !important;
    transform: translateX(5px);
    border-color: var(--db-accent);
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}

/* Button Icon (Arrow) */
.dashboard .markdown-preview-view ul ul > li a::before {
    content: "→";
    margin-right: 12px;
    font-size: 1.1em;
    color: var(--text-muted);
    transition: all 0.2s ease;
    opacity: 0.6;
}

.dashboard .markdown-preview-view ul ul > li a:hover::before {
    color: var(--text-on-accent, white);
    opacity: 1;
    transform: translateX(3px);
}
</style>

# Command Center

- **🧠 Deep Learning Core**
    - [[Deep Learning/Transformers|Transformers]]
    - [[Deep Learning/Convolutional Neural Network (CNN)|Convolutional Neural Networks]]
    - [[Deep Learning/Long Short Term Memory Networks (LSTM)|LSTMs]]
    - [[Deep Learning/GAN|Generative Adversarial Nets]]
    - [[Deep Learning/Variational Auto Encoders|Variational Auto Encoders]]
    - [[Deep Learning/CheatSheet|Theory CheatSheet]]

- **🎵 Infinitune Hub**
    - [[Infinitune/1. Project Overview/1. Project Overview|1. Project Overview]]
    - [[Infinitune/3. Core Concepts & Technologies/3. Core Concepts & Technologies|3. Core Concepts]]
    - [[Infinitune/4. Architecture & Code Deep-Dive/4. Architecture & Code Deep-Dive|4. Architecture Dive]]
    - [[Infinitune/5. Interview Preparation Guide/5. Interview Preparation Guide|5. Interview Prep]]
    - [[Infinitune/Flowchart.canvas|Architecture Flowchart]]

- **⚡ Action Center**
    - [➕ Create New Note](obsidian://new)
    - [🔍 Search Workspace](obsidian://search)
    - [🕸️ View Vault Graph](obsidian://show-graph)
    - [[README|Vault Readme]]
