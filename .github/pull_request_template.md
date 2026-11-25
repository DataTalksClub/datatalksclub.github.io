## Stop: new content is authored on the new DataTalks.Club site

This repository (`datatalksclub.github.io`) is the **old static site**. New content is no longer
added here. Use the new flow instead (see `_docs/content-authoring.md` in
[DataTalksClub/website](https://github.com/DataTalksClub/website)):

| Content | Where to add it now |
| --- | --- |
| Events, Hireable With AI sessions, banners | `dtc events create` / `update` / `upload-banner` on https://prod.datatalks.club (website DB) |
| Podcast episodes and transcripts, articles, books, their images | PR to [DataTalksClub/content](https://github.com/DataTalksClub/content) (Content Sync publishes it) |
| Academy pages, `slack.yaml` | PR to [DataTalksClub/content](https://github.com/DataTalksClub/content) |
| Code and design changes | PR to [DataTalksClub/website](https://github.com/DataTalksClub/website) |

If this PR only fixes the old site until the DNS flip (typo, broken link), say so below and ignore
the warning from the "New content guard" check.

## Why this change must live on the old repo
