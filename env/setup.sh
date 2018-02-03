#!/bin/bash

REPODIR=""

# Install pip and xvfb
sudo apt-get install python-pip xvfb xserver-xephyr

# Install pip packages
sudo pip install selenium pyvirtualdisplay

# Copy profile
profile="$HOME/.mozilla/firefox/neoplayer"
profiles="$HOME/.mozilla/firefox/profiles.ini"
if [[ -e "$profile" ]]; then
	if [[ -e "${profile}.OLD" ]]; then
		rm -rf "${profile}.OLD"
	fi
	mv "$profile" "${profile}.OLD"
fi
if [[ -e "$profiles" ]]; then
	if [[ -e "${profiles}.OLD" ]]; then
		rm "${profiles}.OLD"
	fi
	mv "$profiles" "${profiles}.OLD"
fi
cp -R "$REPODIR/env/profile/neoplayer" "$profile"
cp "$REPODIR/env/profile/profiles.ini" "$profiles"
