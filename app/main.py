def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return  # неправильный формат команды

    cmd, src, dst = parts
    if cmd != "cp":
        return  # неизвестная команда

    # 🧩 Новая проверка — копирование файла "в самого себя"
    if src == dst:
        return

    try:
        with open(src, "r") as f_in, open(dst, "w") as f_out:
            f_out.write(f_in.read())
    except FileNotFoundError:
        print(f"Source file '{src}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
