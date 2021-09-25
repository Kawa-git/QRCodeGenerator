import qrcode 
import argparse

parser = argparse.ArgumentParser(description="Simple QRcode generator")
parser.add_argument("link", type=str, help="Used to generate the QRcode")
parser.add_argument("-c", "--complexity", type=int, help="Complexity of the generated QRcode", default=6)
parser.add_argument("-o", "--output", type=str, help="Renames the output image", default="qrcode")
args = parser.parse_args()

def main(link):
    output = args.output + ".png"
    qr = qrcode.QRCode(
        version=args.complexity,
        box_size=10,
        border=5   
    )
    data = link

    qr.add_data(data)
    qr.make(fit = True)

    img = qr.make_image()
    img.save(output)

if __name__ == "__main__":
    main(args.link)

    
