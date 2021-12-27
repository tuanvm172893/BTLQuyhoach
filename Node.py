# Thư viện
import random
import math
import matplotlib.pyplot as plt
import math


# Các cài đặt mặc định


# Lớp mô hình hóa các nút
# Thuộc Tính:
#   Tọa độ x,y
#   Khoảng cách tới nút trung tâm đang tạm xét (tính theo Đề các)
#   Tên nút đánh từ 1 đến nút MAX
class Node:
    name = 0
    x = 0
    y = 0

    # MENTOR
    traffic = 0
    weight = 0
    awardPoint = 0
    distanceToCenter = 0

    def __init__(self):
        self.ListConnect = []

    def create_name(self, name):
        self.name = name
        self.group_node_to_center = name

    def create_position(self, MAX):
        self.x = random.randint(0, MAX)
        self.y = random.randint(0, MAX)

    def set_position(self, x, y):
        self.x = round(x,2)
        self.y = round(y,2)

    def set_distance(self, center):
        self.distanceToCenter = round(0.5*(math.sqrt((self.get_position_x() - center.get_position_x()) ** 2 + (
                self.get_position_y() - center.get_position_y()) ** 2)),4)

    def set_traffic(self, t):
        self.traffic = t

    def set_award(self, t):
        self.awardPoint = t

    def set_weight(self, w):
        self.weight = w

    def set_connect(self,i):
        self.ListConnect.append(i)


    def check_connect(self,i):
        if i in self.ListConnect:
            return True
        return False

    def remove_connect(self,i):
        self.ListConnect.remove(i)

    def get_list_connect(self):
        return self.ListConnect

    def reset_list_connect(self):
        self.ListConnect.clear()

    def set_next_connect(self, index):
        self.next_connect = index

    def get_weight(self):
        return self.weight

    def get_award(self):
        return self.awardPoint

    def get_traffic(self):
        return self.traffic

    def get_distance(self):
        return self.distanceToCenter

    def get_position_x(self):
        return self.x

    def get_position_y(self):
        return self.y

    def get_name(self):
        return self.name

    def compare_position(self, other):  # Return 1 if same 0 if not same
        return (self.get_position_x() == other.get_position_x()) and (self.get_position_y() == other.get_position_y())

    def caculate_distance(self, other):
        return round(0.5*(math.sqrt((self.get_position_x() - other.get_position_x()) ** 2 + (
                self.get_position_y() - other.get_position_y()) ** 2)),4)

    def copyNode(self, other):
        self.x = other.get_position_x()
        self.y = other.get_position_y()
        self.name = other.get_name()
        self.traffic = other.get_traffic()


    def printInitial(self):
        print('Node: {:<3} | Position: x = {:<4} y = {:<4} | Traffic: {:<2} | Weight Esau William: {:<2}'.format(self.get_name(),
                                                                                                       self.get_position_x(),
                                                                                                       self.get_position_y(),
                                                                                                       self.get_traffic(),
                                                                                                       self.get_weight_ew()))

    def printMentor(self):
        print('Node: {:<3} | Position: x = {:<4} y = {:<4} | Traffic: {:<2}'.format(
            self.get_name(),
            self.get_position_x(),
            self.get_position_y(),
            self.get_traffic()))

    def printCenterPress(self):
        print('Node trung tâm trọng lực: Position: x = {:<6} y = {:<6}'.format(round(self.x,2),round(self.y,2)))


'''




'''


# Tạo một số hàm

# Hàm sắp xếp danh sách dựa trên tọa độ x của node


def sortListPosition(m):
    return m.get_position_x()


def printList(_list):
    for i in _list:
        print(i.get_name)
    print()

def printInitialList(_list):
    for i in _list:
        i.printInitial()

def printMentorList(_list):
    for i in _list:
        i.printMentor()


def printList2D(_list):
    for i in _list:
        for j in i:
            print(j.get_name)
        print()


def find_index_node(m,ListPosition):
    for i in range(0, len(ListPosition)):
        if ListPosition[i].get_name() == m:
            return i
    return 0

