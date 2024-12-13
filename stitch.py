try: import os, cv2, install_lib
except ImportError:
    try:
        import install_lib
        install_lib.install()
    except ImportError: print("How did you manage to lose install_lib??? did you delete it or smth?")

def Video(FPS: int):
    print("Please wait. This might take a few minutes.")
    PATH="output"
    imgs = [img for img in os.listdir(PATH) if img.endswith(".png")]
    frame = cv2.imread(os.path.join(PATH, imgs[0]))
    # h,w,l = frame.shapes
    video = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*'XVID'), FPS, (720,720))
    for img in imgs:
        frame = cv2.imread(os.path.join(PATH, img))
        video.write(frame)
        print(img,"done")
    video.release()
    cv2.destroyAllWindows()
    print("Done!")
Video(30)