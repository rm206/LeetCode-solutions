class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        st0, st1 = students.count(0), students.count(1)
        
        while students:
            if students[0] == sandwiches[0]:
                sandwiches.pop(0)
                curr_student = students.pop(0)
                if curr_student == 0:
                    st0 -= 1
                else:
                    st1 -= 1
            
            elif students[0] != sandwiches[0] and ((sandwiches[0] == 0 and st0 > 0) or (sandwiches[0] == 1 and st1 > 0)):
                students.append(students.pop(0))
            
            else:
                break
        
        return st0 + st1
                