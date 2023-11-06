def first_non_repeating_letter(str):
    if str == "":
        return ""
    counting_items = {}
    for i in range(len(str)):
        if str[i].lower() not in counting_items: 
            counting_items[str[i].lower()] = [str[i]]#We can add the lower case of the letter as key, but keep the original, that way if we get a duplicate it won't matter since it's no longer unique
            counting_items[str[i].lower()].append(i)
            counting_items[str[i].lower()].append(1)
        else:
            counting_items[str[i].lower()].append(1) #If character is added lower or upper case we don't care and append stuff to it to exclude it from "winning"


    potential_winners = {key: value[:2] for key, value in counting_items.items() if len(value) == 3} #Keeps items that is only added once
    if len(potential_winners) > 0:
        char = min(potential_winners.values(), key=lambda x: x[1])
        return char[0]
    return "" #Return empty string if a given string contains only repeating characters "aaaaaaaa"

