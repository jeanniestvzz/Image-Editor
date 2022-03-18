import numpy as np
import cv2

def main():
    print("")
    print("EDIT IMAGES")
    
    while True:
        print("")
        print("Select from the choices below, an image you want to edit:")
        print("")
        print("1. An image of the castle and Disney's Magic Kingdom")
        print("2. An image of Toy Story Land at Disney's Hollywood Studios")
        print("3. Another image")
        print("0. Exit program")
        print("")

        x = input()
        x = int(x)
        print("")

        # READ FILES
        if x == 1:
            file = "DisneyCastle.jpg"
        elif x == 2:
            file = "ToyStoryLand.jpg"
        elif x == 3:
            print("Enter the location and name of the file. (Must be in an image file format like PNG, JPG, or JPEG)")
            file = input()
        elif x == 0:
            cv2.destroyAllWindows()
            exit()
        else:
            fail()
            exit()
        
        img = cv2.imread(file)

        # EDITING AND VIEWING IMAGE INFO OPTIONS
        print("")
        print("====================================================")
        print("Select from the choices below to view or edit image:")
        print("")
        print("1. View height, width, and number of channels of the image")
        print("2. View the difference of each channel in RGB Color Space")
        print("3. View the difference of each channel in HSV Color Space")
        print("4. Add alpha channel / transparency to the image")
        print("5. Add blur to the image / Make image smooth")
        print("6. Add dilation to the image")
        print("7. Add erosion to the image")
        print("8. Resize the image")
        print("9. Rotate the image")
        print("0. Exit program")
        print("")

        y = input()
        y = int(y)
        print("")

        # RUNNING OPTIONS BASED ON INPUT
        if y == 1:
            img_shape(img)
        elif y == 2:
            rgb_split(img)
        elif y == 3:
            hsv_split(img)
        elif y == 4:
            add_alpha_channel(img, file)
        elif y == 5:
            add_blur(img)
        elif y == 6:
            add_dilation(img)
        elif y == 7:
            add_erosion(img)
        elif y == 8:
            resize(img,file)
        elif y == 9:
            rotate(img, file)
        elif y == 0:
            cv2.destroyAllWindows()
            exit()
        else:
            fail()
            continue
        
        # VIEW IMAGE
        view_image("Original File", img, 0, 0)

        cv2.waitKey(0)

    #EXIT PROGRAM
    exit()

def view_image(window_name, var, width_pos = 40, height_pos = 40):
    cv2.imshow(window_name, var)
    cv2.moveWindow(window_name, width_pos, height_pos)

def save_image_to_disc(filename, var):
    cv2.imwrite(filename, var)
    print("IMAGE SAVED AS:   " + filename)

def view_or_save(var, file_name, window_name, width_pos = 40, height_pos = 40):
    # INPUT
    print("Enter '1' to view image, '2' to save image, or '3' to view and save.")
    z = input()
    z = int(z)

    # RETURN
    if z == 1:
        view_image(window_name, var, width_pos, height_pos)
    elif z == 2:
        save_image_to_disc(file_name, var)
    elif z == 3:
        view_image(window_name, var, width_pos, height_pos)
        save_image_to_disc(file_name, var)
    else:
        print("Not an option. Image not saved. View window.")
        view_image(window_name, var, width_pos, height_pos)

def rename_file(add, old_filename):
    per = old_filename.find(".")
    new_filename = old_filename[:per] + add + old_filename[per:]
    return new_filename

def to_png(filename):
    if filename.endswith("jpg"):
            new_file = filename.replace("jpg", "png")
    if filename.endswith("jpeg"):
        new_file = filename.replace("jpeg", "png")
    
    return new_file

def fail():
    print("Not an option. Bye!")

def num_channels(img1):
    height,width,channels = img1.shape
    return(int(channels))

def img_shape(img1):
    height,width,channels = img1.shape
    print("Height: " + str(height))
    print("Width: " + str(width))
    print("Number of channels: " + str(channels))
    print("")

def rgb_split(img1):
    height,width,channels = img1.shape

    if num_channels(img1) == 3:
        #GET CHANNELS
        b = img1[:,:,0]
        g = img1[:,:,1]
        r = img1[:,:,2]

        # CREATING NEW
        blue = np.empty([height,width,3],'uint8')
        green = np.empty([height,width,3],'uint8')
        red = np.empty([height,width,3],'uint8')

        # MERGE
        blue[:,:] = cv2.merge([b,b,b])
        green[:,:] = cv2.merge([g,g,g])
        red[:,:] = cv2.merge([r,r,r])

        # DISPLAY CHANNELS
        view_image("Blue", blue, 0, height)
        view_image("Green", green, 40, height)
        view_image("Red", red, 80, height)
    else: 
        print("Does not have 3 channels")
        print("")

