# Fields and industries

Load this when the field affects the advice, or when the user is moving from academic writing to industry writing (thesis → first job, researcher → product team).

## From academic to industry writing

Many users learned English writing through papers. The habits that earn a good review can make a business document hard to use. Point out the shift when you see academic habits in work writing.

| Academic habit | In industry | Example |
|---|---|---|
| Background → method → result → conclusion | Conclusion first, then support | *We recommend vendor B: 18% cheaper and 2 weeks faster.* first, method later |
| Hedging (*may suggest*, *it appears that*) | Commit, and state the confidence | *B is likely the better choice (high confidence on cost, medium on delivery).* |
| *In this paper, we propose…* | *This memo recommends…* / *I propose…* | |
| Passive voice to sound objective | Active voice with owners | *The test was delayed* → *The vendor delayed the test by two days.* |
| Long, complete explanations | Enough to decide; details in an appendix | |
| Literature review | Prior decisions, competitors, benchmarks | *Two competitors already offer this; see Appendix A.* |
| *Further research is needed* | A next step with an owner and date | *Ming will run a 2-week pilot starting 3 June.* |
| *Significant* (statistical) | *Large*, *material*, or the number | |
| Precision about method | Precision about impact: money, time, risk, customers | |
| Neutral tone | A clear recommendation is expected | |

The reverse direction also happens: industry writers drafting a paper or a grant overclaim, skip method detail and write marketing language. Point that out too.

## Field notes

Use these for the norms of each field. Generate vocabulary with `vocab.md`; this table is about tone and traps.

| Field | Typical documents | Norms | Traps for non-native writers |
|---|---|---|---|
| **Software / tech / product** | Design docs, PRDs, tickets, release notes, incident reports | Direct, concise, active voice; *we* and *you*; numbered steps | Buzzwords (*leverage, empower, seamless*); *fix* vs *resolve* vs *close* a ticket; vague bug reports (*it doesn't work*) |
| **AI / data science** | Papers, model cards, experiment reports | Precise about data and metrics; honest about limits | *Accuracy* vs *precision* vs *recall* used loosely; *significant* without a test; *state-of-the-art* claims |
| **Finance / banking** | Research notes, credit memos, investor updates | Numbers first; exact terms; conservative claims | *Revenue* vs *income* vs *profit*; *percent* vs *percentage points*; *leverage* has a technical meaning; promissory language in regulated contexts |
| **Consulting / strategy** | Decks, executive summaries, proposals | Answer first; MECE structure; action titles on slides | Topic titles (*Analysis*); unsupported superlatives; long sentences in slides |
| **Accounting / audit** | Audit findings, management letters | Standard terminology; neutral, factual | *Account* vs *accounting*; *control deficiency* vs *weakness*; editorializing findings |
| **Manufacturing / supply chain** | Supplier emails, 8D reports, quality reports | Specific quantities, dates, part numbers | *Delivery* vs *shipment* vs *lead time*; *claim* (wasei) for complaint; *defect* vs *defective* |
| **Healthcare / pharma / biomed** | Clinical papers, protocols, patient materials, regulatory docs | Very cautious claims; standard reporting guidelines (CONSORT, etc.) | *Patients* vs *cases* vs *subjects* (*participants* preferred); *cure*; plain language required for patient materials |
| **Legal / compliance** | Contracts, policies, memos | Exact and consistent defined terms; *shall/must/may* used carefully | Changing a defined term for style; translating 应 / べき inconsistently (*should* vs *must*) |
| **Engineering (civil, mechanical, electrical)** | Design reports, specifications, method statements | Units and tolerances exact; standards cited | Brittman habits (`data-in-sentence`, `symbol-in-text`, `respectively`); unit spacing |
| **Marketing / communications** | Campaign briefs, copy, press releases | Reader-focused, energetic but concrete | AI-flavored hype; literal translation of slogans; cultural references that don't travel |
| **Sales / business development** | Cold emails, proposals, follow-ups | Short; about the client's problem, not your company | Long company introductions; *We are a leading provider of…* |
| **HR / people** | Job posts, policies, performance reviews | Neutral, inclusive, specific | Gendered terms; vague feedback (*needs to improve communication*) |
| **Education / academia administration** | Course descriptions, reports to committees | Clear, structured, rule-based | Translating 培养 as *cultivate*; overlong sentences |
| **Government / public sector** | Policy briefs, official letters | Formal but plain; increasing push for plain language | Very long sentences; nominalizations (*the implementation of the enhancement of…*) |

If the user's field isn't listed, infer its norms from the closest neighbor and say so.
