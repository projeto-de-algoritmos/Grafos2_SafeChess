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

def main():
    size = int(input())
    
    G = Graph(size)
    n_pecas = int(input())
    G.add_black_pieces(n_pecas)
    
    print(G.process())    

if __name__ == '__main__': 
    main()