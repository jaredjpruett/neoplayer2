#!/bin/bash

function requireTmux() {
    if [[ -z ${TMUX+x} ]]; then
        echo "Player must be run from within tmux session." 1>&2
        exit 1
    fi
}

#requireTmux

python -B main.py
rm -f geckodriver.log
