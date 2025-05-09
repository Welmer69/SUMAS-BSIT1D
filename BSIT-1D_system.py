# SUMAS: Smart Utility Monitor and Alert System

import time

utility_status = {
    "electricity": "Normal",
    "water": "Normal"
}

outage_reports = []

def report_outage():
    print("\n--- Report an Outage ---")
    name = input("Your name: ")
    location = input("Your location: ")
    utility = input("Type of outage (electricity/water): ").lower()
    if utility not in ["electricity", "water"]:
        print("Invalid utility type.")
        return
    note = input("Description (optional): ")

    report = {
        "name": name,
        "location": location,
        "utility": utility,
        "note": note,
        "time": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    outage_reports.append(report)
    print("Outage reported successfully!\n")

def view_reports():
    print("\n--- Community Outage Reports ---")
    if not outage_reports:
        print("No outage reports yet.\n")
        return
    for i, report in enumerate(outage_reports, 1):
        print(f"{i}. {report['time']} - {report['utility'].title()} outage at {report['location']} by {report['name']}")
        if report['note']:
            print(f"   Note: {report['note']}")
    print()

def broadcast_alert():
    print("\n--- Broadcast Utility Alert ---")
    utility = input("Utility to update (electricity/water): ").lower()
    if utility not in ["electricity", "water"]:
        print("Invalid utility type.")
        return
    status = input(f"Enter new status for {utility}: ")
    utility_status[utility] = status
    print(f"{utility.title()} status updated to: {status}\n")

def view_utility_status():
    print("\n--- Real-Time Utility Status ---")
    for utility, status in utility_status.items():
        print(f"{utility.title()}: {status}")
    print()

def main():
    while True:
        print("=== SUMAS: Smart Utility Monitor and Alert System ===")
        print("[1] Report an Outage")
        print("[2] View Outage Reports (Admin)")
        print("[3] Broadcast Utility Alert (Admin)")
        print("[4] View Real-Time Utility Status")
        print("[5] Exit")
        choice = input("Select an option: ")

        if choice == "1":
            report_outage()
        elif choice == "2":
            view_reports()
        elif choice == "3":
            broadcast_alert()
        elif choice == "4":
            view_utility_status()
        elif choice == "5":
            print("Exiting SUMAS. Stay safe!")
            break
        else:
            print("Invalid choice. Try again.\n")



main()