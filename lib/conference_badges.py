def badge_maker(name):
    badge = f"Hello, my name is {name}."
    return badge

def batch_badge_creator(names):
    batch = []
    for name in names:
        batch.append(badge_maker(name))
    return batch

def assign_rooms(names):
    rooms = []
    index = 0
    for name in names:
        assign_room = f"Hello, {name}! You'll be assigned to room {index+1}!"
        rooms.append(assign_room)
        index += 1
    return rooms

def printer(names):
    for name in names:
        print(badge_maker(name))
        rooms = assign_rooms(names)
    for room in rooms:
        print(room)
