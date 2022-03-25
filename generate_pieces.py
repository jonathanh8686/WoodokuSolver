ORIGINAL_PIECE_FILE_PATH = "piece_data.txt"

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

def print_piece(piece):
    for i in piece:
        print("".join(i))
                 
piece_set = set()
if(__name__ == "__main__"):
    all_pieces = []
    original_pieces = process_original_pieces()
    for original in original_pieces:
        for i in range(4):
            print_piece(rotate_piece(original, i))
            print("----")
            piece_set.add(rotate_piece(original, i))
    print(piece_set)



    


