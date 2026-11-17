# Anna Brabec portfolio

A German portfolio and blog for **annabrabec.com**, focused on Digital Marketing and Eventmanagement, built with Hugo and the [Roxo theme](https://themes.gohugo.io/themes/roxo-hugo/). The homepage introduces selected work, articles, Anna's profile and contact details. A separate About page contains experience and education.

## Local preview

Requires Node.js 22 or newer and the pinned Hugo binary. From this folder in PowerShell:

```powershell
git submodule update --init --recursive
npm.cmd ci
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\setup-hugo.ps1
npm.cmd run css
& .\.tools\hugo\hugo.exe server --baseURL 'http://localhost:1313/' --disableFastRender
```

Open <http://localhost:1313/>. Press Ctrl+C to stop. For subsequent previews, only the last two commands are needed. The development configuration includes drafts; production excludes them. Hugo watches content and layouts. Run `npm.cmd run css` after changing CSS or HTML classes, or use `npm.cmd run css:watch` in a second terminal.

## Content

- Two academic project pages: Anima Corporate Design and the master's thesis on advertising and brand image.
- Two shorter blog posts about Anna's design-process reflection and unconfirmed storytelling hypothesis, with bibliographic source notes.
- An Anima gallery with original logo iterations, the final logo and application mockups.
- The two original, explicitly labelled AI-generated thesis test ads and a comparison of the measured brand-image scores.
- Online experience and education, including the semester abroad in Lucerne.
- A direct email contact action and links to email and LinkedIn.
- Shared navigation, a mobile menu, article reading time and optional tables of contents for longer posts.

See [Content authoring](docs/CONTENT-AUTHORING.md) for commands to add projects and posts, update experience and education, edit the email address and update layouts.

The website uses a green introduction (`#D3E6D3`), white content sections and dark-green headings (`#486b48`). Montserrat is the single, self-hosted font family, in weights 400, 600 and 700. The single name moves into the header in one smooth, scroll-triggered animation. This explicitly requested effect remains enabled in the preview; other theme motion preferences remain in place. Local templates customize the pinned Roxo theme without changing the theme submodule. The original source PDFs remain outside the website.

## Production build and GitHub Pages

```powershell
npm.cmd run css
& .\.tools\hugo\hugo.exe --gc --minify
```

The workflow builds CSS and Hugo output and deploys from `main`. See [GitHub Pages setup](docs/GITHUB-PAGES-SETUP.md) for repository creation, pushing, hosting settings and the **annabrabec.com** domain. Standard Hugo is sufficient; the website build does not need Hugo Extended, Go or Python. The website does not offer a CV download. The optional `scripts/create-cv.py` creates an offline copy under `output/pdf/` using Python and ReportLab; that folder is excluded from Git and deployment.

The included workflow publishes the website through GitHub Pages. Domain DNS and mailbox provisioning are managed separately from the repository.
