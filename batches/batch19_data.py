"""Batch 19 lead data (24 Nov 2026): 2 leads from India, MENA and the US with a fresh trigger and visible signs of needing a founder voice. Personal-branding, ghostwriting and PR firms excluded."""

DATE = "2026-11-24"
BATCH = "19"

# confirmed = LinkedIn profile matched to this person through their own indexed posts or a Prospeo match on name and company.
# When False, the URL is a people-search link and the profile must be confirmed before sending.
LEADS = [
    # ---------------- MENA ----------------
    dict(name='Muhannad Tobal',
         role='Co-founder & CEO',
         company='InvoiceQ',
         region='MENA',
         city='Amman',
         url='https://www.linkedin.com/in/muhannad-tobal-15908695',
         confirmed=True,
         trigger='$5M Series A led by Manara Ventures and Next Ventures (e-invoicing and tax compliance across Saudi, UAE, Jordan, Oman, Qatar and Egypt)',
         trigger_date='2026-11',
         source='https://www.finsmes.com/2026/11/invoiceq-raises-5m-in-series-a-funding.html',
         pattern='Not indexed',
         last_post='',
         activity="Profile confirmed via Prospeo. Headline: 'Co-Founder and CEO at InvoiceQ'. Finance background (ex-MadfoatCom finance manager). Co-founders Fadi Al-Jabali (CTO), Amer Ayyad (COO), Mohammad Baseet. Earlier: $1.2M pre-Series A in Dec 2024. Company says it serves 1,000+ businesses and is ZATCA-qualified and UAE FTA-accredited. Team of about 55.",
         angle='E-invoicing mandates are rolling out across the Gulf, and finance teams are choosing vendors now. A CEO with a finance background explaining the rules plainly is the trust signal buyers look for.',
         score=50,
         connect="Hi Muhannad, congrats on InvoiceQ's Series A.\nE-invoicing across six markets is no small thing.\nWould be good to connect.",
         dm="Thanks for connecting, Muhannad.\nFinance teams in the Gulf are picking e-invoicing vendors right now.\nIs a founder voice on LinkedIn part of how you'll reach them?",
         teardown='E-invoicing mandate explainers; finance-team pain points; GCC expansion content.',
         notes="Prospeo lists Muhannad's location as Newark, NJ, while the company is in Amman. Confirm before scheduling a call. Confirm last post before sending."),
    # ---------------- US ----------------
    dict(name='Neelima Rustagi',
         role='Co-founder & CEO',
         company='Metano',
         region='US',
         city='San Jose',
         url='https://www.linkedin.com/search/results/people/?keywords=Neelima%20Rustagi%20Metano',
         confirmed=False,
         trigger='$12M seed led by Sierra Ventures; out of stealth 19 Nov (security and governance for AI agents)',
         trigger_date='2026-11',
         source='https://dealroom.co/news/174393-metano-leaves-stealth-with-12m-to-secure-enterprise-ai-agents/',
         pattern='Not indexed',
         last_post='',
         activity='No confirmed profile found. Co-founder and CTO Ratnesh Pandey. Security background at ServiceNow, Zscaler, Palo Alto Networks, FireEye and Microsoft. Other investors: Correlation Ventures, High Alpha, 360 ONE. Offers a free 30-day evaluation edition.',
         angle='Security buyers trust people with a track record. A CEO with years at Zscaler and Palo Alto talking about how AI agents should be governed is a voice CISOs would follow.',
         score=50,
         connect="Hi Neelima, congrats on Metano's $12M seed and coming out of stealth.\nSecuring AI agents at work is a timely problem.\nWould be good to connect.",
         dm="Thanks for connecting, Neelima.\nCISOs will be looking at Metano for the first time this month.\nIs a founder voice on LinkedIn part of how you'll reach them?",
         teardown='Confirm profile; AI agent governance point of view; CISO content.',
         notes='VERIFY PROFILE. No email found. Confirm last post before sending.'),
]
