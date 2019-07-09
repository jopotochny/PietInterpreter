from PIL import Image
import heapq
BLACK = '#000000'
WHITE = '#ffffff'
LIGHT_RED = ['#ffc0c0', 'ffbfc0', 'ffbdbe']
RED = ['#ff0000']
DARK_RED = ['#c00000', 'd20000']
LIGHT_YELLOW = ['#ffffc0', 'feffb8']
YELLOW = ['#ffff00', 'feff00']
DARK_YELLOW = ['#c0c000', 'c1c000', 'bfc200']
LIGHT_GREEN = ['#c0ffc0', 'c0ffbf', 'adffba']
GREEN = ['#00ff00']
DARK_GREEN = ['#00c000', '00c500']
LIGHT_CYAN = ['#c0ffff']
CYAN = ['#00ffff']
DARK_CYAN = ['#00c0c0', '00c0c1', '00c3c2']
LIGHT_BLUE = ['#c0c0ff', 'c1c0ff', 'c1bfff']
BLUE = ['#0000ff', '1500ff', '1c00ff']
DARK_BLUE = ['#0000c0', '0c00c0', '1300c8']
LIGHT_MAGENTA = ['#ffc0ff', 'ffbbff']
MAGENTA = ['#ff00ff', 'ff01ff']
DARK_MAGENTA = ['#c000c0', 'd200c7']

stack = []


# can point up, down, left, or right
dp_directions = ['right', 'down', 'left', 'up']
direction_pointer = 'right'
def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)
# can point left or right
codel_chooser = 'left'

image_path = './images/fib_piet.png'
img = Image.open(image_path)
pixels = img.convert('RGBA').load()
width, height = img.size

pixel_coord_x = 0
pixel_coord_y = 0
def pretty_print_color(color):
    if color in LIGHT_RED:
        print("Light Red")
    if color in RED:
        print("Red")
    if color in DARK_RED:
        print("Dark Red")
    if color in LIGHT_YELLOW:
        print("Light Yellow")
    if color in YELLOW:
        print("Yellow")
    if color in DARK_YELLOW:
        print("Dark Yellow")
    if color in LIGHT_GREEN:
        print("Light Green")
    if color in GREEN:
        print("Green")
    if color in DARK_GREEN:
        print("Dark Green")
    if color in LIGHT_CYAN:
        print("Light Cyan")
    if color == CYAN:
        print("Cyan")
    if color in DARK_CYAN:
        print("Dark Cyan")
    if color in LIGHT_BLUE:
        print("Light Blue")
    if color in BLUE:
        print("Blue")
    if color in DARK_BLUE:
        print("Dark Blue")
    if color in LIGHT_MAGENTA:
        print("Light Magenta")
    if color in MAGENTA:
        print("Magenta")
    if color in DARK_MAGENTA:
        print("Dark Magenta")

def calculate_color_properties(color):
    color_hue = 0
    color_darkness = 0
    if color in LIGHT_RED:
        color_hue = 0
        color_darkness = 0
    elif color in RED:
        color_hue = 0
        color_darkness = 1
    elif color in DARK_RED:
        color_hue = 0
        color_darkness = 2
    elif color in LIGHT_YELLOW:
        color_hue = 1
        color_darkness = 0
    elif color in YELLOW:
        color_hue = 1
        color_darkness = 1
    elif color in DARK_YELLOW:
        color_hue = 1
        color_darkness = 2
    elif color in LIGHT_GREEN:
        color_hue = 2
        color_darkness = 0
    elif color in GREEN:
        color_hue = 2
        color_darkness = 1
    elif color in DARK_GREEN:
        color_hue = 2
        color_darkness = 2
    elif color in LIGHT_CYAN:
        color_hue = 3
        color_darkness = 0
    elif color in CYAN:
        color_hue = 3
        color_darkness = 1
    elif color in DARK_CYAN:
        color_hue = 3
        color_darkness = 2
    elif color in LIGHT_BLUE:
        color_hue = 4
        color_darkness = 0
    elif color in BLUE:
        color_hue = 4
        color_darkness = 1
    elif color in DARK_BLUE:
        color_hue = 4
        color_darkness = 2
    elif color in LIGHT_MAGENTA:
        color_hue = 5
        color_darkness = 0
    elif color in MAGENTA:
        color_hue = 5
        color_darkness = 1
    elif color in DARK_MAGENTA:
        color_hue = 5
        color_darkness = 2
    return {
        'color': color,
        'color_hue': color_hue,
        'color_darkness': color_darkness
    }
