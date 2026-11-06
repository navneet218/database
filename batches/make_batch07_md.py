"""Render batch07_data.py into the batch 07 markdown doc."""
import csv
import batch07_data as b
import emails_data as em

def q(text):
    return "\n".join("> " + line for line in text.split("\n"))

def month(s):
    import datetime
    if not s: return "none indexed"
    if len(s) == 7:
        return datetime.date(int(s[:4]), int(s[5:]), 1).strftime("%b %Y")
    return s

L = sorted(b.LEADS, key=lambda l: (-l["score"], not l["confirmed"], ["India","MENA","US"].index(l["region"])))
out = []
w = out.append
CONTACTS = {r["name"]: r for r in csv.DictReader(open("contacts.csv"))}
nv = sum(1 for l in L if CONTACTS.get(l["name"], {}).get("status") == "VERIFIED")
nunc = sum(1 for l in L if not l["confirmed"])
w("# Batch 07: 11 leads, 6 Nov 2026\n")
w("Eleven founders and CEOs: four from India, four from MENA and three from the US. Short of 20 again: Ocient's and Laza Medical's reported rounds could not be confirmed, Sovra and 1001 turned out to be June rounds, and Larridin, Reflex, Journify, Tutor Intelligence, NoorNation, Popcorn AI Studio, Vitalls, Ghanem, CapQuest and Synapse Analytics are already in earlier batches. Every lead has a trigger from the last 60 days.\n")
w("Competitor screen: no one here runs a personal-branding, LinkedIn ghostwriting, content or PR business. Their companies are space tech, biomaterials, biotech, grocery, trade finance, construction, enterprise AI and insurance. JustAd finances ad spend for SMBs; it is not a branding agency.\n")
w("All 205 leads, plus the pipeline tracker, are in `Gliped_Outreach_Tracker.xlsx` at the repo root.\n")
w("## Read before sending\n")
w("- **Recent LinkedIn activity is not confirmed for anyone in this batch.** LinkedIn is blocked from the research environment, search engines index very few 2026 posts, and Gojiberry (which can filter for activity in the last 90 days) returned 401 Unauthorized. Open each person's `/recent-activity/all/` for 30 seconds. If there is nothing from the last 60 days, move them to nurture instead of sending.")
w(f"- **{nunc} profiles need confirming** (marked *verify profile*). The link is a people search; match company and role, then paste the real URL into the workbook.")
w(f"- **{nv} verified work emails** (Prospeo, SMTP checked). The rest are LinkedIn only for now.")
w("- Mamun's $3M seed is reported in one headline only, so the email congratulates the Hong Kong move instead. Venomics AI's $2.7M may be an April round announced in November.\n- Badr Al-Malluh's trigger (8 Sept) is at the 60-day limit. Shashank Shekhar Sharma (Solgram) is not batch 01's Shashank ND.")
w("- Batch 06 follow-up: Nooks' $500M is a growth capital commitment, not a standard equity round. The Dan Lee draft already says \"the new round\", so no change needed.\n")
w("## Patterns in this batch\n")
from collections import Counter
c = Counter(l["pattern"] for l in L)
w("| Pattern | Count | Who |\n|---|---|---|")
for p, n in c.most_common():
    w(f"| {p} | {n} | " + ", ".join(l["name"] for l in L if l["pattern"] == p) + " |")
w("")
w("Chiran Chiranjeevi Phanindra already has 'Science Communicator' in the headline, and Anish Agarwal and Kartik Sunagar are professors: pitch turning existing expertise into posts, not writing from scratch.\n")
w("## Summary\n")
w("| # | Name | Company | Region | Trigger date | Pattern | Last indexed own post | Score | Profile | Email |\n|---|---|---|---|---|---|---|---|---|---|")
for i, l in enumerate(L, 1):
    w(f"| {i} | {l['name']} | {l['company']} | {l['region']} | {l['trigger_date']} | {l['pattern']} | {month(l['last_post'])} | {l['score']} | {'confirmed' if l['confirmed'] else 'verify'} | {CONTACTS.get(l['name'], {}).get('email') or CONTACTS.get(l['name'], {}).get('status', '').lower().replace('_', ' ')} |")
w("\nSequence and follow-ups are the same as batch 01 (see the *Sequence* tab in the workbook).\n\n---\n\n## Lead cards\n")
for i, l in enumerate(L, 1):
    tag = "" if l["confirmed"] else " *(verify profile)*"
    w(f"### {i}. {l['name']}, {l['role']}, {l['company']} ({l['region']}){tag}")
    w(f"- **LinkedIn:** {l['url']}")
    c = CONTACTS.get(l["name"], {})
    w(f"- **Email:** {c.get('email') or {'NO_MATCH': 'not found', 'PENDING': 'lookup pending'}.get(c.get('status'), 'not checked')}")
    w(f"- **Trigger:** {l['trigger']} ({l['trigger_date']}). [Source]({l['source']})")
    w(f"- **Activity pattern:** {l['pattern'].lower()}. {l['activity']}")
    w(f"- **Angle:** {l['angle']}")
    w("- **Connection note:**"); w(q(l["connect"]))
    w("- **First DM:**"); w(q(l["dm"]))
    w(f"- **Teardown focus:** {l['teardown']}")
    subj, body = em.render(l["name"])
    w(f"- **Cold email:** subject *{subj}*"); w(q(body))
    if l["notes"]: w(f"- **Notes:** {l['notes']}")
    w("")
open("2026-11-06-batch-07.md", "w").write("\n".join(out))
print("ok", len(L))
