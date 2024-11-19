#Program 3 – Girl Guide Cookies
#Description:   The organizers of the annual Girl Guide cookie sale event want to raise 
#               the stakes on the number of cookies sold and are offering cool prizes to
#               those guides who go above and beyond in their sales efforts. The organizers
#               want a program to print the guide list and their prizes.

#Student #: W0516070    
#Student Name: Valentine Byrnes 


    # YOUR CODE STARTS HERE, each line must be indented (one tab)
def guideInput():
    numOfGuides = []
    numOfGuides = input("Enter the number of guides selling cookies: ")
    validNumber = True
    for num in numOfGuides:
        if not num.isnumeric():
            validNumber = False
    if validNumber == False:
        print("\nPlease enter a number instead. Try again.\n")
        main()
    return numOfGuides

def guidesLoop(numOfGuides):
    guideNames = []        
    boxCount = []
    guideCount = int(numOfGuides)
    validName = True
    for i in range(guideCount):
        name = input(f"\nEnter the name of guide #{i + 1}: ")
        guideNames.append(name)
        for char in name:
            if char.isnumeric():
                validName = False
                break
            elif char.lower() not in "abcdefghijklmnopqrstuvwxyz":
                validName = False
                break
        if validName == False:
            print("\nPlease enter a valid name (letters only). Try again.\n")
            main()
        boxes = int(input(f"Enter the number of boxes sold by {guideNames[i]}: "))
        boxCount.append(boxes)
    
    return guideNames, boxCount

def avg(boxCount, guideCount):
    totalBoxes = sum(boxCount)
    avgBoxes = totalBoxes / guideCount
    print(f"\n\nThe average number of boxes sold by each guide is: {avgBoxes:.1f}")
    return avgBoxes

def winner(guideNames, boxCount, avgBoxes):
    print("\nGuide\t\t Prizes Won:")
    print("---------------------------------------------------------------------------------")
    for i in range(len(guideNames)):
        prize = ["Trip to Girl Guide Jamboree in Aruba!", "Super Seller Badge", "Left over cookies", ""]
        if boxCount[i] == max(boxCount):
            print(f"{guideNames[i]:<16} - {prize[0]}")
        elif boxCount[i] >= int(avgBoxes):
            print(f"{guideNames[i]:<16} - {prize[1]}")
        elif boxCount[i] < avgBoxes and boxCount[i] != 0:
            print(f"{guideNames[i]:<16} - {prize[2]}")
        else:
            print(f"{guideNames[i]:<16} - {prize[3]}")

def main():
    numOfGuides = guideInput()
    guideCount = int(numOfGuides)
    guideNames, boxCounts = guidesLoop(numOfGuides)
    avgBoxes = avg(boxCounts, guideCount)
    winner(guideNames, boxCounts, avgBoxes)
    # YOUR CODE ENDS HERE

main()