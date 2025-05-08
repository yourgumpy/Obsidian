import subprocess
import datetime

def git_commit_push():
    # Get current date as commit message
    commit_message = datetime.datetime.now().strftime('%d-%b-%Y %H:%M')

    # Run git commands
    try:
        subprocess.run(["git", "add", "."], check=True)  # git add .
        subprocess.run(["git", "commit", "-m", commit_message], check=True)  # git commit
        subprocess.run(["git", "push", "origin", "master"], check=True)  # git push
        print(f"Successfully committed and pushed with message: {commit_message}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    git_commit_push()
