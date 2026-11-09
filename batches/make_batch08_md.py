"""Render batch08_data.py into the batch 08 markdown doc."""
import csv
import batch08_data as b
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
w("# Batch 08: 7 leads, 9 Nov 2026\n")
w("Seven founders and CEOs: two from India, two from MENA and three from the US. This is the thinnest batch so far. Indian deal flow stopped over Diwali (StartupTalky reported no new rounds on 6 November), and most of the week's Indian and MENA rounds are already in batches 05 to 07. Deep.SA (February) and Persona MENA (no named founder) were dropped. Every lead has a trigger from the last 60 days.\n")
w("Competitor screen: no one here runs a personal-branding, LinkedIn ghostwriting, content or PR business. Their companies are logistics, fitness, payments, construction, autonomous trucking, electric vehicles and AI infrastructure.\n")
w("All 212 leads, plus the pipeline tracker, are in `Gliped_Outreach_Tracker.xlsx` at the repo root.\n")
w("## Read before sending\n")
w("- **Recent LinkedIn activity is not confirmed for anyone in this batch.** LinkedIn is blocked from the research environment, search engines index very few 2026 posts, and Gojiberry (which can filter for activity in the last 90 days) returned 401 Unauthorized. Open each person's `/recent-activity/all/` for 30 seconds. If there is nothing from the last 60 days, move them to nurture instead of sending.")
w(f"- **{nunc} profiles need confirming** (marked *verify profile*). The link is a people search; match company and role, then paste the real URL into the workbook.")
w(f"- **{nv} verified work emails** (Prospeo, SMTP checked). The rest are LinkedIn only for now.")
w("- Large companies (Harbinger, fal): offer to work alongside the comms or marketing team. Harbinger is moving into defense, so keep any content measured.\n- enza's new round (Seed+ with 4DX Ventures) has only one source, so the email says \"new funding round\". Tushar Sharma (OBSESS) is a nurture lead: small angel round with conflicting amounts.")
w("- Tracker update: Shashank ND (batch 01, listed under Practo) has co-founded Cent, which raised a $15M Series A in late October. Update that row instead of adding a new lead.\n")
w("## Patterns in this batch\n")
from collections import Counter
c = Counter(l["pattern"] for l in L)
w("| Pattern | Count | Who |\n|---|---|---|")
for p, n in c.most_common():
    w(f"| {p} | {n} | " + ", ".join(l["name"] for l in L if l["pattern"] == p) + " |")
w("")
w("Eyal Cohen and Rajit Arya are hiring engineers, and their headlines show it: pitch the founder voice as a hiring channel. Burkay Gur already gives quotes to the press: pitch reuse of those.\n")
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
open("2026-11-09-batch-08.md", "w").write("\n".join(out))
print("ok", len(L))
