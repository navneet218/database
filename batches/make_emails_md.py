"""Render every lead's cold email (all batches) into cold-emails.md."""
import csv
import emails_data as em

rows = list(csv.DictReader(open("../gliped-crm-processed-tracker.csv")))
out = ["# Cold emails for every lead\n",
       "One email per lead, generated from `emails_data.py`. Send LinkedIn first. Email is the second channel for leads who don't accept within 5 days or don't reply to the first DM. Verify the work email before sending (Prospeo or similar), and paste it into the Leads tab.\n",
       "Follow-up, 5 days later on the same thread:\n",
       "> Bumping this in case it got buried, [Name]. Happy to send the 3-point teardown instead of a call if that's easier.\n"]
for batch in sorted({r["batch"] for r in rows}):
    out.append(f"## Batch {batch}\n")
    for r in rows:
        if r["batch"] != batch:
            continue
        subj, body = em.render(r["name"])
        out.append(f"### {r['name']}, {r['company']} ({r['region']})")
        out.append(f"**Subject:** {subj}\n")
        out.append("\n".join("> " + line for line in body.split("\n")) + "\n")
open("cold-emails.md", "w").write("\n".join(out))
print("ok", len(rows))
