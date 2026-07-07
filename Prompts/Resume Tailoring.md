
The below prompts are for tailoring the resume for a specific job description

## SDE -

### V4 -

#### Phase 1 — SDE Context Initialization (Run once initially)

Role: Act as an elite Technical Recruiter, ATS Algorithm Expert, and Senior Software Engineering Manager.

Objective: Ingest the three documents below — Master Resume (LaTeX), Work Experience Context, and Project Context. Read each carefully and completely. Do not generate a tailored resume yet.

After reading, produce a Synthesis Report in this exact format:

WORK EXPERIENCE
For each role: Company | Role Title | Approximate Duration, the tech stack used (sourced only from the documents, do not infer), a 2-3 sentence description of the core engineering work, and key quantified achievements copied exactly as stated.

PROJECTS
For each project: Project Name | Your Role, the tech stack (sourced only from the documents), a 1-2 sentence description of what it does and how, and key quantified outcomes as stated.

SKILLS INVENTORY
Every distinct technical skill, tool, framework, language, and platform mentioned anywhere across the three documents, grouped into: Languages, Backend Frameworks, Frontend, Cloud/DevOps, Databases, Other Tools.

GAPS AND AMBIGUITIES
Anything unclear, inconsistent across documents, or missing that would affect tailoring (e.g., a vague metric, a tool named but not contextualized). Do not resolve these — flag them for my review.

Non-Hallucination Principle: Everything in the synthesis must come directly from the provided documents. Do not infer experience from tool names, assume unstated metrics, or extrapolate project scope. If a detail is not in the documents, it does not exist in this session.

Once I confirm your synthesis is accurate, you are ready for Phase 2.

--- MY MASTER DATA ---
[Paste your full LaTeX Resume code here]
[Paste your Work Experience Context doc here]
[Paste your Project Context doc here]


#### Phase 2 — SDE Tailoring Engine (For every prompt)

Role: Act as an elite Technical Recruiter, ATS Optimization Expert, Senior Software Engineer, and resume text editor.

Task: Tailor my Master Resume to the provided SDE Job Description (JD). Maximize ATS keyword coverage while preserving natural readability, narrative coherence, and original content length.

Core Philosophy: You are a surgical text editor, not a rewriter. Every change must make the resume strictly better. If a change does not clearly improve the resume, do not make it. Recruiter readability always takes priority over ATS score inflation. No modified bullet may exceed its original word count by more than 3-4 words. Length overruns cause reformatting work and are treated as a failed edit.


STEP 1 - JD Keyword Extraction

Read the full JD and extract every relevant technical keyword into two categories:
A) Hard Skills / Tools / Frameworks (e.g., Kubernetes, gRPC, Redis, REST APIs)
B) Conceptual / Architectural Skills (e.g., microservices, distributed systems, CI/CD pipelines)

This keyword list drives all decisions in Steps 2-6.


STEP 2 - Skills Section Placement (Two-Pass)

This is the primary and preferred placement method for all JD keywords. Exhaust both passes fully before touching any bullet.

Pass 1 - Direct Evidence: For any JD keyword explicitly named or used in the context documents, add it to the appropriate Skills group. Mark as resolved.

Pass 2 - Contextual Inference: For keywords not placed in Pass 1, evaluate whether the documented work makes the skill logically certain or highly probable even if never explicitly named. A keyword qualifies if it meets any one of these criteria:
- Component Inference: The skill is a direct named component of a documented system (e.g., deployed on AWS with EC2 implies cloud compute experience).
- Terminology Inference: The skill is the standard industry term for something demonstrably done but described differently (e.g., "automated build and deploy scripts" implies CI/CD).
- Prerequisite Inference: The skill is a technical prerequisite for the documented work (e.g., built and shipped a REST API implies HTTP and JSON handling).

A keyword does not qualify if it represents capability never demonstrated in any documented context, is adjacent to their domain but not shown, or is a stretch where reasonable doubt exists. Log every inferred skill as "Inferred from [role/project name]" with one sentence of justification.


STEP 3 - Narrative Dependency Mapping

Before reordering anything, identify locked sequences within each section: any bullet that introduces a system, component, or context that a later bullet explicitly builds upon; any bullet that establishes the scale or problem setup that makes a subsequent achievement meaningful; any bullet describing a prerequisite step before its outcome. Locked sequences must never be broken regardless of JD relevance.


STEP 4 - Conditional Bullet Reordering

Reorder a bullet only if all three conditions are simultaneously met:
A) The bullet is not part of a locked sequence identified in Step 3.
B) Moving it would bring a bullet addressing a core JD requirement from position 3 or lower to position 1 within that section.
C) The current top 1-2 bullets do not already address the same JD requirement.

If the gain is marginal, do not reorder. Default is to preserve the original order.


STEP 5 - Surgical Bullet Modification (Last Resort, High Bar)

Only for JD keywords that could not be placed via either pass of Step 2. A modification requires all four gates to pass. If any gate fails, the keyword is a true gap — log it, do not force it.

Gate 1 - Concept Exists: The bullet already describes work that embodies this skill. The concept is present, just expressed generically. This is a terminology upgrade, not introducing a new capability.
Gate 2 - Zero New Claims: The modification introduces no new facts, metrics, or capabilities. The bullet's meaning does not change.
Gate 3 - Significant Impact: A technical hiring manager would meaningfully change their assessment of this bullet's relevance to the JD. Cosmetic improvement does not pass this gate.
Gate 4 - Naturalness and Length: Read the modified bullet aloud. It must sound at least as natural as the original and must not exceed the original word count by more than 3-4 words. If the injection requires more space than that, it fails this gate. One injected keyword per bullet maximum.

If all four gates pass, make the minimal text change required — a terminology upgrade, not a sentence rewrite.


STEP 6 - True Gap Logging

Any JD keyword that could not be placed via Steps 2 or 5 is a true gap. For each: name it, confirm it is absent from both explicit documents and reasonable contextual inference, and suggest one specific actionable way to address it in a future resume version. Do not force placements to avoid logging a gap.


STEP 7 - Professional Summary Optimization

Rewrite the summary in 2-3 lines as a targeted hook for this SWE role. Mirror JD language on years of experience, core tech stack, and system design objectives. Use only documented facts. Introduce no new claims. Match the approximate character length of the original summary — do not write a longer summary that will overflow the resume layout.


STEP 8 - Content Quality Audit

Review every bullet in the resume, original and modified, against every item below and fix all failures before proceeding.

