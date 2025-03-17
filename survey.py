import os

# File to store survey data
FILE_PATH = "survey_data.txt"

# Function to add a new survey response
def add_survey_response():
    user_id = input("Enter User ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    father_name = input("Enter Father's Name: ")
    marital_status = input("Enter Marital Status (Married/Unmarried): ")
    occupation = input("Enter Occupation: ")
    salary = input("Enter Salary (Per Month): ")
    gender = input("Enter Gender (Male/Female/Other): ")
    family_members = input("Enter Number of Family Members: ")
    home_no = input("Enter Home/Building No.: ")
    village = input("Enter Village: ")
    post_office = input("Enter Post Office: ")
    police_station = input("Enter Police Station: ")
    district = input("Enter District: ")
    state = input("Enter State: ")
    pincode = input("Enter Pincode: ")
    mobile_number = input("Enter Mobile Number: ")
    vehicles = input("Enter Vehicles and their Number (e.g., Car: XYZ123, Bike: ABC456): ")
    
    # Storing data in text file with newline formatting
    with open(FILE_PATH, "a") as file:
        file.write(f"User ID: {user_id}\n")
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Father's Name: {father_name}\n")
        file.write(f"Marital Status: {marital_status}\n")
        file.write(f"Occupation: {occupation}\n")
        file.write(f"Salary: {salary}\n")
        file.write(f"Gender: {gender}\n")
        file.write(f"Family Members: {family_members}\n")
        file.write(f"Home/Building No.: {home_no}\n")
        file.write(f"Village: {village}\n")
        file.write(f"Post Office: {post_office}\n")
        file.write(f"Police Station: {police_station}\n")
        file.write(f"District: {district}\n")
        file.write(f"State: {state}\n")
        file.write(f"Pincode: {pincode}\n")
        file.write(f"Mobile Number: {mobile_number}\n")
        file.write(f"Vehicles: {vehicles}\n")
        file.write("----------------------------------------\n")
    
    print("\n✅ Survey Response Added Successfully!\n")

# Function to show all survey responses
def show_all_responses():
    if not os.path.exists(FILE_PATH) or os.stat(FILE_PATH).st_size == 0:
        print("\n⚠️ No survey responses found!")
        return
    
    print("\n📌 Survey Responses:")
    with open(FILE_PATH, "r") as file:
        content = file.read().strip()
        if not content:
            print("\n⚠️ No survey responses found!")
        else:
            print(content)

# Function to search response by user ID or name
def search_response():
    search_query = input("Enter User ID or Name to search: ").strip().lower()
    found = False
    with open(FILE_PATH, "r") as file:
        lines = file.readlines()
        record = ""
        for line in lines:
            if "----------------------------------------" in line:
                if search_query in record.lower():
                    print("\n✅ Match Found!")
                    print(record)
                    found = True
                record = ""
            record += line
    if not found:
        print("\n❌ No matching record found!")

# Function to update survey response
def update_response():
    search_query = input("Enter User ID or Name to update: ").strip().lower()
    if not os.path.exists(FILE_PATH) or os.stat(FILE_PATH).st_size == 0:
        print("\n⚠️ No survey responses found!")
        return
    
    with open(FILE_PATH, "r") as file:
        lines = file.readlines()
    
    updated_lines = []
    record = ""
    found = False
    for line in lines:
        if "----------------------------------------" in line:
            if search_query in record.lower():
                print("\n✅ Match Found! Enter new details:")
                add_survey_response()
                found = True
            else:
                updated_lines.append(record)
            record = ""
        record += line
    
    if found:
        with open(FILE_PATH, "w") as file:
            file.writelines(updated_lines)
        print("\n✅ Survey Response Updated Successfully!")
    else:
        print("\n❌ No matching record found!")

# Function to delete a survey response
def delete_response():
    search_query = input("Enter User ID or Name to delete: ").strip().lower()
    if not os.path.exists(FILE_PATH) or os.stat(FILE_PATH).st_size == 0:
        print("\n⚠️ No survey responses found!")
        return
    
    with open(FILE_PATH, "r") as file:
        lines = file.readlines()
    
    updated_lines = []
    record = ""
    found = False
    for line in lines:
        if "----------------------------------------" in line:
            if search_query in record.lower():
                print("\n✅ Survey Response Deleted Successfully!")
                found = True
            else:
                updated_lines.append(record)
            record = ""
        record += line
    
    if found:
        with open(FILE_PATH, "w") as file:
            file.writelines(updated_lines)
    else:
        print("\n❌ No matching record found!")

# Function to show statistics
def show_statistics():
    if not os.path.exists(FILE_PATH) or os.stat(FILE_PATH).st_size == 0:
        print("\n⚠️ No survey responses found!")
        return
    
    count = open(FILE_PATH).read().count("----------------------------------------")
    print(f"\n📊 Total Number of Surveys Conducted: {count}")

# Main Menu
def main():
    while True:
        print("\n📌 Survey System")
        print("1. Add Survey Response")
        print("2. Show All Survey Responses")
        print("3. Search Survey Response")
        print("4. Update Survey Response")
        print("5. Delete Survey Response")
        print("6. Show Survey Statistics")
        print("7. Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            add_survey_response()
        elif choice == "2":
            show_all_responses()
        elif choice == "3":
            search_response()
        elif choice == "4":
            update_response()
        elif choice == "5":
            delete_response()
        elif choice == "6":
            show_statistics()
        elif choice == "7":
            print("\n📌 Exiting Survey System. Thanks For Your Valuable Time!\n")
            break
        else:
            print("\n⚠️ Invalid choice! Please enter a valid option.")

# Run the program
if __name__ == "__main__":
    main()
