class Transcript:

    def __init__(self):
        self.subjects = []

    def add_subject(self, subject):
        """Add a subject to self.subjects
        
        Arguments:
            subject {Subject}
        """

        self.subjects.append(subject)

    def get_wam(self):
        """Calculates your WAM (Weighted Average Mark) based on all the subjects in self.subjects
        
        Returns:
            float -- WAM
        """

        total_credits = 0
        total_marks = 0

        for each in self.subjects:
            total_credits += each.get_credit_points()
            total_marks += each.get_mark() * each.get_credit_points()

        if total_credits == 0:
            return 0

        wam = total_marks / total_credits
        return wam

    def print_transcript(self):
        print("Year\tSession\tCode\tName\t Mark\tCPs")
        for each in self.subjects:
            print("\t".join([each.year, each.session, each.unit_code, each.name, each.mark, each.credit_points]))

    def __str__(self):
        pass


class Subject:

    def __init__(self, year, session, code, name, mark, credit_points):
        self.unit_code = code
        self.name = name
        self.department = code[:4]
        self.level = code[4]
        self.year = year
        self.session = session
        self.credit_points = credit_points
        self.mark = mark

    def get_credit_points(self):
        return self.credit_points

    def get_mark(self):
        return self.mark

    def __str__(self):
        pass


