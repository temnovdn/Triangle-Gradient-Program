from gradient import *
from point import Point
from Tkinter import *


def draw_triangle():
    red_x = IntVar()
    red_x = red_x_input.get()
    red_y = IntVar()
    red_y = red_y_input.get()

    green_x = IntVar()
    green_x = green_x_input.get()
    green_y = IntVar()
    green_y = green_y_input.get()

    blue_x = IntVar()
    blue_x = blue_x_input.get()
    blue_y = IntVar()
    blue_y = blue_y_input.get()
    if ((0 <= red_x <= draw_area_width) and
            (0 <= red_y <= draw_area_height) and
            (0 <= green_x <= draw_area_width) and
            (0 <= green_y <= draw_area_height) and
            (0 <= blue_x <= draw_area_width) and
            (0 <= blue_y <= draw_area_height)):
        try:
            gradient = TriangleGradient(Point(int(red_x), int(red_y)), Point(int(green_x), int(green_y)),
                                        Point(int(blue_x), int(blue_y)))
            draw_area.blank()

            for point in gradient.internal_points:
                draw_area.put("#%02x%02x%02x" % (point.red, point.green, point.blue), (point.x, point.y))

            label = Label(master=root, image=draw_area)
            label.pack(anchor=W)
        except ValueError:
            label = Label(master=apex_coordinates_input, text="Input values could not be apexes of triangle")
            label.pack(anchor=N)
    else:
        label = Label(master=apex_coordinates_input, text="Input values are beyond draw area size")
        label.pack(anchor=N)


window_width = 900
window_height = 1100
text_area_width = 20

root = Tk()
root.title('Triangle gradient')
root.geometry('{0!s}x{1!s}+50+50'.format(window_height, window_width))

draw_area_width = window_width - text_area_width
draw_area_height = window_height - 20

draw_area = PhotoImage(width=draw_area_width, height=draw_area_height)

apex_coordinates_input = Frame(master=root, width=text_area_width, height=window_height)
apex_coordinates_input.pack(anchor=E)

coordinate_frames_height = window_height // 3
red_coordinates = Frame(master=apex_coordinates_input, width=text_area_width, height=coordinate_frames_height)
red_coordinates.pack()

green_coordinates = Frame(master=apex_coordinates_input, width=text_area_width, height=coordinate_frames_height)
green_coordinates.pack()

blue_coordinates = Frame(master=apex_coordinates_input, width=text_area_width, height=coordinate_frames_height)
blue_coordinates.pack()

red_x_area = Frame(master=red_coordinates, width=text_area_width)
red_x_area.pack(anchor=NW)
red_y_area = Frame(master=red_coordinates, width=text_area_width)
red_y_area.pack(anchor=NW)

red_x_input = Entry(master=red_x_area, bg='red', fg='white', width=10)
red_x_label = Label(master=red_x_area, text='Red apex x (%s-%s):' % (0, draw_area_width))
red_x_label.pack(side=LEFT)
red_x_input.pack(side=RIGHT)
red_y_input = Entry(master=red_y_area, bg='red', fg='white', width=10)
red_y_label = Label(master=red_y_area, text='Red apex y (%s-%s):' % (0, draw_area_height))
red_y_label.pack(side=LEFT)
red_y_input.pack(side=RIGHT)

green_x_input = Entry(master=green_coordinates, bg='green', fg='white', width=10)
green_x_label = Label(master=green_coordinates, text='Red apex x  (%s-%s):' % (0, draw_area_width))
green_x_label.pack(side=LEFT)
green_x_input.pack(side=RIGHT)
green_y_input = Entry(master=green_coordinates, bg='green', fg='white', width=10)
green_y_input.insert(END, '%s-%s' % (0, draw_area_height))
green_y_input.pack(side=RIGHT)

blue_x_input = Entry(master=blue_coordinates, bg='blue', fg='white', width=10)
blue_x_input.insert(END, '%s-%s' % (0, draw_area_width))
blue_x_input.pack(side=LEFT)
blue_y_input = Entry(master=blue_coordinates, bg='blue', fg='white', width=10)
blue_y_input.insert(END, '%s-%s' % (0, draw_area_height))
blue_y_input.pack(side=RIGHT)

draw_button = Button(master=apex_coordinates_input, text="Draw!", command=draw_triangle)
draw_button.pack()

mainloop()
