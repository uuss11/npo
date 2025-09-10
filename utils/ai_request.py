# utils/ai_request.py
import httpx
from bot_config import OPENROUTER_API_KEY

async def ai_reply(text):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "deepseek/deepseek-chat-v3.1:free",
        "messages": [
            {"role": "system", "content": "أجب بشكل واضح، مختصر، ومفهوم وباللغة العربية فقط."},
            {"role": "user", "content": text}
        ],
        "temperature": 0.7,
        "max_tokens": 500
    }

    try:
        async with httpx.AsyncClient(timeout=20.0) as http_client:
            response = await http_client.post(
                "https://openrouter.ai/api/v1/chat/completions",
                json=payload,
                headers=headers
            )

            if response.status_code != 200:
                return f"❌ خطأ {response.status_code} من OpenRouter: {response.text}"

            result = response.json()
            return result.get("choices", [{}])[0].get("message", {}).get("content", "⚠️ لم يتم العثور على رد مناسب.")
    
    except Exception as e:
        return f"❌ خطأ في الذكاء الاصطناعي: {str(e)}"
