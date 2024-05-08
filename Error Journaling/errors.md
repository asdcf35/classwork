### Entry 1:

**Date:**: 07/05/2024
**Error:** IndexError: list index out of range
**Description:** Inputted a number that was higher than the highest list index(a page number for a page that doesn't exist)
**Steps Taken:**

- checked to see if I used the wrong number
- checked to see if my expression inside was working
- looked over the input(saw the mistake: I entered 12 instead of 1, causing the error)
**Resolution:** put the code in a try-catch block, prints a message saying the number entered was invalid
