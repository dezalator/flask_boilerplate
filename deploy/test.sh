#!/usr/bin/env bash
CONNECTION="alex@127.0.0.1"

ssh -A "$CONNECTION" "cd flask_boilerplate
        git pull --ff-only
        make up"