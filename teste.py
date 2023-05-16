from collections import defaultdict
import heapq

class Node:
    def __init__(self, position):
        self.position = position
        self.weigth = 1
        # self.is_black_piece = False
        # self.is_attacked = False
        # self.piece = ''

class Graph(object):
    def __init__(self, size):
        self.size = size
        self.nodes = []
        self.adj = defaultdict(list)
        for i in range(size):
            node_list = []
            for j in range(size):
                node = Node((i,j))
                # node_list[j] = node
                node_list.append(node)
                # node_list.append((i,j))
            self.nodes.append(node_list)

    def add_edge(self, u, v): 
        xu, yu = u
        xv, yv = v
        self.adj[(xu,yu)].append(self.nodes[yv][xv])
        self.adj[(xv,yv)].append(self.nodes[yu][xu])


# def dijkstra(graph, starting_vertex):
#     x, y = starting_vertex
#     # node_indices = {(node.position): i for i, node_list in enumerate(graph.nodes) for node in node_list}
#     distances = {node: float('infinity') for node_list in graph.nodes for node in node_list}
#     distances[starting_vertex] = 0

#     pq = [(0, starting_vertex)]
#     while len(pq) > 0:
#         current_distance, current_vertex = heapq.heappop(pq)

#         if current_distance > distances[current_vertex]:
#             continue

#         for neighbor_node in graph.adj[current_vertex]:
#             neighbor_position = neighbor_node.position

#             distance = current_distance + 1

#             if distance < distances[neighbor_position]:
#                 distances[neighbor_position] = distance
#                 heapq.heappush(pq, (distance, neighbor_position))

#     return distances
def dijkstra(graph, starting_vertex):
    x, y = starting_vertex
    distances = {node.position: float('infinity') for node_list in graph.nodes for node in node_list}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor_node in graph.adj[current_vertex]:
            neighbor_position = neighbor_node.position

            # Calculate the distance by adding the weight of the neighbor node
            distance = current_distance + neighbor_node.weight

            if distance < distances[neighbor_position]:
                distances[neighbor_position] = distance
                heapq.heappush(pq, (distance, neighbor_position))

    return distances

def create_chessboard_graph(n, non_edges):
    chessboard = Graph(n)
    positions = [(i, j) for i in range(n) for j in range(n)]
    # chessboard.add(positions)

    for position in positions:
        if position not in positions:
            i, j = position
            neighbors = [
                (i-1, j), (i+1, j), (i, j-1), (i, j+1),
                (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)
            ]
            valid_neighbors = [(x, y) for (x, y) in neighbors if 0 < x < n and 0 < y < n]
            for neighbor in valid_neighbors:
                if(neighbor not in non_edges):
                    chessboard.add_edge(position, neighbor)
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
                "1. Torre\n"+
                "2. Bispo\n"+
                "3. Cavalo\n"+
                "4. Peão\n"
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
            non_edges.append((x,y))
        except: 
            print("Entre com um número")
            exit(0)
        
    black_king = tuple(map(int, input("Digite a posição do rei preto (x y):").split()))

    black_dest = tuple(map(int, input("Digite a posição de destino do rei preto (x y): ").split()))
    # print(non_edges)
    chessboard = create_chessboard_graph(n, non_edges)
    # display_chessboard(chessboard, white_pieces, black_king, black_dest)
    # print(chessboard.__dict__) 
    # print(chessboard.adj)
    path = dijkstra(chessboard, black_king)
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