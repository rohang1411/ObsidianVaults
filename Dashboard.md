---
banner: "https://images.unsplash.com/photo-1550684848-fac1c5b4e853?q=80&w=2070&auto=format&fit=crop"
banner_y: 0.53
cssclasses:
  - notion-page
---

<style>
/* =========================================
   Notion-Style Aesthetic Dashboard CSS
   ========================================= */

/* Base Typography & Spacing */
.notion-dashboard {
    max-width: 900px;
    margin: 0 auto;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    color: var(--text-normal);
    padding-bottom: 50px;
}

/* Hide Default Obsidian Page Title */
.notion-page .markdown-preview-view h1.page-title,
.notion-page .markdown-source-view.mod-cm6 .cm-scroller .cm-sizer .cm-heading.cm-heading-1 {
    display: none !important;
}

/* --- THE WELCOME HEADER --- */
.notion-header {
    margin-top: 40px;
    margin-bottom: 30px;
    animation: fadeDown 0.8s ease-out;
}

.notion-greeting {
    font-size: 2.8rem;
    font-weight: 800;
    margin: 0;
    letter-spacing: -1px;
    background: linear-gradient(120deg, var(--text-normal) 0%, var(--text-muted) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.notion-subtitle {
    font-size: 1.1rem;
    color: var(--text-muted);
    margin-top: 8px;
    font-weight: 500;
}

/* --- QUICK ACTIONS DOCK --- */
.notion-quick-dock {
    display: flex;
    gap: 15px;
    margin-bottom: 50px;
    flex-wrap: wrap;
    animation: fadeUp 0.8s ease-out 0.2s both;
}

.dock-btn {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 12px 20px;
    background: var(--background-secondary);
    border: 1px solid var(--background-modifier-border);
    border-radius: 12px;
    color: var(--text-normal);
    text-decoration: none !important;
    font-weight: 600;
    font-size: 0.95rem;
    transition: all 0.2s ease;
    cursor: pointer;
}

.dock-btn:hover {
    background: var(--interactive-accent);
    color: var(--text-on-accent, white) !important;
    transform: translateY(-2px);
    box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
    border-color: var(--interactive-accent);
}

.dock-icon {
    font-size: 1.2rem;
}

/* --- SECTION HEADERS --- */
.notion-section-title {
    font-size: 1.4rem;
    font-weight: 700;
    color: var(--text-normal);
    margin: 0 0 20px 0;
    display: flex;
    align-items: center;
    gap: 10px;
    border-bottom: 1px solid var(--background-modifier-border);
    padding-bottom: 8px;
}

/* --- ACTIVE WORKSPACES (GRID) --- */
.notion-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
    gap: 24px;
    margin-bottom: 50px;
}

.notion-card {
    background: var(--background-primary);
    border: 1px solid var(--background-modifier-border);
    border-radius: 16px;
    padding: 24px;
    display: flex;
    flex-direction: column;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    position: relative;
    overflow: hidden;
}

.notion-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.08);border-color: var(--text-muted);
}

.card-icon-header {
    font-size: 2.5rem;
    margin-bottom: 15px;
    background: var(--background-secondary);
    width: 60px;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 14px;
}

.card-title {
    font-size: 1.3rem;
    font-weight: 700;
    margin: 0 0 8px 0;
}

.card-desc {
    color: var(--text-muted);
    font-size: 0.9rem;
    margin: 0 0 20px 0;
    line-height: 1.5;
}

/* Custom Links inside Cards */
.notion-link-list {
    display: flex;
    flex-direction: column;
    gap: 8px;
    margin-bottom: 15px;
}

.notion-link-item {
    display: flex;
    align-items: center;
    padding: 8px 12px;
    border-radius: 8px;
    color: var(--text-normal);
    text-decoration: none !important;
    font-weight: 500;
    font-size: 0.95rem;
    transition: all 0.2s ease;
    background: transparent;
}

.notion-link-item:hover {
    background: var(--background-secondary-alt);
    color: var(--interactive-accent);
    transform: translateX(4px);
}

.notion-link-item::before {
    content: '📄';
    margin-right: 12px;
    font-size: 1.1rem;
    opacity: 0.7;
}

