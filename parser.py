from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""

def parse_file( fname, points, transform, screen, color ):
    f = open(fname, "r")
    commands = []
    for item in f.readlines():
        commands.append(item[0:-1])
    i = 0
    while (i < (len(commands) - 1)):
        if (commands[i] == "line"):
            p = (commands[i+1]).split(" ")
            add_edge(points, float(p[0]), float(p[1]), float(p[2]), float(p[3]), float(p[4]), float(p[5]))
            i+=2
        elif (commands[i] == "ident"):
            ident(transform)
            i+=1
        elif (commands[i] == "scale"):
            p = (commands[i+1]).split(" ")
            matrix_mult(make_scale(float(p[0]), float(p[1]), float(p[2])), transform)
            i+=2
        elif (commands[i] == "move"):
            p = (commands[i+1]).split(" ")
            matrix_mult(make_translate(float(p[0]), float(p[1]), float(p[2])), transform)
            i+=2
        elif (commands[i] == "rotate"):
            p = (commands[i+1]).split(" ")
            if (p[0] == "x"):
                matrix_mult(make_rotX(float(p[1])), transform)
            if (p[0] == "y"):
                matrix_mult(make_rotY(float(p[1])), transform)
            if (p[0] == "z"):
                matrix_mult(make_rotZ(float(p[1])), transform)
            i+=2
        elif (commands[i] == "apply"):
            matrix_mult(transform, points)
            i+=1
        elif (commands[i] == "display"):
            screen = new_screen()
            draw_lines(points, screen, [100,100,100])
            display(screen)
            i+=1
        elif (commands[i] == "save"):
            screen = new_screen()
            draw_lines(points, screen, [100,100,100])
            save_ppm(screen, 'binary.ppm')
            save_ppm_ascii(screen, 'ascii.ppm')
            save_extension(screen, commands[i+1])
            i+=2
        elif (commands[i] == "quit"):
            break
