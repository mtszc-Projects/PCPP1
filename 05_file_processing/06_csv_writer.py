"""
3.4.1.1 LAB: CSV – Lab 2
https://edube.org/learn/pcpp1-5/lab-csv-lab-2
Have you ever prepared a report? Your task will be to prepare a report summarizing the results of exams in maths,
physics and biology. The report should include the name of the exam, the number of candidates, the number of passed
exams, the number of failed exams, and the best and the worst scores. All the data necessary to create the report is in
the exam_results.csv file.
Note that one candidate may have several results for the same exam. The number of candidates should express the number
of unique people in each exam identified by Candidate ID. The final report should look like this:
Exam Name,Number of Candidates,Number of Passed Exams,Number of Failed Exams,Best Score,Worst Score
Maths,8,4,6,90,33
Physics,3,0,3,66,50
Biology,5,2,3,88,23
"""
import csv


class Exam:
    def __init__(self, name, candidates, passes, fails, bests, worsts):
        self.name = name
        self.candidates = candidates
        self.passes = passes
        self.fails = fails
        self.bests = bests
        self.worsts = worsts


class Results:
    __exams = []

    @classmethod
    def append_exams(cls, exam):
        cls.__exams.append(exam)

    @staticmethod
    def grab_exam(file, name):
        with open(file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            exam = [exam for exam in reader if exam['Exam Name'] == f'{name}']
            return exam

    @staticmethod
    def count_candidates(exam):
        candidates = []
        for candidate in exam:
            if candidate['Candidate ID'] not in candidates:
                candidates.append(candidate['Candidate ID'])
        return candidates

    @staticmethod
    def count_passes_fails(exam, grade):
        counter = 0
        for result in exam:
            if result['Grade'] == grade:
                counter += 1
        return counter

    @staticmethod
    def grab_score(exam, score):
        if score == 'max':
            maximum = 0
            for points in exam:
                if int(points['Score']) > maximum:
                    maximum = int(points['Score'])
            return maximum
        else:
            minimum = 100
            for points in exam:
                if int(points['Score']) < minimum:
                    minimum = int(points['Score'])
            return minimum

    def load_results_from_csv(self, file):
        maths = self.grab_exam(file, 'Maths')
        physics = self.grab_exam(file, 'Physics')
        biology = self.grab_exam(file, 'Biology')
        exams = [['Maths', maths], ['Physics', physics], ['Biology', biology]]
        for exam in exams:
            self.append_exams(Exam(exam[0],
                                   len(self.count_candidates(exam[1])),
                                   self.count_passes_fails(exam[1], 'Pass'),
                                   self.count_passes_fails(exam[1], 'Fail'),
                                   self.grab_score(exam[1], 'max'),
                                   self.grab_score(exam[1], 'min')))

    @classmethod
    def dump_to_file(cls, file):
        with open(file, 'w', newline='') as csvfile:
            fieldnames = ['Exam Name',
                          'Number of Candidates',
                          'Number of Passed Exams',
                          'Number of Failed Exams',
                          'Best Score',
                          'Worst Score']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for exam in cls.__exams:
                writer.writerow({'Exam Name': f'{exam.name}',
                                 'Number of Candidates': f'{exam.candidates}',
                                 'Number of Passed Exams': f'{exam.passes}',
                                 'Number of Failed Exams': f'{exam.fails}',
                                 'Best Score': f'{exam.bests}',
                                 'Worst Score': f'{exam.worsts}'})


results_1 = Results()
results_1.load_results_from_csv('exam_results.csv')
results_1.dump_to_file('exam_results_processed.csv')

# TODO: Expected result
"""
Exam Name,Number of Candidates,Number of Passed Exams,Number of Failed Exams,Best Score,Worst Score
Maths,8,4,6,90,33
Physics,3,0,3,66,50
Biology,5,2,3,88,23
"""