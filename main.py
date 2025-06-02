import subprocess

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
            
        return return_code
        
    except Exception as e:
        print(f"Error executing command: {e}")
        return 1

if __name__ == "__main__":
    # Example usage
    command = input("Enter command to run: ")
    run_command(command)