Tense: Past tense for all non-current roles. Present tense for current role only.
Action Verb Variety: No action verb repeated more than twice within a section. Swap repeats for a precise alternative.
Banned Cliche Verbs: spearheaded, orchestrated, leveraged, utilized, fostered, delved, championed, harnessed. Replace with plain, direct alternatives.
Banned Filler Words: various, multiple, several, robust, cutting-edge, innovative, complex, dynamic, seamless, end-to-end. Remove or replace.
Bullet Structure: Every bullet follows Action Verb + Technical Task + Measurable Impact. Flag any bullet missing a quantifiable outcome in the Gap section if the context docs cannot supply a metric.
Grammar: Confirm no awkward phrasing was introduced by any keyword injection. Check subject-verb agreement, article usage, and parallel structure within multi-part bullets.
Injection Density: No single bullet contains more than one injected or modified keyword. If two keywords belong to the same bullet, choose the higher-JD-priority one and place the other in the Skills section.


STEP 9 - Multi-Persona Review

Silently evaluate the full draft before generating any output and fix every issue found.

Senior Software Engineer lens: Are all system design concepts used in a technically accurate and contextually appropriate way? Does the reordering make logical sense for the JD's specific tech stack? Were any skills from the context docs that overlap with the JD overlooked?

Recruiter lens: Is the most relevant experience visible within the first 6 seconds of scanning? Is every bullet immediately understandable to a technical recruiter? Does the overall resume feel cohesive, human-written, and internally consistent?


OUTPUT FORMAT - Produce in this exact order.

SECTION 1 - ATS Score and Gap Analysis
Estimated ATS match score from 0-100.
True gaps only (from Step 6): keyword, reason it could not be placed, one actionable suggestion for a future resume version.

SECTION 2 - Change Log
Skills added via Direct Evidence: keyword and the Skills group it was added to.
Skills added via Contextual Inference: keyword, Skills group, one-sentence inference justification.
Bullets reordered: section name, original position to new position, one-line justification referencing the three-gate test.
Bullets modified: full BEFORE text and full AFTER text for each, and which gates justified the change.
Content Quality Audit fixes applied, listed briefly.

SECTION 3 - Change Report
This is the only output you will produce for resume edits. Do not output any LaTeX code. For every change to be made — skills additions, bullet text modifications, bullet reordering, and summary rewrite — list it in this exact format:

CHANGE [number]
LOCATION: [Section name and enough detail to find it, e.g., "GEP Worldwide experience - Bullet 3" or "Skills Section - Backend Frameworks group"]
ACTION: [ADD / REPLACE / REORDER]
FIND: [The exact text string as it appears in the current resume. For a reorder, the exact bullet text to be moved.]
REPLACE WITH: [The exact new text string. For a skills addition, the exact keyword and where in the group it should appear. For a reorder, the new position relative to named surrounding bullets.]
REASON: [One sentence stating which step and which rule triggered this change.]

I will apply all changes manually to the LaTeX source.

--- TARGET JOB DATA ---
Job Title: [Insert Job Title]
Job Description:
[Paste Job Description here]

### OLD
#### V3 -

#### Phase 1 — SDE Context Initialization (Run once initially)

Role: Act as an elite Technical Recruiter, ATS Algorithm Expert, and Senior Software
Engineering Manager.

Objective: Ingest the three documents provided below — Master Resume (LaTeX), Work
Experience Context, and Project Context. Read each document carefully and completely.
Do not generate a tailored resume yet.

After reading, produce a structured synthesis that confirms your understanding. This
synthesis is your working knowledge base for all future tailoring in this session.
Format it exactly as follows:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SYNTHESIS REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WORK EXPERIENCE
For each role, list:
  • Company | Role Title | Approximate Duration
  • Tech stack used (languages, frameworks, tools, cloud services) — sourced only
    from the documents; do not infer or add anything not explicitly stated
  • 2–3 sentence description of the core engineering work done
  • Key quantified achievements as stated in the documents (copy numbers exactly)

PROJECTS
For each project, list:
  • Project Name | Your Role
  • Tech stack used — sourced only from the documents
  • 1–2 sentence description of what the project does and how it works technically
  • Key quantified outcomes as stated in the documents

SKILLS INVENTORY
List every distinct technical skill, tool, framework, language, and platform mentioned
anywhere across the three documents. Group into:
  Languages | Backend Frameworks | Frontend | Cloud/DevOps | Databases | Other Tools

GAPS AND AMBIGUITIES
List anything unclear, inconsistent across documents, or missing that would be useful
for resume tailoring (e.g., a metric stated vaguely, a tool named but not
contextualized). Do not resolve these yourself — flag them for my review.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Non-Hallucination Principle:
Everything in your synthesis must come directly from the provided documents. Do not
infer experience from tool names alone. Do not assume a metric if one is not stated.
Do not extrapolate project scope beyond what is written. If a detail is not in the
documents, it does not exist in this session.

Once I confirm your synthesis is accurate, you are ready for Phase 2.

--- MY MASTER DATA ---
[Paste your full LaTeX Resume code here]
[Paste your Work Experience Context doc here]
[Paste your Project Context doc here]


#### Phase 2 — SDE Tailoring Engine (For every prompt)

Role: Act as an elite Technical Recruiter, ATS Optimization Expert, Senior Software
Engineer, and precise LaTeX text editor.

Task: Tailor my Master Resume to the provided SDE Job Description (JD). Maximize ATS
keyword coverage while preserving the natural readability, narrative coherence, and
LaTeX integrity of the original document.

Core Philosophy: You are a surgical text editor, not a rewriter. Every change must
make the resume strictly better — more relevant, cleaner, or more impactful. If a
change does not clearly improve the resume, do not make it. Recruiter readability
always takes priority over ATS score inflation.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EXECUTION STEPS — Follow in this strict order
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1 — JD Keyword Extraction
Carefully read the full JD. Extract and categorize every relevant technical keyword:
  (A) Hard Skills / Tools / Frameworks (e.g., Kubernetes, gRPC, Kafka, Redis, Docker)
  (B) Conceptual / Architectural Skills (e.g., microservices, event-driven architecture,
      distributed systems, CI/CD pipelines, horizontal scaling)

Assign each keyword a priority tier based on how the JD signals it:
  • CORE: Listed in required qualifications, appears multiple times, or is central to
    the role description
  • SECONDARY: Listed in preferred qualifications or appears once in passing

This priority determines how hard to work to place each keyword in Steps 2–5.

─────────────────────────────────────────────────────
STEP 2 — Explicit Skills Placement (Tier 1)
─────────────────────────────────────────────────────
Cross-reference the keyword list against the confirmed Synthesis from Phase 1.
For every keyword that is explicitly present in my documents, add it to the
appropriate logical group in the Skills section:
  Languages | Backend Frameworks | Cloud/DevOps | Databases | CI/CD | Other Tools

This is the safest form of ATS optimization — it carries zero risk of disrupting
bullet readability. Exhaust this step fully before touching any bullet points.
Mark each keyword placed here as RESOLVED (Tier 1). It requires no further action.

─────────────────────────────────────────────────────
STEP 3 — Inferred Skills Placement (Tier 2)
─────────────────────────────────────────────────────
For every keyword that remains UNRESOLVED after Step 2, perform a contextual
inference analysis against my work experience and project descriptions.

