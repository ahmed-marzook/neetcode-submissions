class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i = 0
        while sandwiches and i < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0);
                sandwiches.pop(0);
                i = 0
            else:
                temp = students.pop(0);
                students.append(temp)
                i += 1
        
        return len(students);
