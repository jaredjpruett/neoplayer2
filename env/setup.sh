#!/bin/bash

REPODIR="$HOME/Documents/Git/neoplayer"

# Install dependencies
apt update && apt upgrade -Y
apt install python-pip xvfb xserver-xephyr
pip install selenium pyvirtualdisplay

# Copy profile
profile="$HOME/.mozilla/firefox/neoplayer"
profiles="$HOME/.mozilla/firefox/profiles.ini"
if [[ -e "$profile" ]]; then
	[[ -e "${profile}.OLD" ]] && rm -rf "${profile}.OLD"
	mv "$profile" "${profile}.OLD"
fi
if [[ -e "$profiles" ]]; then
	[[ -e "${profiles}.OLD" ]] && rm -rf "${profiles}.OLD"
	mv "$profiles" "${profiles}.OLD"
fi
cp -R "$REPODIR/env/profile/neoplayer" "$profile"
cp "$REPODIR/env/profile/profiles.ini" "$profiles"
