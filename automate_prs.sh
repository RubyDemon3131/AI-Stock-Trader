#!/bin/bash

# Number of times to create a pull request
n=1024  # Change this to the desired number of merges

# Ensure we're starting from the erikstrom branch
git checkout erikstrom
git pull origin erikstrom  # Fetch the latest changes from the remote erikstrom

for ((i=1; i<=n; i++))
do
    # Create a new branch
    branch_name="branch-$i"
    
    # Delete the branch if it exists
    git branch -D $branch_name 2>/dev/null || true

    # Create a new branch from erikstrom
    git checkout -b $branch_name erikstrom

    # Make a dummy change
    echo "Dummy change number $i" >> README.md

    # Stage and commit the changes
    git add README.md
    git commit -m "Add dummy change number $i"

    # Push the branch to GitHub
    git push origin $branch_name

    # Create the pull request using GitHub CLI
    gh pr create --base erikstrom --head $branch_name --title "Dummy Change $i" --body "This is a dummy change for the shark badge."
    if [ $? -ne 0 ]; then
        echo "Failed to create pull request for $branch_name. Exiting."
        exit 1
    fi

    # Merge the pull request using GitHub CLI
    gh pr merge --merge $branch_name
    if [ $? -ne 0 ]; then
        echo "Failed to merge pull request for $branch_name. Exiting."
        exit 1
    fi

    # Switch back to the erikstrom branch
    git checkout erikstrom

    # Fetch the latest changes after merging
    git pull origin erikstrom

    # Delete the branch locally and remotely
    git branch -D $branch_name
    git push origin --delete $branch_name
done
