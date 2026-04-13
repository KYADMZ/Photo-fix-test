def truncate_file(input_file, output_file, cut_offset):
    with open(input_file, "rb") as f:
        data = f.read()

    print("Tamaño original:", len(data))
    print("Cortando en offset:", cut_offset)

    truncated = data[:cut_offset]

    with open(output_file, "wb") as f:
        f.write(truncated)

    print("Nuevo tamaño:", len(truncated))


if __name__ == "__main__":
    input_file = "reconstruido.NEF"
    output_file = "truncado.NEF"
    cut_offset = 18014254  #Error offset

    truncate_file(input_file, output_file, cut_offset)