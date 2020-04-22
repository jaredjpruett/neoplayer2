#!/bin/bash

repodir="<path>"
profile="$HOME/.mozilla/firefox/neoplayer"
profiles="$HOME/.mozilla/firefox/profiles.ini"

apt update && apt upgrade -Y && apt install python-pip xvfb xserver-xephyr && pip install selenium pyvirtualdisplay

if [[ -e "$profile" ]]; then
	[[ -e "${profile}.OLD" ]] && rm -rf "${profile}.OLD"
	mv "$profile" "${profile}.OLD"
fi
if [[ -e "$profiles" ]]; then
	[[ -e "${profiles}.OLD" ]] && "${profiles}.OLD"
	mv "$profiles" "${profiles}.OLD"
fi

cp -R "$repodir/env/profile/neoplayer" "$profile"
cp "$repodir/env/profile/profiles.ini" "$profiles"
