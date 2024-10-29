import subprocess

# Replace 'your_command' with the command you want to execute
result = subprocess.run(['python','./simple_HTTP_server/back-end/login.py'], capture_output=True, text=True)

# Output the result
print("Exit code:", result.returncode)