'''List Comprehension'''

# row = []
# for i in range(8):
#     row.append("WHITE_PAWN")
#OR
# row = ["WHITE_PAWN" for i in range(8)]

# print(row)

# #printing the sqaure from 1 to 10
# squares= [x**2 for x in range(1,11)]
# print(squares)


# #2 to the power of till 8
# twos = [2**y for y in range(8)]
# print(twos)


#printing odd no. from list
# squares= [x**2 for x in range(1,11)]
# odds = [x for x in squares if x % 2 != 0]
# print(odds)


'''Two Dimensional Arrays'''
# board = []
# for i in range(8):
#     row = ["EMPTY" for i in range(8)]
#     board.append(row)
# #print board
# for index in board:
#     print(index)
# print(len(board)) #8 list of 8 elements


# #chess board 
# board[0][0] ="Rook"
# board[0][7] ="Rook"
# board[7][0] ="Rook"
# board[7][7] ="Rook"

# board[0][1] ="Knight"
# board[0][6] ="Knight"
# board[7][1] ="Knight"
# board[7][6] ="Knight"

# for index in board:
#     print(index)



'''Multidimensional Arrays'''
  #Temperature in 24(hours) * 31(days) = 744 to be stored 
# temps = [[0.0 for hour in range(24)] for day in range(31)]
# temp1 = 19
# temp2 = 32
# count = 0

# for days in temps:
#     if count == 0:
#         days[11] = temp1
#         count = 1
#     else:
#         days[11] = temp2
#         count = 0
# for index in temps:
#     print(index)

# total = 0.0
# for day in temps:
#     total += day[11]
# average =  total  / 31
# print("Average temperature at noon", average)

# #highest temperature
# highest = -100.0
# for day in temps:
#     for temp in day:
#         if temp > highest:
#             highest = temp
# print("The highest temperature is", highest)

# #hot days
# hot_days =0
# for day in temps:
#     if day[11] > 20.0:
#         hot_days += 1
# print(hot_days, "days were hot days in the month.")

#vacancy in room using multi dimensional array (3d)
rooms = [[[False for r in range (20)]for f in range(15)]for t in range(3)]
print (rooms)
  
rooms[1][9][13] = True
rooms[1][9][1] = True

vacancy =0
for room_number in range(20):
    if not rooms[1][9][room_number]:
        vacancy += 1
print("Vacancy in 10th floor of 3rd building is:",vacancy) 