def calculate_color_change(initial_color, new_color):
    initial_color_properties = calculate_color_properties(initial_color)
    new_color_properties = calculate_color_properties(new_color)
    if initial_color_properties['color_hue'] <= new_color_properties['color_hue']:
        hue_change = new_color_properties['color_hue'] - initial_color_properties['color_hue']
    else:
        hue_change = new_color_properties['color_hue'] - initial_color_properties['color_hue'] + 6
    if initial_color_properties['color_darkness'] <= new_color_properties['color_darkness']:
        darkness_change = new_color_properties['color_darkness'] - initial_color_properties['color_darkness']
    else:
        darkness_change = new_color_properties['color_darkness'] - initial_color_properties['color_darkness'] + 3
    return hue_change, darkness_change
def do_operation(hue_change, darkness_change, value):
    global stack
    print("Hue change: {}, Darkness change: {}".format(hue_change, darkness_change))
    if hue_change == 0:
        if darkness_change == 0:
            return
        elif darkness_change == 1:
            stack.append(value)
            print("Pushed {} onto the stack".format(value))
        elif darkness_change == 2:
            stack.pop()
            print("Popped top value off of stack")
    if hue_change == 1:
        if darkness_change == 0:
            first_value = stack.pop()
            second_value = stack.pop()
            stack.append(first_value + second_value)
            print("Popped and added {} and {} and pushed {} onto stack".format(first_value, second_value, first_value + second_value))
        elif darkness_change == 1:
            first_value = stack.pop()
            second_value = stack.pop()
            stack.append(second_value - first_value)
            print("Popped and subtracted {} from {} and pushed {} onto the stack".format(second_value, first_value, second_value - first_value))
        elif darkness_change == 2:
            first_value = stack.pop()
            second_value = stack.pop()
            stack.append(first_value * second_value)
            print("Popped and multiplied {} and {} and pushed {} onto stack".format(first_value, second_value, first_value * second_value))
    if hue_change == 2:
        if darkness_change == 0:
            first_value = stack.pop()
            second_value = stack.pop()
            stack.append(second_value / first_value)
            print("Popped and divided {} from {} and pushed {} onto the stack".format(second_value, first_value, second_value / first_value))
        elif darkness_change == 1:
            first_value = stack.pop()
            second_value = stack.pop()
            mod_value = second_value % first_value
            if first_value < 0:
                if mod_value > 0:
                    mod_value *= -1
            else:
                if mod_value < 0:
                    mod_value *= -1
            stack.append(mod_value)
        elif darkness_change == 2:
            first_value = stack.pop()
            if first_value != 0:
                stack.append(0)
            else:
                stack.append(1)
    if hue_change == 3:
        if darkness_change == 0:
            first_value = stack.pop()
            second_value = stack.pop()
            if second_value > first_value:
                stack.append(1)
            else:
                stack.append(0)
        elif darkness_change == 1:
            first_value = stack.pop()
            if first_value < 0:
                for i in range(abs(first_value)):
                    toggleDP_anticlockwise()
            else:
                for i in range(first_value):
                    toggleDP_clockwise()
        elif darkness_change == 2:
            first_value = stack.pop()
            for i in range(abs(first_value)):
                toggleCC()
    if hue_change == 4:
        if darkness_change == 0:
            stack.append(stack[-1])
        elif darkness_change == 1:
            # need to do roll
            first_value = stack.pop()
            second_value = stack.pop()
            roll_stack(first_value, second_value)
        elif darkness_change == 2:
            val = input("Please input an integer")
            stack.append(int(val))
    if hue_change == 5:
        if darkness_change == 0:
            val = input("Please input one character")
            stack.append(val)
        elif darkness_change == 1:
            first_value = stack.pop()
            print(first_value)
        elif darkness_change == 2:
            first_value = stack.pop()
            print(str(chr(first_value)))


def roll_stack(num_rolls, depth):
    if depth < 0:
        return
    if num_rolls < 0:
        # negative rolls
        for i in range(abs(num_rolls)):
            val = stack.pop(0)
            stack.insert(depth, val)
    else:
        for i in depth(num_rolls):
            val = stack.pop()
            stack.insert(len(stack) - 1 - depth, val)

def toggleCC():
    global codel_chooser
    if codel_chooser == 'left':
        codel_chooser = 'right'
    else:
        codel_chooser = 'left'

