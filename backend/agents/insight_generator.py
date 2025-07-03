import os
import requests

MODEL_MAP = {
    "llama": "meta-llama/Llama-2-7b-chat-hf",
    "qwen": "Qwen/Qwen1.5-7B",
    "deepseek": "deepseek-ai/deepseek-llm-r",
    "gemma": "google/gemma-7b",
    "compound": "Qwen/Compound-mini"
}

def generate_spm(corap, length, model_name="deepseek"):
    API_URL = f"https://api-inference.huggingface.co/models/{MODEL_MAP[model_name]}"
    headers = {"Authorization": f"Bearer {os.getenv('HF_API_KEY')}"}
    
    prompt = f"""
    Create a {length}-page Summary for Policymakers (SPM) with:
    - Executive summary
    - Key findings
    - Recommendations
    - Conclusion
    
    Use this document: {corap}
    """
    
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 2000}
    }
    
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()[0]['generated_text']
