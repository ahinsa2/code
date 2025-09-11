/*A company has a list of meetings to be held in a single meeting room. Each meeting has a start time and an end time. You must determine if a person can attend all the meetings without overlap.

Input Example: [[0,30],[5,10],[15,20]] → Output: false (because meetings overlap) 

Concept: Sorting + Interval Checking 

Hint: Sort by start time and check if start[i] < end[i-1].

REVISIT THIS ONE
*/
import java.util.*;

public class MeetingRoomScheduler {
    public static boolean canAttendMeetings(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] < intervals[i - 1][1]) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        int[][] meetings1 = {{0,30},{5,10},{15,20}};
        System.out.println(canAttendMeetings(meetings1)); // false

        int[][] meetings2 = {{7,10},{2,4}};
        System.out.println(canAttendMeetings(meetings2)); // true
    }
}
