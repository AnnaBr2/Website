# Hugo and GitHub Pages setup guide

This project is ready to become a GitHub Pages website. Preview and personalize the starter, create a GitHub repository, select GitHub Actions as the Pages source, then push `main`. The included workflow builds Hugo and publishes the generated site after each push.

The selected repository is **AnnaBr2/Website**: <https://github.com/AnnaBr2/Website>. Its initial Pages address is **https://annabr2.github.io/Website/**; the final address is **https://annabrabec.com/**. Public DNS checked before domain setup on 17 November 2026 used Namecheap BasicDNS, with a parked `www` record. Section 10 gives the exact Namecheap changes. Git is initialized on `main`; the first-commit and remote-creation commands below are one-time setup steps. Use section 8 for subsequent updates.

Commands below use **Windows PowerShell** and assume the project is in `C:\Users\nop\Desktop\AnnaWebsite`. Run the steps in order and stop if a command reports an error. Repository creation and publication are steps for you to run; the local starter does not create a GitHub repository by itself.

## 1 Install tools and preview locally

Install Git, the GitHub CLI, and Node.js if they are not already available:

```powershell
winget install --exact --id Git.Git
winget install --exact --id GitHub.cli
winget install --exact --id OpenJS.NodeJS.LTS
```

Open a new PowerShell window after installation so the PATH changes take effect. Check the tools, enter the project, and install the pinned Hugo version:

```powershell
git --version
gh --version
Set-Location 'C:\Users\nop\Desktop\AnnaWebsite'
git submodule update --init --recursive
npm.cmd ci
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\setup-hugo.ps1
& .\.tools\hugo\hugo.exe version
npm.cmd run css
& .\.tools\hugo\hugo.exe server -D --baseURL 'http://localhost:1313/'
```

Open <http://localhost:1313/>. Press **Ctrl+C** to stop the server before continuing in that terminal. `-D` includes draft pages in local preview; production builds exclude drafts.

The installer reads `.hugo-version`, downloads the official standard Windows release, checks its SHA256 against the release checksum list, and extracts it under `.tools/hugo/`. It does not change your system PATH. `-ExecutionPolicy Bypass` applies to that invocation only; it does not permanently change the machine policy. If organizational policy blocks scripts, follow your administrator's approved installation method.

