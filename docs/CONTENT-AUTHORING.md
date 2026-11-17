# Portfolio and blog editing

The homepage introduces Anna, shows up to three projects by `weight`, a short profile, and the two newest articles. Links to all projects or posts appear only when more items exist. Projects use image cards; articles use compact rows. Each has a standalone URL. Project pages document the work; blog posts focus on a specific decision, lesson or open question instead of repeating the project summary.

## Current content

- `content/projekte/anima.md`: Corporate Design study project, WS 2025.
- `content/projekte/masterarbeit-markenimage.md`: master's thesis, 2026.
- `content/blog/anima-von-der-markenidee-zum-design.md`: article based on the Anima presentation.
- `content/blog/psychische-gesundheit-markenimage.md`: article based on the thesis.
- `static/images/portfolio/`: selected exports from the presentation and the research overview graphic.
- The homepage and About page target Digital Marketing and Eventmanagement. Anna's supplied role at Cotton Classics is Marketing Allrounderin und Projektmanagement, covering varied marketing activities, digital marketing and the planning, organization and execution of the roadshow. The education section includes International Tourism Management at Lucerne University of Applied Sciences and Arts, February–June 2026, as a semester abroad. A separate Weiterbildung section lists Cambridge Advanced Digital and Google Search Certificate (2025). Add further deliverables or outcomes only when Anna supplies them.

The articles contain bibliographic source notes. The original thesis and presentation are not copied into the public site. The source presentation's unused template slides are excluded. Academic projects are identified as such; no commercial results are implied.

Career and education were checked against Anna's supplied 2026 CV on 17 November 2026. The timeline includes Cotton Classics, Unique Public Relations GmbH, the editorial role for „Im Dialog“ (March–October 2023), Erste Bank AG (July 2022), the two FH St. Pölten degrees, the Lucerne semester abroad and HTL Spengergasse (September 2016–June 2021). Roadshow details, the semester dates and the certificates also use Anna's explicit messages. The source CV remains outside the website; its private contact details and photo are not copied into the site.

## Add an article

From the project directory in PowerShell:

```powershell
& .\.tools\hugo\hugo.exe new content --kind blog blog/mein-neuer-beitrag.md
```

Edit the generated Markdown file. Use a concise `description`, a real publication date, and a `category`. Put headings at level 2 (`##`); reading time is automatic. Short posts use a single reading column. Set `toc: true` only for a longer post that benefits from a table of contents. Change `draft: true` to `draft: false` when the text is ready. Quote YAML values containing a colon followed by a space.

Set `project: /projekte/mein-projekt` to link the related project below the article. Put a short bibliographic note in `source`; it appears once below the text. Ground first-person reflections in Anna's own material and have her review any new wording before publication.

## Add a project

```powershell
& .\.tools\hugo\hugo.exe new content --kind projekte projekte/mein-projekt.md
```

Fill in role, timeframe, methods and the outcome. `project_type` can be `Studienprojekt`, `Masterarbeit` or an appropriate description of a real assignment. Lower `weight` values appear first. Put images in `static/images/portfolio/` and set `cover` to `images/portfolio/dateiname.webp`. Add descriptive alternative text in `cover_alt`. The optional `deliverable` adds a result line to the project card; omit it if it repeats the description.

Visual projects use a `feature` image near the top, a short introduction, a `process` gallery for development, an optional `palette`, and a `gallery` for applications. Set `feature` to enable this layout. Research projects without a feature image use a reading column. Example YAML front matter:

```yaml
short_title: A concise title for the homepage card
feature:
  src: images/portfolio/main-image.webp
  alt: A description of the main visual.
  width: 1600
  height: 900
intro_heading: The idea
process_heading: The development
process:
  - src: images/portfolio/original-logo.webp
    alt: A description of the original artwork.
    title: The decision to notice
    caption: Explain what changed and why, based on the source material.
    width: 1000
    height: 800
    logo: true
gallery_heading: Applications
gallery:
  - src: images/portfolio/dateiname.webp
    alt: A description of the visual.
    title: A short caption heading
    caption: The decision or detail to notice.
    wide: true
```

Omit `wide` for a half-width image on desktop. Gallery images stack on mobile. `logo: true` adds a frame that contains the artwork without cropping it; use original artwork or document extracts rather than entire presentation slides. Optional `palette` entries have `name` and a quoted `hex`; `palette_intro` explains the color system. The Anima page provides a complete example.

