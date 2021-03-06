# *===================================*
# -*- coding: utf-8 -*-
# * Time : 2020-01-06 18:07
# * Author : zhangsf
# *===================================*
# 行政区的毗邻行政区结构
graph = {
    '台湾': ['福建'],
    '海南': ['广东'],
    "内蒙古": ["黑龙江", "吉林", "辽宁", "河北", "山西", "陕西", "宁夏", "甘肃"],
    "黑龙江": ["内蒙古", "吉林"],
    "吉林": ["黑龙江", "内蒙古", "辽宁"],
    "辽宁": ["吉林", "内蒙古", "河北"],
    "河北": ["辽宁", "内蒙古", "山西", "北京", "天津", "山东", "河南"],
    '河南': ['河北', '湖北', '陕西', '山西', '安徽', '山东'],
    "山东": ["河北", "河南", '安徽', '江苏'],
    "北京": ["河北", "天津"],
    "天津": ["河北", "北京"],
    "山西": ["河北", "内蒙古", "陕西", "河南"],
    "陕西": ["宁夏", "内蒙古", "甘肃", "河南", "山西", "四川", "重庆", "湖北"],
    "宁夏": ["陕西", "内蒙古", "甘肃"],
    "甘肃": ["宁夏", "内蒙古", "陕西", "青海", "新疆", "四川"],
    "青海": ["甘肃", "西藏", "新疆", "四川"],
    "新疆": ["西藏", "甘肃", "青海"],
    "西藏": ["新疆", "青海", "四川", "云南"],
    "四川": ["青海", "西藏", "甘肃", "陕西", "云南", "贵州", "重庆"],
    '云南': ['西藏', '四川', '贵州', '广西'],
    '重庆': ['陕西', '四川', '贵州', '湖南', '湖北'],
    '贵州': ['重庆', '四川', '云南', '广西', '湖南'],
    '广西': ['云南', '贵州', '湖南', '广东'],
    '广东': ['福建', '江西', '湖南', '广西', '香港', '澳门', '海南'],
    '湖南': ['湖北', '重庆', '贵州', '广西', '广东', '江西'],
    '江西': ['安徽', '湖北', '湖南', '广东', '福建', '浙江'],
    '福建': ['浙江', '江西', '广东', '台湾'],
    '湖北': ['河南', '陕西', '重庆', '湖南', '江西', '安徽'],
    '河南': ['河北', '山西', '陕西', '湖北', '安徽', '江苏', '山东'],
    '安徽': ['河南', '湖北', '江西', '浙江', '江苏', '山东'],
    '浙江': ['上海', '江苏', '安徽', '江西', '福建'],
    '上海': ['江苏', '浙江'],
    '江苏': ['山东', '安徽', '浙江', '上海'],
    '山东': ['河北', '河南', '江苏'],
    '香港': ['广东'],
    '澳门': ['广东'],

}


def BFS(graph, s):
    queue = []
    queue.append(s)
    seen = set()
    seen.add(s)
    parent = {s: None}
    while (len(queue) > 0):
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
                parent[w] = vertex
        # print(vertex)
    return parent


def DFS(graph, s):
    stack = []
    stack.append(s)
    seen = set()

    while (len(stack) > 0):
        vertex = stack.pop()
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
        print(vertex)


if __name__ == '__main__':
    bfs_province = BFS(graph, '湖北')
    for key in bfs_province:
        v = key
        route = "出发->"
        while v != None:
            route += v + "->"
            v = bfs_province[v]
        route += "到啦！"
        print(route)
