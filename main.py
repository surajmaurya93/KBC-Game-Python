questions = [
      ["1.What is the capital of India?",
        "1.Mumbai", "2.Punjab", "3.Banglore", "4.Delhi", 4],

      ["2.Which Team Won The 2024 T20 World Cup?",
         "1.Australia", "2.India", "3.Afganistan", "4.South Africa", 2],

      ["3.Which city is known as the Pink City of India?",
         "1.Maysore ", "2.Kochi", "3.Jaipur", "4.Banglore", 3],

      ["4.How many states are there in India?",
      "1.26", "2.28", "3.29", "4.31", 2],

      [ "5.Where is India Gate located?",
       "1.Delhi", "2.Agra", "3.Punjab", "4.Mumbai", 1],

      ["6.Which of the following is not a state of India?",
        "1.Vrindachal ", "2.Uttrakhand", "3.Goa", "4.Jharkhand", 1],

      [ "7.Who wrote India's National Anthem?",
       "1.Rabindranath Tagore", "2.Lal Bahadur Shastri", "3.Chetan Bhagat", "4.RK Narayan", 1],

      ["8.The fine step-well complex of 'Agrasen ki Baoli' is located at",
        "1.Mumbai", "2.Uttrakhand", "3.U.P", "4.New Delhi", 4],

      ["9.Which country is the largest producer of coffee in the world?"
         " at the end of a unit or course?", 
         "1.Vietnam", "2.Colombia", "3.Ethiopia", "4.Brazil", 4],

      ["10.Which Indian city hosts Indian movie industry?",
        "1.Goa", "2.Mumbai", "3.Banglore ", "4.Kolkata", 2],

]
rewards = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(len(questions)):
    choose = questions[i]

    print("Choose the correct answer")
    print(choose[0])
    print(f"{choose[1]}      {choose[2]}")
    print(f"{choose[3]}      {choose[4]}")

    answer = int(input("Enter your choice (1-4): \n"))

    if answer == choose[5]:       # we sign index 5 because we write answer in the list of index 5(choose[5])
        money = money + rewards[i]
        print(f"Correct answer, you win Rs.{rewards[i]} \n")
    else:
        print("Incorrect answer! ")
        break

print(f"Game Over!, Your total Reward is {money}")