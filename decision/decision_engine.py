import requests
import time

CONVEX_API_URL = "https://<your-convex-app-url>/api/updateStatus"

def update_hmi_status(task, reason, battery="100%"):
    payload = {
        "task": task,
        "reason": reason,
        "battery": battery
    }
    try:
        response = requests.post(CONVEX_API_URL, json=payload)
        if response.status_code == 200:
            print(f"[HMI Updated]: {task} | Reason: {reason}")
        else:
            print(f"[HMI Update Failed]: Status Code {response.status_code}")
    except Exception as e:
        print(f"[HMI Update Error]: {e}")

def evaluate_decision(object_type, human_nearby=False, human_response=None, gesture=None):
    if human_nearby and object_type == "personal":
        update_hmi_status("Awaiting Permission", "Personal item detected. Asking human.")
        if human_response in ["yes", "thumbs up"] or gesture == "thumbs up":
            return "Leave the item"
        else:
            return "Pick after timeout"
    elif object_type == "trash":
        return "Pick Immediately"
    elif object_type == "dangerous":
        update_hmi_status("Avoiding", "Dangerous item detected.")
        return "Avoid and Announce"
    else:
        return "Ignore"

if __name__ == "__main__":
    # Example simulation
    print("[Decision] Trash:", evaluate_decision("trash"))
    time.sleep(1)
    print("[Decision] Personal Item, Human Nearby, Response 'yes':", evaluate_decision("personal", True, "yes"))
    time.sleep(1)
    print("[Decision] Dangerous Item:", evaluate_decision("dangerous"))