A keyword qualifies for Tier 2 placement if the work I have done, as described
in the documents, clearly implies this skill even if the exact term was never used.

Valid inference criteria — the inference is grounded if:
  • The work description names a system whose standard operation requires this skill
    (e.g., "deployed containerized services" implies Docker/container orchestration
    experience; "built async job processing system" implies a message queue pattern)
  • The project context describes an architectural pattern that is definitionally
    associated with this technology (e.g., "horizontal scaling with load distribution"
    implies load balancer experience; "token-based auth system" implies JWT/OAuth)
  • The Experience Context doc describes the team, system, or codebase in a way that
    makes the skill a logical necessity of the described work

Invalid inference — do NOT infer if:
  • The skill is merely commonly used alongside tools I do have (guilt by association)
  • The inference requires assuming scope or responsibility not described
  • The skill represents a meaningfully different approach that could have been done
    another way (e.g., do not infer Redis just because I built caching)

For every Tier 2 placement, add the keyword to the Skills section AND log it in the
Change Log with a one-sentence explanation of the specific inference made. This
transparency is required so I can verify each inferred skill before submitting.

Mark each keyword placed here as RESOLVED (Tier 2).

─────────────────────────────────────────────────────
STEP 4 — Narrative Dependency Mapping (Pre-Reorder Audit)
─────────────────────────────────────────────────────
Before reordering anything, map the logical dependencies within each section:
  • Identify any bullet that introduces a system, component, or context that a later
    bullet in the same section explicitly builds upon or references
  • Identify bullets that establish scale, architecture, or problem setup that makes
    a subsequent achievement bullet meaningful
  • Identify bullets that describe a prerequisite step in a workflow before its outcome

Mark any such dependent sequence as a LOCKED SEQUENCE. These must not be broken
under any circumstances, even for a highly relevant JD keyword.

─────────────────────────────────────────────────────
STEP 5 — Conditional Bullet Reordering
─────────────────────────────────────────────────────
Reorder bullets only if ALL THREE of the following conditions are simultaneously met:
  (A) DEPENDENCY CLEAR: The bullet is narratively independent — it passes the Step 4
      dependency check and is not part of a locked sequence
  (B) HIGH RELEVANCE GAIN: The reorder moves a bullet directly addressing a CORE JD
      requirement from position 3 or lower to position 1 within that section
  (C) GAP AT THE TOP: The current top 1–2 bullets do not already address the same
      CORE JD requirement

Default stance: preserve the original order unless all three gates pass.
Marginal gains and SECONDARY keyword alignments are never sufficient justification.

─────────────────────────────────────────────────────
STEP 6 — Surgical Bullet Modification (Tier 3)
─────────────────────────────────────────────────────
Only attempt this for CORE keywords that remain UNRESOLVED after Steps 2 and 3.
SECONDARY keywords that could not be placed in the Skills section should go directly
to the Gap Analysis — they do not warrant bullet modification.

A bullet may be modified only if ALL of the following are true:
  (i)   CONCEPT EXISTS: The bullet already describes work that used or embodied this
        skill. The keyword is a more precise or industry-standard label for something
        already present in the bullet — not a new capability being added
  (ii)  SIGNIFICANT IMPACT: Adding this keyword to this bullet would meaningfully
        change how a recruiter or ATS reads it for this specific role. If the bullet
        would remain comparably strong without the change, do not make it
  (iii) ZERO NEW CLAIMS: The insertion requires no new facts, no new metrics, and no
        restructuring of the bullet's meaning. It is a terminology precision upgrade
        only — e.g., "message queue" → "Kafka message queue", "in-memory cache" →
        "Redis in-memory cache", "container orchestration" → "Kubernetes orchestration"

  Naturalness Mandate: After modifying a bullet, read it aloud in full. If the keyword
  sounds inserted, if the sentence became harder to parse, or if the structure feels
  less natural than the original, revert. A bullet that reads worse serves the recruiter
  worse regardless of the keyword it contains.

  Injection Density Rule: No single bullet may receive more than one injected keyword.
  If two CORE keywords both qualify for the same bullet, choose the higher-JD-priority
  one and attempt to place the other in the Skills section via Tier 2 reasoning.

─────────────────────────────────────────────────────
STEP 7 — Gap Analysis (Tier 4)
─────────────────────────────────────────────────────
Any keyword that could not be placed via Tiers 1, 2, or 3 is a true gap. For each:
  • Name the keyword and its JD priority (CORE or SECONDARY)
  • Explain specifically why it could not be placed (no explicit mention, no valid
    inference, no bullet modification passed the Tier 3 gates)
  • Suggest a concrete future action (e.g., a project to build, a technology to add
    to a current system, a certification to pursue)

─────────────────────────────────────────────────────
STEP 8 — Professional Summary Optimization
─────────────────────────────────────────────────────
Rewrite the summary (2–3 lines maximum) as a targeted hook for this specific SWE
role. Mirror the JD's language regarding years of experience, core backend/frontend
tech stack, and system design objectives. Use only what is factually supported by
the confirmed Phase 1 synthesis. Introduce no new claims.

─────────────────────────────────────────────────────
STEP 9 — Content Quality Audit
─────────────────────────────────────────────────────
Review every bullet in the tailored resume — original and modified — against this
checklist. Fix every failure before proceeding to output:

  □ TENSE: Past tense for all non-current roles. Present tense for current role only.
  □ ACTION VERB VARIETY: No action verb repeated more than twice in any section.
    Swap repeats for a more precise, direct alternative.
  □ BANNED CLICHÉ VERBS: spearheaded, orchestrated, leveraged, utilized, fostered,
    delved, championed, harnessed → replace with plain, precise alternatives.
  □ BANNED FILLER WORDS: various, multiple, several, robust, cutting-edge, innovative,
    complex, dynamic, seamless, end-to-end → remove or replace with specific language.
  □ BULLET STRUCTURE: Every bullet should follow [Action Verb] + [Technical Task] +
    [Measurable Impact]. Flag any bullet missing a quantifiable outcome in the Gap
    Analysis if the context docs cannot supply a metric.
  □ GRAMMAR: Read every modified bullet in full sentence context. Confirm no awkward
    phrasing was introduced. Check subject-verb agreement, article usage, and parallel
    structure within multi-part bullets.
  □ INJECTION DENSITY: Confirm no bullet received more than one injected keyword.
  □ INTERNAL CONSISTENCY: The same system, tool, or concept should be referred to by
    the same name throughout the entire document.

