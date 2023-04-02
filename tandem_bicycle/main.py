# time: O(nlogn) | space: O(1)
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    if fastest:
        blueShirtSpeeds.sort(reverse = True)
    else:
        blueShirtSpeeds.sort()

    totalSpeed = 0
    for (redSpeed, blueSpeed) in zip(redShirtSpeeds, blueShirtSpeeds):
        totalSpeed += max(redSpeed, blueSpeed)    
    # Write your code here.
    return totalSpeed



redShirtSpeeds = [5,5,3,9,2]
blueShirtSpeeds = [3,6,7,2,1]
fastest = True

print(tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest))