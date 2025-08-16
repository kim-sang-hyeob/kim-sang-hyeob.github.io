#!/usr/bin/env python3
"""
Sync Notion database pages to Jekyll posts.
"""

import os
import re
import json
from datetime import datetime
from notion_client import Client

try:
    # Optional dependency for converting Notion pages to Markdown.
    from notion_to_md import NotionToMarkdown
except ImportError:
    NotionToMarkdown = None

def slugify(value: str) -> str:
    """Convert a string into a slug usable in file names."""
    value = value.lower()
    value = re.sub(r'[^a-z0-9]+', '-', value)
    return value.strip('-')

def get_property(page: dict, name: str):
    """Extract a typed property from a Notion page."""
    props = page.get('properties', {})
    prop = props.get(name)
    if not prop:
        return None
    if prop['type'] == 'title':
        text = prop['title']
        return text[0]['plain_text'] if text else None
    elif prop['type'] == 'date':
        return prop['date']['start'] if prop['date'] else None
    elif prop['type'] == 'multi_select':
        return [item['name'] for item in prop['multi_select']]
    elif prop['type'] == 'rich_text':
        txts = prop['rich_text']
        return ''.join([t['plain_text'] for t in txts]) if txts else None
    elif prop['type'] == 'checkbox':
        return prop['checkbox']
    return None

def main():
    notion_token = os.environ.get('NOTION_TOKEN')
    database_id = os.environ.get('NOTION_DATABASE_ID')
    if not notion_token or not database_id:
        raise RuntimeError(
            'NOTION_TOKEN and NOTION_DATABASE_ID environment variables must be set.'
        )
    client = Client(auth=notion_token)
    # Collect all pages from the database
    pages = []
    start_cursor = None
    while True:
        resp = client.databases.query(
            database_id=database_id,
            start_cursor=start_cursor,
        )
        pages.extend(resp['results'])
        if not resp.get('has_more'):
            break
        start_cursor = resp.get('next_cursor')
    # Ensure output directory exists
    if not os.path.exists('_posts'):
        os.makedirs('_posts', exist_ok=True)
    # Optionally create assets folder for images (not used in this simplified version)
    # os.makedirs(os.path.join('assets', 'notion'), exist_ok=True)
    # Process each page
    for page in pages:
        # Skip pages without Publish property or unchecked
        publish = get_property(page, 'Publish')
        if publish is False:
            continue
        title = get_property(page, 'Title') or 'Untitled'
        date_str = get_property(page, 'Date') or datetime.utcnow().strftime('%Y-%m-%d')
        slug = get_property(page, 'Slug') or slugify(title)
        categories = get_property(page, 'Category') or []
        tags = get_property(page, 'Tags') or []
        # Convert page to markdown if notion_to_md is available
        body = ''
        if NotionToMarkdown:
            n2m = NotionToMarkdown(client)
            md_blocks = n2m.page_to_markdown(page['id'])
            body = n2m.to_markdown(md_blocks)
        else:
            body = (
                'Conversion library notion_to_md not installed.\n'
                'Install notion-to-md to enable full conversion.'
            )
        # Build front matter and body
        front_matter = [
            '---',
            f'title: "{title}"',
            f'date: {date_str} 00:00:00 +0900',
            f'categories: {json.dumps(categories)}',
            f'tags: {json.dumps(tags)}',
            'toc: true',
            '---',
            '',
        ]
        content_lines = front_matter + body.split('\n')
        filename = f'{date_str}-{slug}.md'
        filepath = os.path.join('_posts', filename)
        if os.path.exists(filepath):
            # Don't overwrite existing posts
            print(f'Skipping existing file {filepath}')
            continue
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(content_lines))

if __name__ == '__main__':
    main()