─────────────────────────────────────────────────────
STEP 10 — Multi-Persona Review
─────────────────────────────────────────────────────
Silently evaluate the full draft before generating any output:

  Senior Software Engineer lens:
  • Are all system design concepts used in a technically accurate and contextually
    appropriate way for this specific tech stack and role?
  • Does the reordering make logical sense for the engineering requirements in the JD?
  • Were any skills from the Phase 1 synthesis that overlap with the JD overlooked?
  • Are all Tier 2 inferred skills genuinely defensible — could I explain this skill
    in an interview based on the work described?

  Recruiter lens:
  • Is the most relevant experience visible within the first 6 seconds of scanning?
  • Is every bullet immediately understandable without specialist domain knowledge?
  • Does the resume feel cohesive, human-written, and internally consistent?

  Fix every issue surfaced before proceeding to output.

─────────────────────────────────────────────────────
STEP 11 — LaTeX Text-Substitution Protocol (CRITICAL)
─────────────────────────────────────────────────────
You are operating as a text editor on a LaTeX file. You are NOT a LaTeX author.

  ABSOLUTE RULES:
  • Do NOT regenerate, restructure, or rewrite any LaTeX commands, macros,
    environments, or document-level structure.
  • Do NOT alter formatting, spacing, section ordering, dates, company names, role
    titles, or degree information unless explicitly justified and logged.
  • ONLY change the plain text content inside \item{} environments and the summary.
  • Every single change must be representable as an exact find-and-replace text pair.

  BEFORE generating the final code block, declare every change in this format:
    CHANGE #N
    FIND:    [exact original text string as it appears in the LaTeX]
    REPLACE: [exact replacement text string]
    REASON:  [which Step and Tier triggered this, and why — one sentence]

  Then produce the final LaTeX code by applying ONLY those substitutions to the
  original. Every other character must remain byte-for-byte identical.

─────────────────────────────────────────────────────
STEP 12 — LaTeX Self-Validation Checklist
─────────────────────────────────────────────────────
Verify each item before outputting. Do not output until all pass:

  □ Every \begin{} has a matching \end{} tag
  □ No new LaTeX commands, macros, or custom environments were introduced
  □ All original section headings, company names, role titles, and dates are
    unchanged (or explicitly listed as intentional changes in the log)
  □ No \item has been deleted unless listed in the Change Log with justification
  □ All special characters are correctly escaped: & % $ # _ ^ ~ { }
  □ The total number of changes in the final code exactly matches the number of
    entries in the Find-Replace Manifest. Resolve any mismatch before outputting.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OUTPUT FORMAT — Produce in this exact order
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 1 — ATS Score & Keyword Placement Summary
  • Estimated ATS match score (0–100)
  • Table of all JD keywords, their priority (CORE/SECONDARY), and resolution:
    Tier 1 (explicit) | Tier 2 (inferred — include the inference reasoning) |
    Tier 3 (bullet modification) | Tier 4 (true gap — include future action)

SECTION 2 — Change Log
  • Skills added (keyword → Skills group → Tier 1 or Tier 2, with Tier 2 reasoning)
  • Bullets reordered (section, original position → new position, three-gate result)
  • Bullets modified (full BEFORE / full AFTER for each change)
  • Content Quality Audit fixes applied

SECTION 3 — Find-Replace Manifest
  All CHANGE #N entries from Step 11

SECTION 4 — Final LaTeX Code
  Complete tailored LaTeX in a single code block

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
--- TARGET JOB DATA ---
Job Title: [Insert Job Title]
Job Description:
[Paste Job Description here]



#### V2 -

1. Role: Act as an elite Technical Recruiter, ATS (Applicant Tracking System) Optimization Expert, and LaTeX formatting specialist.
   
   Context & Objective: I am providing a Job Description (JD) and the LaTeX source code of my resume. My resume’s bullet points have already been rigorously optimized by industry experts for ATS performance and impact.
   
   Your objective is to tailor this resume to the provided JD by maximizing keyword overlap, and then evaluate how well the final tailored version matches the JD. You must operate under a strict "Do No Harm / Minimal Intervention" mandate for the bullet points.
   
   Execution Rules (Strictly follow this order):
   
   The Skills Section (Primary Target): Extract all relevant technical skills, tools, and methodologies from the JD. Integrate as many of these missing keywords as logically possible into my existing Skills section. Group them appropriately within my current categories (e.g., Languages, Frameworks, Tools).
   
   Role Title Optimization: Analyze my current role titles. If making a slight, truthful adjustment to a title (e.g., changing "Software Engineer" to "Backend Developer" or "SDE") creates a significantly stronger ATS match based on the JD, make the change.
   
   Bullet Point Modification (High-Threshold Rule):
   Constraint: Do NOT rewrite bullet points just to sound different. 
   You may only modify a bullet point if a critical keyword from the JD cannot naturally fit into the Skills section (e.g., a specific business impact term, architectural concept, or soft skill), AND adding it makes a massive difference in matching the JD.
   
   Surgical Integration: If you must add a keyword to a bullet point, weave it in seamlessly. It must not feel forcibly stuffed or disrupt the existing "Action Verb + Task + Impact" structure. It must feel highly appropriate for the context of that specific bullet.
   
   Formatting Preservation: Make absolutely ZERO changes to the LaTeX formatting, macros, document structure, spacing, or dates. The structural code must remain identical.
   
   Quality Control & Verification: Once changes are made, rigorously recheck the modified lines. Ensure perfect spelling, grammar, clarity, and tense consistency (past tense for past roles, present for current). Ensure the updated points still convey maximum professional impact.
   
   ATS Match Evaluation & Gap Analysis:: After making all tailoring adjustments, perform a simulated ATS scan of the newly tailored resume against the provided Job Description to calculate a final match score out of 100.
   
   Output Requirements:

	- Targeted ATS Score & Gap Analysis (0-100): Provide the estimated ATS match score. If the score is less than 100: You must explicitly list the exact reasons why it fell short. Provide a clear, actionable breakdown of the missing experiences, metrics, or keywords preventing a perfect score, and tell me exactly what needs to be added (and where) to achieve a 100.

	- Change Log: Briefly list the exact keywords added to the Skills section, any Role Titles changed, and a short explanation of any bullet points altered (showing the "Before" and "After").
	
	
	The Code:
	- IF you only made changes to the Skills section: Output ONLY the LaTeX code for that specific section.

	- IF you made changes to Role Titles or Bullet Points: Output the ENTIRE LaTeX code of the resume.
	
	Job Title - Developer Technology Intern, High-Performance Databases - Summer 2026
	
	Job Description -
	
		Latex Resume Code -

#### V1 -
	
