import os
os.system('title 𝙬𝙞𝙣𝙙𝙤𝙬𝙨 𝙬𝙖𝙩𝙚𝙧𝙢𝙖𝙧𝙠 𝙧𝙚𝙢𝙤𝙫𝙚𝙧')
os.system('cls')

os.system('reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v PaintDesktopVersion /t REG_DWORD /d 0 /f')
print(f'Done! Restart your PC to apply the changes.')
os.system('pause >nul')
