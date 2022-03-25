ORIGINAL_PIECE_FILE_PATH = "original_pieces.txt"
FINAL_PIECE_FILE_PATH = "pieces.txt"

def get_pieces():
    pieces = []
    with open(FINAL_PIECE_FILE_PATH, 'r') as piece_file:
        raw_piece_data = piece_file.readlines()
        current_piece = []
        for row in raw_piece_data:
            if(row.strip() == ""):
                pieces.append(current_piece)
                current_piece = []
            else:
                current_piece.append([int(x) for x in row.strip()])
    return pieces

def process_original_pieces():
    pieces = []
    with open(ORIGINAL_PIECE_FILE_PATH, "r") as piece_file:
        raw_piece_data = piece_file.readlines()
        piece_so_far = []
        for raw_piece_line in raw_piece_data:
            if(raw_piece_line.strip() == ""):
                pieces.append(piece_so_far)
                piece_so_far = []
            else:
                piece_so_far.append([c for c in raw_piece_line.strip()])
    return pieces

def rotate_piece(piece, times=1):
    def rotate_once(piece):
        new_piece = []
        for i in range(len(piece[0])):
            new_piece.append([])
            for j in range(len(piece)):
                new_piece[i].append(piece[j][i])
            new_piece[i] = new_piece[i][::-1]
        return new_piece
    final_new_piece = []
    current_piece = [row[:] for row in piece[:]]
    for _ in range(times):
        current_piece = rotate_once(current_piece)
    return current_piece

piece_set = set()
if(__name__ == "__main__"):
    all_pieces = []
    original_pieces = process_original_pieces()
    for original in original_pieces:
        for i in range(4):
            piece_set.add("\n".join(["".join(x) for x in rotate_piece(original, i)]))

    out_str = ""
    for piece in piece_set:
        out_str += piece + "\n\n"

    with open(FINAL_PIECE_FILE_PATH, "w") as piece_file:
        piece_file.write(out_str)



    


