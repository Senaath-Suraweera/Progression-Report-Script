from graphics import *
import datetime as dt

## have to make the entries pormpts more presentable

def rangeCheck(input) -> bool:
    if input >= 0 and input <= 120:
        return True
    else:
        print("Out of range, please enter a number between 0 and 120")
        return False

# def intCheck(input) -> bool:
#     try:
#         int(input)
#         return True
#     except ValueError:
#         print("Integer Required!")
#         return False

def totalCheck(input) -> bool:
    if len(input) == 3:
        if input[0] + input[1] + input[2] == 120:
            return True
        else:
            print("Total Incorrect, Total Credits should be 120")
            return False
    else:
        print(input)
        print("Stackoverflow")

def validEntryCheck(input) -> bool:
    validEntries = [0, 20, 40, 60, 80, 100, 120]
    if input in validEntries:
        return True
    else:
        print("Invalid Entry, credits can be only 0, 20, 40, 60, 80, 100 or 120")
        return False
        
def checkForUser():
    #returns 1 for student and 2 for staff or -1 for invalid
    user: str = input("Please enter your role(Student/Staff): ").lower()
    switch = {
            "student": 1,
            "staff": 2
    }
    if user not in switch:
        return -1
    else:
        return switch[user]

def insertData():
    dataList = []
    Credit = {
        0: "Pass",
        1: "Defer",
        2: "Fail"
    }

    while True:
        dataList.clear()
        for i in range(3):
            while True:
                try:
                    value = int(input(f"Enter Your Total {Credit[i].upper()} Credits: "))
                    if rangeCheck(value) and validEntryCheck(value):
                        dataList.append(value)
                        break
                except ValueError:
                    print("Please enter a valid number")
                    continue
        if totalCheck(dataList):
            break


    return dataList

def filterLogic(input):
    if input[0] == 120:
        print("\nProgress")
        for i in range(len(input)):
            print(input[i] , end="")
            if i != 2:
                print(" , ", end="")
            else:
                print("\n")
        return 0
    elif input[0] == 100:
        print("\nProgress (module trailer)")
        for i in range(len(input)):
            print(input[i] , end="")
            if i != 2:
                print(" , ", end="")
            else:
                print("\n")
        return 1
    elif input[2] == 120 or input[2] == 100 or input[2] == 80:
        print("\nExclude")
        for i in range(len(input)):
            print(input[i] , end="")
            if i != 2:
                print(" , ", end="")
            else:
                print("\n")
        return 3
    else:
        print("\nDo not Progress - module retriever")
        for i in range(len(input)):
            print(input[i] , end="")
            if i != 2:
                print(" , ", end="")
            else:
                print("\n")
        return 2

def printNestedList(input):
    if len(input) == 0:
        print("No Data to display")
        print("====================================\n")
        return
    for i in input:
        for j in range(len(i)):
            print(i[j], end="")
            if j != 2:
                print(" , ", end="")
            else:
                print("\n")
        print("\n")

def printNestedListToFile(input, Name):
    with open(f"{dt.date.today()}_output.txt", "a") as f:
        f.write(f"{Name}: \n")
        if len(input) == 0:
            f.write("No Data to display")
            f.write("\n====================================\n")
            return
        for i in input:
            for j in range(len(i)):
                f.write(str(i[j]))
                if j != 2:
                    f.write(" , ")
                else:
                    f.write("\n")
            f.write("\n")

def drawHistogram(input):
    max_height = 500  
    max_value = max(input) if max(input) > 0 else 1  

    window = GraphWin("Histogram", 1000, 800)
    window.setBackground("linen")

    title = Text(Point(200, 50), "Histogram Results")
    title.setSize(30)
    title.setTextColor("grey")
    title.setStyle("bold")
    title.draw(window)

    bar_width = 150
    spacing = 25
    base_x = 100
    bar_bottom = 700

    labels = ["Progress", "Trailer", "Retriever", "Excluded"]
    colors = ["pale green", "dark sea green", "sea green", "thistle"]

    for i in range(4):
        count = input[i]
        bar_height = int((count / max_value) * max_height)
        left = base_x + i * (bar_width + spacing)
        right = left + bar_width

        rect = Rectangle(Point(left, bar_bottom - bar_height), Point(right, bar_bottom))
        rect.setFill(colors[i])
        rect.draw(window)

        count_text = Text(Point((left + right) / 2, bar_bottom - bar_height - 20), str(count))
        count_text.setSize(20)
        count_text.setTextColor("grey")
        count_text.setStyle("bold")
        count_text.draw(window)

        label = Text(Point((left + right) / 2, bar_bottom + 20), labels[i])
        label.setSize(16)
        label.setTextColor("grey")
        label.setStyle("bold")
        label.draw(window)

    barLine = Line(Point(50, bar_bottom), Point(950, bar_bottom))
    barLine.setWidth(3)
    barLine.setFill("grey")
    barLine.draw(window)

    total = sum(input)
    totalDisplay = Text(Point(200, 750), f"{total} outcomes in total")
    totalDisplay.setSize(28)
    totalDisplay.setTextColor("grey")
    totalDisplay.setStyle("bold")
    totalDisplay.draw(window)

    window.getMouse()
    window.close()





def main():
    loopFlag: bool = True;
    staffFlag: str = "y"


    print("\n\n====================================")
    print("Welcome to the Progression Report")
    print("====================================\n")
    while loopFlag:
        user = checkForUser()
        if user == -1:
            print("Invalid User Type Entered Try Again!!")
            continue
        elif user == 1:
            List = insertData()
            filterLogic(List)
        else:
            histogramData = [0 , 0 , 0 , 0]
            progress = []
            moduleTrailer = []
            moduleRetreiver = []
            exclude = []
            print("\n~Welcome to the Staff Progression Report Analysis~\n")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            while staffFlag == "y":

                

                List = insertData()


                listIndex = filterLogic(List)

                ##debugging
                ##print(listIndex)

                if listIndex == 0:
                    progress.append(List)
                    histogramData[0] += 1
                elif listIndex == 1:
                    moduleTrailer.append(List)
                    histogramData[1] += 1
                elif listIndex == 2:
                    moduleRetreiver.append(List)
                    histogramData[2] += 1
                else:
                    exclude.append(List)
                    histogramData[3] += 1


                while True:
                    staffFlag = input("\nDo you want to continue with more data? (y/n) or enter (q) to quit and view histogram: \n")
                    if staffFlag.lower() == "n" or staffFlag.lower() == "y" or staffFlag.lower() == "q":
                        break
                    else:
                        print("Invalid Input Try Again!!")
                if staffFlag.lower() == "q":
                    drawHistogram(histogramData)
                    print("\n====================================")
                    print("All Student Data")
                    print("==================================== \n")
                    print("Progress: \n")
                    printNestedList(progress)
                    printNestedListToFile(progress, "Progress")
                    print("Progress(Module Trailer):\n")
                    printNestedList(moduleTrailer)
                    printNestedListToFile(moduleTrailer, "Progress(Module Trailer)")
                    print("Module Retreiver: \n")
                    printNestedList(moduleRetreiver)
                    printNestedListToFile(moduleRetreiver, "Module Retreiver")
                    print("Exclude:\n")
                    printNestedList(exclude)
                    printNestedListToFile(exclude, "Exclude")
                    loopFlag = False
                elif staffFlag.lower() == "n":
                    loopFlag = False
    print("==========================================")
    print("Thank you for using the Progression Report")
    print("==========================================")
    print("Exiting the program...")


if __name__ == "__main__":
    main()