Role: Act as an elite Technical Recruiter, ATS (Applicant Tracking System) Optimization Expert, and LaTeX formatting specialist.
   
   Context & Objective:
   I am providing a Job Description (JD) and the LaTeX source code of my resume. My resume’s bullet points have already been rigorously optimized by industry experts for ATS performance and impact.
   Your objective is to tailor this resume to the provided JD by maximizing keyword overlap, and then evaluate how well the final tailored version matches the JD. You must operate under a strict "Do No Harm / Minimal Intervention" mandate for the bullet points.
   
   Execution Rules (Strictly follow this order):
	   1. The Skills Section (Primary Target):
	      Extract all relevant technical skills, tools, and methodologies from the JD. Integrate as many of these missing keywords as logically possible into my existing Skills section. Group them appropriately within my current categories (e.g., Languages, Frameworks, Tools).
	
	2. Role Title Optimization:
		   Analyze my current role titles. If making a slight, truthful adjustment to a title (e.g., changing "Software Engineer" to "Backend Developer" or "SDE") creates a significantly stronger ATS match based on the JD, make the change.
	
	3. Bullet Point Modification (High-Threshold Rule):
		   Constraint: Do NOT rewrite bullet points just to sound different.
		   You may only modify a bullet point if a critical keyword from the JD cannot naturally fit into the Skills section (e.g., a specific business impact term, architectural concept, or soft skill), AND adding it makes a massive difference in matching the JD.
		   Surgical Integration: If you must add a keyword to a bullet point, weave it in seamlessly. It must not feel forcibly stuffed or disrupt the existing "Action Verb + Task + Impact" structure. It must feel highly appropriate for the context of that specific bullet.
	4. Formatting Preservation:
		   Make absolutely ZERO changes to the LaTeX formatting, macros, document structure, spacing, or dates. The structural code must remain identical.
	
	5. Quality Control & Verification:
		   Once changes are made, rigorously recheck the modified lines. Ensure perfect spelling, grammar, clarity, and tense consistency (past tense for past roles, present for current). Ensure the updated points still convey maximum professional impact.
	   
	6. ATS Match Evaluation & Gap Analysis::
		   After making all tailoring adjustments, perform a simulated ATS scan of the newly tailored resume against the provided Job Description to calculate a final match score out of 100.

	Output Requirements:
		- Targeted ATS Score & Gap Analysis (0-100): Provide the estimated ATS match score. If the score is less than 100: You must explicitly list the exact reasons why it fell short. Provide a clear, actionable breakdown of the missing experiences, metrics, or keywords preventing a perfect score, and tell me exactly what needs to be added (and where) to achieve a 100.
		- Change Log: Briefly list the exact keywords added to the Skills section, any Role Titles changed, and a short explanation of any bullet points altered (showing the "Before" and "After").

	The Code:
		- IF you only made changes to the Skills section: Output ONLY the LaTeX code for that specific section.
		- IF you made changes to Role Titles or Bullet Points: Output the ENTIRE LaTeX code of the resume.
	
	Job Title - Software Engineer Intern, Cloud Services - HP IQ
	
	Job Description -
	
	LaTeX Resume Code -












## DS -

### V4 -

#### Phase 1 — DS/ML Context Initialization

Role: Act as an elite Technical Recruiter, ATS Algorithm Expert, and Lead Machine Learning Engineer.

Objective: Ingest the three documents below — Master Resume (LaTeX), Work Experience Context, and Project Context. Read each carefully and completely. Do not generate a tailored resume yet.

After reading, produce a Synthesis Report in this exact format:

WORK EXPERIENCE
For each role: Company | Role Title | Approximate Duration, the ML and data tech stack used (sourced only from the documents, do not infer), a 2-3 sentence description of the core ML or data engineering work, and key quantified achievements copied exactly as stated.

PROJECTS
For each project: Project Name | Your Role, the tech stack and model architecture used (sourced only from the documents), a 1-2 sentence description of what the system does, how it works technically, and what data it operates on, and key quantified outcomes as stated.

SKILLS INVENTORY
Every distinct technical skill, tool, framework, library, and platform mentioned anywhere across the three documents, grouped into: ML Frameworks, Data Engineering, Languages, Vector Databases, Cloud/MLOps, Other Tools.

GAPS AND AMBIGUITIES
Anything unclear, inconsistent across documents, or missing that would affect tailoring (e.g., a vague metric, an architecture described partially, a tool named but not contextualized). Do not resolve these — flag them for my review.

Non-Hallucination Principle: Everything in the synthesis must come directly from the provided documents. Do not infer model architecture choices beyond what is written, assume unstated benchmark results, or generalize a project's scope beyond what is explicitly described. If a detail is not in the documents, it does not exist in this session.

Once I confirm your synthesis is accurate, you are ready for Phase 2.

--- MY MASTER DATA ---
[Paste your full LaTeX Resume code here]
[Paste your Work Experience Context doc here]
[Paste your Project Context doc here]

#### Phase 2 — DS/ML Tailoring Engine ( (For every prompt))

Role: Act as an elite Technical Recruiter, ATS Optimization Expert, Senior Data Scientist / ML Engineer, and resume text editor.

Task: Tailor my Master Resume to the provided DS/ML Job Description (JD). Maximize ATS keyword coverage while preserving natural readability, narrative coherence, and original content length.

Core Philosophy: You are a surgical text editor, not a rewriter. Every change must make the resume strictly better. If a change does not clearly improve the resume, do not make it. Recruiter readability always takes priority over ATS score inflation. No modified bullet may exceed its original word count by more than 3-4 words. Length overruns cause reformatting work and are treated as a failed edit.


STEP 1 - JD Keyword Extraction

Read the full JD and extract every relevant technical keyword into two categories:
A) Hard Skills / Frameworks / Tools (e.g., PyTorch, LangChain, FAISS, HuggingFace, Spark, dbt, MLflow)
B) Conceptual / Methodological Skills (e.g., RAG pipeline design, LLM fine-tuning, vector search, data streaming, feature engineering, model evaluation)

This keyword list drives all decisions in Steps 2-6.


STEP 2 - Skills Section Placement (Two-Pass)

This is the primary and preferred placement method for all JD keywords. Exhaust both passes fully before touching any bullet.

Pass 1 - Direct Evidence: For any JD keyword explicitly named or used in the context documents, add it to the appropriate Skills group. Mark as resolved.

Pass 2 - Contextual Inference: For keywords not placed in Pass 1, evaluate whether the documented work makes the skill logically certain or highly probable even if never explicitly named. A keyword qualifies if it meets any one of these criteria:
- Component Inference: The skill is a direct named component of a documented pipeline or model architecture (e.g., built a RAG pipeline implies vector search and embedding models; fine-tuned with QLoRA implies parameter-efficient fine-tuning).
- Terminology Inference: The skill is the standard ML industry term for something demonstrably done but described differently (e.g., "ranked results using a scoring model" implies learning-to-rank; "chunked and indexed documents for retrieval" implies document preprocessing strategy).
- Prerequisite Inference: The skill is a technical prerequisite for the documented work (e.g., trained a neural network implies backpropagation and gradient descent; built a data streaming pipeline implies serialization and schema design).

A keyword does not qualify if it represents capability never demonstrated in any documented context, belongs to a different modeling paradigm from what is shown (e.g., do not infer computer vision from NLP work), or is a stretch where reasonable doubt exists.

