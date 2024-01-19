def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    # batch = [badge_maker(name) for name in names ]
    # for name in names:
    #     batch.append(badge_maker(name))
    return [badge_maker(name) for name in names]

def assign_rooms(names):
    index = 0
    rooms = []
    for name in names:
        #assign_room = f"Hello, {name}! You'll be assigned to room {index+1}!"
        rooms.append(f"Hello, {name}! You'll be assigned to room {index+1}!")
        index += 1
    return rooms

def printer(names):
    for name in names:
        print(badge_maker(name))
        rooms = assign_rooms(names)
    for room in rooms:
        print(room)
