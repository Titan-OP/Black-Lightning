import asyncio
import os

from telethon import __version__ 
from userbot import ALIVE_NAME, TG_CHANNEL, TG_GRUP
from userbot.thunderconfig import Config
from userbot.utils import lightning_cmd, sudo_cmd

ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
if ALIVE_PIC is None:
    ALV_LIGHTNING = "https://telegra.ph/file/6f5a1f8f4559393b6ba65.mp4"
else:
    ALV_LIGHTNING = ALIVE_PIC


version = "4.5"
python_version = "3.8.5"

# Functions
def lightning_Read_time(seconds: int) -> str:
    count = 0
    kirsh = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            lol_hehehe, result = divmod(seconds, 60)
        else:
            lol_hehehe, result = divmod(seconds, 24)
        if seconds == 0 and lol_hehehe == 0:
            break
        time_list.append(int(result))
        seconds = int(lol_hehehe)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        kirsh += time_list.pop() + ", "

    time_list.reverse()
    kirsh += ":".join(time_list)

    return kirsh

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ℓιgнтηιηg υѕєя"

TG = str(TG_GRUP) if TG_GRUP else "Not  Yet😁😁"
TG_CHANN = str(TG_CHANNEL) if TG_CHANNEL else "Not Yet😁😁"


from userbot import CMD_LIST

lightning_cap = "**🔥| вℓα¢к ℓιgнтηιηg ιѕ σηℓιηє |🔥**\n\n"
lightning_cap += f"**『ℓιgнтηιηg'ѕ мαѕтєя』**   : {DEFAULTUSER}\n"
lightning_cap += f"{DEFAULTUSER}'s gяσυρ:   {TG}\n"  
lightning_cap += f"{DEFAULTUSER}'s ¢нαηηєℓ:   {TG_CHANN}\n\n"
lightning_cap += f"тєℓєтнση νєяѕιση:   {__version__}\n"
lightning_cap += "ρутнση νєяѕιση:    3.9.0\n"
lightning_cap += "✨ ℓιgнтηιηg ¢нαηηєℓ ✨:   [Jσιη](https://t.me/black_lightning_Channel)\n"
lightning_cap += "✨ ℓιgнтηιηg ѕυρρσят ✨:   [Jσιη](https://t.me/lightning_support_Group)\n"
lightning_cap += "¢σρуяιgнт: [KeinShin](https://github.com/KeinShin/) | [тє¢нησ ρяσ](https://telegram.me/DARK_DEVIL_OP) and [DEVS](https://github.com/KeinShin/Black-Lightning/graphs/contributors)"


@borg.on(lightning_cmd(pattern = r"alive"))
@borg.on(sudo_cmd(pattern = r"alive", allow_sudo=True))
async def lightning(alive):
    await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, ALV_LIGHTNING, caption=lightning_cap)
    await alive.delete()
