import Node
import InitialTopo
import MENTOR
from PrimDijkstra import PrimDijkstra

MAX=1200
NumNode = 100 # Số lượng nút trong mạng
RadiusRatio = 0.3 # Tỉ lệ dùng để tính bán kính quét mạng truy nhập của thuật toán MENTOR
C = 12 # Dung lượng 1 liên kết
w = 2  # Trọng số lưu lượng chuẩn hóa dùng để xét nút backbone của thuật toán MENTOR
anpha = 0.2
Umin = 0.75

InitialTopo = InitialTopo.Global_Init_Topo(MAX,NumNode,False)
ListPosition = InitialTopo["ListPosition"]
TrafficMatrix = InitialTopo["TrafficMatrix"]
# ListPosition = InitialTopo.Global_Init_Topo_Fix_Position(MAX,NumNode,False)
# False/ True: Nếu chọn True, toàn bộ các bước trong tạo topology mạng sẽ được giám sát và hiển thị

ListMentor = MENTOR.MenTor(ListPosition,TrafficMatrix,MAX,C,w,RadiusRatio,10,False)
# 5: Là số giới hạn nút đầu cuối của thuật toán MENTOR.
# Khi một nút Backbone tìm thấy số lượng nút đầu cuối đạt của một mạng truy nhập tới giới hạn. Nó ngừng việc quét tìm nút đầu cuối. Nếu cài đặt giá trị này bằng 0 thì xem như không có giới hạn số lượng nút đầu cuối.
# False/ True: Bật tắt giám sát thuật toán

PrimDijkstra(NumNode, TrafficMatrix, ListMentor, C, anpha, Umin)
# ListFinish = EsauWilliam.Esau_William(ListMentor,w_ew,MAX,5,False)
# False/ True: Bật tắt giám sát thuật toán
# 5: Giới hạn số nút trên cây truy nhập. Nếu đặt bằng 0 thì không giới hạn.

# Node.printList2D(ListFinish)
# Node.matplot_total(ListFinish,MAX)
Node.plt.show()
