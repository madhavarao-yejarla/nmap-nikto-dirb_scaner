import nmap
import subprocess
from datetime import date

# Read target IP address from file
with open("targets.txt", "r") as f:
    targets = [line.strip() for line in f.readlines()]

ports = "0-65535"
output_dir = "/home/attacker"

# Create nmap PortScanner object and perform scan for each target
for target in targets:
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments="-sV -p " + ports)

    # Save XML output to file
    try:
        with open(output_dir + "/" + target + "_" + str(date.today()) + ".xml", "w") as f:
            f.write(nm.get_nmap_last_output().decode())
        print("Scan results saved in " + output_dir + "/" + target + "_" + str(date.today()) + ".xml")
    except Exception as e:
        print(f"Error saving scan results for {target}: {e}")

    # Run Nikto scan for each target
    try:
        nikto_output = subprocess.check_output(["nikto", "-h", target])
        with open(output_dir + "/" + target + "_" + str(date.today()) + ".txt", "w") as f:
            f.write(nikto_output.decode())
        print("Nikto scan results saved in " + output_dir + "/" + target + "_" + str(date.today()) + ".txt")
    except Exception as e:
        print(f"Error running Nikto scan for {target}: {e}")

