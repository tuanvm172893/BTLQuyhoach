# Thư viện
import random
import math
import matplotlib.pyplot as plt
import Node



def sortListPosition(m):
    return m.get_position_x()

def cal_distance(i, j):
    return round(0.5*(math.sqrt((i.x - j.x) ** 2 + (i.y - j.y) ** 2)),4)
    
def Global_Init_Topo(MAX,NumNode,DeBug):
    '''

    Bước 1: Dựng Topology mạng và tính toán lưu lượng tại từng nút mạng

    '''
    print("{:*<100}".format(''))
    print("Bước 1: Dựng Topology mạng và tính toán lưu lượng tại từng nút mạng")
    print("{:*<100}".format(''))
    ListPosition = []


    # Tạo các nút ở vị trí random và đưa vào danh sách, sắp xếp các nút theo thứ tự tọa độ x tăng dần
    count_Node = 0
    while count_Node <100 :
        n = Node.Node()
        n.create_position(MAX)
        n.create_name(count_Node + 1)
        if count_Node == 0:
            ListPosition.append(n)
            count_Node+=1
        else:
            check = 0   
            for n1 in ListPosition:
                if n.get_position_x == n1.get_position_x and n.get_position_y == n1.get_position_y:
                    check = 1
                    break
            if check == 0:
                ListPosition.append(n)
                count_Node+=1
    print(len(ListPosition))   

    with open('Danh_sach_canh.txt', 'a', encoding='utf8') as f:
        for i in ListPosition:
            for j in ListPosition:
                if int(j.name)> int(i.name):
                    f.write("Gia lien ket giua Nut " + str(i.name) + "(" + str(i.x) + "," + str(i.y) + ") va Nut " + str(j.name) + "(" + str(j.x) + "," + str(j.y) + ") la: " + str(cal_distance(i, j)) + "\n" )
    # Cài đặt lại vị trí các nút theo đề bài
    # Nút 1 -> ListPosition[0]

    # Tạo ma trận lưu trữ thông tin về lưu lượng giữa các nút.

    TrafficMatrix = [[0] * NumNode for i in range(NumNode)]

    # for i in TrafficMatrix:
    #     for j in i:
    #         print(j,end=' ')
    #     print()

    # Đưa thông tin lưu lượng vào ma trận

    # Đưa thông tin bằng điểm cố định

    def set_traffic(m, n, value):
        TrafficMatrix[m - 1][n - 1] = value
        TrafficMatrix[n - 1][m - 1] = value

    # Đưa thông tin về mối quan hệ

    for i in range(NumNode):

        if i + 3 < NumNode:
            set_traffic(i + 1, i + 3 + 1, 1)
        if i + 60 < NumNode:
            set_traffic(i + 1, i + 60 + 1, 1)
        if i + 78 < NumNode:
            set_traffic(i + 1, i + 78 + 1, 3)
        if i + 93 < NumNode:
            set_traffic(i + 1, i + 93 + 1, 4)

    set_traffic(13, 7, 20)
    set_traffic(24, 69, 6)
    set_traffic(20, 48, 26)
    set_traffic(55, 35, 10)

    # Sau khi có ma trận lưu lượng, Tiến hành tính lưu lượng của mỗi nút và cập nhật vào nút

    for i in range(len(ListPosition)):
        ListPosition[i].set_traffic(sum(TrafficMatrix[ListPosition[i].get_name() - 1]))

    if DeBug:

        print("---------Topology mạng-------------")
        Node.printInitialList(ListPosition)

        print("----------Kết thúc tạo topology-------------")

    Node.matplotList(ListPosition, MAX)
    Node.plt.show()
    return { "ListPosition": ListPosition, "TrafficMatrix": TrafficMatrix }

def Global_Init_Topo_Fix_Position(MAX,NumNode,DeBug):
    '''

    Bước 1: Dựng Topology mạng và tính toán lưu lượng tại từng nút mạng

    '''
    print("{:*<100}".format(''))
    print("Bước 1: Dựng Topology mạng và tính toán lưu lượng tại từng nút mạng")
    print("{:*<100}".format(''))
    ListPosition = []

    ListXY = [
        [1, 1],
        [0, 0],
        [2, 3],
        [2, 0],
        [4, 2],
        [5, 0],
        [5, 3],
        [6, 1]
    ]

    WI = [7, 3, 2, 5, 4, 4, 2, 6]
    # Tạo các nút ở vị trí xác định và đưa vào danh sách, sắp xếp các nút theo thứ tự tọa độ x tăng dần
    for i in range(NumNode):
        n = Node.Node()
        n.set_position(ListXY[i][0],ListXY[i][1])
        n.create_name(i + 1)
        n.set_traffic(WI[i])
        ListPosition.append(n)
      #  ListPosition.sort(key=sortListPosition)

    if DeBug:

        print("---------Topology mạng-------------")
        Node.printInitialList(ListPosition)

        print("----------Kết thúc tạo topology-------------")
    Node.matplotList(ListPosition, MAX)
    Node.plt.show()
    return ListPosition