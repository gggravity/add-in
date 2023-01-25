from pathlib import Path

path = "L:/RASTER_DATA/"
ext = "*.ecw"

for path in Path(path).rglob(ext):
    code = path.absolute().__str__().split("\\")[2]
    year = path.absolute().__str__().split("\\")[3]
    coords = path.name.split("_")[-1].split(".")[0]

    if coords.startswith("Z"):
        print(path.absolute().__str__() + "|" + code + " " + year + " " + coords)
    else:
        print(path.absolute().__str__() + "|" + code + " " + year)

