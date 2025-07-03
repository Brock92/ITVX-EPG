name: Update EPG

on:
  schedule:
    - cron: '0 */12 * * *'   # Every 12 hours
  workflow_dispatch:         # Allow manual trigger

permissions:
  contents: write

jobs:
  update-epg:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'

      - name: Download and compress EPG
        run: python generate_epg.py

      - name: Commit and push changes
        env:
          GH_TOKEN: ${{ secrets.GH_PAT }}
        run: |
          git config --global user.name "GitHub Actions"
          git config --global user.email "actions@github.com"
          git remote set-url origin https://x-access-token:${GH_TOKEN}@github.com/${{ github.repository }}
          git add guide.xml.gz
          git commit -m "Auto-update EPG $(date -u '+%Y-%m-%d %H:%M:%S UTC')" || echo "No changes to commit"
          git push
