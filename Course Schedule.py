class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        incoming = [0 for _ in range(numCourses)]

        for course, pre in prerequisites:
            graph[pre].append(course)
            incoming[course] += 1

        queue = deque()
        taken_course = []
        for course in range(numCourses):
            if incoming[course] == 0:
                queue.append(course)

        
        while queue:
            course = queue.popleft()
            taken_course.append(course)

            for ngh in graph[course]:
                incoming[ngh] -= 1

                if incoming[ngh] == 0:
                    queue.append(ngh)
       
        if len(taken_course) == numCourses:
            return True
        return False
