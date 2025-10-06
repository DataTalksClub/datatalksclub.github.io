---
title: "Getting Started with Open Source: A Complete Guide with Vincent Warmerdam"
short: "Getting Started with Open Source"
description: "Learn how to get started with open source contributions, create successful projects, and advance your career. Vincent Warmerdam shares practical tips on contributing to existing projects, building your own packages, and leveraging open source for professional growth."
guests: [vincentwarmerdam]
tags: [open-source, python, data-science, career-development, contributing, scikit-learn, machine-learning]
category: "Data Science Career"

image: images/podcast/s02e03-open-source.jpg

season: 2
episode: 3

ids:
  youtube: IxV9EH-tphQ
  anchor: Getting-Started-with-Open-Source---Vincent-Warmerdam-epk60j

links:
  youtube: https://www.youtube.com/watch?v=IxV9EH-tphQ
  anchor: https://anchor.fm/datatalksclub/episodes/Getting-Started-with-Open-Source---Vincent-Warmerdam-epk60j
  spotify: https://open.spotify.com/episode/1dsbDeVncfsEg3m3cYB927
  apple: https://podcasts.apple.com/us/podcast/getting-started-with-open-source-vincent-warmerdam/id1541710331?i=1000507024598
---

Today we're talking open source with our guest, **Vincent Warmerdam**. Vincent is a Research Advocate at Rasa. If you check his LinkedIn, you'll see a lot: he's made Reddit's front page, runs calmcode.io for learning to code, has organized PyData Amsterdam and AI Saturdays Amsterdam, and he's a data evangelist and open-source enthusiast who's created and maintains several open-source packages. And—last but not least—he has over 80 LinkedIn endorsements for "awesomeness." Welcome, Vincent!

**Vincent:** Hi! About those "awesomeness" endorsements—at a previous company I had a running bet with a CTO: who could get the most "awesomeness" endorsements without asking. So yes, I'm slightly cheating there—but it's been a years-long joke.

In this interview, we covered:

