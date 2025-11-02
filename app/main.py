def copy_file(command: str) -> None:
    if (
            command == ""
            or len(command.split(" ")) != 3
            or command.split(" ")[0] != "cp"
    ):
        return
    _, file_name_1, file_name_2 = command.split(" ")
    try:
        with (
            open(file_name_1, "r") as file_in,
            open(file_name_2, "w") as file_out
        ):
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"Source file '{file_name_1}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
