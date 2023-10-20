#! /bin/bash
exec syncthing --no-browser &
rsync -au --partial ~/Documents/Obsidian ~/.backup/ &   # Backup Obsidian Vault


exec  sxhkd &