- [Vincent's journey from design student to Research Advocate](#vincent's-journey-and-open-source-philosophy)
- [Secrets to successful project naming and documentation](#building-and-managing-open-source-projects)
- [Step-by-step guide to making your first contributions](#how-to-start-contributing-to-open-source-projects)
- [Leveraging open source for career advancement and visibility](#career-advancement-through-open-source-projects)

## Vincent's Journey and Open Source Philosophy

**Q: Could you walk us through your career journey and how you ended up in open source?**

**Vincent:** I grew up bilingual—born in the U.S., raised mostly in the Netherlands, with lots of travel back to the U.S. After high school, I wanted to study design, but I got a bad grade for not using a prescribed brainstorming framework—so I pivoted. I discovered econometrics (applied math), and they promised I'd predict stocks… which, spoiler alert, you can't. I did a master's in operations research instead. Around then, AI/ML was getting hyped—there was the free Stanford AI course with Norvig and Thrun; I was an early student. I realized I liked programming more than suit-and-tie consulting.

I backpacked through Latin America with a laptop, did some consulting, and told myself: if I prefer coding to going clubbing every night, that's my sign. Coding won. Back in the Netherlands, I taught at a business school (good money), but wanted data science. I met someone at a meetup who was starting a Hadoop company and needed math for ML—that got me in. I helped bring PyData to the Netherlands and did community work (I'm no longer formally involved). I blogged, built side projects, and Rasa noticed. They asked if I could do my "Vincent stuff" on their stack. It took me a month to realize they meant a full-time role.

**Q: As a Research Advocate at Rasa, what does your role actually involve, and how does it differ from a traditional Developer Advocate?**

**Vincent:** The title is new—we're still defining it, like data science roles were years ago. Think "developer advocate," but closer to research. I make sure non-English languages are better supported (e.g., right-to-left languages like Arabic need different handling). I listen to practitioners building assistants and surface their needs; I also translate what our researchers and engineers build into practical guides. Sometimes that's a blog or video; sometimes it's an open-source tool. I even co-authored a research paper by accident because a tool I made was useful to researchers. I ship a lot of "byproducts": debugging tools on top of Rasa, word-embedding exploration and bias tools, etc.—not the core product, but helpful for the community.

**Q: For those unfamiliar with Rasa, could you explain what the company actually does and how it's positioned in the market?**

**Vincent:** Think of Elastic: they build search infrastructure; they don't build every search app. Rasa builds the *infrastructure* for virtual assistants: standard pipelines, components you can swap, deploy on your own servers (important for healthcare, etc.). Open source and pragmatic—`pip install` and go.

**Q: How do you personally define open source, and what philosophy guides your approach to creating and sharing open source tools?**

**Vincent:** I'm not a license wonk—there are nuances—but my framing is pragmatic. Others shared tools that made my career possible; when I have useful tools, I share them back. Scikit-learn is amazing, but there are experimental tricks they won't include. Nothing stops me from publishing compatible extras.

One caveat: putting code on GitHub is fine, but publishing on PyPI should wait until it's mature. I have a project called Brent that I put on PyPI too early—I'd prefer it had stayed GitHub-only until it was ready.

**Q: Your pinned tweet emphasizes "preferring common sense over hype." How does this philosophy apply to open source development and avoiding the trap of solving the wrong problems?**

**Vincent:** It's easy to optimize a metric by 1% while ignoring a 10% mismatch between the real business problem and the analytical proxy. Keep the real problem front and center.

## Building and Managing Open Source Projects

**Q: You've created and maintain several popular open source packages. Could you walk us through some of your key projects and explain how they came to be?**

**Vincent:** Ideas come from curiosity or wanting a better API. Examples:

* **evol** — evolutionary algorithms with a cleaner API (functional style with `Population`/`Evolution` objects) so it's easier to maintain than nested for-loops
* **clumper** — "pandas, but for nested JSON" with a friendly API
* **memo** — decorators that log function outputs; great for grid searches so you get a JSON trail
* **sklego (scikit-lego)** — extra "lego bricks" for scikit-learn
* **human-learn** — rule-based systems inside scikit-learn ("if this then that"), making human rules grid-searchable
* **whatlies** — explore what lies in word embeddings (visualization + scikit-learn-compatible transformers so you can benchmark quickly)
* Smaller tools like **schedulelord** (cron helpers for Raspberry Pi) and **make-test-docs** (two functions to treat docs/examples as unit tests)

I try to design for low maintenance: small, focused APIs, good docs, and compatibility with existing ecosystems—especially scikit-learn—so people can slot tools into pipelines and compare fairly ("is the 10× slower model also 10× better?").

**Q: Let's dive deeper into scikit-lego. What specific problems does it solve, and how do these "lego bricks" integrate with existing scikit-learn workflows?**

**Vincent:** Exactly—scikit-learn–compatible pipeline components. Some are fancy; some are simple but practical. Example: if your model expects values in [0, 1] but sees a 1,000,000 at inference, it'll behave badly. We have a transformer that clips values to a max—so that outlier becomes 1. It's a drop-in component rather than reinventing the wheel.

We also have interesting **meta-components**. Take classifier thresholds: instead of always using 0.5, you can grid-search the threshold to trade precision/recall. Our components let you tune that inside a pipeline.

**Q: Your project names are wonderfully creative and descriptive. What's your process for naming projects, and why is good naming so important?**

**Vincent:** I actually made **makenames.io** with a friend—a silly name generator trained on Pokémon and IKEA catalogs. I'll generate names for 10 minutes, get frustrated, and then blurt out the clear description—that often *is* the name. I want names that say what they do: *scikit-lego* (lego bricks for scikit-learn), *human-learn* (human rules in sklearn), *whatlies* (what lies in embeddings), *clumper* (clump JSON), *memo* (memorize/log). At a former job, we turned naming into a team sport—*Steven Sequel* for a SQL service; the upgrade was *Steven C. Call: The Sequel*; a document store named *JSON Bourne*. It sounds goofy, but it boosted team energy and clarity: a good name forces you to be clear about what the thing does.

**Q: What are the key elements that make an open source project successful and maintainable, and how do you handle community contributions while maintaining a positive environment?**

**Vincent:** Not just code—**stewardship**. Great docs and a clear path from "zero to solving a problem." My doc checklist:

* **README/Home:** what it does, installation, a concise problem statement, maybe a logo, contribution notes
* **Guides:** a "Getting Started" and at least one **advanced** guide
* **API reference:** every function/method clearly described (images help)
* **Examples:** end-to-end notebooks showing real tasks (e.g., bias analysis with word embeddings, benchmarking embeddings for Arabic)

If there's no "Getting Started," adoption dies. Good docs are part of the product.

For contributions, I include a guide—on *whatlies*, the README has it even if the docs site doesn't. I try to set expectations: every issue is considered, but that doesn't mean it'll be implemented immediately. Stewardship also means nudging for good behavior. Sometimes folks are… unfriendly. Please don't write in ALL CAPS—it reads like shouting. I'm doing volunteer work; basic courtesy helps. I once had someone insist I must use Bokeh instead of Altair and then refuse to contribute—heated debate, zero code. A contribution guide should discourage that and keep discussions constructive.

## How to Start Contributing to Open Source Projects

**Q: For someone who wants to start contributing to open source, what would you recommend as the best first steps, and how should they approach contributing to large projects versus smaller ones?**

**Vincent:** It depends on your goal. Shipping your own library is different from contributing to an existing one. A great first contribution is **using** a tool, hitting a confusing error, and opening a clear **GitHub issue** with a repro and suggested fix (even just a better error message). That already helps maintainers a lot.

At Rasa, we recognize contributors beyond code—merged PRs, good talks, helpful blog posts. If you want to make your **first code PR**, invest in ecosystem basics: `setup.py`/packaging, `pytest`, `flake8`, `black`, pre-commit hooks, Git/GitHub workflows, and CI (e.g., GitHub Actions). Calmcode.io has short tutorials on many of these.

For large projects like scikit-learn, there's lots of traffic and process—they require algorithms to stand the test of time. Consider **smaller projects** where discussion is easier. Start by opening an issue to **propose** your idea—don't code a big feature before the maintainer is interested. As a maintainer, I worry about (1) general usefulness (vs. niche) and (2) long-term **maintenance**—will the contributor stick around? Address those in your proposal.

Projects like **DION** (a checklist for ML risks and unintended side effects) welcome contributions—even anecdotes for docs. It's impactful and approachable.

**Q: How do you manage to find time and energy for so many open source projects while maintaining quality, and what productivity strategies do you use?**

**Vincent:** A lot of my open-source work happens in my employer's time, with their support—so I learn at work and apply it elsewhere (and vice versa). Personally, I've shifted my free time: fewer video games, more tinkering, plus exercise, friends, and family. Productivity tip: **don't start by coding**. Use paper or an e-ink tablet to design the solution first. You should know the shape of the solution before typing a character; exploratory notebooks are the exception, not the rule.

## Career Advancement Through Open Source Projects

**Q: Many developers have internal tools at work that could benefit the broader community. How can someone convince their employer to open source internal libraries, and what are the business benefits for companies?**

**Vincent:** Position it as **hiring and brand** leverage. Cool OSS attracts attention—people check out the company behind it. Talks about your tools boost morale and serve recruiting. There was even a company that built a whimsical "garbage fire" demo; the blog about it drove real product interest. More broadly, some companies give employees a day a month for OSS. Treat it as **training**—contributing grows engineering maturity (Git, CI, packaging, reviews). Yes, regulated domains (e.g., finance) may limit this; be respectful of legal constraints.

**Q: How can open source work and conference speaking help with career advancement, and what strategies have helped you build visibility in the industry?**

**Vincent:** For conference talks, write your proposal so a reviewer thinks, "I'd attend this." At PyData Amsterdam, our rule was just that. Entertaining + educational is gold, but either alone is fine. Great talks often come from "simple but insightful" topics: a weird pandas trick that saved your day, how JSON parsing really works, or a fun dataset (e.g., "Which English words are the most *metal*?"). Many people don't realize their blog post could be a fantastic talk—submit it!

OSS contributions can de-risk you as a candidate—if you've meaningfully contributed to tools a team uses, they know you understand them. It's not a silver bullet, and lack of OSS (family, time, etc.) shouldn't disqualify anyone. Talks and blogs work too—my most-watched talk was about winning with **simple models** (yes, linear regression). Clear thinking > flashy hype.

For building visibility: **meetups and teaching.** I gave free R trainings to app devs, organized events, and said "yes" a lot. Visibility scales better than trying to meet everyone individually. Luck played a role too: being early in "data science," building first recommenders, living in Amsterdam—all helped.

**Q: As we wrap up, could you reflect on how the Research Advocate role at Rasa differs from traditional Developer Advocate positions, and what you see as the future of this type of role?**

**Vincent:** DevRel is a well-trodden path—there are even DevRel conferences. Research Advocacy at Rasa is similar but closer to research. I explore ideas, prototype, sanity-check with researchers, and bring community feedback back to the team (especially for non-English use cases). Next, I want to build a personal Slack assistant with Rasa—automating my own workflows—then share the journey so developers can replicate it. It's a two-way bridge: community ↔ research.
