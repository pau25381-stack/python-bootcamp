invited = {"Ana", "Ben", "Carlo", "Dani"}
attended = {"Ben", "Carlo", "Ely"}

# TODO: Who are all the involved members?
print("Involved Members:", invited | attended)

# TODO: Who was absent?
print("Absent:", invited - attended)

# TODO: Who gatecrashed?
print("Not enrolled but attended:", attended - invited)

# TODO: Who was invited and attended
print("Attended properly:", invited & attended)
