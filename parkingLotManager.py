def parkingLotManager(n, events):
    lot = set()
    for event in events:
        action, plate = event.split()
        if action == "enter":
            if len(lot) < n:
                lot.add(plate)
        elif action == "exit":
            lot.discard(plate)  # no error if not present
    return list(lot)

# Example
events = ["enter A123", "enter B456", "enter C789", "exit A123", "enter D111"]
print(parkingLotManager(2, events))  # ['B456', 'D111']
