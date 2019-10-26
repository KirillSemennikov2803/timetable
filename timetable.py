import random
#academicPlan[[год обучения,Буква],[Название предмета,кол во уроков, Технический предмет-1 или гуманитарный-0]]
#teacher[ФИО,Предмет,Количество уроков]
def setTimeTable(academicPlan:[str,[str,int]],teachers:[str,[str,int]]):
    academicPlanLesson = dict()
    academicPlanLessonClass = dict()
    for clas in academicPlan:
        academicPlanLessonClass.update({clas[0]: 0})
        for lessons in clas[1]:
            academicPlanLessonClass[clas[0]] += lessons[1]
            try:
                academicPlanLesson[lessons[0]] += lessons[1]
            except:
                academicPlanLesson.update({lessons[0]:lessons[1]})
    teacherLesson = dict()
    for teacher in teachers:
        for lessons in teacher[1]:
            try:
                teacherLesson[lessons[0]] += lessons[1]
            except:
                teacherLesson.update({lessons[0]: lessons[1]})
    watchLack = dict()
    for Lesson in academicPlanLesson:
        try:
            if teacherLesson[Lesson] < academicPlanLesson[Lesson]:
                watchLack.update({Lesson:academicPlanLesson[Lesson] - teacherLesson[Lesson]})
        except:
            watchLack.update({Lesson: academicPlanLesson[Lesson]})
    if watchLack == dict():
        return watchLack
    schedule = [] # [str,[str,[[int,str,str]]]] [класс,[день недели,[урок,Предмет,препод]]
    for clas in academicPlan:
        index = 0
        schedule.append([clas[0]])
        index2 = 0;
        for i in range(5,0,-1):
            schedule[index].append([dayOfweek(i),[]])
            lessonInDay = round(academicPlanLessonClass[clas[0]] / i)
            academicPlanLessonClass[clas[0]] -= lessonInDay
            random.seed()
            rand = random.randint(0,len(clas[1])-1)
            lesson = clas[1][rand]
            startLesson = 0
            if lesson[1] >= 2 and startLesson + 2 <= lessonInDay:
                schedule[index][1][1].append([startLesson + 1,lesson[0],""])
                schedule[index][1][1].append([startLesson + 2, lesson[0], ""])
                startLesson+=2
                clas[1][rand][1]-=2
                if lesson[1] <= 0:
                    clas[1].remove(lesson)

            else:
                schedule[index][1][1].append([startLesson+1, lesson[0], ""])
                startLesson+=1
                clas[1][rand][1] -= 1
                if lesson[1] <= 0:
                    clas[1].remove(lesson)
            index2+=1
        index += 1
    a = 1

def dayOfweek(a):
    if a == 5:
        return "Понедельник"
    if a == 4:
        return "Вторник"
    if a == 3:
        return "Среда"
    if a == 2:
        return "Четверг"
    if a == 1:
        return "Пятница"





acdemicPlan = [["1 A",[["Математика",5],["Русский",5]]],["1 B",[["Математика",5],["Английский",5]]]]
Teacher = [["Иванова",[["Русский",10],["Математика",6]]],["Петрова",[["Русский",1],["Английский",6]]]]
b = setTimeTable(acdemicPlan,Teacher)

a=1;