def matplotList(_list, MAX, RoadMatrix = None):
    xpos = []
    ypos = []
    npos = []
    for i in _list:
        xpos.append(i.get_position_x())
        ypos.append(i.get_position_y())
        npos.append(i.get_name())

    for i in range(0, len(_list)):
        plt.text(xpos[i], ypos[i], str(_list[i].get_name()), color='black', size=10, rotation=0.,
                 ha="center", va="center",
                 bbox=dict(facecolor=(1., 0.8, 0.8), edgecolor='none', boxstyle='round')
                 )

    plt.plot(xpos[0], ypos[0], 'ro', markersize=10, markerfacecolor='r',
                 markeredgewidth=1.5, markeredgecolor=(0, 0, 0, 1))
    if RoadMatrix != None:
        for i in range(len(npos)-1):
            for j in range(i+1, len(npos)):
                if RoadMatrix[npos[i]-1][npos[j]-1] == 1:
                    plt.plot([xpos[i], xpos[j]], [ypos[i], ypos[j]])
    plt_margin = MAX * 0.05
    plt.axis([-plt_margin, MAX + plt_margin, -plt_margin, MAX + plt_margin])
    plt.show()

def matplotList1(_list, MAX, RoadMatrix, n, TrafficMatrix):
    xpos = []
    ypos = []
    npos = []
    for i in _list:
        xpos.append(i.get_position_x())
        ypos.append(i.get_position_y())
        npos.append(i.get_name())

    for i in range(0, len(_list)):
        plt.text(xpos[i], ypos[i], str(_list[i].get_name()), color='black', size=10, rotation=0.,
                 ha="center", va="center",
                 bbox=dict(facecolor=(1., 0.8, 0.8), edgecolor='none', boxstyle='round')
                 )

    plt.plot(xpos[0], ypos[0], 'ro', markersize=10, markerfacecolor='r',
                 markeredgewidth=1.5, markeredgecolor=(0, 0, 0, 1))
    if RoadMatrix != None:
        for i in range(len(npos)-1):
            for j in range(i+1, len(npos)):
                if RoadMatrix[npos[i]-1][npos[j]-1] == 1:
                    plt.plot([xpos[i], xpos[j]], [ypos[i], ypos[j]])
                if RoadMatrix[npos[i]-1][npos[j]-1] == 1 and TrafficMatrix[npos[i]-1][npos[j]-1]>0:
                    plt.text(int((xpos[i]+ xpos[j])/2), int((ypos[i]+ ypos[j])/2), "x" + str(n[npos[i]-1, npos[j]-1]))
    plt_margin = MAX * 0.05
    plt.axis([-plt_margin, MAX + plt_margin, -plt_margin, MAX + plt_margin])
    plt.show()
    
def matplotconnectpoints(x, y, n1, n2):
    p1 = n1
    p2 = n2
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1, x2], [y1, y2], 'k-')


def matplotListToCenter(_list, MAX):
    xpos = []
    ypos = []
    npos = []
    for i in _list:
        xpos.append(i.get_position_x())
        ypos.append(i.get_position_y())
        npos.append(i.get_name())

    #for i in range(1, len(_list)):
    #    matplotconnectpoints(xpos, ypos, i, 0)

    plt.plot(xpos, ypos, 'ro', markersize=5, markerfacecolor='w',
             markeredgewidth=1.5, markeredgecolor=(0, 0, 0, 1))

    plt.plot(xpos[0], ypos[0], 'ro', markersize=10, markerfacecolor='r',
             markeredgewidth=1.5, markeredgecolor=(0, 0, 0, 1))

    plt_margin = MAX * 0.05
    plt.axis([-plt_margin, MAX + plt_margin, -plt_margin, MAX + plt_margin])



def matplot_mentor(_list_mentor,MAX):
    for _list in _list_mentor:
        xpos = []
        ypos = []
        npos = []
        print([i.get_name() for i in _list])
        for i in _list:
            xpos.append(i.get_position_x())
            ypos.append(i.get_position_y())
            npos.append(i.get_name())

        plt.text(xpos[0], ypos[0], str(_list[0].get_name()), color='white', size=10, rotation=0.,
                 ha="center", va="center",
                 bbox=dict(facecolor=(1., 0., 0.), edgecolor='black', boxstyle='round')
                 )
        for i in range(1, len(_list)):
            plt.text(xpos[i], ypos[i], str(_list[i].get_name()), color='black', size=10, rotation=0.,
                     ha="center", va="center",
                     bbox=dict(facecolor=(1., 0.8, 0.8), edgecolor='none', boxstyle='round')
                     )

        plt.plot(xpos, ypos, 'ro', markersize=5, markerfacecolor='w',
                 markeredgewidth=1.5, markeredgecolor=(0, 0, 0, 1))

        plt.plot(xpos[0], ypos[0], 'ro', markersize=10, markerfacecolor='r',
                 markeredgewidth=1.5, markeredgecolor=(0, 0, 0, 1))

    plt_margin = MAX * 0.05
    plt.axis([-plt_margin, MAX + plt_margin, -plt_margin, MAX + plt_margin])