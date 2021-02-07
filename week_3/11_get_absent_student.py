all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]
class LinkedTuple:
    def __init__(self):
        self.items = list()
    def add(self,key,value):
        self.items.append((key,value))
    def get(self, key):
        for k, v in self.items:
            if key == k:
                return v

class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())
    def put(self, key, value):
        self.items[hash(key) % len(self.items)].add(key, value)
        # return
    def get(self, key):
        return self.items[hash(key) % len(self.items)].get(key)

def get_absent_student(all_array, present_array):
    # 구현해보세요!
    student_dict = {}
    for key in all_array:
        student_dict[key] = True # O(N) (also O(N) for spatial complexity)
    for key in present_array:
        del student_dict[key] # O(N)
    for key in student_dict.keys():
        return key
# -> final temporal complexity: O(N)

print(get_absent_student(all_students, present_students))