Hugo is pinned to **0.170.0**. The same version file controls CI. The Roxo adaptation requires Node.js 22 or newer for Tailwind CSS. Its selected templates and styles work with standard Hugo and do not require Go modules. The theme is pinned as a Git submodule, and npm dependencies are locked in package-lock.json. See [Hugo installation on Windows](https://gohugo.io/installation/windows/).

## 2 Choose the repository and public address

This setup uses a public project repository named `Website`:

| Site type | Repository name | Public address |
| --- | --- | --- |
| Project website (selected) | `Website` | `https://annabr2.github.io/Website/` |
| Personal or organization homepage | `YOUR-USERNAME.github.io` | `https://YOUR-USERNAME.github.io/` |

The owner is `AnnaBr2`. A custom domain works with the selected project repository; it does not require renaming the repository to `AnnaBr2.github.io`. For a root github.io homepage, the repository name must instead match the owner followed by `.github.io`. See [GitHub Pages site types](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages).

A public repository works with GitHub Free. Private repository support depends on the account plan; a private repository does not by itself make the deployed website private. The commands below create a **public** repository. See [Pages availability and publishing sources](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

## 3 Personalize the starter

Edit these files in your editor before the first publication:

- `content/_index.md`: homepage title and introduction.
- `content/about.md`: standalone biography page.
- `content/projekte/` and `content/blog/`: portfolio case studies and articles; see [Content authoring](CONTENT-AUTHORING.md) for creation commands.
- `hugo.toml`: site title, description, language, domain, and LinkedIn URL.
- `layouts/_partials/essentials/header.html`: navigation.
- `assets/css/custom.css`: colors, typography, and spacing.
- `layouts/_partials/profile.html`: biography, experience, education, and skills.

The production domain is already configured in `hugo.toml`:

```toml
baseURL = 'https://annabrabec.com/'
```

For an initial github.io deployment before the custom domain is connected, the workflow uses the URL reported by GitHub Pages. The deployment workflow gets the actual address from GitHub Pages and passes it to Hugo automatically, overriding this setting for CI. Keeping the local setting accurate also makes local production builds and canonical links correct.

Run a production build:

```powershell
npm.cmd run css
& .\.tools\hugo\hugo.exe --gc --minify
```

Hugo writes the result to `public/`. Do not commit that directory; it is already ignored. The workflow builds and uploads it. This is a static site: forms, account sign-in, and server-side code need a separate service if added later.

## 4 Sign in and create the first commit

Authenticate the CLI and configure Git to use its credentials:

```powershell
gh auth login --hostname github.com --git-protocol https --web
gh auth setup-git
gh auth status
```

Follow the browser sign-in prompts using `AnnaBr2`. Git is already initialized in this prepared folder. Set your commit identity, replacing both sample values; GitHub's private noreply address from **Settings > Emails** can be used for the email.

```powershell
git config user.name 'Your Name'
git config user.email 'YOUR-GITHUB-EMAIL'
git status --short --ignore-submodules
git add .
git commit -m "Create Hugo website and GitHub Pages workflow"
```

These `git config` commands apply to this repository only. Review `git status --short` before staging so that only intended files are committed. The website already exists locally; there is no need to run `hugo new site` in this folder.

## 5 Create the GitHub repository

Set the repository variables in the same PowerShell session:

```powershell
$owner = 'AnnaBr2'
$repo = 'Website'
gh repo create "$owner/$repo" --public --source . --remote origin
```

For an organization, replace `$owner` with its name and ensure your account can create repositories there. For a root homepage, use `$repo = "$owner.github.io"` before creating the repository. The CLI creates an empty remote and connects it as `origin`; pushing happens after Pages is configured. See [GitHub CLI repository creation](https://cli.github.com/manual/gh_repo_create).

**Browser alternative (does not require GitHub CLI):** create a new public repository at <https://github.com/new> with owner `AnnaBr2` and name `Website`. Leave the README, license, and gitignore initialization options unchecked because this folder already contains files. If that empty repository already exists, reuse it. Then run the following instead of `gh repo create`:

```powershell
git remote add origin 'https://github.com/AnnaBr2/Website.git'
```

Choose only one creation method. If you use the browser route, skip the `gh` commands: Git for Windows can handle HTTPS sign-in with its browser-based Credential Manager flow. See [GitHub authentication in Git](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git). If you already created an empty remote, connect it with `git remote add`; do not create another one. If it already contains commits, clone it into a separate folder and copy this starter into that checkout before committing, preserving its history.

## 6 Apply the GitHub hosting settings

Open the repository settings:

```powershell
Start-Process 'https://github.com/AnnaBr2/Website/settings/pages'
```

Apply these settings:

1. **Settings > Pages > Build and deployment > Source:** select **GitHub Actions**. The workflow is already included, so skip the offered workflow templates. Do not choose a branch or `/docs` publishing folder for this setup.
2. **Settings > Actions > General:** ensure Actions are enabled. If actions are restricted, allow the official actions used here: `actions/setup-node`, `actions/checkout`, `actions/configure-pages`, `actions/upload-pages-artifact`, and `actions/deploy-pages`, at the versions in the workflow.
3. Leave the repository's default workflow permissions at read access if that is its default. The workflow explicitly grants the deployment job `pages: write` and `id-token: write`; it does not need a personal access token or repository secret.
4. **Settings > Pages > Custom domain:** leave empty for the default `github.io` address. Enable **Enforce HTTPS** if that control is available; the default Pages address uses HTTPS.
5. After the first deployment creates the `github-pages` environment, inspect **Settings > Environments > github-pages**. If deployment branch rules are configured, they must permit `main`. You can restrict that environment to `main`.

If Pages settings are unavailable until the repository has a branch, push once using the next step, select **GitHub Actions**, then rerun the workflow. A first run failing at “Read GitHub Pages configuration” in that situation is resolved by enabling Pages and rerunning it.

The settings and permissions follow [GitHub's publishing-source guide](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) and [custom workflow guide](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## 7 Push and verify deployment

```powershell
git push -u origin main
gh run list --workflow hugo.yml --limit 5
```

Open the repository's **Actions** tab and select **Deploy Hugo to GitHub Pages**. Wait for both `build` and `deploy` to succeed, then open the address shown by the deployment or **Settings > Pages**. The site may take a few minutes to become available. Check the homepage, About page, navigation, and styling at the published address.

To inspect the latest run in your browser:

```powershell
gh run view --web
```

To start a fresh deployment after changing Pages settings:

```powershell
gh workflow run hugo.yml --ref main
```

No `gh-pages` branch, manually uploaded HTML, or `.nojekyll` file is needed with this artifact deployment workflow. The workflow builds the source on `main`, uploads `public/`, and deploys it to Pages. See [Hugo hosting on GitHub Pages](https://gohugo.io/host-and-deploy/host-on-github-pages/).

## 8 Everyday editing commands

Before editing in a shared repository, bring your local branch up to date:

```powershell
git pull --ff-only
git submodule update --init --recursive
npm.cmd ci
npm.cmd run css
& .\.tools\hugo\hugo.exe server -D --baseURL 'http://localhost:1313/'
```

After editing and stopping the preview with Ctrl+C:

```powershell
npm.cmd run css
& .\.tools\hugo\hugo.exe --gc --minify
git diff
git add .
git commit -m "Update website content"
git push
```

Each push to `main` automatically rebuilds and deploys. To add a page:

```powershell
& .\.tools\hugo\hugo.exe new content contact.md
```

Edit `content/contact.md` and change `draft = true` to `draft = false` when ready to publish. This adaptation has a custom header: add the new page link in `layouts/_partials/nav-links.html` if it should appear in navigation. The contact section links to email and LinkedIn. Career and education information is on the About page; no CV PDF is published.

After changing CSS or HTML classes, run `npm.cmd run css` again. For continuous style rebuilding, run `npm.cmd run css:watch` in a second terminal alongside Hugo.

To work on another Windows computer, install Git, Node.js, and the CLI, sign in, then clone and install the project-local Hugo binary:

```powershell
git clone --recurse-submodules https://github.com/AnnaBr2/Website.git
Set-Location Website
npm.cmd ci
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\setup-hugo.ps1
npm.cmd run css
& .\.tools\hugo\hugo.exe server -D --baseURL 'http://localhost:1313/'
```

To upgrade Hugo, update `.hugo-version`, rerun the installer, preview, and build before committing the version change. Both local installation and CI use that file.

## 9 Troubleshooting

| Symptom | Action |
| --- | --- |
| `git` or `gh` is not recognized | Reopen PowerShell after installation and check `git --version` or `gh --version`. |
| Local Hugo executable is missing | Run `scripts/setup-hugo.ps1` from step 1 and check for download errors. |
| The Roxo theme is missing | Run `git submodule update --init --recursive`. |
| Build reports that compiled CSS is missing | Run `npm.cmd ci`, then `npm.cmd run css`. |
| Push reports authentication failure | Run `gh auth status`, sign in again if needed, and run `gh auth setup-git`. |
| `origin` already exists | Inspect `git remote -v`. If it points to the wrong repository, use `git remote set-url origin "https://github.com/$owner/$repo.git"`. |
| Push is rejected because the remote has commits | Do not force-push. Clone the remote into a separate folder and copy the starter files there, then commit and push. |
| Pages configuration returns 404 | Confirm repository ownership, plan eligibility, and Pages source set to GitHub Actions, then rerun the workflow. |
| Deployment waits or is rejected | Check environment approval or branch rules under `github-pages`; ensure `main` is permitted. |
| Site returns 404 | Confirm both jobs succeeded and use the URL from Settings > Pages, including the repository path for a project site. |
| CSS or navigation is broken on a project site | Retain the workflow's `--baseURL` override and use Hugo `relURL` or page permalinks for links. Avoid hardcoded paths such as `/css/style.css`. |
| New page is missing | Set `draft = false`, check dates are not in the future, and commit the content file. |
| Workflow does not run on push | Push to `main`, check Actions are enabled, and confirm `.github/workflows/hugo.yml` is committed. |

## 10 Connect annabrabec.com through Namecheap

First confirm that the workflow deploys successfully at **https://annabr2.github.io/Website/**. Public DNS checked on 17 November 2026 returns `dns1.registrar-servers.com` and `dns2.registrar-servers.com`, Namecheap's [BasicDNS nameservers](https://www.namecheap.com/support/knowledgebase/article.aspx/923/10/what-is-your-basicdns/). The root currently resolves to `192.64.119.49`, `www` points to `parkingpage.namecheap.com`, and mail uses Namecheap forwarding MX records. Recheck these if the setup has changed since that date.

### Verify ownership

In **GitHub account settings > Pages > Add a domain**, add `annabrabec.com`. GitHub provides a TXT record, normally with host `_github-pages-challenge-AnnaBr2`; copy its exact host and value. In Namecheap, open **Domain List > Manage** beside `annabrabec.com` **> Advanced DNS > Host Records > Add New Record**, choose **TXT Record**, enter the supplied details and save. Namecheap appends the domain to the Host field, so use the host label rather than repeating `.annabrabec.com` when appropriate. Return to GitHub and click **Verify**. Keep the TXT record afterward. Follow the values displayed by GitHub rather than inventing a verification code. See [GitHub domain verification](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages).

### Save the domain in the repository

Open <https://github.com/AnnaBr2/Website/settings/pages>. Under **Custom domain**, enter `annabrabec.com` and click **Save** before changing website routing in DNS. With this custom Actions workflow, no `CNAME` file is required in the source. See [GitHub custom-domain configuration](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).

### Replace Namecheap's parking records

In **Namecheap > Domain List > Manage > Advanced DNS > Host Records**, replace the old `@` website redirect/A record and the `www` parking CNAME with these five records. Keep the nameservers on BasicDNS. Leave **Mail Settings**, MX records and email-related TXT records in place so this website change does not interrupt email forwarding.

| Type | Host | Value | TTL |
| --- | --- | --- | --- |
| A Record | `@` | `185.199.108.153` | Automatic |
| A Record | `@` | `185.199.109.153` | Automatic |
| A Record | `@` | `185.199.110.153` | Automatic |
| A Record | `@` | `185.199.111.153` | Automatic |
| CNAME Record | `www` | `annabr2.github.io` | Automatic |

The CNAME value contains no `https://` and no `/Website` path. Save all changes. Namecheap's [GitHub Pages guide](https://www.namecheap.com/support/knowledgebase/article.aspx/9645/2208/how-do-i-link-my-domain-to-github-pages/) covers this screen, and its [hosting connection guide](https://www.namecheap.com/support/knowledgebase/article/9837/46/how-to-connect-a-domain-to-a-server-or-hosting/) explains removal of default parking and URL redirect records. No website URL redirect is needed at Namecheap; GitHub handles the `www` redirect after both DNS entries work.

IPv6 is optional. If you add AAAA records for `@`, use all four GitHub addresses: `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, and `2606:50c0:8003::153`. Do not retain old AAAA records pointing to a different host.

### Enable HTTPS and rebuild

Wait for GitHub's DNS check and certificate issuance, then enable **Settings > Pages > Enforce HTTPS**. DNS and availability of this checkbox can each take up to 24 hours. GitHub provisions the certificate; a separate Namecheap SSL purchase is unnecessary for Pages hosting. See [GitHub HTTPS setup](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https).

Under **Actions > Deploy Hugo to GitHub Pages > Run workflow**, select `main` and run it again after saving the domain, so the build uses the custom URL. `baseURL` is already `https://annabrabec.com/`; the workflow also reads the current Pages URL.

These PowerShell commands check DNS without changing it:

```powershell
Resolve-DnsName annabrabec.com -Type A
Resolve-DnsName www.annabrabec.com -Type CNAME
```

Finally check **https://annabrabec.com/**, the About page, project links and styling. **https://www.annabrabec.com/** should redirect to the main domain. The contact button opens an email to `brabecanna22@gmail.com`; no domain mailbox or email forwarding is required for this contact address.
