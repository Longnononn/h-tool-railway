import os
import discord
from deep_translator import GoogleTranslator
from openai import OpenAI
from dotenv import load_dotenv

# Tải biến môi trường từ file .env nếu có
load_dotenv()

# --- 1. Cấu hình & Biến môi trường ---
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
HUGGINGFACE_TOKEN = os.getenv("HF_TOKEN")

# Khởi tạo client OpenRouter
try:
    openrouter_client = OpenAI(
        base_url="https://router.huggingface.co/v1",
        api_key=HUGGINGFACE_TOKEN,
    )
except Exception as e:
    print(f"Lỗi khởi tạo client OpenRouter: {e}")
    openrouter_client = None

# Khởi tạo Google Translate
translator = GoogleTranslator(source='auto', target='vi')

# Cấu hình Discord client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# --- 2. Hàm chính ---
async def ask_huggingface(prompt):
    """Gửi yêu cầu đến Hugging Face (qua OpenRouter) và dịch câu trả lời."""
    if not openrouter_client:
        return "⚠️ Lỗi: Client OpenRouter chưa được khởi tạo. Vui lòng kiểm tra lại token."
    
    try:
        completion = openrouter_client.chat.completions.create(
            model="openai/gpt-oss-120b:cerebras",
            messages=[
                {"role": "user", "content": prompt}
            ],
        )
        raw_reply = completion.choices[0].message.content.strip()
        
        # Deep Translator tự động dịch
        translated = translator.translate(raw_reply)
        
        return translated
    except Exception as e:
        return f"⚠️ Lỗi từ Hugging Face: {e}"

# --- 3. Các sự kiện Discord ---
@client.event
async def on_ready():
    print(f"🤖 Bot đã sẵn sàng: {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    async with message.channel.typing():
        reply = await ask_huggingface(message.content)
        
        # Chia tin nhắn thành các phần 4000 ký tự và gửi
        max_length = 4000
        if len(reply) > max_length:
            chunks = [reply[i:i + max_length] for i in range(0, len(reply), max_length)]
            for chunk in chunks:
                await message.channel.send(chunk)
        else:
            await message.channel.send(reply)

# Chạy bot
if __name__ == "__main__":
    client.run(DISCORD_TOKEN)
