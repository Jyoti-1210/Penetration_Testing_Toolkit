# Penetration_Testing_Toolkit
This modular toolkit is designed for ethical hacking and security testing. 

Key features include:  

Port Scanner: Discover open ports on target systems.  

Brute-Force Attack Module: Automate login attacks using a dictionary-based approach.

# 🧰 Building Toolkit

Port Scanner Module:

Utilize Python's socket library to scan for open ports.

Implement threading to enhance scanning speed.

Brute-Force Module:

Employ the requests library to send HTTP requests for login attempts.

Incorporate a dictionary attack mechanism using common password lists.

# 🛠️ Project Structure
Penetration_Testing_Toolkit/
├── main.py

├── port_scanner.py

├── brute_forcer.py

├── utils.py

└── README.md

# ✅ How to Use

1. Install dependencies

   pip install tqdm paramiko
   
2. Port Scan
   
   python main.py scan 192.168.1.5 --start 20 --end 100
   
3. Brute Force
   
   python main.py brute 192.168.1.5 root passwords.txt
 

