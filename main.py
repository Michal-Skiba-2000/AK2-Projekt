from graph.edge_list_graph import EdgeListGraph

if __name__ == '__main__':
    control_flow_graph = EdgeListGraph([['a', 'b', 100], ['a', 'c', 40], ['b', 'c', 30], ['b', 'e', 10], ['c', 'd', 90]])
    print('Graph: {}'.format(control_flow_graph))
    control_flow_graph.tsp('a')
    control_flow_graph.pettis_hansen()
    print('')

    control_flow_graph = EdgeListGraph([['a', 'b', 100], ['a', 'c', 40], ['b', 'c', 30], ['c', 'd', 90]])
    print('Graph: {}'.format(control_flow_graph))
    control_flow_graph.tsp('a')
    control_flow_graph.pettis_hansen()
    print('')

    control_flow_graph = EdgeListGraph([['m', 'a', 100], ['a', 'b', 80], ['a', 'c', 20]])
    print('Graph: {}'.format(control_flow_graph))
    control_flow_graph.tsp('m')
    control_flow_graph.pettis_hansen()
    print('')

    control_flow_graph = EdgeListGraph([['m', 'a', 100], ['a', 'b', 80], ['a', 'c', 20], ['b', 'd', 80], ['c', 'e', 20]])
    print('Graph: {}'.format(control_flow_graph))
    control_flow_graph.tsp('m')
    control_flow_graph.pettis_hansen()
    print('')

    control_flow_graph = EdgeListGraph([['a', 'b', 100], ['a', 'c', 90], ['a', 'd', 80], ['b', 'c', 20], ['b', 'd', 40], ['c', 'd', 30]])
    print('Graph: {}'.format(control_flow_graph))
    control_flow_graph.tsp('a')
    control_flow_graph.pettis_hansen()
    print('')

    control_flow_graph = EdgeListGraph([['a', 'b', 100, 1, 20], ['a', 'c', 90, 1, 15], ['a', 'd', 80, 1, 40], ['b', 'c', 20, 20, 15], ['b', 'd', 40, 20, 40], ['c', 'd', 30, 15, 40]])
    print('Graph: {}'.format(control_flow_graph))
    control_flow_graph.cache()
    print('')
