import random


def get_skills():
    # Add at least 3 random skills for the user to select from
    # randomList = random.choices(mylist, weights=[1, 1, 1, 1, 1, 1], k=3)
    mylist = ["Python", "C++", "JavaScript", "Meeting", "Leeting", "Eating"]
    return mylist


def show_skills(skills):
    # Pretty print skills to the user
    # Write your code here
    print("Skills")
    for i in range(len(skills)):
        print(f"{i+1}.{skills[i]}")


def get_user_skills(skills):
    # Show the available skills and have user pick from them
    # Write your code here
    choosenSkill1 = False
    choosenSkill2 = False
    indexList = [1, 2, 3, 4, 5, 6]
    choosenSkillsList = []
    while choosenSkill1 == False:
        skill1 = input("Choose a skill from above by entering its number:")
        if int(skill1) in indexList:
            skill1 = str(skills[int(skill1)-1])
            choosenSkillsList.append(skill1)
            choosenSkill1 = True
        else:
            print("Choose one of the above skills again please!")
    while choosenSkill2 == False:
        skill2 = input(
            "Choose another skill from above by entering its number:")
        if int(skill2) in indexList:
            skill2 = str(skills[int(skill2)-1])
            choosenSkillsList.append(skill2)
            choosenSkill2 = True
        else:
            print("Choose one of the above skills again please!")

    return choosenSkillsList


def get_user_cv(skills):
    # Get the users CV from their inputs
    # Write your code here
    cv = {'name': input("What's your name?"), 'age': int(input(
        "How old are you?")), 'experience': int(input("How many years of experience do you have?")), 'skills': skills}

    return cv


def check_acceptance(cv, desired_skill):
    # Check if the cv is acceptable or not and return a boolean based on that
    # Write your code here
    mySkill = get_skills()
    checkAcceptance = False
    if cv.get('age') < 40 and cv.get('age') > 25 and cv.get('experience') > 3 and mySkill[2] in desired_skill:

        checkAcceptance = True
    else:
        pass
    return checkAcceptance


def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome

    print("Welcome to the special recruitment program, please answer the following questions:")
    getSkills = get_skills()
    showSkills = show_skills(getSkills)
    desired_skills = get_user_skills(getSkills)
    cv = get_user_cv(desired_skills)
    checkAcceptance = check_acceptance(cv=cv, desired_skill=desired_skills)
    if checkAcceptance == True:
        print(f"You have been accepted, {cv.get('name').title()}")
    else:
        print(f"You have NOT been accepted, {cv.get('name').title()}")


if __name__ == "__main__":
    main()