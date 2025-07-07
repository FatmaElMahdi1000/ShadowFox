justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

justice_league_members = len(justice_league)
print(f"1. justice_league_members = {justice_league_members} member!") #Task1

justice_league.extend(["Batgirl", "Nightwing"])#New_members_added
print(f"2. updated list of members: {justice_league} ") #Task2


for i, value in enumerate(justice_league):
    if justice_league[i] == "Wonder Woman":
        justice_league[i] = justice_league[0]
        justice_league[0] = "Wonder Woman"
print(f"3. updated list of members: {justice_league}")  #Task3

for i, value in enumerate(justice_league):
    if justice_league[i] == "Aquaman" and justice_league[i + 1] ==  "Green Lantern":
        justice_league[i + 1]= justice_league[i] 
        justice_league[i] = "Green Lantern"
        
print(f"4. updated list of members: {justice_league}") #Task4

print("#___Another way to do no.4___USING: Remove(), Index(), insert() methods#")
justice_league= ['Wonder Woman', 'Batman', 'Superman', 'Flash',   'Aquaman', 'Green Lantern', 'Batgirl', 'Nightwing']
justice_league.remove("Green Lantern")
Flash_index = justice_league.index('Flash')
Placing_Green_Lantern = justice_league.insert(Flash_index + 1, "Green Lantern")
print(justice_league)


del justice_league[0:]
justice_league.extend(["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"])
print(f"5. New list of members: {justice_league}")  #Task5


justice_league.sort()
print(f"6. justice_league_sorted_alphabetically: {justice_league}")

new_leader = justice_league[0]

print(f"BOUNS QUESTION: NEW LEADER IS: {new_leader}")  #Task6

