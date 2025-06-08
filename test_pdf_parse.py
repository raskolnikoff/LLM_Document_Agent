from unstructured.partition.pdf import partition_pdf

if __name__ == "__main__":
    elements = partition_pdf("docs/AppleComputerDirectory(BrianW.Kelly,DennisJ.Grimes).pdf", strategy="fast")
    for e in elements:
        print(e.text[:100])
