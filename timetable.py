
#academicPlan[[год обучения,Буква],[Название предмета,кол во уроков, Технический предмет-1 или гуманитарный-0]]
#teacher[ФИО,Предмет,Количество уроков]
def setTimeTable(academicPlan:[[int,str],[str,int]],teachers:[str,[str,int]]):
    academicPlanLesson = dict()
    for clas in academicPlan:
        for lessons in clas[1]:
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
    if watchLack != dict():
        return watchLack
acdemicPlan = [[[1,"A"],[["Математика",5],["Русский",5]]],[[1,"B"],[["Математика",5],["Английский",5]]]]
Teacher = [["Иванова",[["Русский",10],["Математика",6]]],["Петрова",[["Русский",1],["Английский",6]]]]
b = setTimeTable(1,Teacher)

a=1;