.card-footer-link {
    margin-top: auto;
    color: var(--text-muted);
    font-size: 0.9rem;
    font-weight: 600;
    text-decoration: none !important;
    transition: color 0.2s;
    display: flex;
    align-items: center;
}

.card-footer-link:hover {
    color: var(--interactive-accent);
}
.card-footer-link::after {
    content: '→';
    margin-left: 5px;
    transition: transform 0.2s;
}
.card-footer-link:hover::after {
    transform: translateX(3px);
}

/* --- EMBEDDED DYNAMIC CONTENT (FLOWCHART) --- */
.notion-embed-container {
    background: var(--background-secondary);
    border-radius: 16px;
    padding: 2px;
    border: 1px solid var(--background-modifier-border);
    margin-bottom: 40px;
    overflow: hidden;
    height: 450px;
    position: relative;
    box-shadow: inset 0 2px 10px rgba(0,0,0,0.05);
}

/* Make Obsidian's iframe embed fill the container seamlessly */
.notion-embed-container .internal-embed {
    width: 100% !important;
    height: 100% !important;
    border: none !important;
    margin: 0 !important;
}

/* Animations */
@keyframes fadeDown {
    from { opacity: 0; transform: translateY(-20px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Remove default link styling globally inside dashboard */
.notion-dashboard a.internal-link {
    text-decoration: none !important;
}
</style>

<div class="notion-dashboard">

    <!-- 1. WELCOME HEADER -->
    <div class="notion-header">
        <h1 class="notion-greeting">Good evening, Rohan.</h1>
        <div class="notion-subtitle">Welcome to your central knowledge hub.</div>
    </div>

    <!-- 2. QUICK ACTIONS DOCK -->
    <div class="notion-quick-dock">
        <a href="obsidian://new" class="dock-btn">
            <span class="dock-icon">✏️</span> New Note
        </a>
        <a href="obsidian://search" class="dock-btn">
            <span class="dock-icon">🔍</span> Global Search
        </a>
        <a href="obsidian://show-graph" class="dock-btn">
            <span class="dock-icon">🌌</span> Vault Graph
        </a>
    </div>

    <!-- 3. ACTIVE WORKSPACES -->
    <h2 class="notion-section-title">📌 Active Workspaces</h2>
    
    <div class="notion-grid">
        
        <!-- CARD: Deep Learning -->
        <div class="notion-card">
            <div class="card-icon-header">🧠</div>
            <h3 class="card-title">Deep Learning</h3>
            <p class="card-desc">Core architectures, math fundamentals, and network models.</p>
            
            <div class="notion-link-list">
                <a href="deep-learning/transformers" class="internal-link notion-link-item">Transformers</a>
                <a href="deep-learning/convolutional-neural-network-(cnn)" class="internal-link notion-link-item">CNNs</a>
                <a href="deep-learning/gan" class="internal-link notion-link-item">Generative Adversarial Nets</a>
            </div>
            
            <a href="deep-learning" class="card-footer-link">View all 17 notes</a>
        </div>

        <!-- CARD: Infinitune -->
        <div class="notion-card">
            <div class="card-icon-header">🎵</div>
            <h3 class="card-title">Infinitune</h3>
            <p class="card-desc">System documentation, architecture dives, and interview prep.</p>
            
            <div class="notion-link-list">
                <a href="infinitune/1.-project-overview/1.-project-overview" class="internal-link notion-link-item">Project Overview</a>
                <a href="infinitune/4.-architecture-&-code-deep-dive/4.-architecture-&-code-deep-dive" class="internal-link notion-link-item">Code Deep-Dive</a>
                <a href="infinitune/5.-interview-preparation-guide/5.-interview-preparation-guide" class="internal-link notion-link-item">Interview Prep Guide</a>
            </div>
            
             <a href="infinitune" class="card-footer-link">Go to project folder</a>
        </div>

    </div>

    <!-- 4. DYNAMIC VISUALIZATION -->
    <h2 class="notion-section-title">🗺️ System Architecture Map</h2>
    <div class="notion-embed-container">
        <!-- Embedding the Infinitune Flowchart Canvas directly! -->
        ![[Infinitune/Flowchart.canvas]]
    </div>

</div>
