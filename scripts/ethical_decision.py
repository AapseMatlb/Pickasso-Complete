
def evaluate_decision(object_type):
    if object_type == "trash":
        return "Pick Immediately"
    elif object_type == "dangerous":
        return "Avoid and Announce"
    elif object_type == "personal":
        return "Seek Human Permission"
    else:
        return "No Action"
if __name__ == "__main__":
    print("[Decision] Decision for 'trash':", evaluate_decision("trash"))
