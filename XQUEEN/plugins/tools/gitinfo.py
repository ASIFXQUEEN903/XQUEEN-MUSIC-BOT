import aiohttp
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Replace XQUEEN with your actual app instance if different
from XQUEEN import app

@app.on_message(filters.command(["github", "git"]))
async def github(_, message):
    if len(message.command) != 2:
        return await message.reply_text("/git ASIFXQUEEN903")

    username = message.text.split(None, 1)[1]
    URL = f'https://api.github.com/users/{username}'

    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("❌ GitHub user not found (404).")

            result = await request.json()

            try:
                url = result['html_url']
                name = result.get('name', 'N/A')
                company = result.get('company', 'N/A')
                bio = result.get('bio', 'N/A')
                created_at = result.get('created_at', 'N/A')
                avatar_url = result['avatar_url']
                blog = result.get('blog', 'N/A')
                location = result.get('location', 'N/A')
                repositories = result.get('public_repos', 0)
                followers = result.get('followers', 0)
                following = result.get('following', 0)

                caption = f"""**ɢɪᴛʜᴜʙ ɪɴғᴏ ᴏғ {name}**
                
**ᴜsᴇʀɴᴀᴍᴇ:** `{username}`
**ʙɪᴏ:** `{bio}`
**ʟɪɴᴋ:** [GitHub]({url})
**ᴄᴏᴍᴩᴀɴʏ:** `{company}`
**ᴄʀᴇᴀᴛᴇᴅ ᴏɴ:** `{created_at}`
**ʀᴇᴩᴏsɪᴛᴏʀɪᴇs:** `{repositories}`
**ʙʟᴏɢ:** `{blog}`
**ʟᴏᴄᴀᴛɪᴏɴ:** `{location}`
**ғᴏʟʟᴏᴡᴇʀs:** `{followers}`
**ғᴏʟʟᴏᴡɪɴɢ:** `{following}`"""
            except Exception as e:
                return await message.reply_text("❌ Error while processing GitHub data.")

    close_button = InlineKeyboardButton("❌ Close", callback_data="close")
    reply_markup = InlineKeyboardMarkup([[close_button]])

    await message.reply_photo(photo=avatar_url, caption=caption, reply_markup=reply_markup)
