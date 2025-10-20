# ============================================================
# 🔰 Nextcord Bot Template + Pastebin UI System
# ============================================================
# ✅ ใช้งานง่าย: แก้แค่ config.json ก็รันได้เลย
# ✅ มี UI ปุ่ม (Add / Remove / View)
# ✅ มี Modal (กล่องป้อนข้อความ)
# ✅ เขียนเป็น Template พร้อมคอมเมนต์ภาษาไทยครบ
# ============================================================

import nextcord
from nextcord.ext import commands
import requests
import pastebin
import json
import asyncio

# ============================================================
# ⚙️ โหลดข้อมูลจาก config.json
# ============================================================
# ตัวอย่าง config.json
# {
#   "token": "YOUR_DISCORD_TOKEN",
#   "guild_id": 123456789012345678,
#   "channel_id": 987654321098765432,
#   "pastebincode": "abcd1234",
#   "pastebin_cookie": "PASTEBIN_LOGIN_COOKIE"
# }

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

TOKEN = config["token"]
GUILD_ID = config["guild_id"]
CHANNEL_ID = config["channel_id"]
PASTEBIN_CODE = config["pastebincode"]
PASTEBIN_COOKIE = config["pastebin_cookie"]

# เข้าสู่ระบบ Pastebin API
api = pastebin.login(PASTEBIN_COOKIE)


# ============================================================
# 🧩 Modal: สำหรับเพิ่มข้อมูลใน Pastebin
# ============================================================
class AddModal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(title="➕ Add Line to Pastebin")

        self.text_input = nextcord.ui.TextInput(
            label="ใส่ข้อความที่จะเพิ่ม",
            placeholder="เช่น HWID หรือข้อความที่ต้องการบันทึก",
            max_length=1000
        )
        self.add_item(self.text_input)

    async def callback(self, interaction: nextcord.Interaction):
        new_text = self.text_input.value
        old_content = requests.get(f"https://pastebin.com/raw/{PASTEBIN_CODE}").text
        api.edit(PASTEBIN_CODE, old_content + "\n" + new_text)

        embed = nextcord.Embed(
            title="✅ เพิ่มข้อมูลเรียบร้อย!",
            description=f"เพิ่มข้อความ: ```{new_text}```",
            color=0x2ecc71
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)


# ============================================================
# 🧩 Modal: สำหรับลบข้อมูลใน Pastebin
# ============================================================
class RemoveModal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(title="🗑️ Remove Line from Pastebin")

        self.text_input = nextcord.ui.TextInput(
            label="ใส่ข้อความที่จะลบออก",
            placeholder="เช่น HWID หรือข้อความที่ต้องการลบ",
            max_length=1000
        )
        self.add_item(self.text_input)

    async def callback(self, interaction: nextcord.Interaction):
        remove_text = self.text_input.value
        content = requests.get(f"https://pastebin.com/raw/{PASTEBIN_CODE}").text
        updated = content.replace(remove_text, "")
        api.edit(PASTEBIN_CODE, updated)

        embed = nextcord.Embed(
            title="🧹 ลบข้อมูลเรียบร้อย!",
            description=f"ลบข้อความ: ```{remove_text}```",
            color=0xe74c3c
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)


# ============================================================
# 🧩 View (UI ปุ่ม)
# ============================================================
class PastebinView(nextcord.ui.View):
    """View แสดงปุ่มควบคุม Pastebin"""
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(label="➕ Add", style=nextcord.ButtonStyle.green, custom_id="add_button")
    async def add_button(self, button, interaction):
        await interaction.response.send_modal(AddModal())

    @nextcord.ui.button(label="🗑️ Remove", style=nextcord.ButtonStyle.red, custom_id="remove_button")
    async def remove_button(self, button, interaction):
        await interaction.response.send_modal(RemoveModal())

    @nextcord.ui.button(label="📜 View", style=nextcord.ButtonStyle.blurple, custom_id="view_button")
    async def view_button(self, button, interaction):
        try:
            data = requests.get(f"https://pastebin.com/raw/{PASTEBIN_CODE}").text
            embed = nextcord.Embed(
                title="📜 Pastebin Content",
                description=f"```{data[:1900]}```",
                color=0x3498db
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"❌ เกิดข้อผิดพลาด: {e}", ephemeral=True)


# ============================================================
# 🤖 ตัวหลักของบอท
# ============================================================
class PastebinBot(commands.Bot):
    def __init__(self):
        super().__init__(intents=nextcord.Intents.default())

    async def on_ready(self):
        print(f"✅ บอทล็อกอินสำเร็จในชื่อ: {self.user}")
        await self.change_presence(activity=nextcord.Game(name="📦 Pastebin Control"))

        # ส่ง UI ปุ่มไปยังช่องที่ตั้งไว้ใน config.json
        channel = self.get_channel(CHANNEL_ID)
        if channel:
            embed = nextcord.Embed(
                title="🔧 ระบบจัดการ Pastebin",
                description="ใช้ปุ่มด้านล่างเพื่อเพิ่ม / ลบ / ดูข้อมูล",
                color=0x2ecc71
            )
            await channel.send(embed=embed, view=PastebinView())


# ============================================================
# 🚀 เริ่มรันบอท
# ============================================================
bot = PastebinBot()
bot.run(TOKEN)