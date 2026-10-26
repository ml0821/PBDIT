class Article:
    def __init__(self, title, author, abstract, category, status="Pending"):
        self.title = title
        self.author = author
        self.abstract = abstract
        self.category = category
        self.status = status  # "Pending" or "Published"

    def __str__(self):
        status_label = "Published (Approved)" if self.status == "Published" else "Pending Review"
        return f"Title: {self.title} | Author: {self.author} | Category: {self.category} | Status: {status_label}"


class InstitutionalRepositorySystem:
    def __init__(self):
        # Pre-registered accounts (Confidential database)
        self.users = {
            "FAC-001": {"password": "password123", "name": "Martin Lansang", "role": "Faculty"},
            "FAC-002": {"password": "password123", "name": "Jeffrey Francisco", "role": "Faculty"},
            "LIB-001": {"password": "password123", "name": "Jehan Gojit", "role": "Librarian"},
            "STD-001": {"password": "password123", "name": "Mary Jane Silao", "role": "Student"},
            "STD-002": {"password": "password123", "name": "Krisha Esguerra", "role": "Student"},
            "STD-003": {"password": "password123", "name": "Ella Lopez", "role": "Student"},
            "STD-004": {"password": "password123", "name": "Gaby Mendoza", "role": "Student"}
        }

        # Initial sample articles
        self.articles = [
            Article("Introduction to Computing", "Martin Lansang",
                    "Discusses the fundamental concepts and foundations of technology and computers, serving as a guide and reference for university students.", "Technology", "Published"),
            Article("Principles of Marketing", "Jeffrey Francisco",
                    "Covers core concepts such as market segmentation, consumer behavior, and the marketing mix, providing foundational knowledge for understanding strategic business management.", "Management", "Published")
        ]

    def main_menu(self):
        while True:
            print("\n==================================================")
            print(" INSTITUTIONAL REPOSITORY SYSTEM")
            print("==================================================")
            print("[1] Log in (Faculty, Librarian, or Student)")
            print("[2] Exit")

            choice = input("Select an option (1-2): ").strip()

            if choice == "1":
                self.login_user()
            elif choice == "2":
                print("\nThank you for using the Institutional Repository System. Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1 or 2.")

    def login_user(self):
        print("\n--- SYSTEM LOGIN ---")
        user_id = input("Enter your ID / Username (e.g., FAC-001, LIB-001, STD-001): ").strip()

        # Check if the user ID is NOT pre-registered in the system
        if user_id not in self.users:
            print("\n[Access Denied]: The user is not yet registered.")
            print(
                ">> Notice: Students and users who are not yet registered must report to the Information and Communications Office.")
            return

        password = input("Enter Password: ").strip()

        if self.users[user_id]["password"] != password:
            print("Incorrect password! Please try again.")
            return

        current_user = self.users[user_id]
        print(f"\nLogin successful! Welcome, {current_user['name']} ({current_user['role']}).")

        # Route to respective portal based on role
        if current_user["role"] == "Faculty":
            self.faculty_portal(user_id)
        elif current_user["role"] == "Librarian":
            self.librarian_portal(user_id)
        elif current_user["role"] == "Student":
            self.student_portal(user_id)

    def change_password(self, user_id):
        print("\n--- CHANGE PASSWORD ---")
        old_pass = input("Enter current password: ").strip()
        if old_pass != self.users[user_id]["password"]:
            print("The current password you entered is incorrect.")
            return

        new_pass = input("Enter NEW password: ").strip()
        confirm_pass = input("Confirm NEW password: ").strip()

        if new_pass == confirm_pass and new_pass != "":
            self.users[user_id]["password"] = new_pass
            print(">> Success! Your password has been updated.")
        else:
            print("New passwords do not match or field is blank. Please try again.")

    def faculty_portal(self, user_id):
        user_info = self.users[user_id]
        while True:
            print(f"\n[FACULTY PORTAL - {user_info['name']}]")
            print("[1] Upload New Publication File")
            print("[2] View My Uploads and Status")
            print("[3] Change Password")
            print("[4] Log out (Return to Main Menu)")

            choice = input("Select an option (1-4): ").strip()

            if choice == "1":
                print("\n--- Upload Publication File ---")
                title = input("Article Title: ")
                abstract = input("Abstract / Summary: ")
                category = input("Category / Field: ")

                new_art = Article(title, user_info['name'], abstract, category, status="Pending")
                self.articles.append(new_art)
                print(">> Publication file uploaded successfully! It is now pending librarian approval.")

            elif choice == "2":
                print(f"\n--- Publications by {user_info['name']} ---")
                my_articles = [art for art in self.articles if user_info['name'].lower() in art.author.lower()]
                if not my_articles:
                    print("You haven't uploaded any articles yet.")
                else:
                    for idx, art in enumerate(my_articles, 1):
                        print(f"\n[{idx}] {art}")
                        print(f"    Abstract: {art.abstract}")

            elif choice == "3":
                self.change_password(user_id)
            elif choice == "4":
                print(">> Logged out from Faculty Portal.")
                break
            else:
                print("Invalid choice. Please try again.")

    def librarian_portal(self, user_id):
        user_info = self.users[user_id]
        while True:
            print(f"\n[LIBRARIAN PORTAL - {user_info['name']}]")
            print("[1] Review and Approve Pending Submissions")
            print("[2] View All Repository Records")
            print("[3] Change Password")
            print("[4] Log out (Return to Main Menu)")

            choice = input("Select an option (1-4): ").strip()

            if choice == "1":
                print("\n--- Pending Submissions ---")
                pending = [art for art in self.articles if art.status == "Pending"]
                if not pending:
                    print("No pending articles waiting for approval.")
                else:
                    for idx, art in enumerate(pending, 1):
                        print(f"\n[{idx}] Title: {art.title} | Author: {art.author} | Category: {art.category}")

                    sub_choice = input("Enter the number of the article to review (or 0 to cancel): ").strip()
                    if sub_choice.isdigit() and 1 <= int(sub_choice) <= len(pending):
                        selected_art = pending[int(sub_choice) - 1]
                        approval = input(f"Approve '{selected_art.title}' for publication? (yes/no): ").strip().lower()
                        if approval in ["yes", "y"]:
                            selected_art.status = "Published"
                            print(f">> Success! Article approved. Author ({selected_art.author}) has been notified.")
                        else:
                            print("Article kept as Pending.")

            elif choice == "2":
                print("\n--- Complete Repository Records ---")
                for idx, art in enumerate(self.articles, 1):
                    print(f"\n[{idx}] {art}")

            elif choice == "3":
                self.change_password(user_id)
            elif choice == "4":
                print(">> Logged out from Librarian Portal.")
                break
            else:
                print("Invalid choice. Please try again.")

    def student_portal(self, user_id):
        user_info = self.users[user_id]
        while True:
            print(f"\n[STUDENT PORTAL - {user_info['name']}]")
            print("[1] Search Scholarly Articles")
            print("[2] View All Published Articles")
            print("[3] Change Password")
            print("[4] Log out (Return to Main Menu)")

            choice = input("Select an option (1-4): ").strip()

            if choice == "1":
                keyword = input("Enter search keyword (title, author, or keyword): ").lower()
                results = [art for art in self.articles if art.status == "Published" and (
                        keyword in art.title.lower() or keyword in art.author.lower() or keyword in art.abstract.lower()
                )]

                print(f"\nResults Found: {len(results)}")
                if results:
                    for idx, art in enumerate(results, 1):
                        print(f"\n[{idx}] {art}")
                        print(f"    Abstract: {art.abstract}")

                    dl = input("\nWould you like to view/download the full content? (yes/no): ").strip().lower()
                    if dl in ["yes", "y"]:
                        print(">>> Full-text copy downloaded/accessed successfully!")
                else:
                    print("No matching published articles found.")

            elif choice == "2":
                print("\n--- Available Published Articles ---")
                published = [art for art in self.articles if art.status == "Published"]
                if not published:
                    print("Currently no published articles available.")
                else:
                    for idx, art in enumerate(published, 1):
                        print(f"\n[{idx}] {art}")
                        print(f"    Abstract: {art.abstract}")
            elif choice == "3":
                self.change_password(user_id)
            elif choice == "4":
                print(">> Logged out from Student Portal.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    repo = InstitutionalRepositorySystem()
    repo.main_menu()