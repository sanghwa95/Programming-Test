import json
from collections import OrderedDict
from hashlib import md5
import glob
import os

project_path = input() # 프로젝트 경로 입력 받기

# 지금까지의 커밋 횟수 가져오기
if not os.path.isfile('number_of_commits.txt'):
    f = open('number_of_commits.txt', 'w')
    f.close()
    f = open('number_of_commits.txt', 'r')
else:
    f = open('number_of_commits.txt', 'r')
n = f.readline()
if n == '':
    number_of_commits = 0
else: number_of_commits = int(n)
f.close()

hashcode = md5(str(number_of_commits).encode('utf8')).hexdigest() # commit에 대한 해쉬값 생성

# 테스트 클래스 개수 구하기
def findTestFolder(name, path):
    for dirpath, dirname, filename in os.walk(path):
        if name in dirname:
            return os.path.join(dirpath, name)
test_folder = findTestFolder("test", project_path)
test_class_lst = glob.glob(test_folder+'\\*.class')
number_of_classes = len(test_class_lst)
list_of_classes = ', '.join(test_class_lst)

# 테스트 케이스 개수 구하기
number_of_testcases = 0
list_of_methods = []
test_java_lst = glob.glob(test_folder+'\\*.java')
for test_class in test_java_lst:
    f = open(test_class, "r")
    for line in f.readlines():
        if '@Test' in line:
            number_of_testcases += 1
        if 'public void test' in line:
            list_of_methods.append(line[13:-3])
    f.close()
list_of_methods = ', '.join(list_of_methods)
number_of_commits = number_of_commits + 1
file_data = OrderedDict() # json 파일 만들기

file_data["location"] = project_path
file_data["number_of_commits"] = str(number_of_commits)
file_data["tests_of_commits"] = { 'commits':hashcode, 'num_of_test_classes':number_of_classes, 'number_of_testcases':number_of_testcases, 'list_of_classes':list_of_classes, 'list_of_methods':list_of_methods }

f = open('number_of_commits.txt', 'w')
f.write(str(number_of_commits))
f.close()

print(json.dumps(file_data, ensure_ascii=False, indent="\t"))

# output.json 파일 만들기
with open('output.json', 'w') as outfile:
    json.dump(file_data, outfile, indent="\t")
