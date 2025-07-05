import pandas as pd

# 50+ Real and Fake Indian headlines
headlines = [
    # ✅ Real headlines
    ("ISRO launches Aditya L1 mission", 1),
    ("PM Modi inaugurates Delhi-Mumbai Expressway", 1),
    ("India wins T20 World Cup final", 1),
    ("RBI keeps repo rate unchanged in June", 1),
    ("CBSE declares Class 10 board results", 1),
    ("Mumbai local train services restored after floods", 1),
    ("Karnataka announces free electricity scheme", 1),
    ("Delhi govt bans diesel autos from 2025", 1),
    ("Ayodhya Ram Mandir opens to public", 1),
    ("India launches Chandrayaan-3", 1),
    ("Gaganyaan human spaceflight mission announced", 1),
    ("India signs FTA with European Union", 1),
    ("Supreme Court upholds women's right to property", 1),
    ("Mumbai metro line 3 inaugurated", 1),
    ("NDA secures majority in Lok Sabha elections", 1),
    ("Telangana declares June 30 as public holiday", 1),
    ("Maharashtra records highest rainfall in June", 1),
    ("Bengaluru hosts Global Startup Summit", 1),
    ("India's first AI college launched in Pune", 1),
    ("Goa bans plastic below 75 microns", 1),

    # ❌ Fake headlines
    ("ISRO admits moon landing was fake", 0),
    ("Modi bans all smartphones in India", 0),
    ("India to cancel 2024 elections", 0),
    ("Delhi Metro running on solar balloons", 0),
    ("CBSE leaks all Class 12 exam papers", 0),
    ("India declares war on Sri Lanka", 0),
    ("New Parliament to be built on Mars", 0),
    ("Aditya L1 explodes mid-flight", 0),
    ("Mumbai local trains banned forever", 0),
    ("Rahul Gandhi joins NASA", 0),
    ("Chandrayaan-3 finds gold on the moon", 0),
    ("Indian army to replace soldiers with robots", 0),
    ("PM Modi resigns from politics", 0),
    ("India to ban all festivals next year", 0),
    ("Supreme Court disbanded", 0),
    ("All engineering colleges shut down", 0),
    ("Mumbai renamed as South London", 0),
    ("Petrol to be free in 2025", 0),
    ("India merges with Russia", 0),
    ("IPL replaced by World Kabaddi League", 0),
]

# Save to CSV
df = pd.DataFrame(headlines, columns=["text", "label"])
df.to_csv("extra_indian_headlines.csv", index=False)
print("✅ Created extra_indian_headlines.csv successfully!")
