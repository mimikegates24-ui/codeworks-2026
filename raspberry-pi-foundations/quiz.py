Quiz made by kerstin gatson.

Score = 0

questions = [
    {
       "question": "1.How is a black hole formed?",
       "options":["A.Plantes gets thrown out of orbit?
, "B. Stars collapse under their own gravity", "C. A star collides with another staris","D.A white hole mixes with a star"]
       "answer" : "B"
    }

    {
    "question": "1.What is the biggest animal?",
       "options":["A. Giraffen", "B. Elefiant", "C. Megelodon is","D. Blue whale"]
       "answer" : "C"

    }



    {
    "question": "1.What animal has the thickest fur for warmth?",
       "options":["A.An arctic fox", "B. A wolf", "C. A maned (deer, fox, wolf,) Chrysocyon brachyurus,? Its one animal", "D. reindeer"]
       "answer" : "D"

    



     }       ]



print("====Welcome to my quize====\n")

for q in questions:
    print(q["questions"])

    for options in q["options"]:
        print(options)

        response = input ("Enter Your Anwser (A,B<c or D): ").strip().upper()

        if response == q ["answer"]:
            print("correct!\n")
            score +=1
            else:
                print("Incorrect..The correct answer was {q['answer]}.\n")

                print("=" * 40)
                ptint(f"Your final score is {score}/{len(questions)}")