Mathematical Accuracy Rule: All contextual inferences must respect ML terminology boundaries. Do not use "fine-tuning" to imply "RAG." Do not use "embeddings" to imply "supervised classification." Inferences must be technically sound. Log every inferred skill as "Inferred from [role/project name]" with one sentence of justification.


STEP 3 - Narrative Dependency Mapping

Before reordering anything, identify locked sequences within each section: any bullet that introduces a dataset, model architecture, or pipeline component that a later bullet explicitly builds upon; any bullet that establishes the problem setup, data scale, or baseline metric that makes a subsequent result meaningful; any bullet describing a data preparation or training step before its evaluation outcome. Locked sequences must never be broken regardless of JD relevance.


STEP 4 - Conditional Bullet Reordering

Reorder a bullet only if all three conditions are simultaneously met:
A) The bullet is not part of a locked sequence identified in Step 3.
B) Moving it would bring a bullet addressing a core JD requirement from position 3 or lower to position 1 within that section.
C) The current top 1-2 bullets do not already address the same JD requirement.

If the gain is marginal, do not reorder. Default is to preserve the original order.


STEP 5 - Surgical Bullet Modification (Last Resort, High Bar)

Only for JD keywords that could not be placed via either pass of Step 2. A modification requires all four gates to pass. If any gate fails, the keyword is a true gap — log it, do not force it.

Gate 1 - Concept Exists: The bullet already describes work that embodies this skill. The concept is present, just expressed generically or with less precise ML terminology. This is a terminology upgrade, not introducing a new capability (e.g., "similarity search over indexed embeddings" to "FAISS-based similarity search over indexed embeddings").
Gate 2 - Zero New Claims: The modification introduces no new facts, performance numbers, or capabilities. The bullet's meaning does not change.
Gate 3 - Significant Impact: A technical hiring manager would meaningfully change their assessment of this bullet's relevance to the JD. Cosmetic improvement does not pass this gate.
Gate 4 - Naturalness and Length: Read the modified bullet aloud. It must sound at least as natural as the original and must not exceed the original word count by more than 3-4 words. If the injection requires more space than that, it fails this gate. One injected keyword per bullet maximum.

If all four gates pass, make the minimal text change required — a terminology upgrade, not a sentence rewrite.


STEP 6 - True Gap Logging

Any JD keyword that could not be placed via Steps 2 or 5 is a true gap. For each: name it, confirm it is absent from both explicit documents and reasonable contextual inference, and suggest one specific actionable way to address it in a future resume version. Do not force placements to avoid logging a gap.


STEP 7 - Professional Summary Optimization

Rewrite the summary in 2-3 lines as a targeted hook for this DS/ML role. Mirror JD language on ML frameworks, data pipeline methodologies, and modeling objectives. Use only documented facts. Introduce no new claims. Match the approximate character length of the original summary — do not write a longer summary that will overflow the resume layout.


STEP 8 - Content Quality Audit

Review every bullet in the resume, original and modified, against every item below and fix all failures before proceeding.

Tense: Past tense for all non-current roles. Present tense for current role only.
Action Verb Variety: No action verb repeated more than twice within a section. Swap repeats for a precise alternative.
Banned Cliche Verbs: spearheaded, orchestrated, leveraged, utilized, fostered, delved, championed, harnessed. Replace with plain, direct alternatives.
Banned Filler Words: various, multiple, several, robust, cutting-edge, innovative, complex, dynamic, seamless, end-to-end. Remove or replace.
Bullet Structure: Every bullet follows Action Verb + Technical Task + Measurable Impact. Flag any bullet missing a quantifiable outcome in the Gap section if the context docs cannot supply a metric.
Grammar: Confirm no awkward phrasing was introduced by any keyword injection. Check subject-verb agreement, article usage, and parallel structure within multi-part bullets.
Injection Density: No single bullet contains more than one injected or modified keyword. If two keywords belong to the same bullet, choose the higher-JD-priority one and place the other in the Skills section.
ML Terminology Consistency: Ensure the same concept is referred to by the same term throughout the document. Do not say "vector store" in one bullet and "vector database" in another for the same system.


STEP 9 - Multi-Persona Review

Silently evaluate the full draft before generating any output and fix every issue found.

Senior ML Engineer lens: Is all ML terminology used in a mathematically and architecturally accurate way appropriate to this specific role? Does the reordering make logical sense for the modeling and data pipeline emphasis of the JD's domain (e.g., NLP vs. recommendations vs. data engineering)? Were any ML skills from the context docs that overlap with the JD missed?

Recruiter lens: Is the business or research impact of the ML work immediately visible and quantified? Is every bullet understandable to a technical recruiter familiar with ML concepts but not necessarily this specific architecture? Does the resume feel cohesive, human-written, and internally consistent?


OUTPUT FORMAT - Produce in this exact order.

SECTION 1 - ATS Score and Gap Analysis
Estimated ATS match score from 0-100.
True gaps only (from Step 6): keyword, reason it could not be placed, one actionable suggestion for a future resume version.

SECTION 2 - Change Log
Skills added via Direct Evidence: keyword and the Skills group it was added to.
Skills added via Contextual Inference: keyword, Skills group, one-sentence inference justification.
Bullets reordered: section name, original position to new position, one-line justification referencing the three-gate test.
Bullets modified: full BEFORE text and full AFTER text for each, and which gates justified the change.
Content Quality Audit fixes applied, listed briefly.

SECTION 3 - Change Report
This is the only output you will produce for resume edits. Do not output any LaTeX code. For every change to be made — skills additions, bullet text modifications, bullet reordering, and summary rewrite — list it in this exact format:

CHANGE [number]
LOCATION: [Section name and enough detail to find it, e.g., "GEP Worldwide experience - Bullet 3" or "Skills Section - ML Frameworks group"]
ACTION: [ADD / REPLACE / REORDER]
FIND: [The exact text string as it appears in the current resume. For a reorder, the exact bullet text to be moved.]
REPLACE WITH: [The exact new text string. For a skills addition, the exact keyword and where in the group it should appear. For a reorder, the new position relative to named surrounding bullets.]
REASON: [One sentence stating which step and which rule triggered this change.]

I will apply all changes manually to the LaTeX source.

--- TARGET JOB DATA ---
Job Title: [Insert Job Title]
Job Description:
[Paste Job Description here]


### V3 -

#### Phase 1 — DS/ML Context Initialization

Role: Act as an elite Technical Recruiter, ATS Algorithm Expert, and Lead Machine
Learning Engineer.

Objective: Ingest the three documents provided below — Master Resume (LaTeX), Work
Experience Context, and Project Context. Read each document carefully and completely.
Do not generate a tailored resume yet.

After reading, produce a structured synthesis that confirms your understanding. This
synthesis is your working knowledge base for all future tailoring in this session.
Format it exactly as follows:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SYNTHESIS REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WORK EXPERIENCE
For each role, list:
  • Company | Role Title | Approximate Duration
  • ML/data tech stack used (frameworks, libraries, data tools, cloud services) —
    sourced only from the documents; do not infer or add anything not explicitly stated
  • 2–3 sentence description of the core ML or data engineering work done
  • Key quantified achievements as stated in the documents (copy numbers exactly)

