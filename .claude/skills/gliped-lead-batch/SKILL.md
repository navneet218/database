---
name: gliped-lead-batch
description: Source a new batch of Gliped leads (founders, CXOs and senior leaders in India, UK, Canada and US with a recent trigger), read their LinkedIn posting pattern, and deliver per-lead LinkedIn messages plus a customised cold email, then update the Excel tracker. Use whenever Prabal asks for the next set of leads, a new batch, or more prospects.
---

# Gliped lead batch

Produces a batch of net-new leads for Gliped (LinkedIn personal branding for founders and CXOs). Every lead gets LinkedIn outreach **and a customised cold email**. A lead without an email is not finished.

Read `outreach-playbook.md` (scoring, signals, sequence) and look at the last batch in `batches/` before starting, so tone and format match.

## Files

| File | What it holds |
|---|---|
| `gliped-crm-processed-tracker.csv` | Everyone already sourced. Dedupe against it; append the new batch at the end. |
| `batches/batchNN_data.py` | The batch's leads as a list of dicts (same keys as `batch02_data.py`). |
| `batches/emails_data.py` | `EMAILS[name] = (subject, body)` for every lead. Add the new batch's emails here. |
| `batches/build_tracker.py` | Builds `Gliped_Outreach_Tracker.xlsx` (Leads, Tracker, Dashboard, Sequence). Import the new batch file and add it to `leads`. |
| `batches/make_batch02_md.py` | Template for the batch doc. Copy it for the new batch number. |
| `batches/make_emails_md.py` | Renders `batches/cold-emails.md` for all leads. |

## Steps

1. **Source.** Search recent funding and leadership news (last 90 days) per region: Inc42, Entrackr, StartupTalky, YourStory (India); EU-Startups, Tech.eu, UKTN, FinSMEs (UK); BetaKit, FinSMEs Canada (Canada); FinSMEs, TechCrunch (US). Split evenly across the four regions unless told otherwise. Skip anyone already in the CSV.
2. **Read the posting pattern.** Search `site:linkedin.com/posts <name> <company>`. Decode each post's date from its activity ID: `datetime.utcfromtimestamp((activity_id >> 22) / 1000)`. Separate the person's own posts from posts about them. Label the pattern: Milestone-only, Went quiet, Company-news voice, Company-page voice, Emerging writer, Already consistent, Near-silent, Research voice, or Not indexed.
3. **Confirm identity.** If the name is common or no own posts match the company, set `confirmed=False` and use a LinkedIn people-search URL. Never guess a profile.
4. **Score** with the playbook model: trigger (max 30) + gap (max 20) + fit (10) + active in last 30 days (10). Trigger older than 90 days means nurture.
5. **Write the LinkedIn messages:** connection note, first DM, teardown focus (see batch 02 for format).
6. **Write the cold email** (rules below) and add it to `emails_data.py`.
7. **Build:** append the batch to the CSV, write `batches/YYYY-MM-DD-batch-NN.md`, run `python3 make_emails_md.py` and `python3 build_tracker.py` from `batches/`, then verify formulas (pycel if LibreOffice is unavailable). If Prabal has been filling in the Tracker, ask for his copy first, because rebuilding resets Tracker inputs.
8. **Deliver:** commit, push, send the workbook with SendUserFile, and summarise top leads, profiles that need confirming, and anything odd.

## Cold email rules

- **Subject:** 2 to 5 words, sentence case, specific to them (company, trigger or gap). No emojis, no "Quick question", no clickbait, no fake "Re:".
- **Body:** 40 to 90 words, short lines, in this order:
  1. `Hi [First name],`
  2. One-line hook on their trigger ("Congrats on the $20M Series A.").
  3. One or two lines naming the gap, grounded in what the research found (posting pattern, dates, who tells their story now).
  4. One line on what Gliped does, framed around their situation.
  5. **CTA as the last line of the body:** one question, low commitment. Default: "Worth a 15-minute call next week?" Variants: "Open to a quick call?", or for pre-seed, "Want the 3-point teardown instead?"
- **Sign-off** comes from `SIGNOFF` in `emails_data.py` and includes the opt-out line (needed for CASL in Canada, PECR in the UK, CAN-SPAM in the US). Use `SIGNOFF_FR` and write in French for Quebec leads who post in French.
- **Voice:** Prabal's. Plain, warm, direct. No em dashes. No "I hope this finds you well". No praise for a post whose text you haven't read (titles and comment counts are fine to cite). No invented client results, numbers or Gliped service claims.
- **Adjust by pattern:** Already consistent means pitch time back and reach, not writing. Writers (journalists, ex-creative leads) means pitch distribution and strategy only. Large companies mean offer to work alongside their comms team.
- **Channel order:** LinkedIn first. Email goes if the connection isn't accepted within 5 days or there's no reply to the first DM, to a verified work email only. One email follow-up after 5 days, on the same thread.

## Guardrails

- Prabal sends everything by hand. Don't automate connection requests, DMs or emails.
- Quality over quota. If fewer leads are worth sending, deliver fewer and say so.
- Flag any identity, date or role you couldn't confirm, in the lead's notes and in the summary.