Research pages can use `finding: {label: ..., title: ..., text: ...}` for a brief, accurate finding before the detailed method and results. Avoid presenting participant counts or correlations as commercial performance metrics. Set `related_article: /blog/mein-beitrag` for the related story and `source` for a single source/context note below the gallery or body. Keep academic context and necessary research limitations clear without repeating the same disclaimer under every image.

The thesis page places `{{< research-material >}}` and `{{< research-results >}}` in its Markdown body. Their data comes from `research_material`, `material_note` and `result_comparison` in the front matter. The ads are extracted from PDF pages 118–119 (printed pp. 108–109), labelled as AI-generated material for a fictional brand. Numbers inside the test ads are not study results. The comparison table uses the reported means and group sizes from printed pp. 136–137, and retains the non-significant test result. Any future chart should identify the metric and uncertainty clearly; the difference in means does not establish effectiveness.

`presentation_tool` optionally identifies the tool used for the project presentation. For Anima, Canva is verified by the supplied presentation's metadata; this field does not claim that every logo or mockup was created in Canva. Exact production time and collaboration details remain unspecified.

Draft pages show an editorial draft notice. Published project pages use the explicit `project_type` to distinguish academic work from other assignments.

For inline images in these pages, use paths such as `../../images/portfolio/dateiname.webp`. These retain the repository prefix when GitHub Pages uses a project URL. The `project` and `related_article` fields generate cross-links automatically.

## Preview and build

```powershell
npm.cmd run css
& .\.tools\hugo\hugo.exe server --baseURL 'http://localhost:1313/' --disableFastRender
```

`config/development/hugo.toml` enables drafts in local development. Production builds exclude drafts. After changing CSS or template classes, rebuild CSS or run `npm.cmd run css:watch` in a second terminal.

```powershell
npm.cmd run css
& .\.tools\hugo\hugo.exe --gc --minify
```

## Contact and career information

The email button uses `params.email` in `hugo.toml`, currently `contact@annabrabec.com`. This is a mail link; mailbox provisioning is handled by the domain's email provider.

The hero contains the Contact and Work actions without an additional email/copy row. The email address remains available in the contact section and inner-page footers. The homepage profile links to the About page, which contains the full career and education section.

There is no public CV download. The previous PDF is retained offline under `output/pdf/`. The optional `scripts/create-cv.py` requires Python with ReportLab and writes only to that ignored folder; it does not copy a PDF into `static/`. Website deployment does not need Python.

Keep the homepage introduction and `layouts/_partials/profile.html` synchronized with the About page and Anna's supplied career history. If an offline CV is generated later, review its dates, wording and layout separately before using it.

## Where to change the layout

- `layouts/home.html` and `content/_index.md`: homepage order, introduction and hero actions. The primary action opens an email to `params.email`; the secondary action jumps to the work. The degree remains between the name and actions; `banner.intro` contains Anna's personal introduction, without an additional professional-focus headline.
- `layouts/_partials/nav-links.html`: shared desktop and mobile links.
- `layouts/_partials/profile.html`: full career and education section on the About page.
- `layouts/_partials/article-card.html`: compact blog rows.
- `layouts/_partials/call-to-action.html`: homepage email and LinkedIn actions. Inner pages use a simple email link in the footer.
- `layouts/projekte/` and `layouts/blog/`: list and detail layouts.
- `assets/css/custom.css`: colors, typography, spacing and responsive behavior.

Montserrat is the single font family used across the interface and reading text. Heading sizes and line breaks are designed to avoid splitting words; verify long titles at 320px as well as desktop sizes. The cropped logo artwork is extracted from Anna's original presentation, not recreated.

The homepage uses one visible name element. `assets/js/name-motion.js` chooses a destination after 12px of downward scrolling and returns to the hero within 2px of the top. CSS completes a single 650ms compositor transition; pauses or further mouse-wheel events never split it into increments or restart it. Reversing direction to the top reverses from the current visual position. The user explicitly requested this animation to stay enabled, including in the preview's reduced-motion environment; only this transition and its header fade are exempt from the theme's duration override. The placeholder preserves document flow during animation; resize and font loading recalculate positions only when geometry actually changes. Without JavaScript the name remains in the introduction and navigation still works. Footer branding uses the domain to avoid repeating the name.

`static/images/portfolio/masterarbeit-preview.svg` is a designed document illustration using the thesis title, not a screenshot or extract of the original PDF. Keep personal identifiers out of preview artwork.

Use the existing [GitHub Pages guide](GITHUB-PAGES-SETUP.md) for repository creation, publishing and domain settings.
