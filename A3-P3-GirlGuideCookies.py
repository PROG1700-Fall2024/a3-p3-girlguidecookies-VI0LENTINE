#Program 3 – Girl Guide Cookies
#Description:   The organizers of the annual Girl Guide cookie sale event want to raise 
#               the stakes on the number of cookies sold and are offering cool prizes to
#               those guides who go above and beyond in their sales efforts. The organizers
#               want a program to print the guide list and their prizes.

#Student #: W0516070    
#Student Name: Valentine Byrnes 


    # YOUR CODE STARTS HERE, each line must be indented (one tab)
#Asks for number of guides. Checks for unnecessary symbols/floats
def guideInput():
    numOfGuides = input("Enter the number of guides selling cookies: ")
    while not validNumber(numOfGuides):
        print("\nPlease enter a valid, whole number of guides (no letters, decimals, or symbols). Try again.\n")
        numOfGuides = input("Enter the number of guides selling cookies: ")

    return int(numOfGuides)

# #Took this from my part 1 as both part 1 and part 3 were giving me TypeErrors before using this function.
def validNumber(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

#User must enter a valid name and a number of boxes. Otherwise, it will cause an error.
def guidesLoop(numOfGuides):
    guideNames = [] 
    boxCount = []
    guideCount = int(numOfGuides)
    for i in range(guideCount):
        name = input(f"\nEnter the name of guide #{i + 1}: ")
        while validName(name) == False:
            print("\nPlease enter a valid name (letters only). Try again.\n")
            name = input(f"\nEnter the name of guide #{i + 1}: ")
        guideNames.append(name)

        boxes = input(f"Enter the number of boxes sold by {name}: ")
        while not validNumber(boxes) or '+' in boxes or '-' in boxes or '.' in boxes:
            print("\nPlease enter a valid, whole number of boxes (no +, -, .). Try again.\n")
            boxes = input(f"Enter the number of boxes sold by {name}: ")
        boxCount.append(int(boxes))

    return guideNames, boxCount

#Checks for anything that isn't a letter in the name input
def validName(a):
    try:
        str(a)
        return True
    except:
        return False

#Calculate average number of boxes and output results
def avg(boxCount, guideCount):
    totalBoxes = sum(boxCount)
    avgBoxes = totalBoxes / guideCount
    print(f"\n\nThe average number of boxes sold by each guide is: {avgBoxes:.1f}")

    return avgBoxes

#Output which guide gets what prize (or lack thereof)
def winner(guideNames, boxCount, avgBoxes):
    noPrize = 0
    print("\nGuide\t\t Prizes Won:")
    print("---------------------------------------------------------------------------------")
    for i in range(len(guideNames)):
        prize = ["Trip to Girl Guide Jamboree in Aruba!", "Super Seller Badge", "Left over cookies", ""]
        if boxCount[i] == max(boxCount):
            print(f"{guideNames[i]:<16} - {prize[0]}")
        elif boxCount[i] >= int(avgBoxes):
            print(f"{guideNames[i]:<16} - {prize[1]}")
        elif boxCount[i] < avgBoxes and boxCount[i] != noPrize:
            print(f"{guideNames[i]:<16} - {prize[2]}")
        else:
            print(f"{guideNames[i]:<16} - {prize[3]}")

#Majority of functions called here
def main():
    numOfGuides = guideInput()
    guideCount = numOfGuides
    guideNames, boxCount = guidesLoop(numOfGuides)
    avgBoxes = avg(boxCount, guideCount)
    winner(guideNames, boxCount, avgBoxes)

main()