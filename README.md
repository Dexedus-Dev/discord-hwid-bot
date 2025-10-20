# 🔰 Nextcord Bot Template + Pastebin UI System

> 🧩 บอท Discord สำหรับจัดการข้อมูลใน Pastebin ได้โดยตรง  
> พร้อมระบบ UI ปุ่ม / Modal ใช้งานง่าย แค่ตั้งค่า `config.json` ก็พร้อมใช้งาน

---

## ✨ ฟีเจอร์
- ✅ เพิ่มหรือลบข้อมูลใน Pastebin ผ่าน Discord โดยไม่ต้องเปิดเว็บ
- ✅ มีปุ่ม UI (Add / Remove / View)
- ✅ มี Modal (กล่องกรอกข้อความ)
- ✅ ระบบ Embed สวยงาม ดูง่าย
- ✅ Template พร้อมแจกหรือปรับใช้ในโปรเจกต์ของคุณ

---

## ⚙️ การตั้งค่าเริ่มต้น

### 1️⃣ สร้างไฟล์ `config.json`
สร้างไฟล์ชื่อ `config.json` แล้วใส่ค่าตามนี้:

```json
{
  "token": "YOUR_DISCORD_TOKEN",
  "guild_id": 123456789012345678,
  "channel_id": 987654321098765432,
  "pastebincode": "abcd1234",
  "pastebin_cookie": "PASTEBIN_LOGIN_COOKIE"
}
```

| คีย์ | คำอธิบาย |
|------|------------|
| `token` | Token ของ Discord Bot |
| `guild_id` | ID เซิร์ฟเวอร์ Discord ของคุณ |
| `channel_id` | ช่องที่บอทจะส่ง UI ปุ่ม |
| `pastebincode` | รหัส Pastebin เช่น `abcd1234` จากลิงก์ `https://pastebin.com/abcd1234` |
| `pastebin_cookie` | ค่า Cookie `_identity-frontend` จาก Pastebin |

---

## 🍪 วิธีนำค่า `_identity-frontend` จาก Pastebin

> ⚠️ จำเป็นต้องล็อกอินบัญชี Pastebin ก่อนถึงจะได้ Cookie นี้

### ✅ ขั้นตอน (บน Google Chrome / Edge / Firefox)

1. เข้าสู่ระบบ Pastebin: [https://pastebin.com/login](https://pastebin.com/login)
2. หลังจากล็อกอินแล้ว ให้กด **F12** เพื่อเปิด **DevTools**
3. ไปที่แท็บ **Application** (หรือ **Storage** บางเบราว์เซอร์)
4. เลือกเมนูด้านซ้าย **Cookies → https://pastebin.com**
5. หาแถวที่ชื่อว่า `_identity-frontend`
6. คัดลอกค่าจากคอลัมน์ **Value**
7. นำค่าที่ได้ใส่ลงใน `pastebin_cookie` ในไฟล์ `config.json`

> 🧠 ตัวอย่างค่า Cookie  
> `_identity-frontend=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...`

---

## 🚀 การรันบอท

1. ติดตั้งไลบรารีที่จำเป็น:
   ```bash
   pip install nextcord pastebin requests
   ```

2. รันบอท:
   ```bash
   python main.py
   ```

3. บอทจะส่ง Embed + ปุ่ม UI ไปยังช่องที่กำหนดใน `config.json`

---

## 🧩 การใช้งาน

| ปุ่ม | หน้าที่ |
|------|----------|
| ➕ **Add** | เปิด Modal สำหรับเพิ่มข้อความใหม่ลงใน Pastebin |
| 🗑️ **Remove** | เปิด Modal สำหรับลบข้อความออกจาก Pastebin |
| 📜 **View** | แสดงข้อมูลทั้งหมดจาก Pastebin ใน Embed |

---

## 🧠 เคล็ดลับเพิ่มเติม
- หากต้องการให้บอทส่ง Embed ซ้ำ (ในกรณีเผลอลบข้อความ) ให้พิมพ์คำสั่ง `/reload` หรือรันบอทใหม่
- สามารถใช้ Pastebin เดียวกันกับหลายบอทได้ (หากแชร์ Cookie)

---

## 🪪 License

Distributed under the MIT License.  
สร้างโดย [Dexedus Dev](https://github.com/Dexedus-Dev)

---

> 💬 หากเจอปัญหา หรืออยากให้เพิ่มฟีเจอร์อื่น ๆ  
> สามารถเปิด Issue หรือ Pull Request ได้ที่ GitHub Repo ของคุณ
