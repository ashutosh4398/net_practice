# O(nlogn) time | O(1) space
# nlogn since we are sorting
# 

def decide_rows(redShirtHeights, blueShirtHeights):
    # returns smaller row, larger row ie front row, back row
    tallerRed = redShirtHeights[-1]
    tallerBlue = blueShirtHeights[-1]
    if tallerRed < tallerBlue:
        return (redShirtHeights, blueShirtHeights)
    return (blueShirtHeights, redShirtHeights)
    
    


def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    # sort both students height wise
    redShirtHeights.sort()
    blueShirtHeights.sort()

    front_row, back_row = decide_rows(redShirtHeights, blueShirtHeights)
    for (r1, r2) in zip(front_row, back_row):
        if r1 >= r2:
            return False

    return True


print(classPhotos([5,8,1,3,4], [6,9,2,4,5]))