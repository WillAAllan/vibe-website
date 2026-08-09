# VIBE Recognition — Marketing Website

Static marketing site for VIBE Recognition, deployed to **Netlify**.

## Deploy (current: manual zip)

```bash
git pull                       # get latest
python make_netlify_zip.py     # builds netlify-deploy.zip
# then upload netlify-deploy.zip in the Netlify dashboard (drag-and-drop deploy)
```

`make_netlify_zip.py` bundles the site and **renames some files** into the names Netlify serves,
and writes a `_redirects` file for clean URLs. Current mapping (`files_to_add`):

| Served as | Source file |
|---|---|
| `index.html` | `vibe-website-redesign.html` |
| `infographic.html` | `VIBE_Recognition_Infographic.html` |
| `terms.html` | `terms-and-conditions.html` |
| `resources.html`, `library.html`, `portal.html`, `sitemap.xml` | (same name) |
| the 8 `VIBE_*.pdf` module/marketing PDFs | (same name) |
| `favicon.png` | `public/branding/favicon.png` |

`_redirects`: `/`→`/index.html`, `/terms`→`/terms.html`, `/library`→`/library.html`,
`/portal`→`/portal.html`.

> **Planned:** connect Netlify directly to this repo so `git push` auto-deploys. Because of the
> renaming above, a plain "serve repo root" connect would 404 the homepage — either set a Netlify
> **build command** that runs `make_netlify_zip.py` and publishes its output, or restructure the repo
> to contain the real `index.html`/`terms.html`/`infographic.html` + a committed `_redirects`.

## Video Library (`library.html`)

Two sections: **Why Recognition Matters** (`#insightGrid`, thought-leadership) and **See It In
Action** (`#howtoGrid`, product guides). Each video is a `.vid-card` with `data-title`, `data-desc`,
`data-tags`, `data-src="https://www.youtube.com/embed/{ID}?rel=0"`, and a thumbnail from
`https://img.youtube.com/vi/{ID}/hqdefault.jpg`. Videos are **external YouTube embeds** (no local
files).

Filter chips ↔ `data-tags` tokens: Why Recognition=`why-recognition`, Getting Started=
`getting-started`, For Staff=`staff`, For Admins=`admin`, Nominations=`nominations`.

**To add a video:** copy an existing `.vid-card` block, replace the YouTube ID in **two** places
(`data-src` and the thumbnail URL), set `data-title`/`data-desc`/`data-tags` and the visible `<h3>`,
`<p>`, and `<span class="tag">` chips → commit → deploy.

Current videos: *Why Recognition* — The Real Cost of Disengagement (`r1Y62Vg_Tmw`), Ready to Make It
Stick (`twTKGe6IyAU`); *See It In Action* — VIBE Pulse (`qFzR3U0JBio`), VIBE WHS (`ZsjPsLkF2YM`),
Admin Dashboard Walkthrough (`a4MNo660pBg`), How to Submit a Nomination (`v_WkXG5JSng`).

## Binary files

`.gitattributes` marks `*.pdf`/`*.png`/`*.zip`/`*.docx`/`*.pptx`/`*.xlsx` as binary so they stay
intact across clones. Keep it.