PROJECTS
For each project, list:
  • Project Name | Your Role
  • Tech stack and model architecture used — sourced only from the documents
  • 1–2 sentence description of what the system does, how it works technically,
    and what data it operates on
  • Key quantified outcomes as stated in the documents

SKILLS INVENTORY
List every distinct technical skill, tool, framework, library, and platform mentioned
anywhere across the three documents. Group into:
  ML Frameworks | Data Engineering | Languages | Vector Databases |
  Cloud/MLOps | Other Tools

GAPS AND AMBIGUITIES
List anything unclear, inconsistent across documents, or missing that would be useful
for resume tailoring (e.g., a metric stated vaguely, an architecture described
partially, a tool named but not contextualized). Do not resolve these — flag for review.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Non-Hallucination Principle:
Everything in your synthesis must come directly from the provided documents. Do not
infer model architecture choices beyond what is written. Do not assume a benchmark
result if one is not stated. Do not generalize a project's scope or approach beyond
what is explicitly described. If a detail is not in the documents, it does not exist
in this session.

Once I confirm your synthesis is accurate, you are ready for Phase 2.

--- MY MASTER DATA ---
[Paste your full LaTeX Resume code here]
[Paste your Work Experience Context doc here]
[Paste your Project Context doc here]


#### Phase 2 — DS/ML Tailoring Engine ( (For every prompt))

Role: Act as an elite Technical Recruiter, ATS Optimization Expert, Senior Data
Scientist / ML Engineer, and precise LaTeX text editor.

Task: Tailor my Master Resume to the provided DS/ML Job Description (JD). Maximize ATS
keyword coverage while preserving the natural readability, narrative coherence, and
LaTeX integrity of the original document.

Core Philosophy: You are a surgical text editor, not a rewriter. Every change must make
the resume strictly better — more relevant, cleaner, or more impactful. If a change does
not clearly improve the resume, do not make it. Recruiter readability always takes
priority over ATS score inflation.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EXECUTION STEPS — Follow in this strict order
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1 — JD Keyword Extraction
Carefully read the full JD. Extract and categorize every relevant technical keyword into:
  (A) Hard Skills / Frameworks / Tools (e.g., PyTorch, LangChain, FAISS, HuggingFace,
      Spark, dbt, Airflow, MLflow)
  (B) Conceptual / Methodological Skills (e.g., RAG pipeline design, LLM fine-tuning,
      vector search, data streaming, A/B testing, feature engineering, model evaluation)

This master keyword list drives all decisions in Steps 2–6.

─────────────────────────────────────────────────────
STEP 2 — Skills Section Placement (Two-Pass)
─────────────────────────────────────────────────────
This is the primary and preferred placement method for all JD keywords. Exhaust both
passes here before touching any bullet point.

  PASS 1 — Direct Evidence:
  Cross-reference every JD keyword against the synthesis from Phase 1. For any keyword
  that is explicitly named or used in the context documents, add it to the appropriate
  Skills group immediately. These are confirmed and fully resolved — mark them and
  move on.

  PASS 2 — Contextual Inference:
  For keywords not placed in Pass 1, evaluate whether the documented work makes it
  logically certain or highly probable that this skill was used, even if never
  explicitly named.

  A keyword qualifies for contextual inference if it meets any ONE of these criteria:
    (i)  COMPONENT INFERENCE: The skill is a direct, named component of a pipeline,
         model architecture, or system already documented. (e.g., built a RAG pipeline
         → vector search and embedding models are implied; fine-tuned an LLM with
         QLoRA → parameter-efficient fine-tuning is implied)
    (ii) TERMINOLOGY INFERENCE: The skill is the standard ML/data industry term for
         something they demonstrably did, described differently in the documents.
         (e.g., "ranked results using a scoring model" → learning-to-rank implied;
         "chunked and indexed documents for retrieval" → document preprocessing/
         chunking strategy implied)
    (iii) PREREQUISITE INFERENCE: The skill is a technical prerequisite that must have
         been applied to accomplish the documented work. (e.g., trained a neural network
         → backpropagation and gradient descent are prerequisites; built a data
         streaming pipeline → serialization/schema design is a prerequisite)

  A keyword does NOT qualify for contextual inference if:
    • It represents a modeling or engineering capability they might know but never
      demonstrated in any documented context
    • It is a different modeling paradigm from what is shown (e.g., they did NLP
      work — do not infer computer vision skills)
    • It is a stretch — if reasonable doubt exists, it does not qualify

  Mathematical Accuracy Rule: Contextual inference must respect ML terminology
  boundaries. Do not use "fine-tuning" to imply "RAG." Do not use "embeddings" to
  imply "supervised classification." Inferences must be technically sound.

  For every contextually inferred skill, log it in the Change Log as
  "Inferred from [project/role name]" with one sentence of justification.

─────────────────────────────────────────────────────
STEP 3 — Narrative Dependency Mapping (Pre-Reorder Audit)
─────────────────────────────────────────────────────
Before reordering anything, map the logical dependencies within each section:
  • Identify any bullet that introduces a dataset, model architecture, or pipeline
    component that a later bullet explicitly builds upon or references.
  • Identify bullets that establish the problem setup, data scale, or baseline metric
    that makes a subsequent result or improvement bullet meaningful.
  • Identify bullets that describe a data preparation or training step before its
    evaluation outcome.

Mark any such dependent sequence as a LOCKED SEQUENCE. These must not be broken
under any circumstances, even for a highly relevant JD keyword.

─────────────────────────────────────────────────────
STEP 4 — Conditional Bullet Reordering
─────────────────────────────────────────────────────
Reorder bullets only if ALL THREE of the following conditions are simultaneously met:
  (A) DEPENDENCY CLEAR: The bullet is narratively independent — it passes the Step 3
      check and is not part of a locked sequence.
  (B) HIGH RELEVANCE GAIN: The reorder would move a bullet that directly addresses a
      core JD requirement from position 3 or lower to position 1 within that section.
  (C) GAP AT THE TOP: The current top 1–2 bullets in that section do not already
      address the same core JD requirement.

If the gain is marginal, do NOT reorder. Preserve the original ordering by default.

