# Notion CMS Integration

This repository includes a workflow that turns pages in a Notion database into Jekyll posts.

## Notion database setup

1. **Create a database** in Notion to act as your blog CMS.
2. Add these properties to the database:
   - **Title** (type: title) – the post title.
   - **Date** (type: date) – the publish date.
   - **Slug** (type: text) – optional custom slug; leave blank to derive from the title.
   - **Category** (type: multi-select) – one or more categories (e.g. `paper review`, `deepdive`).
   - **Tags** (type: multi-select) – optional tags.
   - **Publish** (type: checkbox) – only pages with this checked will be converted to posts.
3. Write your post content using regular Notion blocks (paragraphs, headings, lists, code blocks, etc.). Images and embeds may not be fully supported.

## GitHub configuration

1. In Notion, create an **internal integration** (Settings → Integrations) and share your database with it.
2. In this repository, open **Settings → Secrets and variables → Actions** and add two secrets:
   - `NOTION_TOKEN` – your integration secret token.
   - `NOTION_DATABASE_ID` – the ID of your database (found in its URL).
3. Commit your changes to Notion. The GitHub Action will use these secrets to fetch your data.

## Running the import

This repository contains:

- `.github/workflows/notion-to-posts.yml`: a GitHub Actions workflow that calls the Python import script.
- `scripts/notion_to_posts.py`: a Python script that queries the Notion database and writes files under `_posts/` using the format `YYYY-MM-DD-slug.md`.
- `scripts/requirements.txt`: a list of Python dependencies (`notion-client` and `notion-to-md`).

The workflow runs daily at midnight UTC. You can also trigger it manually from the **Actions** tab. Only pages with **Publish** checked will be imported. Existing files in `_posts/` will never be overwritten.

## Limitations

- The script does not download images or other media. If your posts include images, you should upload them to this repository (e.g. under `assets/images/`) and update the links accordingly.
- Complex Notion blocks (such as tables, columns, callouts) may not render perfectly in Markdown. Feel free to extend `scripts/notion_to_posts.py` to handle more block types or to download images.

