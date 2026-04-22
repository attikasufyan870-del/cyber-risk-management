# ============================================
#  AS | Attika Sufyan
#  Cybersecurity Student
#  GitHub: github.com/attikasufyan870-del
#  Course: EC-Council Cybersecurity
#  Topic: Risk Management - Chapter 2
#  Date: April 2026
# ============================================

# Cyber Risk Assessment Tool

def assess_risk(asset, threat, vulnerability):
    print(f"\n🔍 Risk Assessment for: {asset}")
    print(f"⚠️  Threat: {threat}")
    print(f"🔓 Vulnerability: {vulnerability}")
    
    # Risk Score
    print("\n📊 Risk Elements:")
    print("1. Asset value — kitna important hai?")
    print("2. Threat level — kitna dangerous hai?")
    print("3. Vulnerability — kitna exposed hai?")
    
    score = int(input("\nRisk Score do (1-10): "))
    
    if score <= 3:
        print("🟢 LOW RISK — Theek hai")
    elif score <= 6:
        print("🟡 MEDIUM RISK — Dhyan do")
    else:
        print("🔴 HIGH RISK — Foran action lo!")

# Main Program
print("=== Cyber Risk Assessment Tool ===")
asset = input("Asset ka naam likho (e.g., Database): ")
threat = input("Threat kya hai (e.g., Hacking): ")
vuln = input("Vulnerability kya hai (e.g., Weak Password): ")

assess_risk(asset, threat, vuln)
