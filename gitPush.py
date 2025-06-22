import subprocess
import datetime

def git_pull_commit_push():
    # Generate commit message with current date and time
    commit_message = datetime.datetime.now().strftime('%d-%b-%Y %H:%M')

    try:
        # Step 1: Pull latest changes from origin/master
        subprocess.run(["git", "pull", "origin", "master"], check=True)
        print("Pulled latest changes from origin/master.")

        # Step 2: Add changes
        subprocess.run(["git", "add", "."], check=True)

        # Step 3: Commit with timestamp message
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Step 4: Push to origin/master
        subprocess.run(["git", "push", "-u", "origin", "master"], check=True)

        print(f"Successfully committed and pushed with message: {commit_message}")

    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {e}")

if __name__ == "__main__":
    git_pull_commit_push()
