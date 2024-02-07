import argparse


def Main(filePath) -> None:
    parentText = r"""<li><h3>Home</h3><ul><li><code><a title="Home" href="..\index.html">Index</a></code></li> </ul><li><h3>Base Call</h3><ul><li><code><a title="Main" href="..\Main.html">Main</a></code></li> </ul>"""
    targetString = """<ul id="index">"""
    with open(file=filePath, mode="r", encoding="utf-8") as fp:
        docstring = []
        for line in fp:
            docstring.append(line)
            if targetString in line:
                docstring.append(parentText)
    with open(file=filePath, mode="w", encoding="utf-8") as fp:
        fp.writelines(docstring)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--File")
    args = parser.parse_args()
    Main(args.File)
