# ImpersonaGuard - MITRE ATT&CK Mapping & Attacker Playbooks

## 1. Overview
This document maps the targeted Spear-Phishing and OSINT harvesting threats against ImpersonaGuard to the globally recognized MITRE ATT&CK framework.

## 2. MITRE ATT&CK Techniques Mapping
We map the attacker's lifecycle into three main phases:

### Phase A: Reconnaissance (الاستطلاع)
- **Technique ID:** T1589 (Gather Victim Identity Information)
- **Description:** Attackers use automated Web Scraping (OSINT) to harvest employee public data, interests, and professional footprints from blogs and social media.
- **Project Mitigation:** The Blue engine monitors and analyzes digital footprints and restricts unauthorized profiling.

### Phase B: Initial Access (الوصول الأولوي)
- **Technique ID:** T1566 (Phishing)
- **Description:** Crafting and sending customized Spear-Phishing emails to employees based on the harvested OSINT data.
- **Project Mitigation:** Enforcing strict email authentication protocols (SPF, DKIM, DMARC) and domain similarity checks to intercept the email.

### Phase C: Credential Access (الحصول على بيانات الاعتماد)
- **Technique ID:** T1598 (Phishing for Information)
- **Description:** Luring employees to fake login pages or tricking them into revealing credentials.
- **Project Mitigation:** Real-time URL and content analysis, followed by automated case investigation and quarantine actions.

---

## 3. Attacker Playbook Scenario (سيناريو هجومي واقعي)
1. **Step 1 (Scraping):** The attacker runs a python script to scrape a target employee's public blog posts.
2. **Step 2 (Weaponization):** The attacker drafts a spear-phishing email pretending to be from the company's HR or management, referencing the scraped topics.
3. **Step 3 (Delivery & Detection):** The email is sent to the employee. **ImpersonaGuard Blue Engine** detects the domain mismatch and missing cryptographic validation (SPF/DKIM), quarantines the message instantly, and opens an investigation case.