# Project

This repo contains a self-contained HTML app that embeds a fixed Python script (execute.py), a CSV placeholder (data.csv), and a CI workflow (ci.yml). The app demonstrates how to bake content directly into a single HTML file for offline demos.

- execute.py is corrected to a robust, minimal example that writes result.json using pandas when available.
- data.csv is provided as a placeholder that mirrors the data.xlsx attachment in this challenge.
- ci.yml defines a GitHub Actions workflow that runs ruff, executes the Python script, and deploys the generated result.json to GitHub Pages.

Note: result.json is not committed; it is produced by CI.
