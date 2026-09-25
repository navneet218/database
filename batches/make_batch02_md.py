"""Render batch02_data.py into the batch 02 markdown doc."""
import batch02_data as b
import emails_data as em

def q(text):
    return "\n".join("> " + line for line in text.split("\n"))

def month(s):
    import datetime
    if not s: return "none indexed"
    if len(s) == 7:
        return datetime.date(int(s[:4]), int(s[5:]), 1).strftime("%b %Y")
    return s

L = sorted(b.LEADS, key=lambda l: (-l["score"], not l["confirmed"], ["India","UK","Canada","US"].index(l["region"])))
out = []
w = out.append
w("# Batch 02: 40 leads, 25 Sep 2026\n")
w("Forty founders and CEOs, ten each from India, the UK, Canada and the US. Same method as batch 01: a trigger from the last 90 days, a posting timeline decoded from indexed LinkedIn posts, and messages in Prabal's voice. None of these people are in batch 01.\n")
w("The full list of all 60 leads, plus the pipeline tracker, is in `Gliped_Outreach_Tracker.xlsx` at the repo root.\n")
w("## Read before sending\n")
w("- **14 leads have an unconfirmed profile** (marked *verify profile* below). Their names are common or they have no indexed posts, so the LinkedIn link is a people search. Open it, match the company and role, then paste the real profile URL into the workbook.")
w("- Only post titles and dates were visible, not post text. Don't praise a post you haven't read.")
w("- Check each person's `/recent-activity/all/` for 30 seconds before sending, to confirm role, last post and whether an agency already runs their feed.")
w("- Stéphane Garneau's messages are in French. Confirm Micrologic's funding date before sending.")
w("- Kimia Hamidi is a nurture lead (trigger older than 90 days). Carried over from batch 01 research.\n")
w("## Patterns in this batch\n")
from collections import Counter
c = Counter(l["pattern"] for l in L)
w("| Pattern | Count | Who |\n|---|---|---|")
for p, n in c.most_common():
    w(f"| {p} | {n} | " + ", ".join(l["name"] for l in L if l["pattern"] == p) + " |")
w("")
w("Batch 02 has more founders who already post (Guy Shahar, Jon Steinback, Noah Schochet, Oscar Levy). For them, pitch time back, cadence and reach, not writing from scratch.\n")
w("## Summary\n")
w("| # | Name | Company | Region | Trigger date | Pattern | Last indexed own post | Score | Profile |\n|---|---|---|---|---|---|---|---|---|")
for i, l in enumerate(L, 1):
    w(f"| {i} | {l['name']} | {l['company']} | {l['region']} | {l['trigger_date']} | {l['pattern']} | {month(l['last_post'])} | {l['score']} | {'confirmed' if l['confirmed'] else 'verify'} |")
w("\nSequence and follow-ups are the same as batch 01 (see the *Sequence* tab in the workbook).\n\n---\n\n## Lead cards\n")
for i, l in enumerate(L, 1):
    tag = "" if l["confirmed"] else " *(verify profile)*"
    w(f"### {i}. {l['name']}, {l['role']}, {l['company']} ({l['region']}){tag}")
    w(f"- **LinkedIn:** {l['url']}")
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
open("2026-09-25-batch-02.md", "w").write("\n".join(out))
print("ok", len(L))
