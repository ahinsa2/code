def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])  
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True

'''A company has a list of meetings to be held in a single meeting room. Each meeting has a start time and an end time. You must determine if a person can attend all the meetings without overlap.

Input Example: [[0,30],[5,10],[15,20]] → Output: false (because meetings overlap)

Concept: Sorting + Interval Checking

Hint: Sort by start time and check if start[i] < end[i-1].'''