def toggleDP_clockwise():
    global direction_pointer
    if direction_pointer == 'right':
        direction_pointer = 'down'
    elif direction_pointer == 'down':
        direction_pointer = 'left'
    elif direction_pointer == 'left':
        direction_pointer = 'up'
    else:
        direction_pointer = 'right'

def toggleDP_anticlockwise():
    global direction_pointer
    if direction_pointer == 'right':
        direction_pointer = 'up'
    elif direction_pointer == 'down':
        direction_pointer = 'right'
    elif direction_pointer == 'left':
        direction_pointer = 'down'
    else:
        direction_pointer = 'left'

def get_codals_in_current_block(initialX, initialY, image):
    count = 1
    x = initialX
    y = initialY
    pixels = image.convert('RGBA').load()
    r, g, b, a = pixels[x, y]
    color = rgb2hex(r, g, b)
    coords_seen = [(x,y)]
    stack = [(x,y)]
    width, height = image.size
    new_pixel = None
    while len(stack) > 0:
        x, y = stack.pop()
        if x > 0 and coords_seen.count((x - 1, y)) == 0:
            # check left neighbor
            new_pixel = (x - 1, y)
            coords_seen.append(new_pixel)
            r, g, b, a = pixels[new_pixel[0], new_pixel[1]]
            if rgb2hex(r, g, b) == color:
                # then we should expand here too
                count += 1
                stack.append(new_pixel)
        if x < width - 1 and coords_seen.count((x + 1, y)) == 0:
            # check right neighbor
            new_pixel = (x + 1, y)
            coords_seen.append(new_pixel)
            r, g, b, a = pixels[new_pixel[0], new_pixel[1]]
            if rgb2hex(r, g, b) == color:
                # then we should expand here too
                count += 1
                stack.append(new_pixel)
        if y > 0 and coords_seen.count((x , y - 1)) == 0:
            # check up neighbor
            new_pixel = (x, y - 1)
            coords_seen.append(new_pixel)
            r, g, b, a = pixels[new_pixel[0], new_pixel[1]]
            if rgb2hex(r, g, b) == color:
                # then we should expand here too
                count += 1
                stack.append(new_pixel)
        if y < height - 1 and coords_seen.count((x, y + 1)) == 0:
            # check down neighbor
            new_pixel = (x, y + 1)
            coords_seen.append(new_pixel)
            r, g, b, a = pixels[new_pixel[0], new_pixel[1]]
            if rgb2hex(r, g, b) == color:
                # then we should expand here too
                count += 1
                stack.append(new_pixel)
    eight_exit_points = {
        'up': {
            'right': (),
            'left': ()
        },
        'right': {
            'right': (),
            'left': ()
        },
        'down': {
            'right': (),
            'left': ()
        },
        'left': {
            'right': (),
            'left': ()
        }
    }
    bad_coords = []
    for coord in coords_seen:
        r, g, b, a = pixels[coord[0], coord[1]]
        if color != rgb2hex(r, g, b):
            bad_coords.append(coord)
    coords_seen[:] = [x for x in coords_seen if x not in bad_coords]

    sorted_x = sorted(coords_seen, reverse=True)
    largest_x = sorted_x[0][0]
    filtered_x = list(filter(lambda x: x[0] == largest_x, sorted_x))

    if len(filtered_x) == 1:
        # then for the right side of the block we only have one codel
        eight_exit_points['right']['right'] = filtered_x[0]
        eight_exit_points['right']['left'] = filtered_x[0]
    else:
        # we have two codels for the right side
        sorted_xy = sorted(filtered_x, key=lambda x: x[1], reverse=True)
        eight_exit_points['right']['right'] = sorted_xy[0]
        eight_exit_points['right']['left'] = sorted_xy[-1]

    smallest_x = sorted_x[-1][0]
    filtered_x = list(filter(lambda x: x[0] == smallest_x, sorted_x))

    if len(filtered_x) == 1:
        # then for the left side of the block we only have one codel
        eight_exit_points['left']['right'] = filtered_x[0]
        eight_exit_points['left']['left'] = filtered_x[0]
    else:
        # we have two codels for the left side
        sorted_xy = sorted(filtered_x, key=lambda x: x[1], reverse=False)
        eight_exit_points['left']['right'] = sorted_xy[0]
        eight_exit_points['left']['left'] = sorted_xy[-1]

    sorted_y = sorted(coords_seen, key=lambda x: x[1], reverse=True)
    largest_y = sorted_y[0][1]
    filtered_y = list(filter(lambda x: x[1] == largest_y, sorted_y))

    if len(filtered_y) == 1:
        # then for the bottom side of the block we only have one codel
        eight_exit_points['down']['right'] = filtered_y[0]
        eight_exit_points['down']['left'] = filtered_y[0]
    else:
        # we have two codels for the bottom side
        sorted_yx = sorted(filtered_y, key=lambda x: x[0], reverse=True)
        eight_exit_points['down']['right'] = sorted_yx[-1]
        eight_exit_points['down']['left'] = sorted_yx[0]

    smallest_y = sorted_y[-1][1]
    filtered_y = list(filter(lambda x: x[1] == smallest_y, sorted_y))

    if len(filtered_y) == 1:
        # then for the top side of the block we only have one codel
        eight_exit_points['up']['right'] = filtered_y[0]
        eight_exit_points['up']['left'] = filtered_y[0]
    else:
        # we have two codels for the top side
        sorted_yx = sorted(filtered_y, key=lambda x: x[0], reverse=False)
        eight_exit_points['up']['right'] = sorted_yx[-1]
        eight_exit_points['up']['left'] = sorted_yx[0]
    return count, eight_exit_points

