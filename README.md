# csaez.github.io

Personal resume/CV site for Cesar Saez, built with Jekyll and hosted on
GitHub Pages.

## Publishing

Pushing a commit to the `main` branch triggers GitHub Actions, which builds
and deploys the site automatically. The live site is typically updated within
a few minutes of each push.

## Content

All resume content lives in the `_data/` directory as YAML files with
Markdown strings:

- `_data/intro.yml` - header intro paragraph
- `_data/experience.yml` - work history entries
- `_data/skills.yml` - skills list
- `_data/education.yml` - education history
- `_data/recommendations.yml` - recommendations

Edit those files to update the site; no other changes are needed.

## Local Preview

```
bundle exec jekyll serve
```

Then open http://localhost:4000 in your browser.

## Credits

Based on the [resume-template](https://github.com/jglovier/resume-template)
by Joel Glovier.
