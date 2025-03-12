import requests


def track_ip(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()

        print(f"📌 IP Address: {data.get('ip', 'N/A')}")
        print(f"🌍 Country: {data.get('country', 'N/A')}")
        print(f"🏙 City: {data.get('city', 'N/A')}")
        print(f"📍 Region: {data.get('region', 'N/A')}")
        print(f"🌎 Location (Lat, Lon): {data.get('loc', 'N/A')}")
        print(f"🖥 ISP: {data.get('org', 'N/A')}")
        print(f"🕛 Timezone: {data.get('timezone', 'N/A')}")
        print(f"🔗 Network: {data.get('network', 'N/A')}")

    except Exception as e:
        print("🚨 Error fetching data:", e)


# 🔹 Track an IP address (Replace with any IP)
ip_address = input("🔎 Enter IP Address: ")
track_ip(ip_address)
