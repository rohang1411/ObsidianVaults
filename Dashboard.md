---
cssclasses:
  - premium-dashboard
---

<style>
/* === PREMIUM OBSIDIAN DASHBOARD CSS === */

/* Base Container Styling */
.premium-dashboard-wrapper {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
    font-family: var(--font-text);
    color: var(--text-normal);
}

/* Hide the default Obsidian H1 page title for a cleaner look */
.markdown-preview-view h1.page-title {
    display: none !important;
}

/* --- HERO BANNER --- */
.hero-banner {
    width: 100%;
    height: 300px;
    border-radius: 24px;
    overflow: hidden;
    position: relative;
    margin-bottom: 3rem;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
    display: flex;
    align-items: flex-end;
    background-image: url('https://images.unsplash.com/photo-1550684848-fac1c5b4e853?q=80&w=2070&auto=format&fit=crop');
    background-size: cover;
    background-position: center;
}

.hero-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(to top, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.2) 50%, rgba(0,0,0,0) 100%);
    z-index: 1;
}

.hero-content {
    position: relative;
    z-index: 2;
    padding: 3rem;
    width: 100%;
}

.hero-content h1 {
    font-size: 3.5rem;
    font-weight: 800;
    color: #ffffff !important;
    margin: 0 0 10px 0;
    letter-spacing: -1px;
    text-shadow: 0 2px 10px rgba(0,0,0,0.5);
    border: none;
}

.hero-content p {
    font-size: 1.2rem;
    color: rgba(255, 255, 255, 0.9) !important;
    margin: 0;
    max-width: 600px;
    text-shadow: 0 1px 5px rgba(0,0,0,0.5);
}

/* --- SECTION TITLES --- */
.section-title {
    font-size: 2rem;
    font-weight: 700;
    margin: 3rem 0 1.5rem 0;
    color: var(--text-normal);
    display: flex;
    align-items: center;
    gap: 12px;
    border-bottom: 2px solid var(--background-modifier-border);
    padding-bottom: 10px;
}

.section-title span.icon {
    font-size: 1.2em;
}


/* --- PROJECT GRID --- */
.project-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
    margin-bottom: 4rem;
}

/* --- CARD DESIGN --- */
.project-card {
    background: var(--background-primary);
    border-radius: 20px;
    overflow: hidden;
    border: 1px solid var(--background-modifier-border);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
    transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
    display: flex;
    flex-direction: column;
    height: 100%;
    position: relative;
}

.project-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
    border-color: var(--interactive-accent);
}

/* Card Cover Image */
.card-cover {
    height: 180px;
    width: 100%;
    overflow: hidden;
    position: relative;
}

.card-cover img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.6s ease;
}

.project-card:hover .card-cover img {
    transform: scale(1.05);
}

/* Card Badge */
.card-badge {
    position: absolute;
    top: 15px;
    right: 15px;
    background: rgba(0,0,0,0.6);
    backdrop-filter: blur(10px);
    color: white;
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 0.5px;
    z-index: 2;
}

/* Card Body */
.card-body {
    padding: 2rem;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
}

.card-title {
    font-size: 1.6rem;
    font-weight: 800;
    margin: 0 0 10px 0;
    color: var(--text-normal);
    border: none;
}

.card-desc {
    color: var(--text-muted);
    font-size: 1rem;
    line-height: 1.6;
    margin-bottom: 2rem;
}

