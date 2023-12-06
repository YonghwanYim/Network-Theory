"""
* Author : Yonghwan Yim
* Title : Label Correcting Algorithm using FIFO
"""

import numpy as np

# cycle check fuction : DFS 통해 확인
def cycle_check(arcs, stack, edge):
    if edge in stack:
        global IsCycle
        IsCycle = True
        return True

    stack.append(edge)
    successive_edges = [arc for arc in arcs if arc[0] == edge[1]]

    for edge in successive_edges:
        cycle_check(arcs, stack, edge)
    stack.pop()

    return IsCycle


def get_node_arc_set(total_num_arcs, total_num_nodes, negative_ratio, negative_cost_range, positive_cost_range):
    num_arcs = 0
    arcs = []

    negative_cost = np.random.choice(negative_cost_range, int(total_num_arcs * negative_ratio))
    positive_cost = np.random.choice(positive_cost_range, int(total_num_arcs * (1 - negative_ratio)))
    costs = np.concatenate([negative_cost, positive_cost])
    np.random.shuffle(costs)

    while num_arcs != total_num_arcs:
        i, j = np.random.choice(np.arange(0, total_num_nodes), 2, replace=False)  # 랜덤으로 서로 다른 두 노드 i,j 선택
        if (i, j) in list(map(lambda x: x[:2], arcs)):  # 이미 존재하는 arc 뽑았을 경우 continue
            continue

        temp_arcs = copy.deepcopy(arcs)
        temp_arcs.append((i, j))

        global IsCycle
        IsCycle = False
        IsCycle = cycle_check(temp_arcs, [], (i, j))  # 전역 변수 통해 Cycle 이 있는지 아닌지 확인

        if IsCycle == True:
            continue
        else:  # (i,j) 를 arcs에 추가했을 때 Cycle이 발생하지 않으므로 arcs 에 (i,j)를 추가 ( arcs := temp_arcs )
            arcs.append((i, j, costs[num_arcs]))
            num_arcs += 1

    return arcs


def init_FIFO(s, total_num_nodes ) :
    inf = 99999
    d = [ inf if idx != s else 0 for idx in range(total_num_nodes) ]
    pred = [ inf if idx != s else 0 for idx in range(total_num_nodes) ]
    q = [s]
    return q, d, pred

def MLC_FIFO( q, d, pred, arcs ):
    while q != [] :
        i = q.pop(0)
        i_arcs = [ arc for arc in arcs if arc[0] == i]

        for arc in i_arcs :
            j = arc[1] ; cost = arc[2]
            if d[j] > d[i] + cost :
                d[j] = d[i] + cost
                pred[j] = i
                if j not in q :
                    q.append(j)
    return d, pred