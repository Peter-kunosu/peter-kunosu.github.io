# Peter's Portfolio — Hugo + Blowfish

A clean English-language developer portfolio, hosted on GitHub Pages. Displays up to 8 recently updated public repositories, excluding forks, archived repositories and the portfolio itself. GitHub Actions refreshes the project list on every push to `main`, once daily, and on manual runs.

## 1. Create the GitHub repository

Create a **public** repository named exactly `peter-kunosu.github.io` under the `peter-kunosu` account. Do not initialize it with a README if you are pushing this project directly.

## 2. Install the Blowfish theme

Blowfish is loaded as a Git submodule. In the project directory, run:

```bash
git init
git branch -M main
git submodule add -b main https://github.com/nunocoracao/blowfish.git themes/blowfish
```

**Important:** Run the submodule command before committing. The ZIP intentionally excludes the theme source code; the submodule downloads the latest Blowfish theme.

## 3. Preview locally

Install Hugo Extended (compatible with the installed Blowfish theme), Git and Python 3. Then run:

```bash
python3 scripts/fetch_projects.py
hugo server -D
```

Open http://localhost:1313/.

## 4. Publish

```bash
git add .
git commit -m "Launch portfolio"
git remote add origin https://github.com/peter-kunosu/peter-kunosu.github.io.git
git push -u origin main
```

In the repository's **Settings → Pages → Build and deployment**, set **Source** to **GitHub Actions**. Open the **Actions** tab and check the deployment run. Your site should become available at https://peter-kunosu.github.io/.

## 5. Customize

- Edit `hugo.toml` to change your display name, tagline, description and social links.
- Edit `layouts/index.html` to change homepage copy.
- Edit `assets/css/custom.css` for styling.
- Edit `scripts/fetch_projects.py` to change the number of repositories (currently 8) or filtering rules.

## Notes

- Only **public** repositories are shown. The list is based on GitHub's repository `updated` ordering, not commit activity across all branches.
- If the GitHub API is unavailable, the build intentionally fails instead of silently publishing stale project data.
- The first build fetches projects; `data/github.json` initially contains an empty list.
- Scheduled GitHub Actions may be delayed, and GitHub can disable scheduled workflows after prolonged inactivity in public repositories.
- The workflow pins Hugo to `0.147.9`; if a newer Blowfish release requires a newer Hugo version, update `hugo-version` in `.github/workflows/deploy.yml`.
