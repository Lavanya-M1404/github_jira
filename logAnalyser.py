##################
#####
##
#python prgm to analyse the logs
##
#####
#################

import re

def analyze_logs(log_file, output_file):
    with open(log_file, 'r') as file:
        logs = file.readlines()
    
    errors = [log.strip() for log in logs if "[ERROR]" in log]

    with open(output_file, 'w') as out_file:
        for error in errors:
            out_file.write(error + "\n")

    print(f"✅ Extracted {len(errors)} errors. Saved to {output_file}")

# Run the function
log_file = "app.log"
output_file = "error_logs.txt"
analyze_logs(log_file, output_file)



