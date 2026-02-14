import os
import random
import time
from collections import Counter
from colorama import Fore, Style, init

init(autoreset=True)

# --- AESTHETICS ---
CYAN = Fore.CYAN
BLUE = Fore.BLUE
RED = Fore.RED
YELLOW = Fore.YELLOW
WHITE = Fore.WHITE

ART = f"""
{CYAN}   ██████╗██╗   ██╗ █████╗ ███╗   ██╗ ██████╗ ████████╗██╗ ██████╗
  ██╔════╝╚██╗ ██╔╝██╔══██╗████╗  ██║██╔═══██╗╚══██╔══╝██║██╔════╝
  ██║      ╚████╔╝ ███████║██╔██╗ ██║██║   ██║   ██║   ██║██║     
  ██║       ╚██╔╝  ██╔══██║██║╚██╗██║██║   ██║   ██║   ██║██║     
  ╚██████╗   ██║   ██║  ██║██║ ╚████║╚██████╔╝   ██║   ██║╚██████╗
   ╚═════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚═╝ ╚═════╝
{BLUE}  [= CYANOTIC COMBOMAKER =]  @CyanLinks  [= RAW DATA. NO BULLSHIT. =]
"""

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class CyanoticEngine:
    def __init__(self):
        self.current_file = ""

    def load_file(self):
        path = input(f"{YELLOW}Path to .txt: ").strip('"').strip("'")
        if os.path.exists(path):
            self.current_file = path
            print(f"{CYAN}[+] File loaded: {os.path.basename(path)}")
        else:
            print(f"{RED}[!] File not found!")
        time.sleep(1)

    # 1. Domain Sorter & Analytics
    def domain_sorter(self):
        if not self.current_file: return
        out_dir = "sorted_domains"
        if not os.path.exists(out_dir): os.mkdir(out_dir)
        domains = []
        print(f"{CYAN}[*] Processing domains...")
        with open(self.current_file, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                if ':' in line:
                    email = line.split(':')[0]
                    domain = email.split('@')[-1].lower() if '@' in email else "invalid"
                    domains.append(domain)
                    with open(f"{out_dir}/{domain}.txt", 'a', encoding='utf-8') as out:
                        out.write(line)
        
        stats = Counter(domains)
        total = sum(stats.values())
        print(f"\n{CYAN}--- TOP DOMAINS ---")
        for dom, count in stats.most_common(5):
            print(f"{WHITE}{dom}: {(count/total)*100:.1f}% ({count})")
        input(f"\n{BLUE}Done. Saved in /sorted_domains. Enter...")

    # 2. De-Duplicator & Sanitizer
    def sanitizer(self):
        if not self.current_file: return
        print(f"{CYAN}[*] Deep cleaning...")
        seen = set()
        count = 0
        with open("cleaned_output.txt", 'w', encoding='utf-8') as out:
            with open(self.current_file, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    line = line.strip()
                    if ':' in line and line not in seen:
                        parts = line.split(':')
                        if len(parts[0]) > 4 and len(parts[1]) > 3: # Basic valid check
                            out.write(line + '\n')
                            seen.add(line)
                            count += 1
        print(f"{CYAN}[+] Duplicates & Trash removed. Saved: {count}")
        time.sleep(1)

    # 3. Anarchy Mixer (Shuffle)
    def mixer(self):
        if not self.current_file: return
        print(f"{CYAN}[*] Shuffling rows for anti-pattern protection...")
        with open(self.current_file, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        random.shuffle(lines)
        with open("shuffled_output.txt", 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print(f"{CYAN}[+] Done. Saved as shuffled_output.txt")
        time.sleep(1)

    # 4. Geo-Targeter
    def geo_extractor(self):
        if not self.current_file: return
        tld = input(f"{YELLOW}Enter TLD (e.g. .de, .fr, .it): ").lower()
        count = 0
        with open(f"geo_{tld}.txt", 'w', encoding='utf-8') as out:
            with open(self.current_file, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    if f"{tld}:" in line.lower().split('@')[-1]:
                        out.write(line)
                        count += 1
        print(f"{CYAN}[+] Extracted {count} rows.")
        time.sleep(1)

def main():
    engine = CyanoticEngine()
    while True:
        clear()
        print(ART)
        print(f"{WHITE}Target: {YELLOW}{os.path.basename(engine.current_file) if engine.current_file else 'NONE'}")
        print(f"""
{CYAN}[1] {WHITE}LOAD DATA
{CYAN}[2] {WHITE}DOMAIN SORTER + STATS
{CYAN}[3] {WHITE}CLEAN TRASH + DEDUP
{CYAN}[4] {WHITE}ANARCHY MIXER (SHUFFLE)
{CYAN}[5] {WHITE}GEO-EXTRACTOR (TLD)
{RED}[0] {WHITE}EXIT
        """)
        choice = input(f"{BLUE}$> {WHITE}")
        if choice == '1': engine.load_file()
        elif choice == '2': engine.domain_sorter()
        elif choice == '3': engine.sanitizer()
        elif choice == '4': engine.mixer()
        elif choice == '5': engine.geo_extractor()
        elif choice == '0': break

if __name__ == "__main__":
    main()
