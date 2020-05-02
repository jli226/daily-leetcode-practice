# 551. Student Attendance Record I
# Easy

# 243

# 779

# Add to List

# Share
# You are given a string representing an attendance record for a student. The record only contains the following three characters:
# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.
# A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

# You need to return whether the student could be rewarded according to his attendance record.

# Example 1:
# Input: "PPALLP"
# Output: True


def checkRecord(self, s):
        return len(s.split('A')) <= 2 and s.find('LLL') == -1
