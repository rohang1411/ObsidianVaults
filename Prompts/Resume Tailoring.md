
The below prompts are for tailoring the resume for a specific job description

## SDE -

### V3 -

Phase 1 — SDE Context Initialization

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






### V2 -

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

### V1 -
	
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


