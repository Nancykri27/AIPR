def calculate_score():
    print("\n=== Job Applicant Scoring System ===\n")
    
    # Basic Information
    applicant_name = input("Enter applicant name: ")
    
    # Education Score (0-25 points)
    print("\nEducation Level:")
    print("1. High School (5 points)")
    print("2. Bachelor's Degree (15 points)")
    print("3. Master's Degree (20 points)")
    print("4. PhD (25 points)")
    education = int(input("Select education level (1-4): "))
    education_score = {1: 5, 2: 15, 3: 20, 4: 25}.get(education, 0)
    
    # Experience Score (0-25 points)
    years_experience = float(input("\nYears of relevant experience: "))
    experience_score = min(years_experience * 5, 25)  # 5 points per year, max 25
    
    # Skills Score (0-30 points)
    print("\nRate the following skills from 0-5 (0=None, 5=Expert):")
    skills = {
        "Programming": 2,
        "Communication": 2,
        "Problem Solving": 2,
        "Teamwork": 1,
        "Leadership": 1
    }
    
    skills_score = 0
    for skill, multiplier in skills.items():
        rating = float(input(f"{skill}: "))
        skills_score += rating * multiplier
    
    # Interview Score (0-20 points)
    interview_score = float(input("\nInterview performance score (0-20): "))
    
    # Calculate Total Score
    total_score = education_score + experience_score + skills_score + interview_score
    max_score = 100
    
    # Results
    print("\n=== Results ===")
    print(f"Applicant: {applicant_name}")
    print(f"Education Score: {education_score}/25")
    print(f"Experience Score: {experience_score:.1f}/25")
    print(f"Skills Score: {skills_score}/30")
    print(f"Interview Score: {interview_score}/20")
    print(f"Total Score: {total_score:.1f}/{max_score}")
    
    # Recommendation
    if total_score >= 80:
        print("Recommendation: Highly Recommended")
    elif total_score >= 60:
        print("Recommendation: Recommended")
    elif total_score >= 40:
        print("Recommendation: Consider")
    else:
        print("Recommendation: Not Recommended")

if __name__ == "__main__":
    calculate_score()