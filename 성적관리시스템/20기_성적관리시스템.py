# default, 입력하면 다른 값
import sys
import copy
# 파일 읽기
default = 'students.txt'

if len(sys.argv)==1:
    f = open(default, 'r')
elif len(sys.argv) ==2:
    file = sys.argv[1]
    if 'txt' not in file:
        print('다시 입력하세요')
        exit()
    f = open(file, 'r')
else:
    print('다시 입력하세요')
    exit()

# 파일 딕셔너리로 만들기
data  = f.readlines()
stu_dict = {}
for words in data:
    word_lis = words.split()
    name = str(word_lis[1]+' '+word_lis[2])
    stu_dict[word_lis[0]] = [name,int(word_lis[3]), int(word_lis[4])]

# mean, grade 구하기
def mean_grade(stu_dict):
    for stu in stu_dict:
        mean = round((int(stu_dict[stu][1])+int(stu_dict[stu][2]))/2, 1)
        if mean >= 90:
            grade = 'A'
        elif mean >= 80:
            grade = 'B'
        elif mean >= 70:
            grade = 'C'
        elif mean >= 60:
            grade = 'D'
        else:
            grade = 'F'
        stu_dict[stu].append(mean)
        stu_dict[stu].append(grade)
    return stu_dict
    

def show(stu_dict):
    # 기본으로 출력하기
    print('  Student         Name        Midterm  Final  Average  Grade   ')
    print('-----------------------------------------------------------')

    stu_dict = sorted(stu_dict.items(), key = lambda a:a[1][3], reverse=True)
    print_list = copy.deepcopy(stu_dict)
    for stu in print_list:
        print(stu[0], end='     ')
        if len(stu[1][0]) < 16:
            stu[1][0] = str(stu[1][0]+' '*(16-len(stu[1][0])))
        for num in stu[1]:
            print(num, end='     ')
        print('\n')
        

# search 함수
def search(stu_dict, stu_id):
    print_list = copy.deepcopy(stu_dict)
        
    if stu_id in print_list:
        print('  Student         Name      Midterm  Final  Average  Grade   ')
        print('-----------------------------------------------------------')
        print(stu_id, end='   ')
        if len(print_list[stu_id][0]) < 16:
            print_list[stu_id][0] = ' '*(16-len(print_list[stu_id][0])) +print_list[stu_id][0]
        for num in print_list[stu_id]:
            print(num, end='     ')
        print('')
    else:
        print('NO SUCH PERSON.')
        pass
    
def changescore(stu_dict, stu_id):
    test_type = ['mid', 'final']
    
    if stu_id not in stu_dict:
        print('NO SUCH PERSON.')
        pass
    else:
        test = input('Mid/Final?').lower()
        if test not in test_type:
            pass
        else:
            score = int(input('Input new score:'))
            if score not in list(range(1, 101)):
                pass
            else:
                search(stu_dict, stu_id)
                print('\n\n')
                for stu in stu_dict:
                    stu_dict[stu] = stu_dict[stu][:-2]
                if test == 'mid':
                    stu_dict[stu_id][1] = int(score)
                else:
                    stu_dict[stu_id][2] = int(score) 
                mean_grade(stu_dict)
                print('Score changed.')
                search(stu_dict, stu_id)
                print('')
    return stu_dict

def add(stu_dict, stu_id):
    if stu_id in stu_dict:
        print('ALREADY EXISTS.')
    else:
        name = input('Name:')
        mid = int(input('Midterm Score:'))
        final = int(input('Final Score:'))
        for stu in stu_dict:
            stu_dict[stu] = stu_dict[stu][:-2]
        stu_dict[stu_id] = [name, mid, final]
        mean_grade(stu_dict)
        print('Score added.')
    return stu_dict
        
def searchgrade(stu_dict, gr):
    grade_list = ['A', 'B', 'C', 'D', 'F']
    if gr not in grade_list:
        pass
    else:
        id_list = []
        for item in stu_dict:S
            if stu_dict[item][4] == gr:
                id_list.append(item)
        if len(id_list) == 0:
            print('NO RESULTS.')
            pass
        else:
            print('  Student         Name      Midterm  Final  Average  Grade   ')
            print('-----------------------------------------------------------')
            for stu_id in id_list:
                print(stu_id, end='   ')
                print_list = copy.deepcopy(stu_dict)
                if len(print_list[stu_id][0]) < 16:
                    print_list[stu_id][0] = ' '*(16-len(print_list[stu_id][0])) +print_list[stu_id][0]
                for num in print_list[stu_id]:
                    print(num, end='     ')
            print('')
        
def remove(stu_dict) :
    if len(stu_dict) == 0:
        print('List is empty')
    else:
        stu_id = input('Student ID:')
        if stu_id not in stu_dict:
            print('NO SUCH PERSON.')
            pass
        else:
            stu_dict.pop(stu_id)
            print('Student removed.')
    return stu_dict

def quit(stu_dict):
    save = input('Save data?[yes/no] ')
    if save == 'yes':
        stu_dict = sorted(stu_dict.items(), key = lambda a:a[1][3], reverse=True)
        file = input('File name:')
        result = open(file, 'w')
        for stu in stu_dict:
            num = stu[0]
            name = stu[1][0]
            mid = stu[1][1]
            fin = stu[1][2]
            data = '{0} {1} {2} {3}\n'.format(num,name, mid, fin)
            result.write(data)
        f.close()
        result.close()
        print('$')
        exit()
    else:
        f.close()
        print('$')
        exit()

                
mean_grade(stu_dict)
show(stu_dict)
            
# 명령어 시작
while True:
    # 명령어 받을 준비    
    order = input('# ').lower()
    
    # show
    if order=='show':
        show(stu_dict)
    elif order == 'search':
        stu_id = input('Student ID:')
        search(stu_dict, stu_id)
    elif order == 'changescore':
        stu_id = input('Student ID:')
        changescore(stu_dict, stu_id)
    elif order == 'add':
        stu_id = input('Student ID:')
        add(stu_dict, stu_id)
    elif order == 'searchgrade':
        gr = input('Grade to search:')
        searchgrade(stu_dict, gr)
    elif order=='remove':
        remove(stu_dict) 
    elif order == 'quit':
        quit(stu_dict)
    else:
        print('error!')
        


f.close()

