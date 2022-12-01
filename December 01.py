with open("/storage/emulated/0/Download/input.txt", "r+") as input_file:
    raw_list = list(input_file).copy()
    clean_list = [x.strip("\n") for x in raw_list]
    elf_list = []
    counter = 0
    for item in clean_list:
        if item.isnumeric():
            counter += int(item)
        else:
            elf_list.append(counter)
            counter = 0
    elf_list.sort(reverse=True)
    print(f"Top elf: {elf_list[0]}\nTop 3: {sum(elf_list[:3])}")
