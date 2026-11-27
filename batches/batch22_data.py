"""Batch 22 lead data (27 Nov 2026): 2 leads from India, MENA and the US with a fresh trigger and visible signs of needing a founder voice. Personal-branding, ghostwriting and PR firms excluded."""

DATE = "2026-11-27"
BATCH = "22"

# confirmed = LinkedIn profile matched to this person through their own indexed posts or a Prospeo match on name and company.
# When False, the URL is a people-search link and the profile must be confirmed before sending.
LEADS = [
    # ---------------- India ----------------
    dict(name='Gaurav Mittal',
         role='Co-founder & CEO',
         company='Vegapay',
         region='India',
         city='Mumbai',
         url='https://www.linkedin.com/in/gaurav-mittal-8084349',
         confirmed=True,
         trigger='Reported $10M round to expand credit infrastructure and UPI-linked lending (B2B card and lending platform for banks)',
         trigger_date='2026-11',
         source='https://www.tice.news/tice-dispatch/startup-news-evening-dispatch-november-26-2026-12843293',
         pattern='Not indexed',
         last_post='',
         activity="Profile confirmed via Prospeo. Headline: 'Co-Founder & CEO, Vegapay'. Card and payments veteran: Zeta, MatchMove, Mastercard, Amex, ICICI. Co-founders Himanshu Agrawal, Puneet Sharma, Abhinav Garg. Earlier: $1.1M pre-seed (2023), $5.5M seed led by Elevation (2024). Team of about 110, hiring 16 roles including founder's office. The $10M round comes from one daily roundup.",
         angle='Banks choose infrastructure partners they trust. A CEO with two decades in cards and prepaid explaining credit on UPI plainly is the trust signal bank buyers look for.',
         score=50,
         connect="Hi Gaurav, congrats on Vegapay's new round.\nCredit on UPI is one of the big shifts in Indian lending.\nWould be good to connect.",
         dm="Thanks for connecting, Gaurav.\nBank product heads will be looking at Vegapay as credit on UPI grows.\nIs a founder voice on LinkedIn part of how you'll reach them?",
         teardown='Credit on UPI explainers; cards and lending point of view; bank buyer and hiring content.',
         notes='Round amount not confirmed (one roundup): the email cites no figure. Hiring 16 roles: hiring is a second reason to post. Confirm last post before sending.'),
    # ---------------- MENA ----------------
    dict(name='Yash Sultania',
         role='Co-founder & CEO',
         company='XEBO.ai',
         region='MENA',
         city='Dubai',
         url='https://www.linkedin.com/in/yashsultania',
         confirmed=True,
         trigger='$10.5M Series A; Emirates Growth Fund is its first institutional investor (AI experience-management platform)',
         trigger_date='2026-11',
         source='https://www.finsmes.com/2026/11/xebo-ai-raises-10-5m-in-series-a-funding.html',
         pattern='Not indexed',
         last_post='',
         activity="Profile confirmed via Prospeo. Headline: 'Co-Founder & CEO at Xebo.ai'. Company formerly Survey2Connect, founded 2018; co-founders Anand Nigam and Dr Adil Ali M. Offices in Dubai and Riyadh, registered in Delaware; Prospeo lists Yash in Delhi. Team of about 97. First institutional round.",
         angle='A first institutional round after eight years of building is a story. Enterprise CX buyers in the Gulf respond to a founder who explains what customer feedback actually reveals.',
         score=50,
         connect="Hi Yash, congrats on XEBO.ai's $10.5M Series A.\nA first institutional round after years of building is a real milestone.\nWould be good to connect.",
         dm="Thanks for connecting, Yash.\nCX leaders in the Gulf will be looking at XEBO.ai after this round.\nIs a founder voice on LinkedIn part of how you'll reach them?",
         teardown='Eight-year founder story; CX insight posts; Gulf enterprise and government buyer content.',
         notes='Counted as MENA (Dubai office, FinSMEs calls it Dubai-based) though Yash appears to be in Delhi. Confirm last post before sending.'),
]
