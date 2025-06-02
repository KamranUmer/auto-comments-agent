import subprocess
# yes it works for commit message but toke some time to show on contribution graph
# it works but need to do it auto matically via agent
# one another thing to be add it should check my work dally that it should be automatically commits my data every day
# and there will be check condition if no changes so the bot will write something and then commit it
# auto commit 02/jun/025 01

def run_command(command):
    try:
        # Run the command and capture output
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        
        # Get return code
        return_code = process.returncode
        
        # Print output
        if stdout:
            print("Output:")
            print(stdout)
        
        # Print errors if any
        if stderr:
            print("Errors:")
            print(stderr)
            
        return return_code, stdout, stderr
        
    except Exception as e:
        print(f"Error executing command: {e}")
        return 1, "", str(e)

def auto_git_commit(commit_message="Auto commit: changes detected"):
    """
    Check if there are any changes to commit in the git repository.
    If yes, commit those changes with the provided commit message.
    """
    # Show git status before operations
    print("Current git status:")
    run_command("git status")
    
    # Check git status programmatically
    status_code, status_output, _ = run_command("git status --porcelain")
    
    if status_code != 0:
        print("Error checking git status. Make sure you're in a git repository.")
        return False
    
    # If there are changes to commit
    if status_output.strip():
        print(f"Changes detected. Staging all changes with 'git add .'")
        
        # Stage all changes
        stage_code, _, _ = run_command("git add .")
        if stage_code != 0:
            print("Error staging changes.")
            return False
        
        # Show status after staging
        print("\nStatus after staging:")
        run_command("git status")
        
        # Commit changes
        print(f"\nCommitting with message: '{commit_message}'")
        commit_code, _, _ = run_command(f'git commit -m "{commit_message}"')
        if commit_code != 0:
            print("Error committing changes.")
            return False
        
        # Show status after commit
        print("\nStatus after commit:")
        run_command("git status")
        
        print("Changes successfully committed.")
        return True
    else:
        print("No changes to commit.")
        return False

if __name__ == "__main__":
    # Example usage
    choice = input("What do you want to do? (1: Run command, 2: Auto git commit): ")
    
    if choice == "1":
        command = input("Enter command to run: ")
        run_command(command)
    elif choice == "2":
        message = input("Enter commit message (or press Enter for default): ")
        if message:
            auto_git_commit(message)
        else:
            auto_git_commit()
    else:
        print("Invalid choice.")
