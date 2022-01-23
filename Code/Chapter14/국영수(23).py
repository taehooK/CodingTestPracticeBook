def get_input():
    n = int(input())
    students = []
    for i in range(n):
        students.append(input().split())

    return students

def solution(students):
    students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
    for student in students:
        print(student[0])

if __name__ == '__main__':
    students = get_input()
    solution(students)
