from collections import defaultdict
import heapq

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
        for i in range(self.size-1):
            for j in range(self.size-1):
                self.adj[(i,j)].append(self.nodes[i][j+1])
                self.adj[(i,j+1)].append(self.nodes[i][j])
                self.adj[(j,i)].append(self.nodes[j][i+1])
                self.adj[(j,i+1)].append(self.nodes[j][i])
            
    def insert_piece(self, position, piece):
        # Implementar para inserir o atributo 'is_black_piece' no node de posição 'position'
        if not self.nodes[position.i][position.j].is_black_piece:    
            self.nodes[position.i][position.j].is_black_piece = True
            self.nodes[position.i][position.j].piece = piece
        
            self.fill_attacked(self.nodes[position.i][position.j])

    def fill_attacked(self, node):
        # Preenche com attacked os nós em que a posição esteja dentro dos possíveis ataques da peça 'piece'
        t
            
    def add_black_pieces(self, n_pecas):
        # Adiciona todas as N peças pedidas
        for k in range(n_pecas):
            i, j = map(int, input().split())
            piece = input()
            self.insert_piece(0, (i, j), piece)

    def process(self):
        king_pos = self.add_white_king()

        finalX, finalY = map(int, input().split())

        return self.is_path_safe(king_pos, (finalX, finalY))

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

def dijkstra(graph, starting_vertex):
    distances = {node: float('infinity') for node in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

def create_chessboard_graph(n):
    chessboard = Graph()
    positions = [(i, j) for i in range(n) for j in range(n)]
    chessboard.add(positions)

    for position in positions:
        i, j = position
        neighbors = [
            (i-1, j), (i+1, j), (i, j-1), (i, j+1),
            (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)
        ]
        valid_neighbors = [(x, y) for (x, y) in neighbors if 0 <= x < n and 0 <= y < n]
        chessboard.add_edges_from([(position, neighbor) for neighbor in valid_neighbors])

    return chessboard
    
def torre_positions(x, y, n): 
    moves = [x, y]
    dx, dy = x, y 
    while(dy < n and dx<n): 
        dy += 1
        dx += 1
        moves.append((x, dy))
        moves.append((dx, y))

    dx, dy = x, y 
    while(dy > 0 and dx > 0): 
        dy -= 1
        dx -= 1
        moves.append((x, dy))
        moves.append((dx, y))

    return moves

def peao_positions(x, y):
    i, j = x, y
    moves = [
        (i, j),(i-1, j), (i+1, j), (i, j-1), (i, j+1),
        (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)
    ]
    return moves

def is_valid_position(x, y, n, visited):
    return x >= 0 and x < n and y >= 0 and y < n and (x,y) not in visited

def get_cavalo_positions(x, y, n):
    moves = []
    visited = []
    directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                  (1, -2), (1, 2), (2, -1), (2, 1)] 

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_valid_position(nx, ny, n, visited):
            visited.append((nx, ny))
            moves.append((nx, ny))

    return moves

def bispo_positions(x, y, n):
    moves = [x, y]
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    for dx, dy in directions:
        new_x, new_y = x, y
        while True:
            new_x += dx
            new_y += dy
            if is_valid_position(new_x, new_y, n, moves):
                moves.append((new_x, new_y))
            else:
                break

    return moves

def main():
    n = int(input("Digite o tamanho do tabuleiro (N): "))
    white_count = int(input("Digite o número de peças do time branco: "))
    non_edges = []
    white_pieces = []
    for _ in range(white_count):
        x, y = map(int, input("Digite a posição da peça branca (x y): ").split())
        try: 
            piece = int(input("Qual a peca que está nessa posicao:\n"+
                "1. Torre"+
                "2. Bispo"+
                "3. Cavalo"+
                "4. Peão"
            ))
            if(piece==1):
                for i in torre_positions(x, y, n): 
                    non_edges.append(i)
            elif(piece==2): 
                for i in bispo_positions(x, y, n): 
                    non_edges.append(i)
            elif(piece==3): 
                for i in get_cavalo_positions(x, y, n):
                    non_edges.append()
            elif(piece==4): 
                for i in peao_positions(x, y, n): 
                    non_edges.append(i)

            white_pieces.append((x, y))
            non_edges.append(piece)
        except: 
            print("Entre com um número")
            exit(0)
        
    black_king = tuple(map(int, input("Digite a posição do rei preto (x y):").split()))

    black_dest = tuple(map(int, input("Digite a posição de destino do rei preto (x y): ").split()))

    chessboard = create_chessboard_graph(n)
    # display_chessboard(chessboard, white_pieces, black_king, black_dest)

    path = dijkstra(chessboard, white_pieces, black_king, black_dest)
    if path is None:
        print("Fim de Jogo: O Rei está em perigo!")
    else:
        print("Caminho seguro encontrado:")
        print(path)
    
    # G = Graph(size)
    # n_pecas = int(input())
    # G.add_black_pieces(n_pecas)
    
    # print(G.process())    

if __name__ == '__main__': 
    main()