
"""
Yuslen Lopez

The following is the provided solutions to Google's Apply Your Knowledge Video Part: 1 

Problem: There is a hotel with 10 floors and each floor has 26 rooms.
You want to keep a track of how many room are occupied. The reservations are
structure with a string who's first char is + or - for if booking or freeing.
And the next two chars include a digit for the floor and a letter for the room.
How many rooms are occupied?


"""



def hotel_count_occupied(A: list):
    #--------------------------solution 1------------------#
    # # Time: O(N) Space: O(1) for data structure of set size

    # #data structure defining array of arrays
    # hotel = [[0 for _ in range(26)]for _ in range (10)]

    # for reservation in A:
    #   floor = int(reservation[1])
    #   #ord returns ASCII value of letters and then we subtract minus the starting letter ASCII value
    #   room = ord(reservation[2])-ord("A")

    #   if reservation[0] =="+":
    #     hotel[floor][room] = 1
    #   else:
    #     hotel[floor][room] = 0

    # bookings = 0
    # for floor in hotel:
    #   for room in floor:
    #     bookings+=room

    # return bookings

    #------------------------solution 2 (using sets)---------------------------------#


    # Time: O(N) Space: O(1)
    booking = set()

    for reservation in A:
      if reservation[0] == "+":
        booking.add(reservation[1:])
      else:
        booking.remove(reservation[1:])

    return len(booking)



print(hotel_count_occupied(["+0A","+9Z","+4F","-9Z","+3G","+9Z"])) #4 rooms
print(hotel_count_occupied(["+4B","-4B","+4B","-4B"])) #0 rooms
print(hotel_count_occupied(["+4A","+5B","+5A"])) #3 rooms
