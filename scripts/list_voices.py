import asyncio
import edge_tts

async def main():
    voices = await edge_tts.list_voices()
    vietnamese_voices = [v for v in voices if 'vi-VN' in v['Locale']]
    for v in vietnamese_voices:
        print(f"Name: {v['ShortName']}, Gender: {v['Gender']}")

if __name__ == "__main__":
    asyncio.run(main())
