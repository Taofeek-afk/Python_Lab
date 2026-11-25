# Our team's match results are recorded in a collection of strings. 
# Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.

# For example: ["3:1", "2:2", "0:1", ...]

# Points are awarded for each match as follows:

#     if x > y: 3 points (win)
#     if x < y: 0 points (loss)
#     if x = y: 1 point (tie)

# def points(games): # "x:y"
#     point = 0
#     for score in games:
#         if score[0] > score[2]:
#             point += 3
#         elif score[0] == score[2]:
#             point += 1     
#     return point


# print(points(["1:3", "9:7", "2:9"]))
