# VIBE Recognition — Marketing Website

Static marketing site for VIBE Recognition, hosted on **Netlify** and **auto-deployed from this
repo**: every push to `main` publishes automatically. No build step, no zip.

## How it's served

The repo *is* the published site — Netlify serves the root directly (`netlify.toml` sets
`publish = "."`). Files are already named as they're served:

- `index.html` — homepage
- `terms.html`, `resources.html`, `library.html`, `portal.html`, `infographic.html`
- the 8 `VIBE_*.pdf` module/marketing PDFs (linked from `resources.html`)
- `favicon.png` (at root; pages reference `/favicon.png`)
- `sitemap.xml`

`_redirects` gives clean URLs: `/`→`/index.html`, `/terms`→`/terms.html`,
`/library`→`/library.html`, `/portal`→`/portal.html`.

## Deploy

```bash
git add -A
git commit -m "…"
git push            # Netlify auto-deploys main
```

That's it. (History note: the site used to be built into `netlify-deploy.zip` via a
`make_netlify_zip.py` script and drag-dropped to Netlify. That's retired now that Netlify is
connected to the repo; `netlify-deploy.zip` is git-ignored.)

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
`<p>`, and `<span class="tag">` chips → commit → push.

Current videos — *Why Recognition:* The Real Cost of Disengagement (`r1Y62Vg_Tmw`), Ready to Make It
Stick (`twTKGe6IyAU`); *See It In Action:* VIBE Pulse (`qFzR3U0JBio`), VIBE WHS (`ZsjPsLkF2YM`),
Admin Dashboard Walkthrough (`a4MNo660pBg`), How to Submit a Nomination (`v_WkXG5JSng`).

## Binary files

`.gitattributes` marks `*.pdf`/`*.png`/`*.zip`/`*.docx`/`*.pptx`/`*.xlsx` as binary so they stay
intact across clones. Keep it.
