def binary_ply_to_ascii(input_file, output_file):
    # Step 1: Open and read the binary PLY file
    with open(input_file, "rb") as binary_file:
        binary_data = binary_file.read()
        print(binary_data)
    # Step 2: Separate header and binary data
    header, binary_data = binary_data.split(b"end_header\n", 1)

    # Step 3: Convert binary data to ASCII with error handling
    try:
        ascii_data = header.decode() + binary_data.decode(errors='replace')
    except UnicodeDecodeError as e:
        print(f"Error decoding binary data: {e}")
        return

    # Step 4: Save the ASCII data to a new file with explicit encoding
    with open(output_file, "w", encoding='utf-8') as ascii_file:
        ascii_file.write(ascii_data)

# Example usage
input_binary_ply = "C:/Users/SKH/Github_local/3D_Modeling_with_Three.js/pointcloudprocessing/data/polycam_pcd.ply"
output_ascii_ply = "C:/Users/SKH/Github_local/3D_Modeling_with_Three.js/pointcloudprocessing/data/polycam_pcd.ply"
binary_ply_to_ascii(input_binary_ply, output_ascii_ply)
