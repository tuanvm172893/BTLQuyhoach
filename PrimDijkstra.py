import math
import copy
import Node
import sys

                 
def cal_GiaBackbone(n, FinalRoadMap, listNodeBackbone, TrafficMatrix):
    gia = 0
    for i in range(len(listNodeBackbone)):
        for j in range(len(listNodeBackbone)):
            i1 = listNodeBackbone[i].get_name() - 1
            j1 = listNodeBackbone[j].get_name() - 1
            if j1 != i1:
                if FinalRoadMap[i1][j1]==1 and TrafficMatrix[i1][j1]>0:
                        gia = gia + listNodeBackbone[i].caculate_distance(listNodeBackbone[j])*n[i1, j1]  
    return gia/2         

def PrimDijkstra(NumNode, TrafficMatrix, ListMentor, C, anpha, Umin):

    listNodeBackbone = []
    homeNode = None

    # Tìm Home Node 
    for _list in ListMentor:
        listNodeBackbone.append(_list[0])

    MomentHomeNode = math.inf
    for targetNode in listNodeBackbone:
        MomentTargetNode = 0
        for otherNode in listNodeBackbone:
            if targetNode != otherNode:
                MomentTargetNode += targetNode.caculate_distance(otherNode)*otherNode.get_traffic()
        if MomentTargetNode < MomentHomeNode:
            homeNode = targetNode
            MomentHomeNode = MomentTargetNode

        print("Xét nút: ",targetNode.get_name())
        print("Moment:",MomentTargetNode)

    print("Nút home:",homeNode.get_name())
    # Dựng cây với Prim - Dijkstra BFS
    color = [0] * NumNode
    L = [math.inf] * NumNode
    d = [0] * NumNode
    color[homeNode.get_name() - 1] = 1
    d[homeNode.get_name() - 1] = 0
    pre = [-1] * NumNode
    queue = [homeNode]
    while len(queue) > 0:
        # print(len(queue))
        currentNode = queue[0]
        for q in queue:
            if L[q.get_name() - 1] < L[currentNode.get_name() - 1]:
                currentNode = q
        queue.remove(currentNode)
        indexCurrentNode = currentNode.get_name() - 1
        for neighborNode in listNodeBackbone:
            if currentNode == neighborNode or neighborNode== homeNode:
                continue
            indexNeighborNode = neighborNode.get_name() - 1
            distance = neighborNode.caculate_distance(currentNode)
            new_L = anpha * d[indexCurrentNode] + distance
            if color[indexNeighborNode] == 0:
                L[indexNeighborNode] = new_L
                d[indexNeighborNode] = d[indexCurrentNode] + distance
                color[indexNeighborNode] = 1
                pre[indexNeighborNode] = indexCurrentNode
                queue.append(neighborNode)
            else:
                if L[indexNeighborNode] > new_L and indexNeighborNode!=pre[indexCurrentNode] and indexCurrentNode!=pre[indexNeighborNode]:
                    L[indexNeighborNode] = new_L
                    d[indexNeighborNode] = d[indexCurrentNode] + distance
                    pre[indexNeighborNode] = indexCurrentNode

    RoadMatrix = [[-1] * NumNode for i in range(NumNode)]
    for node in listNodeBackbone:
        index = node.get_name() - 1
        if pre[index] != -1:
            RoadMatrix[index][pre[index]] = 1
            RoadMatrix[pre[index]][index] = 1

    Node.matplotList(listNodeBackbone, 1000, RoadMatrix)
    
    
    # Cập nhật lưu lượng
    for i in range(len(ListMentor)-1):
        _list1 = ListMentor[i]
        k = _list1[0].get_name() - 1
        for j in range(i+1, len(ListMentor)):
            _list2 = ListMentor[j]
            q = _list2[0].get_name() - 1
            for i1 in range(0, len(_list1)):
                k1 = _list1[i1].get_name() - 1
                for i2 in range(0, len(_list2)):
                    q1 = _list2[i2].get_name() - 1
                    TrafficMatrix[k][q] += TrafficMatrix[k1][q1]
                    TrafficMatrix[q][k] += TrafficMatrix[k1][q1]
    
    print("Cap nhat luu luong: ")
    for i in range(len(ListMentor)-1):

        for j in range(i+1, len(ListMentor)):
            _list1 = ListMentor[i]
            _list2 = ListMentor[j]
            k = _list1[0].get_name() - 1
            q = _list2[0].get_name() - 1
            print("Luu luong({}, {}): {}".format(k+1, q+1, TrafficMatrix[k][q]))

    writeOutput1(listNodeBackbone, TrafficMatrix)

    FinalRoadMap = copy.deepcopy(RoadMatrix)
    # Tính số đường sử dụng + Độ sử dụng
    color = [0] * NumNode
    
    n = {}
            
    def DFS(start, hops, current, _list):
        if (len(_list) - 1 == hops):
            
            s = _list[0].get_name() - 1
            e = _list[hops].get_name() - 1
            if (s > e):
                return
            print("--------------------------------------------------------")
            print("Đường đi: ", [i.get_name() for i in _list])
            if TrafficMatrix[s][e] == 0:
                print("Hai nút không có lưu lượng")
                return
            n[s, e] = math.ceil(TrafficMatrix[s][e]/C)
            n[e, s] = n[s,e]
            u = TrafficMatrix[s][e] / (n[s, e]*C)

            if hops == 1:
                print("T({}, {}): {}, n = {}".format(s+1, e+1, TrafficMatrix[s][e], n[s, e]))
                return

            if u >= Umin :
                print("U > Umin => Thêm liên kết trực tiếp")
                FinalRoadMap[s][e] = 1
                FinalRoadMap[e][s] = 1

            else:
                print("U < Umin => Chuyển lưu lượng qua mạng")

                hNode = _list[1]
                minDistance = _list[0].caculate_distance(_list[1]) + _list[hops].caculate_distance(_list[1])
                for i in range(2, len(_list)-1):
                    distance = _list[0].caculate_distance(_list[i]) + _list[hops].caculate_distance(_list[i])
                    if minDistance > distance:
                        minDistance = distance
                        hNode = _list[i]
                iHomeNode = hNode.get_name() - 1
                TrafficMatrix[iHomeNode][s] += TrafficMatrix[s][e]
                TrafficMatrix[s][iHomeNode] += TrafficMatrix[s][e]
                TrafficMatrix[iHomeNode][e] += TrafficMatrix[s][e]
                TrafficMatrix[e][iHomeNode] += TrafficMatrix[s][e]
                print("Nút home: {}".format(iHomeNode+1))
                print("T({}, {}): {}".format(s+1, iHomeNode+1, TrafficMatrix[s][iHomeNode]))
                print("T({}, {}): {}".format(iHomeNode+1, e+1, TrafficMatrix[iHomeNode][e]))
            print("T({}, {}): {}, n = {}, u = {}".format(s+1, e+1, TrafficMatrix[s][e], n[s, e], u))

            return

        i = current.get_name() - 1
        for next in listNodeBackbone:
            j = next.get_name() - 1
            if (RoadMatrix[i][j] == 1) and (next not in _list):
                _list.append(next)
                color[j] = 1
                DFS(start, hops, next, _list)
                _list = _list[:-1]
                color[j] = 0

    original_stdout = sys.stdout
    with open('mentor_output_2.txt', 'w', encoding='utf8') as f:
        sys.stdout = f
        maxHop = len(listNodeBackbone) - 1
        for i in range(maxHop, 0, -1):
            print("***********************")
            print("Xét {} hops: ".format(i))
            for start in listNodeBackbone:
                color = [0] * NumNode
                DFS(start, i, start, [start])
        print("----------------------------------------------------------------------")        
        print("Gia cua mang Backbone: ", cal_GiaBackbone(n, FinalRoadMap, listNodeBackbone, TrafficMatrix))        
        sys.stdout = original_stdout
   
    Node.matplotList1(listNodeBackbone, 1000, FinalRoadMap, n, TrafficMatrix)
    return cal_GiaBackbone(n, FinalRoadMap, listNodeBackbone, TrafficMatrix)


def writeOutput1(listNodeBackbone, TrafficMatrix):
    original_stdout = sys.stdout
    with open('mentor_output.txt', 'a', encoding='utf8') as f:
        sys.stdout = f
        print("Lưu lượng thực tế giữa các nút backbone:")
        for i in range(len(listNodeBackbone)-1):

            for j in range(i+1, len(listNodeBackbone)):
                k = listNodeBackbone[i].get_name() - 1
                q = listNodeBackbone[j].get_name() - 1
                print("Luu luong({}, {}): {}".format(k+1, q+1, TrafficMatrix[k][q]))

        sys.stdout = original_stdout
