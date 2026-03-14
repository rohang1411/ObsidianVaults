---
cssclasses:
  - dashboard
---
<style>
/* Dashboard Container styling */
.dashboard-container {
    max-width: 1100px;
    margin: 0 auto;
    padding: 2rem;
    font-family: var(--font-text);
    color: var(--text-normal);
}

/* Header/Hero Section */
.dashboard-header {
    background: linear-gradient(135deg, var(--interactive-accent) 0%, var(--background-secondary) 100%);
    padding: 3rem;
    border-radius: 20px;
    margin-bottom: 3rem;
    position: relative;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    border: 1px solid var(--background-modifier-border);
}

.dashboard-header h1 {
    font-size: 3em;
    font-weight: 800;
    margin: 0 0 10px 0;
    color: var(--text-on-accent, var(--text-normal));
    letter-spacing: -1px;
}

.dashboard-header p {
    font-size: 1.2em;
    opacity: 0.9;
    margin: 0;
    color: var(--text-on-accent, var(--text-muted));
}

/* Section Headings */
.dashboard-section-title {
    font-size: 1.8em;
    font-weight: 700;
    margin-bottom: 1.5rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid var(--background-modifier-border);
    color: var(--text-normal);
    display: flex;
    align-items: center;
    gap: 10px;
}

/* Grid Layout */
.dashboard-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 2rem;
    margin-bottom: 3rem;
}

/* Card Styling - Glassmorphism feel */
.dashboard-card {
    background-color: var(--background-primary-alt);
    border-radius: 16px;
    padding: 1.5rem;
    border: 1px solid var(--background-modifier-border);
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    height: 100%;
}

.dashboard-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
    border-color: var(--interactive-accent);
}

/* Card Decorative Top Bar */
.dashboard-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 6px;
    background: var(--interactive-accent);
    opacity: 0;
    transition: opacity 0.3s ease;
}

.dashboard-card:hover::before {
    opacity: 1;
}

/* Card Header */
.card-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 1rem;
}

.card-icon {
    font-size: 2em;
    background: var(--background-secondary);
    width: 50px;
    height: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 12px;
    color: var(--interactive-accent);
}

.card-title {
    font-size: 1.4em;
    font-weight: 600;
    margin: 0;
    color: var(--text-normal);
}

.card-desc {
    color: var(--text-muted);
    font-size: 0.95em;
    margin-bottom: 1.5rem;
    line-height: 1.5;
    flex-grow: 1; /* Pushes links to the bottom */
}

/* Links List inside Cards */
.card-links {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.card-links li {
    margin: 0;
}

.card-links a.internal-link {
    display: flex;
    align-items: center;
    padding: 8px 12px;
    background: var(--background-secondary);
    border-radius: 8px;
    color: var(--text-normal);
    text-decoration: none;
    font-weight: 500;
    transition: all 0.2s ease;
    border: 1px solid transparent;
}

.card-links a.internal-link:hover {
    background: var(--background-modifier-hover);
    color: var(--interactive-accent);
    border-color: var(--background-modifier-border);
    transform: translateX(4px);
}

.card-links a.internal-link::before {
    content: '→';
    margin-right: 8px;
    font-size: 1.1em;
    opacity: 0.5;
    transition: opacity 0.2s, transform 0.2s;
}

.card-links a.internal-link:hover::before {
    opacity: 1;
    transform: translateX(2px);
    color: var(--interactive-accent);
}

/* Quick Links Row */
.quick-links-container {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
}

.quick-pill {
    background: var(--background-secondary);
    border: 1px solid var(--background-modifier-border);
    padding: 10px 20px;
    border-radius: 30px;
    font-weight: 600;
    color: var(--text-normal);
    text-decoration: none;
    transition: all 0.2s ease;
    display: inline-flex;
    align-items: center;
    gap: 8px;
}

.quick-pill:hover {
    background: var(--interactive-accent);
    color: var(--text-on-accent, white);
    border-color: var(--interactive-accent);
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
}

/* Utility to hide standard markdown headers in dashboard view if needed */
.dashboard h1.page-title {
    display: none;
}
</style>

<div class="dashboard-container">

    <!-- Hero Section -->
    <div class="dashboard-header">
        <h1>Command Center</h1>
        <p>Welcome back, Rohan. Here is an overview of your active knowledge bases.</p>
    </div>

    <!-- Main Projects -->
    <h2 class="dashboard-section-title">✨ Active Projects & Learning</h2>
    
    <div class="dashboard-grid">
        
        <!-- Deep Learning Card -->
        <div class="dashboard-card">
            <div class="card-header">
                <div class="card-icon">🧠</div>
                <h3 class="card-title">Deep Learning</h3>
            </div>
            <p class="card-desc">Core concepts, architectures, and notes on neural networks and deep thinking models.</p>
            
            <ul class="card-links">
                <li>[[Deep Learning/Transformers|Transformers]]</li>
                <li>[[Deep Learning/Convolutional Neural Network (CNN)|CNNs]]</li>
                <li>[[Deep Learning/GAN|GANs]]</li>
                <li>[[Deep Learning/Variational Auto Encoders|Variational Auto Encoders]]</li>
                <li>[[Deep Learning/CheatSheet|CheatSheet]]</li>
            </ul>
        </div>

        <!-- Infinitune Card -->
        <div class="dashboard-card">
            <div class="card-header">
                <div class="card-icon">🎵</div>
                <h3 class="card-title">Infinitune</h3>
            </div>
            <p class="card-desc">Project documentation, architecture deep-dives, and research outlines for Infinitune.</p>
            
            <ul class="card-links">
                <li>[[Infinitune/1. Project Overview/1. Project Overview|Project Overview]]</li>
                <li>[[Infinitune/3. Core Concepts & Technologies/3. Core Concepts & Technologies|Core Concepts]]</li>
                <li>[[Infinitune/4. Architecture & Code Deep-Dive/4. Architecture & Code Deep-Dive|Architecture Dive]]</li>
                <li>[[Infinitune/5. Interview Preparation Guide/5. Interview Preparation Guide|Interview Prep]]</li>
                <li>[[Infinitune/Flowchart.canvas|System Flowchart]]</li>
            </ul>
        </div>
        
         <!-- General Notes Placeholder (Optional) -->
        <div class="dashboard-card">
            <div class="card-header">
                <div class="card-icon">📝</div>
                <h3 class="card-title">Quick Capture</h3>
            </div>
            <p class="card-desc">Recent thoughts or standalone notes that need sorting.</p>
            
            <ul class="card-links">
                 <!-- Add any general links here or leave as a template -->
                <li>[[README]]</li>
            </ul>
        </div>

    </div>

    <!-- Quick Tools / Links -->
    <h2 class="dashboard-section-title">⚡ Quick Actions</h2>
    
    <div class="quick-links-container">
        <!-- These can be modified later to point to specific daily notes or templates -->
        <a href="obsidian://new" class="quick-pill">➕ New Note</a>
        <a href="obsidian://search" class="quick-pill">🔍 Search Vault</a>
        <a href="obsidian://show-graph" class="quick-pill">🕸️ Open Graph View</a>
    </div>

</div>
