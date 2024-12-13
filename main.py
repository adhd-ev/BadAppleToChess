#Time Complexity: O(n)
#Space Complexity: O(n*m)
import install_lib; install_lib.install()
DEVMODE = True if input("Type 1 to enable Dev Mode\n")=="1" else False
PRINTLINKS = True if input("Type 1 to enable link printing\n")=="1" else False
import requests, os, time; from PIL import Image
board = [['k']*8]*8
PATH = "img/"
dirs = os.listdir(PATH)
for item in dirs:
    LINK = "https://lichess1.org/export/fen.gif?fen="
    if os.path.isfile(PATH+item):
        im = Image.open(PATH+item)
        imResize = im.resize((8,8), Image.LANCZOS)
        px = imResize.load() #pixel data
        for x in range(8):
            for y in range(8):
                board[x][y]='K' if px[y,x][0] > 128 else 'k'
                LINK += board[x][y]
            LINK+='/'
        if DEVMODE:
            f, e = os.path.splitext(PATH+item)
            imResize.save(f+' _R.jpg', 'JPEG', quality=100)
    LINK+="_-_-_-_1_0&color=white"
    LINK = LINK[::-1].replace("/","",1)[::-1]
    print(LINK, str(item)) if PRINTLINKS else print(str(item))
    try: chessImg = Image.open(requests.get(LINK,stream=True).raw)
    except:
        print("Lichess API did not respond. Trying again... (1/3)")
        time.sleep(69) #yeah this is needed since lichess api bricks for a minute i think
        try: chessImg = Image.open(requests.get(LINK,stream=True).raw)
        except:
            print("Lichess API failed to respond. Trying again... (2/3)")
            time.sleep(69) 
            try: chessImg = Image.open(requests.get(LINK,stream=True).raw)
            except:
                print("Lichess API failed to respond. Trying again... (3/3)")
                time.sleep(69) 
                try: chessImg = Image.open(requests.get(LINK,stream=True).raw)
                except:
                    print("Lichess API failed to respond. Breaking...")
                    break
    f, e = os.path.splitext('output/'+item)
    chessImg.save(f+'.png','PNG',quality=720)
if 'y' in input("Finished saving. Begin making video? (y/n)"):
    import stitch
    print("Stitching...")
    stitch.Video(30)
