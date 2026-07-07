from scholarly import scholarly
import json
from datetime import datetime
import os

author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
# Only fetch basics/indices/counts (fast, single request).
# 'publications' causes many per-paper requests and often hangs.
scholarly.fill(author, sections=['basics', 'indices', 'counts'])
name = author['name']
author['updated'] = str(datetime.now())

# Build minimal publications dict from the search result (no per-paper fetch)
author['publications'] = {}
if 'publications' in author:
    for pub in author['publications']:
        pub_id = pub.get('author_pub_id', '')
        if pub_id:
            author['publications'][pub_id] = {
                'num_citations': pub.get('num_citations', 0),
                'bib': {'title': pub.get('bib', {}).get('title', '')}
            }

print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open('results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": f"{author.get('citedby', 0)}",
}
with open('results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
