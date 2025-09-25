#Kurkeli Kurkeli
#09/24/2025
#Comp 163 Section 5
#AI use for debugging
#AI use for explaining certain syntax

#Foundation Setup
student_name = "Kurkeli kurkeli"
current_gpa = 3.5
study_hours = 25
social_points = 50
stress_level = 26

print(f"Welcome to College Life, {student_name}!")
print("Starting stats -> "
      f"GPA: {current_gpa}, Study Hours: {study_hours}, "
      f"Social: {social_points}, Stress: {stress_level}")

#Course Planning Decision
print("\nChoose your course load:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")

course_choice = input("Your choice (A/B/C): ").strip().upper()

if course_choice == "A":
    if current_gpa >= 3.0:
        pass
    else:
        pass
elif course_choice == "B":
    pass
elif course_choice == "C":
    if current_gpa >= 3.5:
        pass
    else:
        pass
else:
    print("Invalid choice. Defaulting to Standard load.")
    pass

#Show updated stats
print("After course planning -> "
      f"GPA: {current_gpa}, Study Hours: {study_hours}, "
      f"Social: {social_points}, Stress: {stress_level}")
#Study Strategy Decision
available_options = ["Programming", "Math", "English", "History"]
print("\nPick a study focus from this list:", available_options)
study_choice = input("Type exactly one option: ").strip().title()

#membership operators
# AI helped me understand operator syntax
if study_choice in available_options:
    #Logical operator usage
    if study_choice == "Programming" and study_hours >= 20:
        current_gpa += 0.1       # example adjustment
        social_points -= 5
    elif study_choice == "Math" or study_choice == "English":
        current_gpa += 0.05
        social_points += 2
    else:
        if not (stress_level > 70):
            social_points += 3
elif study_choice not in available_options:
    print("That option is not available. No changes made for study focus.")

print("After study strategy -> "
      f"GPA: {current_gpa}, Study Hours: {study_hours}, "
      f"Social: {social_points}, Stress: {stress_level}")
#Final Semester Assessment
print("\nFinal check-in: Choose a final push activity:")
print("1) Group study marathon")
print("2) Solo deep-dive")
print("3) Big social event")

final_choice_raw = input("Enter 1, 2, or 3: ").strip()

#Use identity operators meaningfully with a sentinel
final_choice = None
if final_choice_raw.isdigit():
    final_choice = int(final_choice_raw)

#Identity check
if final_choice is None:
    print("No valid final choice entered. Proceeding with neutral outcome.")
else:
    if final_choice == 1:
        #branch
        if study_hours >= 25:
            #adjustments
            current_gpa += 0.10
            stress_level += 5
        else:
            current_gpa += 0.05
            stress_level += 10
    elif final_choice == 2:
        if stress_level <= 50:
            current_gpa += 0.10
            stress_level -= 5
        else:
            current_gpa += 0.02
            stress_level -= 2
    elif final_choice == 3:
        if social_points >= 60:
            social_points += 5
            stress_level -= 5
        else:
            social_points += 3
            stress_level += 2
    else:
        print("Unknown option. No final adjustments made.")

#Determine 3 different endings
ending = "Undefined"
if current_gpa >= 3.5:
    if stress_level <= 50:
        ending = "A) Academic Star with Healthy Balance"
    else:
        ending = "B) Academic Star but Overstressed"
elif 2.5 <= current_gpa < 3.5:
    if social_points >= 60:
        ending = "C) Balanced Scholar with Strong Community"
    else:
        ending = "D) Steady Progress, Room to Grow"
else:
    if stress_level > 70:
        ending = "E) Burnout Warning — Recalibrate"
    else:
        ending = "F) Rebuilding Year — Foundations Set"

print("\n=== FINAL RESULTS ===")
print(f"Ending: {ending}")
print(f"Final stats -> GPA: {current_gpa}, Study Hours: {study_hours}, "
      f"Social: {social_points}, Stress: {stress_level}")