/* Internal Links inside Card */
.card-links {
    margin-top: auto;
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.card-links a.internal-link {
    display: flex;
    align-items: center;
    padding: 10px 16px;
    background: var(--background-secondary);
    border-radius: 12px;
    color: var(--text-normal);
    text-decoration: none;
    font-weight: 500;
    transition: all 0.2s ease;
    border: 1px solid transparent;
}

.card-links a.internal-link:hover {
    background: var(--interactive-accent);
    color: var(--text-on-accent, white) !important;
    transform: translateX(5px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.card-links a.internal-link::before {
    content: '→';
    margin-right: 12px;
    opacity: 0.5;
    transition: all 0.2s ease;
}

.card-links a.internal-link:hover::before {
    opacity: 1;
    transform: translateX(3px);
    color: var(--text-on-accent, white);
}

/* --- QUICK ACTIONS BAR --- */
.quick-actions-bar {
    display: flex;
    gap: 1.5rem;
    flex-wrap: wrap;
    background: var(--background-secondary);
    padding: 2rem;
    border-radius: 20px;
    border: 1px solid var(--background-modifier-border);
}

.action-btn {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 12px 24px;
    background: var(--background-primary);
    border: 1px solid var(--background-modifier-border);
    border-radius: 14px;
    color: var(--text-normal);
    font-weight: 600;
    text-decoration: none;
    transition: all 0.2s ease;
}

.action-btn:hover {
    background: var(--interactive-accent);
    color: var(--text-on-accent, white) !important;
    border-color: var(--interactive-accent);
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}

/* Reset Obsidian link styling inside cards so they don't look weird */
.premium-dashboard-wrapper a {
    text-decoration: none !important;
}

</style>

<div class="premium-dashboard-wrapper">

    <!-- HERO BANNER -->
    <div class="hero-banner">
        <div class="hero-overlay"></div>
        <div class="hero-content">
            <h1>Command Center</h1>
            <p>Welcome to your personal knowledge base. Select a workspace below to begin learning.</p>
        </div>
    </div>

    <!-- MAIN PROJECTS SECTION -->
    <h2 class="section-title"><span class="icon">✨</span> Active Workspaces</h2>

    <div class="project-grid">

        <!-- CARD 1: DEEP LEARNING -->
        <div class="project-card">
            <div class="card-badge">ACTIVE</div>
            <div class="card-cover">
                <img src="https://images.unsplash.com/photo-1620712943543-bcc4688e7485?q=80&w=1965&auto=format&fit=crop" alt="AI Brain Concept">
            </div>
            <div class="card-body">
                <h3 class="card-title">Deep Learning</h3>
                <p class="card-desc">Core concepts, neural network architectures, and intensive deep learning study materials.</p>
                
                <div class="card-links">
                    <a href="deep-learning/transformers" class="internal-link">Transformers Architecture</a>
                    <a href="deep-learning/convolutional-neural-network-(cnn)" class="internal-link">Convolutional Networks</a>
                    <a href="deep-learning/variational-auto-encoders" class="internal-link">Variational Auto Encoders</a>
                    <a href="deep-learning/gan" class="internal-link">Generative Adversarial Nets</a>
                    <a href="deep-learning/cheatsheet" class="internal-link">Quick CheatSheet</a>
                </div>
            </div>
        </div>

        <!-- CARD 2: INFINITUNE -->
        <div class="project-card">
            <div class="card-badge">DEVELOPMENT</div>
            <div class="card-cover">
                <img src="https://images.unsplash.com/photo-1614149162883-504ce4d13909?q=80&w=1974&auto=format&fit=crop" alt="Music Audio Concept">
            </div>
            <div class="card-body">
                <h3 class="card-title">Infinitune</h3>
                <p class="card-desc">Project documentation, system architecture deep-dives, and interview preparation guides.</p>
                
                <div class="card-links">
                    <a href="infinitune/1.-project-overview/1.-project-overview" class="internal-link">Project Overview</a>
                    <a href="infinitune/4.-architecture-&-code-deep-dive/4.-architecture-&-code-deep-dive" class="internal-link">Architecture Deep-Dive</a>
                    <a href="infinitune/5.-interview-preparation-guide/5.-interview-preparation-guide" class="internal-link">Interview Prep Guide</a>
                    <a href="infinitune/flowchart" class="internal-link">System Flowchart</a>
                </div>
            </div>
        </div>

    </div>

    <!-- QUICK ACTIONS SECTION -->
    <h2 class="section-title"><span class="icon">⚡</span> Quick Actions</h2>
    
    <div class="quick-actions-bar">
        <a href="obsidian://new" class="action-btn">➕ Create New Note</a>
        <a href="obsidian://search" class="action-btn">🔍 Search Vault</a>
        <a href="obsidian://show-graph" class="action-btn">🕸️ Open Graph View</a>
    </div>

</div>
