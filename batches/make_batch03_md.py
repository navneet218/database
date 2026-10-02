"""Render batch03_data.py into the batch 03 markdown doc."""
import csv
import batch03_data as b
import emails_data as em

def q(text):
    return "\n".join("> " + line for line in text.split("\n"))

def month(s):
    import datetime
    if not s: return "none indexed"
    if len(s) == 7:
        return datetime.date(int(s[:4]), int(s[5:]), 1).strftime("%b %Y")
    return s

L = sorted(b.LEADS, key=lambda l: (-l["score"], not l["confirmed"], ["MENA","UK","US"].index(l["region"])))
out = []
w = out.append
CONTACTS = {r["name"]: r for r in csv.DictReader(open("contacts.csv"))}
nv = sum(1 for l in L if CONTACTS.get(l["name"], {}).get("status") == "VERIFIED")
npend = sum(1 for l in L if CONTACTS.get(l["name"], {}).get("status") == "PENDING")
nunc = sum(1 for l in L if not l["confirmed"])
w("# Batch 03: 60 leads, 2 Oct 2026\n")
w("Sixty founders and CEOs, twenty each from MENA, the UK and the US. No India leads today (public holiday). Same method as batches 01 and 02: a trigger from the last 90 days, a posting timeline decoded from indexed LinkedIn posts, and messages in Prabal's voice. None of these people are in earlier batches.\n")
w("All 120 leads, plus the pipeline tracker, are in `Gliped_Outreach_Tracker.xlsx` at the repo root.\n")
w("## Read before sending\n")
w(f"- **{nunc} leads have an unconfirmed profile** (marked *verify profile* below). Their names are common or no own posts or Prospeo match turned up, so the LinkedIn link is a people search. Open it, match the company and role, then paste the real profile URL into the workbook.")
w(f"- **{nv} verified work emails** (Prospeo, SMTP or BounceBan checked). {npend} US leads are still pending because Prospeo hit its rate limit; retry those before emailing them. MENA match rates were low, so most MENA leads are LinkedIn only.")
w("- Only post titles and dates were visible, not post text. Don't praise a post you haven't read.")
w("- Check each person's `/recent-activity/all/` for 30 seconds before sending, to confirm role, last post and whether an agency already runs their feed.")
w("- MENA timing: Saudi and Egypt work Sunday to Thursday, the UAE Monday to Friday. Avoid Friday sends to the Gulf.")
w("- Triggers from July 2026 are 60 to 90 days old. Send those this week or move them to nurture.\n")
w("## Patterns in this batch\n")
from collections import Counter
c = Counter(l["pattern"] for l in L)
w("| Pattern | Count | Who |\n|---|---|---|")
for p, n in c.most_common():
    w(f"| {p} | {n} | " + ", ".join(l["name"] for l in L if l["pattern"] == p) + " |")
w("")
w("Few batch 03 founders post regularly. Ahmed Abaza, Ross Finman and Cheryl Sew Hoy already write, so pitch cadence, time back and reach to them, not writing from scratch. Ladi Delano runs a large company: offer to work alongside the comms team.\n")
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
open("2026-10-02-batch-03.md", "w").write("\n".join(out))
print("ok", len(L))
