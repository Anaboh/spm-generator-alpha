def create_corap(text_content):
    return {
        "executive_summary": text_content[0]['content'][:500] + "...",
        "core_content": [entry['content'] for entry in text_content],
        "figures": [],
        "tables": []
    }
