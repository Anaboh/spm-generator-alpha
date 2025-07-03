def chat_with_pdf(question, text_content):
    relevant = []
    for page in text_content:
        if question.lower() in page['content'].lower():
            relevant.append({
                "page": page['page'],
                "excerpt": page['content'][:200] + "..."
            })
    
    if not relevant:
        return "Not found in document", []
    
    response = f"Found {len(relevant)} relevant sections:\n"
    for i, ref in enumerate(relevant):
        response += f"{i+1}. Page {ref['page']}: {ref['excerpt']}\n"
    
    return response, relevant
