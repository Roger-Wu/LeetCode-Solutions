class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self.prereqList = [[] for i in xrange(numCourses)]
        for prereq in prerequisites:
            self.prereqList[prereq[0]].append(prereq[1])

        self.courseTaken = [False]*numCourses
        self.courseWillTake = [False]*numCourses
        self.courseTakenOrder = []

        for course in xrange(numCourses):
            if self.takeCourse(course) == "prereq cycle":
                return []
        return self.courseTakenOrder

    def takeCourse(self, course):
        # recursively take courses

        if self.courseTaken[course]:
            return "has taken"
        if self.courseWillTake[course]:
            # if a course has not been taken but has been tried to take, it forms a prereq cycle
            return "prereq cycle"

        self.courseWillTake[course] = True

        # take all the prerequisite courses
        for prereq in self.prereqList[course]:
            if self.takeCourse(prereq) == "prereq cycle":
                # halt if detects a prereq cycle
                return "prereq cycle"

        # after all the prereqs are taken, take this course
        self.courseTakenOrder.append(course)
        self.courseTaken[course] = True
        return "taken"
