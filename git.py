#!/bin/bash

# --- CONFIGURATION ---
GITHUB_USER=Leonydis139
REPO_NAME=probable-journey
REPO_URL=https://github.com/Leonydis137/probable-journey.git
COMMIT_MSG=Initial commit of probable-journey
# ----------------------

# Step 1: Go into the folder
cd autonomous_ai || { echo "Folder 'autonomous_ai' not found."; exit 1; }

# Step 2: Initialize git
git init

# Step 3: Add all files
git add .

# Step 4: Commit
git commit -m "$COMMIT_MSG"

# Step 5: Add GitHub remote
git remote add origin "probable-journey"

# Step 6: Rename default branch and push
git branch -M main
git push -u origin main
