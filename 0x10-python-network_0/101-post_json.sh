#!/bin/bash
# Script that sends a JSON POST request to a URL
curl -s -X POST -d @"$2" -H "Content-Type: application/json" "$1"