def hsv_split(img1):
    height,width,channels = img1.shape

    if num_channels(img1) == 3:
        # CONVERT FROM BGR TO HSV
        hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)

        # GET CHANNELS
        h = hsv[:,:,0]
        s = hsv[:,:,1]
        v = hsv[:,:,2]

        # CREATING NEW
        hue = np.empty([height,width,3],'uint8')
        saturation = np.empty([height,width,3],'uint8')
        value = np.empty([height,width,3],'uint8')

        # MERGE
        hue[:,:] = cv2.merge([h,h,h])
        saturation[:,:] = cv2.merge([s,s,s])
        value[:,:] = cv2.merge([v,v,v])

        # DISPLAY CHANNELS
        view_image("Hue", hue, 0, height)
        view_image("Saturation", saturation, 40, height)
        view_image("Value", v, 80, height)
    else: 
        print("Does not have 3 channels")
        print("")

def add_alpha_channel(img1, filename):
    if num_channels(img1) == 3:
        # GET CHANNELS
        b = img1[:,:,0]
        g = img1[:,:,1]
        r = img1[:,:,2]

        # OPTIONS
        print("Select an option:")
        print("1. Make all non-blue parts of image transparent")
        print("2. Make all non-green parts of image transparent")
        print("3. Make all non-red parts of image transparent")
        print("")

        # INPUT
        z = input()
        z = int(z)
        print("")

        # MERGE
        if z == 1:
            rgba = cv2.merge((b,g,r,b))
        elif z == 2:
            rgba = cv2.merge((b,g,r,g))
        elif z == 3:
            rgba = cv2.merge((b,g,r,r))
        else:
            fail()
            return
        
        # SAVE IMAGE ONLY
        new_file = rename_file("_transparent", filename)
        save_image_to_disc(to_png(new_file), rgba)
    else:
        print("Does not have 3 channels")
        print("")

def add_blur(img1):
    # VERITCAL BLUR
    print("How much vertical blur? (Must be an odd integer)")
    y_blur = input()
    y_blur = int(y_blur)

    # HORIZONTAL BLUR
    print("How much horizontal blur? (Must be an odd integer)")
    x_blur = input()
    x_blur = int(x_blur)
    print("")

    blur = cv2.GaussianBlur(img1, (x_blur, y_blur), 0)

    view_image("Blur", blur)

def add_dilation(img1):
    #print("How dilated do you want the image?")
    # DILATION
    kernel = np.ones((5,5), 'uint8')
    dilate = cv2.dilate(img1, kernel, iterations=1)

    #VIEW IMAGE
    view_image("Dilated Image", dilate)

def add_erosion(img1):
    # EROSION
    kernel = np.ones((5,5), 'uint8')
    erode = cv2.erode(img1, kernel, iterations=1)

    # VIEW IMAGE
    view_image("Eroded Image", erode)

def resize_scale(img1, sf):
    img_scale = cv2.resize(img1, (0,0), fx=sf, fy=sf)
    return img_scale

def resize_desird_size(img1, x, y):
    img_desired_size = cv2.resize(img1, (x,y), interpolation=cv2.INTER_NEAREST)
    return img_desired_size

def resize(img1, filename):
    # OPTIONS
    print("Select an option: ")
    print('1. Resize an image by a scale factor')
    print('2. Resize an image by a certain desired size')

    # INPUT
    z = input()
    z = int(z)
    print("")

    # APPLY RESIZING
    if z == 1:
        # INPUT
        print("By how much would you like to scale up or down? (Enter in decimal form)")
        scale_factor = input()
        scale_factor = float(scale_factor)

        # APPLY SCALE FACTOR
        img_resized = resize_scale(img1, scale_factor)
    elif z == 2:
        # INPUT
        print("What is your desired size on the x axis?")
        x_axis = input()
        x_axis = int(x_axis)
        print("What is your desired size on the y axis?")
        y_axis = input()
        y_axis = int(y_axis)

        # APPLY DESIRED SIZE
        img_resized = resize_desird_size(img1, x_axis, y_axis)
    else:
        fail()
        return
    
    view_or_save(img_resized, rename_file("_resized", filename), "Resized Image")

def rotate(img1, filename):
    height,width,channels = img1.shape

    # INPUT
    print("Select an option:")
    print("1. Rotate about the center of the image")
    print("2. Rotate about the top left corner of the image")
    print("3. Rotate about the bottom right corner of the image")
    print("4. Customize where to rotate about")
    print("")

    center = input()
    center = int(center)

    if center == 1:
        x_rot = width / 2
        y_rot = height / 2
    elif center == 2:
        x_rot = 0
        y_rot = 0
    elif center == 3:
        x_rot = width
        y_rot = height
    elif center == 4:
        x_rot = input()
        x_rot = int(x_rot)
        if x_rot > width:
            print("Invalid entry.")
            return
        y_rot = input()
        y_rot = int(y_rot)
        if y_rot > height:
            print("Invalid entry.")
            return
    else:
        print("Not an option. Rotating about center by default.")
        x_rot = width / 2
        y_rot = height / 2

    print("By how much degrees you like to rotate? (Range is [-360, 360])")
    angle = input()
    angle = float(angle)
    if angle > 360 or angle < 360:
        print("Invalid entry. Rotating by 180 degrees by default.")
    print("")

    matrix = cv2.getRotationMatrix2D((x_rot,y_rot), angle, 1)
    rotated = cv2.warpAffine(img1, matrix, (img1.shape[1], img1.shape[0]))

    view_or_save(rotated, rename_file("_rotated", filename), "Rotated Image")

main()