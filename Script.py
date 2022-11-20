class script(object):
    START_TXT = """<b>🧤Helo {}, I'm <a href=https://telegram.me/{}>{}</a> &amp; I Can Provide You Any Movies &amp; Series</b> 😇"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """<i><b><u>AutoFilter + UrlShortner Bot</u></b>

🔅 Want An </i><i><b>'AutoFilter + UrlShortner Bot'</b> Like Me For Your Group &amp; Earn Money Using It?

📲 </i><i><b>Contact »</b> </i><i>@MrKrazyBot</i>"""    
    SOURCE_TXT = """<i><b><u>AutoFilter + UrlShortner Bot</u></b>

🔅 Want An </i><i><b>'AutoFilter + UrlShortner Bot'</b> Like Me For Your Group &amp; Earn Money Using It?

📲 </i><i><b>Contact »</b> </i><i>@MrKrazyBot</i>"""    
    MANUELFILTER_TXT = """Help: <b>FILTERS »</b>

» <b>Filter is A Feature Where Users can Set Automated Reply to a Specific Word</b>

<b>Important Notes:</b>
1.<i> I Have To Be Admin </i>
2.<i> Only admins can add Filters in Chat</i>
3.<i> Buttons have a limit of 64 Characters</i>

<b>Commands and Usage:</b>
• <i> /filter - Add a Filter</i>
• <i> /filters - List of All Filters</i>
• <i> /del - Delete a Filter</i>
• <i> /delall - Delete All Filters</i> """
    BUTTON_TXT = """Help: <b>BUTTONS »</b>

» Supports both url and alert inline buttons.

<b>NOTE:</b>
1. <i>Telegram will not allows you to send buttons without any content, so content is mandatory.</i>
2. <i>Supports buttons with any telegram media type</i>
3. <i>Buttons should be properly parsed as markdown format</i>

<b>URL Buttons:</b>
<code>[Button Text](buttonurl:https://t.me/HeroFlixbot)</code>

<b>Alert Buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>AUTO FILTER »</b>

Add Me In Your Group as Admin & I Will Provide Any Movie, Series, Animation etc.,"""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. <i>Only Admins Can Add Connection</i>
2. <i>Send <code>/connect</code> To Connect Me to Your PM</i>

<b>Commands and Usage:</b>
•<i> /connect  - Connect a Chat to your PM</i>
•<i> /disconnect  - Disconnect from a Chat</i>
•<i> /connections - List Of All Connections</i>"""
    EXTRAMOD_TXT = """Help: <b>Extra Features of Me »</b>

<b>Commands and Usage:</b>
•<i> /id - Get ID Of A User</i>
•<i> /info  - Get Info About a User</i>
•<i> /imdb  - Get Movie/Series Info from IMDb</i>"""
    ADMIN_TXT = """Help: <b>ADMIN MODS »</b>

<b>NOTE:</b>
This Works Only For Admins!

<b>Commands and Usage:</b>
•<i> /stats - Get Status of DataBase</i>
•<i> /delete - Delete A File</i>
•<i> /users - List of My Users </i>
•<i> /chats - Get List Of My Chats </i>
•<i> /leave  - Leave from a chat</i>
•<i> /disable  - Disable a Chat</i>
•<i> /ban  - Ban a User</i>
•<i> /unban  - Unban a User</i>
•<i> /channel - List of All Connected Channels</i>
•<i> /broadcast - Broadcast a Message to All Users</i>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: {}
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: {}
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: {}
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: {} 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: {} 𝙼𝚒𝙱"""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
