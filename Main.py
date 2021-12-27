import Node
import InitialTopo
import MENTOR
from PrimDijkstra import PrimDijkstra
import matplotlib.pyplot as plt
import copy

if __name__ == '__main__':
    
    MAX=1000
    NumNode = 100 # Số lượng nút trong mạng
    RadiusRatio = 0.3 # Tỉ lệ dùng để tính bán kính quét mạng truy nhập của thuật toán MENTOR
    C = 12 # Dung lượng 1 liên kết
    w = 2  # Trọng số lưu lượng chuẩn hóa dùng để xét nút backbone của thuật toán MENTOR
    anpha = 0.2
    Umin = 0.75
    list_anpha = [x / 10.0 for x in range(0, 11, 1)]
    list_giaBackBone = []
    InitialTopo = InitialTopo.Global_Init_Topo(MAX,NumNode,False)
    ListPosition = InitialTopo["ListPosition"]
    TrafficMatrix = InitialTopo["TrafficMatrix"]
    # ListPosition = InitialTopo.Global_Init_Topo_Fix_Position(MAX,NumNode,False)
    # False/ True: Nếu chọn True, toàn bộ các bước trong tạo topology mạng sẽ được giám sát và hiển thị

    ListMentor = MENTOR.MenTor(ListPosition,TrafficMatrix,MAX,C,w,RadiusRatio,0,False)
    # 0: Là số giới hạn nút đầu cuối của thuật toán MENTOR.
    # Khi một nút Backbone tìm thấy số lượng nút đầu cuối đạt của một mạng truy nhập tới giới hạn. Nó ngừng việc quét tìm nút đầu cuối. Nếu cài đặt giá trị này bằng 0 thì xem như không có giới hạn số lượng nút đầu cuối.
    # False/ True: Bật tắt giám sát thuật toán
    
    for apha in list_anpha:
        TrafficMatrix1 = copy.deepcopy(TrafficMatrix)
        ListMentor1 = copy.deepcopy(ListMentor)
        list_giaBackBone.append(PrimDijkstra(NumNode, TrafficMatrix1, ListMentor, C, apha, Umin))
    plt.plot(list_anpha, list_giaBackBone)
    plt.show()
