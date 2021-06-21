import sys


class EdgeListGraph:
    def __init__(self, edge_list):
        self.edge_list = edge_list

    def pettis_hansen(self):
        edge_list = list(self.edge_list)
        while len(edge_list) != 1:
            max_edge = self._get_max_edge(edge_list)
            edge_list.remove(max_edge)
            first_vertex_edges = self._get_vertex_edges(max_edge[0], edge_list)
            second_vertex_edges = self._get_vertex_edges(max_edge[1], edge_list)
            new_vertex_name = self._join_edge_with_reorder(max_edge)
            for info in first_vertex_edges:
                vertex_in_info = self._vertex_in_info(info[1], second_vertex_edges)
                value = 0
                if vertex_in_info is not None:
                    edge = second_vertex_edges[vertex_in_info][0]
                    value = edge[2]
                    edge_list.remove(edge)
                    second_vertex_edges.pop(vertex_in_info)
                index = edge_list.index(info[0])
                edge_list[index] = [new_vertex_name, info[1], info[0][2]+value]
            for info in second_vertex_edges:
                index = edge_list.index(info[0])
                edge_list[index] = [new_vertex_name, info[1], info[0][2]]
        max_order = self._join_edge_with_reorder(edge_list[0])
        print('Pettis-Hansen order: {}'.format(max_order))
        print('Control flow transfers: {}'.format(self._get_control_flow_transfer(max_order)))
        return max_order

    def tsp(self, first_vertex):
        vertexes = []
        for edge in self.edge_list:
            vertexes.append(edge[0])
            vertexes.append(edge[1])
            edge_list = list(self.edge_list)
        vertexes = list(set(vertexes))
        tsp_order = first_vertex
        vertexes.remove(first_vertex)
        while True:
            max_successor = -sys.maxsize
            max_successor_vertex = None
            for edge in edge_list:
                if first_vertex in edge:
                    if first_vertex == edge[0]:
                        second_vertex = edge[1]
                    else:
                        second_vertex = edge[0]
                    if second_vertex in vertexes:
                        if edge[2] > max_successor:
                            max_successor = edge[2]
                            max_successor_vertex = second_vertex
            if max_successor_vertex is not None:
                tsp_order += max_successor_vertex
                vertexes.remove(max_successor_vertex)
            else:
                break
        while len(vertexes):
            max_edge = [None, None, -sys.maxsize]
            for edge in edge_list:
                if any(vertex in edge for vertex in vertexes) and edge[2] > max_edge[2]:
                    max_edge = edge
            if max_edge == [None, None, sys.maxsize]:
                raise
            if max_edge[0] in vertexes:
                tsp_order += max_edge[0]
                vertexes.remove(max_edge[0])
            else:
                tsp_order += max_edge[1]
                vertexes.remove(max_edge[1])

        print('TSP order: {}'.format(tsp_order))
        print('Control flow transfers: {}'.format(self._get_control_flow_transfer(tsp_order)))

    def cache(self):
        edge_list = list(self.edge_list)
        while len(edge_list) != 1:
            max_edge = self._get_max_edge(edge_list)
            edge_list.remove(max_edge)
            first_vertex_edges = self._get_vertex_edges(max_edge[0], edge_list)
            second_vertex_edges = self._get_vertex_edges(max_edge[1], edge_list)
            new_vertex_name = self._join_edge_with__cache_reorder(max_edge)
            for info in first_vertex_edges:
                vertex_in_info = self._vertex_in_info(info[1], second_vertex_edges)
                value = 0
                size = 0
                if vertex_in_info is not None:
                    edge = second_vertex_edges[vertex_in_info][0]
                    value = edge[2]
                    size = edge[3]
                    edge_list.remove(edge)
                    second_vertex_edges.pop(vertex_in_info)
                index = edge_list.index(info[0])
                if info[0][0] == info[1]:
                    size_2 = info[0][3]
                else:
                    size_2 = info[0][4]
                edge_list[index] = [new_vertex_name, info[1], info[0][2]+value, info[0][3]+size, size_2]
            for info in second_vertex_edges:
                index = edge_list.index(info[0])
                edge_list[index] = [new_vertex_name, info[1], info[0][2], info[0][3]]
        max_order = self._join_edge_with__cache_reorder(edge_list[0])
        print('Cache order: {}'.format(max_order))
        print('Control flow transfers: {}'.format(self._get_control_flow_transfer(max_order)))
        return max_order

    @staticmethod
    def _get_max_edge(edge_list):
        max_edge = [None, None, -sys.maxsize]
        for edge in edge_list:
            if edge[2] > max_edge[2]:
                max_edge = edge
        return max_edge

    @staticmethod
    def _get_vertex_edges(vertex, edge_list):
        result = []
        for edge in edge_list:
            if vertex in edge:
                temp = [edge]
                if vertex != edge[0]:
                    temp.append(edge[0])
                elif vertex != edge[1]:
                    temp.append(edge[1])
                else:
                    raise
                result.append(temp)
        return result

    @staticmethod
    def _vertex_in_info(vertex, info):
        for i in range(len(info)):
            if vertex == info[i][1]:
                return i
        return None

    def _join_edge_with_reorder(self, edge):
        len_0 = len(edge[0])
        len_1 = len(edge[1])
        if len_0 == 1:
            value_0 = self._get_edge_value_for_vertexes(edge[0], edge[1][0])
            value_1 = self._get_edge_value_for_vertexes(edge[0], edge[1][-1])
            if value_0 == 0:
                return edge[1] + edge[0]
            elif value_1 == 0:
                return edge[0] + edge[1]
            elif value_0 > value_1:
                return edge[0] + edge[1]
            else:
                return edge[1] + edge[0]
        elif len_1 == 1:
            value_0 = self._get_edge_value_for_vertexes(edge[0][0], edge[1])
            value_1 = self._get_edge_value_for_vertexes(edge[0][-1], edge[1])
            if value_0 == 0:
                return edge[0] + edge[1]
            elif value_1 == 0:
                return edge[1] + edge[0]
            elif value_0 > value_1:
                return edge[1] + edge[0]
            else:
                return edge[0] + edge[1]
        elif len_0 == 2:
            value_0 = self._get_edge_value_for_vertexes(edge[0][0], edge[1][0])
            value_1 = self._get_edge_value_for_vertexes(edge[0][0], edge[1][-1])
            value_2 = self._get_edge_value_for_vertexes(edge[0][1], edge[1][0])
            value_3 = self._get_edge_value_for_vertexes(edge[0][1], edge[1][-1])

            values = [value_0, value_1, value_2, value_3]
            values = [value for value in values if value != 0]

            if len(values) == 0:
                return edge[0] + edge[1]

            max_value = max(values)

            if max_value == value_0:
                return edge[0][1] + edge[0][0] + edge[1]
            elif max_value == value_1:
                return edge[1] + edge[0]
            elif max_value == value_2:
                return edge[0] + edge[1]
            elif max_value == value_3:
                return edge[1] + edge[0][1] + edge[0][0]
        elif len_1 == 2:
            value_0 = self._get_edge_value_for_vertexes(edge[0][0], edge[1][0])
            value_1 = self._get_edge_value_for_vertexes(edge[0][-1], edge[1][0])
            value_2 = self._get_edge_value_for_vertexes(edge[0][0], edge[1][1])
            value_3 = self._get_edge_value_for_vertexes(edge[0][-1], edge[1][1])

            values = [value_0, value_1, value_2, value_3]
            values = [value for value in values if value != 0]

            if len(values) == 0:
                return edge[0] + edge[1]

            max_value = max(values)

            if max_value == value_0:
                return edge[1][1] + edge[1][0] + edge[0]
            elif max_value == value_1:
                return edge[0] + edge[1]
            elif max_value == value_2:
                return edge[1] + edge[0]
            elif max_value == value_3:
                return edge[0] + edge[1][1] + edge[1][0]
        else:
            return edge[0] + edge[1]

    def _join_edge_with__cache_reorder(self, edge):
        if edge[3] > edge[4]:
            return edge[1] + edge[0]
        else:
            return edge[0] + edge[1]

    def _get_edge_value_for_vertexes(self, vertex_0, vertex_1):
        for edge in self.edge_list:
            if vertex_0 in edge and vertex_1 in edge:
                return edge[2]
        return 0

    def _get_control_flow_transfer(self, max_order):
        control_flow_transfer = 0
        for i in range(len(max_order)-1):
            temp_value = self._get_edge_value_for_vertexes(max_order[i], max_order[i+1])
            if temp_value is not None:
                control_flow_transfer += temp_value
        return control_flow_transfer

    def __str__(self):
        return str(self.edge_list)