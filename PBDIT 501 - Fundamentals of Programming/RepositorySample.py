import tkinter as tk
from tkinter import messagebox, simpledialog


class Article:
    def __init__(self, title, author, abstract, category, status="Pending"):
        self.title = title
        self.author = author
        self.abstract = abstract
        self.category = category
        self.status = status

    def __str__(self):
        s_label = "Published (Approved)" if self.status == "Published" else "Pending Review"
        return f"Title: {self.title} | Author: {self.author} | Category: {self.category} | Status: {s_label}"


class InstitutionalRepositoryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Institutional Repository System")
        self.root.geometry("850x550")
        self.root.resizable(False, False)

        self.users = {
            "FAC-001": {"password": "password123", "name": "Martin Lansang", "role": "Faculty"},
            "FAC-002": {"password": "password123", "name": "Jeffrey Francisco", "role": "Faculty"},
            "LIB-001": {"password": "password123", "name": "Jehan Gojit", "role": "Librarian"},
            "STD-001": {"password": "password123", "name": "Mary Jane Silao", "role": "Student"},
            "STD-002": {"password": "password123", "name": "Krisha Esguerra", "role": "Student"},
            "STD-003": {"password": "password123", "name": "Ella Lopez", "role": "Student"},
            "STD-004": {"password": "password123", "name": "Gaby Mendoza", "role": "Student"}
        }

        self.articles = [
            Article("Introduction to Computing", "Martin Lansang", "Discusses foundations of tech.", "Technology",
                    "Published"),
            Article("Principles of Marketing", "Jeffrey Francisco", "Covers core marketing concepts.", "Management",
                    "Published")
        ]

        self.create_login_screen()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_login_screen(self):
        self.clear_window()

        # Left Banner
        left_frame = tk.Frame(self.root, bg="#1b365d", width=425)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        left_content = tk.Frame(left_frame, bg="#1b365d")
        left_content.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        tk.Label(left_content, text="Institutional\nRepository System", font=("Arial", 22, "bold"), bg="#1b365d",
                 fg="white", justify="left").pack(anchor="w", pady=(0, 15))

        sub = "Access scholarly publications,\nresearch papers, and academic works\nin one place."
        tk.Label(left_content, text=sub, font=("Arial", 11), bg="#1b365d", fg="#d0d7de", justify="left").pack(
            anchor="w")

        # Right Form
        bg_col = "#eef2f7"
        right_frame = tk.Frame(self.root, bg=bg_col, width=425)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        right_content = tk.Frame(right_frame, bg=bg_col)
        right_content.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        tk.Label(right_content, text="Welcome Back", font=("Arial", 20, "bold"), bg=bg_col, fg="#1b365d").pack(
            anchor="w", pady=(0, 5))
        tk.Label(right_content, text="Login to your account", font=("Arial", 10), bg=bg_col, fg="#666").pack(anchor="w",
                                                                                                             pady=(0,
                                                                                                                   20))

        self.id_var = tk.StringVar()
        self.pass_var = tk.StringVar()

        self.id_var.trace_add("write", self.check_inputs)
        self.pass_var.trace_add("write", self.check_inputs)

        tk.Label(right_content, text="Username / ID", font=("Arial", 9, "bold"), bg=bg_col, fg="#333").pack(anchor="w")
        self.id_entry = tk.Entry(right_content, textvariable=self.id_var, font=("Arial", 11), width=28, bg="white",
                                 relief="solid", bd=1)
        self.id_entry.pack(anchor="w", pady=(5, 15), ipady=4)

        tk.Label(right_content, text="Password", font=("Arial", 9, "bold"), bg=bg_col, fg="#333").pack(anchor="w")
        self.pass_entry = tk.Entry(right_content, textvariable=self.pass_var, font=("Arial", 11), width=28, bg="white",
                                   show="*", relief="solid", bd=1)
        self.pass_entry.pack(anchor="w", pady=(5, 20), ipady=4)

        self.login_btn = tk.Button(right_content, text="LOGIN", font=("Arial", 10, "bold"), bg="#dcdcdc", fg="#888888",
                                   width=25, relief="flat", command=self.authenticate_user)
        self.login_btn.pack(anchor="w", ipady=8)

    def check_inputs(self, *args):
        has_id = bool(self.id_var.get().strip())
        has_pass = bool(self.pass_var.get().strip())
        if has_id or has_pass:
            self.login_btn.config(bg="#1b365d", fg="white", cursor="hand2")
        else:
            self.login_btn.config(bg="#dcdcdc", fg="#888888", cursor="")

    def authenticate_user(self):
        uid = self.id_var.get().strip()
        pwd = self.pass_var.get().strip()

        if uid not in self.users:
            messagebox.showerror("Access Denied", "User is not yet registered.")
            return

        if self.users[uid]["password"] != pwd:
            messagebox.showerror("Error", "Incorrect password!")
            return

        u_info = self.users[uid]
        messagebox.showinfo("Success", f"Welcome, {u_info['name']} ({u_info['role']}).")

        if u_info["role"] == "Faculty":
            self.open_faculty_portal(uid)
        elif u_info["role"] == "Librarian":
            self.open_librarian_portal(uid)
        elif u_info["role"] == "Student":
            self.open_student_portal(uid)

    def open_change_password(self, uid):
        pw_win = tk.Toplevel(self.root)
        pw_win.title("Change Password")
        pw_win.geometry("350x250")
        pw_win.config(bg="#fefefe")

        tk.Label(pw_win, text="Current Password:", bg="#fefefe").pack(pady=5)
        old_e = tk.Entry(pw_win, show="*", width=25)
        old_e.pack(pady=2)

        tk.Label(pw_win, text="New Password:", bg="#fefefe").pack(pady=5)
        new_e = tk.Entry(pw_win, show="*", width=25)
        new_e.pack(pady=2)

        tk.Label(pw_win, text="Confirm Password:", bg="#fefefe").pack(pady=5)
        cnf_e = tk.Entry(pw_win, show="*", width=25)
        cnf_e.pack(pady=2)

        def save_pw():
            if old_e.get() != self.users[uid]["password"]:
                messagebox.showerror("Error", "Incorrect current password.")
                return
            if new_e.get() == cnf_e.get() and new_e.get() != "":
                self.users[uid]["password"] = new_e.get()
                messagebox.showinfo("Success", "Password updated!")
                pw_win.destroy()
            else:
                messagebox.showerror("Error", "Passwords do not match.")


        tk.Button(pw_win, text="Update Password", command=save_pw).pack(pady=15)

    def open_faculty_portal(self, uid):
        self.clear_window()
        u = self.users[uid]
        f = tk.Frame(self.root, bg="#eef2f7", padx=20, pady=20)
        f.pack(expand=True, fill=tk.BOTH)
        c = tk.Frame(f, bg="#eef2f7")
        c.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        tk.Label(c, text=f"FACULTY PORTAL - {u['name']}", font=("Arial", 16, "bold"), bg="#eef2f7", fg="#1b365d").pack(
            pady=20)
        tk.Button(c, text="Upload New Publication", width=35, bg="white",
                  command=lambda: self.faculty_upload(uid)).pack(pady=8)
        tk.Button(c, text="View My Uploads", width=35, bg="white", command=lambda: self.faculty_view_uploads(uid)).pack(
            pady=8)
        tk.Button(c, text="Change Password", width=35, bg="white", command=lambda: self.open_change_password(uid)).pack(
            pady=8)
        tk.Button(c, text="Log Out", width=35, bg="#cc0000", fg="black", command=self.create_login_screen).pack(pady=15)

    def faculty_upload(self, uid):
        u = self.users[uid]
        up = tk.Toplevel(self.root)
        up.title("Upload")
        up.geometry("450x400")

        tk.Label(up, text="Title:").pack(anchor="w", padx=20, pady=5)
        t_en = tk.Entry(up, width=50)
        t_en.pack(padx=20)

        tk.Label(up, text="Abstract:").pack(anchor="w", padx=20, pady=5)
        a_txt = tk.Text(up, width=45, height=6)
        a_txt.pack(padx=20)

        tk.Label(up, text="Category:").pack(anchor="w", padx=20, pady=5)
        c_en = tk.Entry(up, width=50)
        c_en.pack(padx=20)

        def sub():
            t = t_en.get().strip()
            a = a_txt.get("1.0", tk.END).strip()
            c = c_en.get().strip()
            if not t or not a or not c:
                messagebox.showerror("Error", "Fill all fields!")
                return
            self.articles.append(Article(t, u['name'], a, c, "Pending"))
            messagebox.showinfo("Success", "Uploaded successfully!")
            up.destroy()

        tk.Button(up, text="Submit", bg="#1b365d", fg="white", command=sub).pack(pady=15)

    def faculty_view_uploads(self, uid):
        u = self.users[uid]
        my_art = [x for x in self.articles if u['name'].lower() in x.author.lower()]
        vw = tk.Toplevel(self.root)
        vw.title("My Uploads")
        vw.geometry("650x450")
        txt = tk.Text(vw, wrap=tk.WORD, padx=15, pady=15)
        txt.pack(expand=True, fill=tk.BOTH)
        if not my_art:
            txt.insert(tk.END, "No uploads yet.")
        else:
            for i, art in enumerate(my_art, 1):
                txt.insert(tk.END, f"[{i}] {art}\n    Abstract: {art.abstract}\n\n" + "-" * 50 + "\n")
        txt.config(state=tk.DISABLED)

    def open_librarian_portal(self, uid):
        self.clear_window()
        u = self.users[uid]
        f = tk.Frame(self.root, bg="#eef2f7", padx=20, pady=20)
        f.pack(expand=True, fill=tk.BOTH)
        c = tk.Frame(f, bg="#eef2f7")
        c.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        tk.Label(c, text=f"LIBRARIAN PORTAL - {u['name']}", font=("Arial", 16, "bold"), bg="#eef2f7",
                 fg="#1b365d").pack(pady=20)
        tk.Button(c, text="Review Pending Submissions", width=38, bg="white", command=self.librarian_review).pack(
            pady=8)
        tk.Button(c, text="View All Records", width=38, bg="white", command=self.librarian_view_all).pack(pady=8)
        tk.Button(c, text="Change Password", width=38, bg="white", command=lambda: self.open_change_password(uid)).pack(
            pady=8)
        tk.Button(c, text="Log Out", width=38, bg="#cc0000", fg="white", command=self.create_login_screen).pack(pady=15)

    def librarian_review(self):
        pend = [x for x in self.articles if x.status == "Pending"]
        if not pend:
            messagebox.showinfo("Info", "No pending articles.")
            return
        rv = tk.Toplevel(self.root)
        rv.title("Review")
        rv.geometry("600x450")
        lb = tk.Listbox(rv, width=90, height=18)
        lb.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
        for art in pend:
            lb.insert(tk.END, f"{art.title} (Author: {art.author})")

        def app_sel():
            sel = lb.curselection()
            if not sel:
                return
            art = pend[sel[0]]
            if messagebox.askyesno("Approve", f"Approve '{art.title}'?"):
                art.status = "Published"
                messagebox.showinfo("Success", "Approved!")
                rv.destroy()

        tk.Button(rv, text="Approve Selected", bg="#1b365d", fg="white", command=app_sel).pack(pady=10)

    def librarian_view_all(self):
        aw = tk.Toplevel(self.root)
        aw.title("All Records")
        aw.geometry("650x450")
        txt = tk.Text(aw, wrap=tk.WORD, padx=15, pady=15)
        txt.pack(expand=True, fill=tk.BOTH)
        for i, art in enumerate(self.articles, 1):
            txt.insert(tk.END, f"[{i}] {art}\n    Abstract: {art.abstract}\n\n" + "-" * 50 + "\n")
        txt.config(state=tk.DISABLED)

    def open_student_portal(self, uid):
        self.clear_window()
        u = self.users[uid]
        f = tk.Frame(self.root, bg="#eef2f7", padx=20, pady=20)
        f.pack(expand=True, fill=tk.BOTH)
        c = tk.Frame(f, bg="#eef2f7")
        c.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        tk.Label(c, text=f"STUDENT PORTAL - {u['name']}", font=("Arial", 16, "bold"), bg="#eef2f7", fg="#1b365d").pack(
            pady=20)
        tk.Button(c, text="Search Articles", width=35, bg="white", command=self.student_search).pack(pady=8)
        tk.Button(c, text="View Published Articles", width=35, bg="white", command=self.student_view_published).pack(
            pady=8)
        tk.Button(c, text="Change Password", width=35, bg="white", command=lambda: self.open_change_password(uid)).pack(
            pady=8)
        tk.Button(c, text="Log Out", width=35, bg="#000", fg="black", command=self.create_login_screen).pack(pady=15)

    def student_search(self):
        kw = simpledialog.askstring("Search", "Enter keyword:")
        if not kw:
            return
        kw = kw.lower()
        res = [x for x in self.articles if x.status == "Published" and (
                    kw in x.title.lower() or kw in x.author.lower() or kw in x.abstract.lower())]
        sw = tk.Toplevel(self.root)
        sw.title("Results")
        sw.geometry("650x450")
        txt = tk.Text(sw, wrap=tk.WORD, padx=15, pady=15)
        txt.pack(expand=True, fill=tk.BOTH)
        if not res:
            txt.insert(tk.END, "No matching articles found.")
        else:
            for i, art in enumerate(res, 1):
                txt.insert(tk.END, f"[{i}] {art}\n    Abstract: {art.abstract}\n\n" + "-" * 50 + "\n")
            if messagebox.askyesno("Download", "Download full content?"):
                messagebox.showinfo("Success", "Downloaded successfully!")
        txt.config(state=tk.DISABLED)

    def student_view_published(self):
        pw = tk.Toplevel(self.root)
        pw.title("Published Articles")
        pw.geometry("650x450")
        txt = tk.Text(pw, wrap=tk.WORD, padx=15, pady=15)
        txt.pack(expand=True, fill=tk.BOTH)
        pub = [x for x in self.articles if x.status == "Published"]
        if not pub:
            txt.insert(tk.END, "No published articles.")
        else:
            for i, art in enumerate(pub, 1):
                txt.insert(tk.END, f"[{i}] {art}\n    Abstract: {art.abstract}\n\n" + "-" * 50 + "\n")
        txt.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = InstitutionalRepositoryGUI(root)
    root.mainloop()
