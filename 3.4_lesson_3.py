def main(name):
    with open(name) as text_file:
        count = 0
        maths, physics, russian = 0, 0, 0
        for students in text_file:
            student = students.strip('\n').split(';')
            student.pop(0)
            subject = ([int(x) for x in student])
            ball = round(sum([int(x) for x in student]) / 3, 9)
            maths += subject[0]
            physics += subject[1]
            russian += subject[2]
            count += 1
            print(ball, file= open('result.txt', 'a+'))
        print(round(maths / count, 9), round(physics / count, 9), round(russian / count, 9), file= open('result.txt', 'a+'))
main('dataset_3363_4.txt')
                
