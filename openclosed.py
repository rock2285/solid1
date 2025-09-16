myFile = """Andy 78
Brenda 96
Carl 87
Donna 71
Ernest 26
Faith 98"""


###############################################################
def letter(grade):
    ret = 'N/A'
    if grade >= 0 and grade < 50:
        ret = "F"
    if grade >= 50 and grade < 80:
        ret = "C"
    if grade >= 80 and grade < 101:
        ret = "A"
    return ret


class GradeBook():
    # you should create 2 new classes, one for memory resident behavior
    # and the other for file access. Instanciate both a s members of
    # Gradebook, and have Gradebook delegate its behaviors so that the
    # code in main.py need not change
    def __init__(self):
        self.gb = {}

    # grading method, could be its own function as above
    def letter(self, grade):
        ret = 'N/A'
        if grade >= 0 and grade < 50:
            ret = "F"
        if grade >= 50 and grade < 80:
            ret = "C"
        if grade >= 80 and grade < 101:
            ret = "A"
        return ret

    # file access methods
    def load(self, fileName):
        # load a gradebook from a file into memory
        # each line should have a name and score
        # lines with invalid data or which are for existing students are ignored.
        st = myFile.split("\n")
        for line in st:
            student = line.split()
            self.gb[student[0]] = student[1]

    def store(self, fileName):
        st = ""
        for name in self.gb.keys():
            st = st + name + " " + self.gb[name] + "\n"
        myFile = st

    # memory resident methods
    def update(self, userName, score):
        # change the score for the user--if the user does not exist, add
        self.gb[userName] = str(score)

    def delete(self, userName):
        # remove the given user
        self.gb.pop(userName, 0)

    def display(self):
        for student in self.gb.keys():
            print(student, self.gb[student], self.letter(int(self.gb[student])))


####################################################

gs = [('A', 90), ("B", 80), ("C", 70), ("F", 0)]
gb = GradeBook()
gb.load("scores.txt")
print("before")
gb.display()
print()
gb.update("Gary", 77)
gb.update("Heidi", 68)
gb.update("Andy", 88)
print("after")
gb.display()
gb.store("newscores.txt")
