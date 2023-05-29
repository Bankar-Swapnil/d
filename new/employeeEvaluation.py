print("***************EMPLOYEE EVALUATION SYSTEM***************")
name=input("\nEnter Employee name: \n")
id=input("Enter Employee ID: \n")
score=0
communication_score=0
Questions=["\nQuality of Work:\nRegularly and accurately completes the work given and posseses proffesionalism & technical proficiency",
          "\nWork Habits: \nPlans & organises work; takes care of equipment & supplies",
          "\nRelationship with People:\nHas the ability to get along with there others & effectively deals with the public",
          "\nDependability:\nCan be relied upon to work steadily, effectively & puntually",
          "\nQuality of Work:\nAmount of work performed",
          "\nInitiative:\nShows initiative , resourcefulness & has a positive response towards work assigned",
          "\nCreativity:\nPosseses creativity, versatality, originality & isn't afraid to think out of the box",
          "\nAnalytical Ability:\nCarries out analysis of data, facts, laws, rules & procedures, thoroughly and accurately",
          "\nAbility as a Supervisor:\nProficient in employee training as well as planning, organizing & laying work for work unit",
          "\nAdministrative Ability:\nPromptness of action, soundness of decision, application of good management principles"]


communication_skills=["Can the employee communicate their ideas clearly?",
                      "Can the employee host meetings and seminars?",
                      "Is the employee proficient in english?"]

print("\n\nRate each of the question below on a scale of 1-5 where:")
print("1 - Unsatisfactory")
print("2 - Fair")
print("3 - Good")
print("4 - Very Good")
print("5 - Excellent")
for question in Questions:
    print(question)
    score+=int(input())

percent_score=score*2

print("\n\nAnswer the below questions as yes or no:")
for question in communication_skills:
    print(question)
    ans=input()
    if(ans=="yes"):
        communication_score=communication_score+1

print(f'\n\nEmployee performance score of {name} (ID:{id}): ',percent_score,"%")

if(percent_score>=75):
    print("Employee has shown excellent performance throughout the year!!")
elif(percent_score>=50 and percent_score<75):
    print("Employee has shown fairly good performance through the year. There is room for improvement.")
elif(percent_score>=25 and percent_score<50):
    print("Employee has shown average performance throughout the year.Has to start taking the job more seriously.")
else:
    print("Employee performance is exceedingly bad. Please report to your supervisor for a detailed evaluation.")

if(communication_score==3):
    print("Employee posseses excellent communcation skills.")
elif(communication_score==2):
    print("Employee posseses good communication skills.Can be better.")
else:
    print("Employee communication skills require lot of work. Report to HR for further instructions.")