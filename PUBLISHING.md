# Publish on GitHub and review the map

Suggested repository name: **testers-enchiridion**.

Suggested description: **A handbook for software and systems testers: 52 chapters inspired by Epictetus, with an interactive concept map. CC BY-SA 4.0.**

All publication files are included. The website is already built in `docs/`; GitHub Pages does not need Python, ReportLab, npm, or a custom build workflow.

## 1. Create and upload the repository

Create an empty repository in the intended personal account or organization. Use **Public** for this review edition. Do not generate another README or license; this package already contains them.

Unzip the publication package. Upload the **contents of the `testers-enchiridion` folder**, so `README.md`, `LICENSE`, `book/`, `data/`, and `docs/` are at the repository root. Do not upload the ZIP itself as the only repository file.

You can use GitHub's **Add file → Upload files** interface, GitHub Desktop, or the command line. To use Git after creating the empty repository, run these commands inside the unpacked project folder; paste the repository's actual HTTPS URL when prompted:

```sh
git init -b main
git add .
git commit -m "Prepare The Tester's Handbook V103 for review"
printf 'Repository HTTPS URL: '
IFS= read -r REPOSITORY_URL
git remote add origin "$REPOSITORY_URL"
git push -u origin main
```

Use your normal GitHub authentication; no credential belongs in the repository or in a message. If Git asks for commit identity, use the identity you normally use for GitHub.

## 2. Enable GitHub Pages

In the repository, open **Settings → Pages**. Under **Build and deployment**, choose:

- **Source:** Deploy from a branch
- **Branch:** `main`
- **Folder:** `/docs`

Save, then wait for GitHub's Pages deployment to finish. Open the site URL shown on that settings page. Add that same URL to the repository's **About → Website** field. You can then add it as the map link at the top of the README.

For a normal project repository, the address has the form `https://OWNER.github.io/testers-enchiridion/`. Use the actual URL GitHub provides; the owner and repository name determine it.

This is a public review deployment. You can hold off on announcing it while making changes, but an unannounced public repository and Pages site can still be discovered.

## 3. Review it on GitHub Pages

- Open the map on desktop and phone. Check that all buttons, chapter text, and lines remain readable.
- Follow **Judgment → §18**. Confirm the raven is explained as an omen and the chapter ends with “It has not been appointed to govern you.” Its testing links should concern accountability, professional conduct, and risk.
- Follow **Character → §46**. Confirm Socrates and being overlooked are central, with no sheep comparison in the testing chapter. Its testing links should be collaboration, professional conduct, and knowledge transfer.
- Switch between **Tester’s chapter** and **Carter passage**. Check that the historical view is labelled as a selected passage, opens the appropriate source page, and does not claim the whole original chapter is reproduced.
- Use the chapter selector, Previous/Next buttons, and keyboard. Reload a direct link such as `#chapter-46` and test the browser's Back button.
- Select a testing concept, open a related chapter, and check that the concept-to-chapter connection makes sense.
- Open **Read**, **Sources**, and **PDF**. Check the PDF contents links and the license/attribution links.

Use issues to record changes with chapter numbers and short explanations. Edit the source files, rebuild, and push again; Pages republishes changes in `docs/`.

## 4. Announce when ready

After the review, you can create a release tagged `v1.03`, attach the PDF, and link the Pages site from the LinkedIn post. The release can preserve a specific edition while the main branch continues to evolve.

## Official references

- [GitHub Pages: configuring a publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [CC BY-SA 4.0 license](https://creativecommons.org/licenses/by-sa/4.0/)