def get_next_pixel(initialX, initialY, image):
    x = initialX
    y = initialY
    width, height = image.size
    pixels = image.convert('RGBA').load()
    r, g, b, a = pixels[x, y]
    current_color = rgb2hex(r, g, b)
    while True:
        # move in direction of direction_pointer
        if direction_pointer == 'right':
            x = x + 1
            if x < width:
                r, g, b, a = pixels[x, y]
                if rgb2hex(r, g, b) == BLACK:
                    toggleCC()
                    return initialX, initialY, current_color
                elif rgb2hex(r, g, b) == WHITE:
                    continue
                elif rgb2hex(r, g, b) != current_color:
                    return x, y, rgb2hex(r, g, b)
            else:
                # then we have fallen off, need to toggle CC
                toggleCC()
                return initialX, initialY, current_color
        if direction_pointer == 'down':
            y = y + 1
            if y < height:
                r, g, b, a = pixels[x, y]
                if rgb2hex(r, g, b) == BLACK:
                    toggleCC()
                    return initialX, initialY, current_color
                elif rgb2hex(r, g, b) == WHITE:
                    continue
                elif rgb2hex(r, g, b) != current_color:
                    return x, y, rgb2hex(r, g, b)
            else:
                # then we have fallen off, need to toggle CC
                toggleCC()
                return initialX, initialY, current_color
        if direction_pointer == 'left':
            x = x - 1
            if x > -1:
                r, g, b, a = pixels[x, y]
                if rgb2hex(r, g, b) == BLACK:
                    toggleCC()
                    return initialX, initialY, current_color
                elif rgb2hex(r, g, b) == WHITE:
                    continue
                elif rgb2hex(r, g, b) != current_color:
                    return x, y, rgb2hex(r, g, b)
            else:
                # then we have fallen off, need to toggle CC
                toggleCC()
                return initialX, initialY, current_color
        if direction_pointer == 'up':
            y = y - 1
            if y > -1:
                r, g, b, a = pixels[x, y]
                if rgb2hex(r, g, b) == BLACK:
                    toggleCC()
                    return initialX, initialY, current_color
                elif rgb2hex(r, g, b) == WHITE:
                    continue
                elif rgb2hex(r, g, b) != current_color:
                    return x, y, rgb2hex(r, g, b)
            else:
                # then we have fallen off, need to toggle CC
                toggleCC()
                return initialX, initialY, current_color

currentX = 0
currentY = 0
num_tries = 0

while True:
    current_num, exit_points = get_codals_in_current_block(currentX, currentY, img)
    print("Number of codels in current block: {}".format(current_num))
    # start checking if we can continue
    currentX, currentY = exit_points[direction_pointer][codel_chooser]
    r, g, b, a = pixels[currentX, currentY]
    current_color = rgb2hex(r, g, b)
    newX, newY, newColor = get_next_pixel(currentX, currentY, img)
    num_tries += 1
    if newX == currentX and newY == currentY:
        # then we haven't moved, need to check next
        if num_tries % 2 == 0:
            toggleDP_clockwise()
        if num_tries == 8:
            # terminate
            print("Terminating...")
            exit(0)
    else:
        num_tries = 0
        hue_change, darkness_change = calculate_color_change(current_color, newColor)
        do_operation(hue_change, darkness_change, current_num)
        currentX = newX
        currentY = newY

