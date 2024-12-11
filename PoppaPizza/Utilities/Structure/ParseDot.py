"""Remove Confusing Links in DOT FILE"""

docString = []
with open("packages.dot", "r", encoding="utf8") as fp:
    for line in fp:
        if "->" in line:
            importer = line.split(" ")[0].replace('"', "")
            imported = line.split(" ")[2].replace('"', "")
            if "." in importer and "." in imported and "Engine" in importer:
                docString.append(line)
        elif "[" in line:
            importer = line.split(" ")[0].replace('"', "")
            if "." in importer and "Engine" in importer:
                docString.append(line)
        else:
            if "rankdir" in line:
                line = line.replace("rankdir=BT", "rankdir=TB")
            docString.append(line)
with open("enginePackages.dot", "w", encoding="utf8") as fp:
    fp.writelines(docString)


docString = []
with open("packages.dot", "r", encoding="utf8") as fp:
    for line in fp:
        if "->" in line:
            importer = line.split(" ")[0].replace('"', "")
            imported = line.split(" ")[2].replace('"', "")
            if (
                "." in importer
                and "." in imported
                and "Engine" not in imported
                and "Defin" not in imported
                and "GameBase" not in imported
            ):
                docString.append(line)
        elif "[" in line:
            importer = line.split(" ")[0].replace('"', "")
            if (
                ("." in importer or "Main" in importer)
                and "Defin" not in importer
                and "Engine" not in importer
            ):
                docString.append(line)
        else:
            if "rankdir" in line:
                line = line.replace("rankdir=BT", "rankdir=TB")
            docString.append(line)
with open("packages.dot", "w", encoding="utf8") as fp:
    fp.writelines(docString)


docString = []
with open("classes.dot", "r", encoding="utf8") as fp:
    for line in fp:
        if "->" in line:
            importer = line.split(" ")[0].replace('"', "")
            imported = line.split(" ")[2].replace('"', "")
            if "State" not in line and "Type" not in line:
                docString.append(line)
        else:
            if "rankdir" in line:
                line = line.replace("rankdir=BT", "rankdir=TB")
            docString.append(line)
with open("classesAndMembers.dot", "w", encoding="utf8") as fp:
    fp.writelines(docString)


docString = []
with open("classesAndMembers.dot", "r", encoding="utf8") as fp:
    allowed = {"None"}
    for line in fp:
        if 'arrowhead="empty"' in line:
            importer = line.split(" ")[0].replace('"', "")
            imported = line.split(" ")[2].replace('"', "")
            allowed.add(importer)
            allowed.add(imported)

with open("classesAndMembers.dot", "r", encoding="utf8") as fp:
    for idx, line in enumerate(fp):
        if idx < 3:
            docString.append(line)
        else:
            if 'arrowhead="diamond"' not in line:
                try:
                    importer = line.split(" ")[0].replace('"', "")
                    imported = line.split(" ")[2].replace('"', "")
                    if importer in allowed and (imported in allowed or "font" in imported):
                        docString.append(line)
                except:
                    pass

    docString.append("}")
with open("classes.dot", "w", encoding="utf8") as fp:
    fp.writelines(docString)
