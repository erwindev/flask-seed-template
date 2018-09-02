#!/usr/bin/env bash

source env.settings
python application.py db upgrade
python service.py
