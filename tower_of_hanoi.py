
def towers_of_hanoi(num_of_rings,from_peg,to_peg,aux_peg):
    def steps_for_tower_of_hanoi(num_of_rings, from_peg, to_peg, aux_peg,from_peg_no = 0,to_peg_no =2,aux_peg_no = 1,):
        if num_of_rings > 0:
            steps_for_tower_of_hanoi(num_of_rings-1, from_peg, aux_peg, to_peg,from_peg_no,aux_peg_no,to_peg_no)
            transfer_peg = pegs[from_peg_no].pop()
            pegs[to_peg_no].append(transfer_peg)
            print('{} ---> {}'.format(from_peg, to_peg))
            print(pegs)

            steps_for_tower_of_hanoi(num_of_rings-1, aux_peg, to_peg, from_peg,aux_peg_no,to_peg_no,from_peg_no)

    pegs = [list(range(num_of_rings,0,-1))] + [[] for _ in range(num_of_rings-1)]

    print(pegs)
    steps_for_tower_of_hanoi(num_of_rings, from_peg, to_peg, aux_peg)


if __name__ == '__main__':
    towers_of_hanoi(3,'A','C','B')