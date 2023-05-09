from collections import deque, defaultdict

class Node:
    def __init__(self, position):
        self.position = position
        self.is_black_piece = False
        self.is_attacked = False
        self.piece = ''

class Graph(object):
    def __init__(self, size):
        self.size = size
        self.nodes = []
        self.adj = defaultdict(list)
        for i in range(size):
            node_list = defaultdict(list)
            for j in range(size):
                node = Node((i,j))
                node_list[j] = node
            self.nodes.append(node_list)
        self.add_edges()

    def add_edges(self):
        for i in range(self.size):
            for j in range(self.size)-1:
                self.adj[(i,j)].append(self.nodes[i][j+1])
                self.adj[(i,j+1)].append(self.nodes[i][j])
        for j in range(self.size):
            for i in range(self.size)-1:
                self.adj[(j,i)].append(self.nodes[j][i+1])
                self.adj[(j,i+1)].append(self.nodes[j][i])
            
    def insert_piece(self, position, piece):
        # Implementar para inserir o atributo 'is_black_piece' no node de posição 'position'

        self.fill_attacked(piece)

    def fill_attacked(self, piece):
        # Preenche com attacked os nós em que a posição esteja dentro dos possíveis ataques da peça 'piece'
        t
            
    def add_black_pieces(self, n_pecas):
        #
        for k in range(n_pecas):
            i, j = map(int, input().split())
            piece = input()
            self.insert_piece(0, (i, j), piece)

    def start_process(self):
        king_pos = self.add_white_king()

        finalX, finalY = map(int, input().split())


    def add_white_king(self):
        # adicionar o rei branco ao tabuleiro
        king_posX, king_posY = map(int, input().split())
        
        # if para verificar se é possível inserir o rei
        if ():
            t

        return ((king_posX, king_posY))
        

    def is_path_safe(self, start_position, end_position):
        # dijkstra modificado para encontrar o caminho mais seguro
        dijkstra()

def main():
    size = int(input())
    
    G = Graph(size)
    # n_pecas = int(input())
    # G.add_black_pieces(n_pecas)
    
    # G.start_process()    

if __name__ == '__main__': 
    main()