#!/bin/bash
# This script takes in URL, sends a request to URL, and also displays the size of the body of the response
curl -s "$1" | wc -c
