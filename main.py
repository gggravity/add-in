from pathlib import Path
from lokaliteter import lokaliteter as lokalitet

path = "L:/RASTER_DATA/"
ext = "*.ecw"

for path in Path(path).rglob(ext):
    code = path.absolute().__str__().split("\\")[2]

    code = code.split()[0]  # fjern ting i ()

    year = path.absolute().__str__().split("\\")[3]
    coords = path.name.split("_")[-1].split(".")[0]

    if not year[0].isdigit():
        year = "ukendt årstal"

    if coords.startswith("Z"):
        print(path.absolute().__str__() + "|" + lokalitet[code] + " " + year + " " + coords)
    else:
        print(path.absolute().__str__() + "|" + lokalitet[code] + " " + year)