─────────────────────────────────────────────────────
STEP 5 — Surgical Bullet Modification (Last Resort, High Bar)
─────────────────────────────────────────────────────
This step is only for JD keywords that could not be placed in the Skills section via
either pass of Step 2. Before modifying any bullet, the keyword must clear all four
gates below. If any gate fails, the keyword is a true gap — log it, do not force it.

  GATE 1 — CONCEPT EXISTS:
  The bullet already describes work that embodies this skill. The concept is present —
  it is just expressed in generic or less precise ML terms. You are upgrading the
  terminology, not introducing a new capability. (e.g., "similarity search over indexed
  embeddings" → "FAISS-based similarity search over indexed embeddings")

  GATE 2 — ZERO NEW CLAIMS:
  The modification introduces no new facts, no new model performance numbers, and no
  new capabilities. The meaning of the bullet does not change.

  GATE 3 — SIGNIFICANT IMPACT:
  A technical hiring manager would meaningfully change their assessment of this bullet's
  relevance to the JD by seeing this keyword. A minor cosmetic improvement does not
  clear this gate. The keyword must address a core, not peripheral, JD requirement.

  GATE 4 — NATURALNESS:
  Read the modified bullet aloud. It must sound at least as natural as the original.
  If the keyword sounds inserted, if the sentence became harder to parse, or if it reads
  like optimization, revert to the original. One injected keyword per bullet maximum.

  If all four gates pass, make the minimal text change required — a terminology upgrade,
  not a sentence rewrite.

─────────────────────────────────────────────────────
STEP 6 — True Gap Logging
─────────────────────────────────────────────────────
Any JD keyword that could not be placed via Step 2 or Step 5 is a true gap. For each:
  • Name the keyword
  • Confirm it is absent from both the explicit documents and any reasonable contextual
    inference
  • Suggest one specific, actionable way to address it in a future resume version
    (e.g., a project type to build, a dataset to work with, a tool to get hands-on with)

This is the correct and honest outcome. Do not force placements to avoid logging a gap.

─────────────────────────────────────────────────────
STEP 7 — Professional Summary Optimization
─────────────────────────────────────────────────────
Rewrite the summary (2–3 lines maximum) as a targeted hook for this specific DS/ML role.
Mirror the JD's language regarding ML frameworks, data pipeline methodologies, and
modeling objectives. Use only what is factually true in my background. No new claims.

─────────────────────────────────────────────────────
STEP 8 — Content Quality Audit
─────────────────────────────────────────────────────
Review every bullet in the tailored resume — original and modified — against this
checklist. Fix every failure before proceeding:

  □ TENSE: Past tense for all non-current roles. Present tense for current role only.
  □ ACTION VERB VARIETY: No action verb repeated more than twice in a section.
    Swap repeats for a more precise alternative.
  □ BANNED CLICHÉ VERBS: spearheaded, orchestrated, leveraged, utilized, fostered,
    delved, championed, harnessed → replace with plain, direct alternatives.
  □ BANNED FILLER WORDS: various, multiple, several, robust, cutting-edge, innovative,
    complex, dynamic, seamless, end-to-end → remove or replace.
  □ BULLET STRUCTURE: Every bullet follows [Action Verb] + [Technical Task] +
    [Measurable Impact]. Flag missing metrics in the Gap section if context docs
    cannot supply a number.
  □ GRAMMAR: Confirm no awkward phrasing was introduced. Check subject-verb agreement,
    article usage, and parallel structure in multi-part bullets.
  □ INJECTION DENSITY: No single bullet contains more than one modified or injected
    keyword. If two belong to the same bullet, choose the higher-JD-priority one and
    place the other in the Skills section.
  □ ML TERMINOLOGY CONSISTENCY: Ensure the same concept is referred to by the same
    term throughout the document. Do not say "vector store" in one bullet and "vector
    database" in another for the same system.

─────────────────────────────────────────────────────
STEP 9 — Multi-Persona Review
─────────────────────────────────────────────────────
Silently evaluate the full draft before generating any output:

  Senior ML Engineer lens:
  • Is all ML terminology used in a mathematically and architecturally accurate way
    appropriate to this specific role?
  • Does the reordering make logical sense for the modeling and data pipeline emphasis
    of the JD's domain (e.g., NLP vs. recommendations vs. data engineering)?
  • Were any ML skills or frameworks from the context docs that overlap with the JD
    missed?

  Recruiter lens:
  • Is the business or research impact of the ML work immediately visible and quantified?
  • Is every bullet understandable to a technical recruiter familiar with ML concepts
    but not necessarily this specific architecture?
  • Does the resume feel cohesive, human-written, and internally consistent?

  Fix every issue surfaced before outputting.

─────────────────────────────────────────────────────
STEP 10 — LaTeX Text-Substitution Protocol (CRITICAL)
─────────────────────────────────────────────────────
You are operating as a text editor on a LaTeX file. You are NOT a LaTeX author.

  ABSOLUTE RULES:
  • Do NOT regenerate, restructure, or rewrite any LaTeX commands, macros, environments,
    or document-level structure.
  • Do NOT alter formatting, spacing, section ordering, dates, company names, role
    titles, or degree information (unless a role title change is explicitly logged).
  • ONLY change the plain text content inside \item{} environments and the summary
    block.
  • Every single change must be representable as an exact find-and-replace text pair.

  BEFORE generating the final code block, declare every change in this format:
    CHANGE #1
    FIND:    [exact original text string]
    REPLACE: [exact replacement text string]
    REASON:  [one sentence — which step triggered this and why]

  Then produce the final LaTeX by applying ONLY those substitutions to the original.
  Every other character must remain byte-for-byte identical.

─────────────────────────────────────────────────────
STEP 11 — LaTeX Self-Validation Checklist
─────────────────────────────────────────────────────
Verify each item before outputting. Do not output until all pass:

  □ Every \begin{} has a matching \end{}.
  □ No new LaTeX commands, macros, or environments were introduced.
  □ All original section headings, company names, role titles, and dates are unchanged
    (or explicitly logged as intentional changes).
  □ No \item has been deleted unless listed in the Change Log with justification.
  □ All special characters are correctly escaped: & % $ # _ ^ ~ { }
  □ The number of changes in the final code exactly matches the number of entries in
    the Find-Replace Manifest. If there is a mismatch, identify and resolve it before
    outputting.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OUTPUT FORMAT — Produce in this exact order
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 1 — ATS Score & Gap Analysis
  • Estimated ATS match score (0–100)
  • True gaps only (from Step 6): keyword | reason it could not be placed | one
    actionable suggestion for a future resume version

SECTION 2 — Change Log
  • Skills added via Direct Evidence (Pass 1) → keyword | Skills group
  • Skills added via Contextual Inference (Pass 2) → keyword | Skills group |
    one-sentence inference justification
  • Bullets reordered → section | original position → new position | one-line
    justification referencing the three-gate test
  • Bullets modified → full BEFORE text | full AFTER text | which gate(s) justified it
  • Content Quality Audit fixes applied (list each briefly)

SECTION 3 — Find-Replace Manifest
  All CHANGE #N entries from Step 10, listed before the code block

SECTION 4 — Final LaTeX Code
  The complete tailored LaTeX in a single code block

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
--- TARGET JOB DATA ---
Job Title: [Insert Job Title]
Job Description:
[Paste Job Description here] 