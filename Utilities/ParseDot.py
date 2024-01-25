"""Get stats from Dot file"""

docString = []
with open("packages.dot", "r", encoding="utf8") as fp:
    for line in fp:
        if "->" in line:
            importer = line.split(" ")[0].replace('"', "")
            imported = line.split(" ")[2].replace('"', "")
            if (
                "." in importer
                and "." in imported
                and "Utils" not in imported
                # and "Game" not in imported
                # and "Asset" not in imported
                # and "Defin" not in imported
                or ("Main" in importer and "." in imported)
            ):
                docString.append(line)
        elif "[" in line:
            importer = line.split(" ")[0].replace('"', "")
            if "." in importer or "Main" in importer:
                docString.append(line)
        else:
            if "rankdir" in line:
                line.replace("BT", "TB")
            docString.append(line)
with open("packages.dot", "w", encoding="utf8") as fp:
    fp.writelines(docString)
