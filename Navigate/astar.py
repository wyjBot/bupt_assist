from re import I
from Navigate.build import buildings
class Graph:
    def __init__(self):
    # def __init__(self, adjacency_list):
        # self.adjacency_list = adjacency_list
        self.adjacency_list = {'1': [('2', 580.1043009666452), ('3', 774.6612162745726), ('4', 715.8910531638177), ('5', 730.468342914325), ('6', 546.8491565322196), ('7', 372.59763821044277), ('8', 184.39088914585776), ('9', 260.76809620810593), ('10', 689.6375859826667), ('11', 352.17183305880667), ('12', 689.6375859826667), ('13', 316.48380685273617), ('14', 340.91787867461574), ('23', 554.2571605311022)], '2': [('1', 580.1043009666452), ('3', 241.49741199441456), ('4', 200.80089641234176), ('5', 164.14932226482082), ('6', 290.73871431235295), ('7', 310.4126286090822), ('8', 459.0871376982805), ('9', 496.95170791536674), ('10', 351.5693388223723), ('11', 228.0), ('12', 351.5693388223723), ('13', 322.92568804602706), ('14', 240.40798655618744), ('23', 56.938563381947034)], '3': [('1', 774.6612162745726), ('2', 241.49741199441456), ('4', 60.0), ('5', 95.51963149007642), ('6', 301.56922919953223), ('7', 430.6146769444813), ('8', 620.7253821135398), ('9', 623.9390995922599), ('10', 248.39484696748443), ('11', 438.6171451277298), ('12', 248.39484696748443), ('13', 471.4679204357387), ('14', 455.0), ('23', 296.27858511880333)], '4': [('1', 715.8910531638177), ('2', 200.80089641234176), ('3', 60.0), ('5', 94.25497334358543), ('6', 246.86838598735156), ('7', 370.71417561242515), ('8', 560.8029957123981), ('9', 564.3580423808985), ('10', 214.7091055358389), ('11', 383.43839140075687), ('12', 214.7091055358389), ('13', 411.5361466505707), ('14', 400.2811511925087), ('23', 257.489805623446)], '5': [('1', 730.468342914325), ('2', 164.14932226482082), ('3', 95.51963149007642), ('4', 94.25497334358543), ('6', 319.85621769789), ('7', 413.7305886685199), ('8', 591.053297089188), ('9', 609.3800127998949), ('10', 307.8701024783017), ('11', 382.6447438551848), ('12', 307.8701024783017), ('13', 444.3894688221133), ('14', 397.20146021886677), ('23', 213.84340064636083)], '6': [('1', 546.8491565322196), ('2', 290.73871431235295), ('3', 301.56922919953223), ('4', 246.86838598735156), ('5', 319.85621769789), ('7', 174.4161689752415), ('8', 368.4616669342959), ('9', 342.58429619584143), ('10', 143.12232530251876), ('11', 301.51782700198675), ('12', 143.12232530251876), ('13', 232.74449510138794), ('14', 319.3258523827972), ('23', 329.73474187595093)], '7': [('1', 372.59763821044277), ('2', 310.4126286090822), ('3', 430.6146769444813), ('4', 370.71417561242515), ('5', 413.7305886685199), ('6', 174.4161689752415), ('8', 197.25364381932212), ('9', 195.7268504830137), ('10',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    317.47283348343365), ('11', 185.31055015837603), ('12', 317.47283348343365), ('13', 60.14149981501958), ('14', 198.25236442474022), ('23', 321.1385993617086)], '8': [('1', 184.39088914585776), ('2', 459.0871376982805), ('3', 620.7253821135398), ('4', 560.8029957123981), ('5', 591.053297089188), ('6', 368.4616669342959), ('7', 197.25364381932212), ('9', 100.0), ('10', 509.9019513592785), ('11', 249.2087478400387), ('12', 509.9019513592785), ('13', 149.27156460625713), ('14', 247.0323865407125), ('23', 448.68808765109867)],
                            '9': [('1', 260.76809620810593), ('2', 496.95170791536674), ('3', 623.9390995922599), ('4', 564.3580423808985), ('5', 609.3800127998949), ('6', 342.58429619584143), ('7', 195.7268504830137), ('8', 100.0), ('10', 475.3945729601885), ('11', 313.53628179207584), ('12', 475.3945729601885), ('13', 174.59095051004218), ('14', 316.26729201736936), ('23', 497.31378424491714)], '10': [('1', 689.6375859826667), ('2', 351.5693388223723), ('3', 248.39484696748443), ('4', 214.7091055358389), ('5', 307.8701024783017), ('6', 143.12232530251876), ('7', 317.47283348343365), ('8', 509.9019513592785), ('9', 475.3945729601885),
                                                                                                                                                                                                                                                                                                                                                                                                                        ('11', 429.7731959999367), ('12', 0.0), ('13', 375.8217662669367), ('14', 448.13502429513363), ('23', 402.9900743194552)], '11': [('1', 352.17183305880667), ('2', 228.0), ('3', 438.6171451277298), ('4', 383.43839140075687), ('5', 382.6447438551848), ('6', 301.51782700198675), ('7', 185.31055015837603), ('8', 249.2087478400387), ('9', 313.53628179207584), ('10', 429.7731959999367), ('12', 429.7731959999367), ('13', 153.52198539622916), ('14', 18.439088914585774), ('23', 204.9438947614688)], '12': [('1', 689.6375859826667),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ('2', 351.5693388223723), ('3', 248.39484696748443), ('4', 214.7091055358389), ('5', 307.8701024783017), ('6', 143.12232530251876), ('7', 317.47283348343365), ('8', 509.9019513592785), ('9', 475.3945729601885), ('10', 0.0), ('11', 429.7731959999367), ('13', 375.8217662669367), ('14', 448.13502429513363), ('23', 402.9900743194552)], '13': [('1', 316.48380685273617), ('2', 322.92568804602706), ('3', 471.4679204357387), ('4', 411.5361466505707), ('5', 444.3894688221133), ('6', 232.74449510138794), ('7', 60.14149981501958), ('8', 149.27156460625713), ('9', 174.59095051004218), ('10', 375.8217662669367), ('11', 153.52198539622916), ('12', 375.8217662669367), ('14', 162.22515218054195), ('23', 323.05572274763995)], '14': [('1', 340.91787867461574), ('2', 240.40798655618744), ('3', 455.0), ('4', 400.2811511925087), ('5', 397.20146021886677), ('6', 319.3258523827972), ('7', 198.25236442474022), ('8', 247.0323865407125), ('9', 316.26729201736936), ('10', 448.13502429513363), ('11', 18.439088914585774), ('12', 448.13502429513363), ('13', 162.22515218054195), ('23', 213.88314566603887)], '15': [('16', 81.0), ('17', 133.13526955694348), ('18', 307.5093494513622), ('19', 599.2703897240377), ('20', 248.07257002740147), ('21',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        393.93527387122873), ('22', 365.0)], '16': [('15', 81.0), ('17', 152.6892268629323), ('18', 353.92230785865985), ('19', 657.224466982172), ('20', 259.0926475220785), ('21', 409.9560952102066), ('22', 418.64543470579014)], '17': [('15', 133.13526955694348), ('16',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        152.6892268629323), ('18', 206.20620747203515), ('19', 515.0242712727236), ('20', 115.0), ('21', 526.9250421075088), ('22', 480.88460154178364)], '18': [('15', 307.5093494513622), ('16', 353.92230785865985), ('17', 206.20620747203515), ('19', 310.09837148879063),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ('20', 156.41611170208776), ('21', 670.090292423342), ('22', 565.3503338638795)], '19':
                            [('15', 599.2703897240377), ('16', 657.224466982172), ('17', 515.0242712727236), ('18',
                                                                                                                310.09837148879063), ('20', 456.4263357870578), ('21', 908.7353850269064), ('22', 754.3208866258444)], '20': [('15', 248.07257002740147), ('16', 259.0926475220785), ('17', 115.0), ('18', 156.41611170208776), ('19', 456.4263357870578), ('21', 641.5800807381726), ('22', 585.0)], '21': [('15', 393.93527387122873), ('16', 409.9560952102066), ('17', 526.9250421075088), ('18', 670.090292423342), ('19', 908.7353850269064), ('20', 641.5800807381726), ('22', 205.91260281974002)], '22': [('15', 365.0), ('16', 418.64543470579014), ('17', 480.88460154178364), ('18', 565.3503338638795), ('19', 754.3208866258444), ('20', 585.0), ('21', 205.91260281974002)], '23': [('1', 554.2571605311022), ('2', 56.938563381947034), ('3', 296.27858511880333), ('4', 257.489805623446), ('5', 213.84340064636083), ('6', 329.73474187595093), ('7', 321.1385993617086), ('8', 448.68808765109867), ('9', 497.31378424491714), ('10', 402.9900743194552), ('11', 204.9438947614688), ('12', 402.9900743194552), ('13', 323.05572274763995), ('14', 213.88314566603887)]}
    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristic function with equal values for all nodes
    # use manhattan distance
    def h(self, current, n):
        # H = {
        #     '1': 1,
        #     '2': 1,
        #     '3': 1,
        #     '4': 1,
        #     '5': 1,
        #     '6': 1,
        #     '7': 1
        # }
        return abs(buildings[int(n) - 1]["bx"] - buildings[int(current) - 1]["bx"]) + abs(
            buildings[int(n) - 1]["by"] - buildings[int(current) - 1]["by"])

        # return H[n]

    def h_time(self, current, n):
        return (abs(buildings[int(n) - 1]["bx"] - buildings[int(current) - 1]["bx"]) + abs(
            buildings[int(n) - 1]["by"] - buildings[int(current) - 1]["by"])) / (1/buildings[int(current) - 1]["crowd"])

    ### Enter ID ('start', 'end') to use this function
    def a_star_algorithm(self, start_node, stop_node):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])
        # current = start_node

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        # if start and end not in the same area, then choose to make it two
        if buildings[int(start_node) - 1]['Area'] != buildings[int(stop_node) - 1]['Area']:
            if (buildings[int(start_node) - 1]['Area'] == 1):
                graph1 = Graph()
                first = graph1.a_star_algorithm(start_node, '23')
                first.append('21')
                last = graph1.a_star_algorithm('21', stop_node)
                return first + last
            elif (buildings[int(start_node) - 1]['Area'] == 2):
                graph1 = Graph()
                first = graph1.a_star_algorithm(start_node, '21')
                first.append('23')
                last = graph1.a_star_algorithm('23', stop_node)
                return first + last

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or g[v] + self.h(stop_node, v) < g[n] + self.h(stop_node, n):
                    # if n == None or g[v] + self.h(current, v) < g[n] + self.h(current, n):
                    n = v

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)
            current = n

        print('Path does not exist!')
        return None

    def a_star_algorithm_auto(self, start_node, stop_node):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])
        # current = start_node

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        # if start and end not in the same area, then choose to make it two
        if buildings[int(start_node) - 1]['Area'] != buildings[int(stop_node) - 1]['Area']:
            if (buildings[int(start_node) - 1]['Area'] == 1):
              first = a_star_algorithm(start_node, '23')
              first.append('21')
              last = a_star_algorithm('21', stop_node)
              return first + last
            elif (buildings[int(start_node) - 1]['Area'] == 2):
              first = a_star_algorithm(start_node, '21')
              first.append('23')
              last = a_star_algorithm('23', stop_node)
              return first + last

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or g[v] + self.h(stop_node, v) < g[n] + self.h(stop_node, n):
                    # if n == None or g[v] + self.h(current, v) < g[n] + self.h(current, n):
                    n = v

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + \
                        (weight / buildings[int(m) - 1]["crowd"])

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + (weight / buildings[int(m) - 1]["crowd"]):
                        g[m] = g[n] + \
                            (weight / buildings[int(m) - 1]["crowd"])
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)
            current = n

        print('Path does not exist!')
        return None


    def a_star_algorithm_time(self, start_node, stop_node):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])
        # current = start_node

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        # if start and end not in the same area, then choose to make it two
        if buildings[int(start_node) - 1]['Area'] != buildings[int(stop_node) - 1]['Area']:
            if (buildings[int(start_node) - 1]['Area'] == 1):
                graph1 = Graph()
                first = graph1.a_star_algorithm_time(start_node, '23')
                first.append('21')
                last = graph1.a_star_algorithm('21', stop_node)
                return first + last
            elif (buildings[int(start_node) - 1]['Area'] == 2):
                graph1 = Graph()
                first = graph1.a_star_algorithm_time(start_node, '21')
                first.append('23')
                last = graph1.a_star_algorithm_time('23', stop_node)
                return first + last

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or g[v] + self.h(stop_node, v) < g[n] + self.h(stop_node, n):
                    # if n == None or g[v] + self.h(current, v) < g[n] + self.h(current, n):
                    n = v

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + \
                        (weight / buildings[int(m) - 1]["crowd"])

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + (weight / buildings[int(m) - 1]["crowd"]):
                        g[m] = g[n] + \
                            (weight / buildings[int(m) - 1]["crowd"])
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)
            current = n

        print('Path does not exist!')
        return None

    """ take into time as the most important factor using A* algorithm """

    def a_star_algorithm(self, start_node, stop_node):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])
        # current = start_node

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        # if start and end not in the same area, then choose to make it two
        if buildings[int(start_node) - 1]['Area'] != buildings[int(stop_node) - 1]['Area']:
            if (buildings[int(start_node) - 1]['Area'] == 1):
              first = self.a_star_algorithm(start_node, '23')
              first.append('21')
              last = self.a_star_algorithm('21', stop_node)
              return first + last
            elif (buildings[int(start_node) - 1]['Area'] == 2):
              first = self.a_star_algorithm(start_node, '21')
              first.append('23')
              last = self.a_star_algorithm('23', stop_node)
              return first + last

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or g[v] + self.h_time(stop_node, v) < g[n] + self.h_time(stop_node, n):
                    # if n == None or g[v] + self.h(current, v) < g[n] + self.h(current, n):
                    n = v

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)
            current = n

        print('Path does not exist!')
        return None

    def wrapper(self, list):
        res = {
            "step": 5,
            "perfer": 4,  # 1步行最短距离策略，2步行最短时间策略，
            #3混合交通方式的最短时间,4自选交通方式为自行车和步行，5自选交通工具为校车和步行
            # "1": {
            #     "desc": "沿着雁北路向南骑行700米，至第一个十字路口",
            #     #以左上角为左边系原点(0，0),x轴正方向向右,y轴正方向向下
            #     "cdntSx": 253,  # 起始横坐标
            #     "cdntSy": 639,  # 起起始纵坐标
            #     "cdntTx": 852,  # 结束横坐标
            #     "cdntSy": 677,  # 结束纵坐标
            #     "duration": 140,  # 以秒为单位
            #     "speed": 5,  # 单位m/s，实际速度=该设施拥挤度*该交通工具理想速度
            #     "bulidId": 11,  # 当前路径所位于的建筑物Id
            #     "by": 1,  # 0表示步行，1表示骑行，2表示校车
            # }
        }
        res["step"] = len(list) - 1
        res["perfer"] = 0

        for i in range(len(list) - 1):
            count = i + 1
            res[str(count)] = {}
            res[str(count)]["cdntSx"] = buildings[int(list[i]) - 1]["bx"]
            res[str(count)]["cdntSy"] = buildings[int(list[i]) - 1]["by"]
            res[str(count)]["cdntTx"] = buildings[int(list[count]) - 1]["bx"]
            res[str(count)]["cdntTy"] = buildings[int(list[count]) - 1]["by"]
            res[str(count)]["speed"] = 5
            res[str(count)]["duration"] = abs(buildings[int(list[count]) - 1]["by"] - buildings[int(list[i]) - 1]["by"]) + abs(
                buildings[int(list[count]) - 1]["bx"] - buildings[int(list[i]) - 1]["bx"]) * 1.0 / res[str(count)]["speed"]
            res[str(count)]["bulidId"] = list[count]
            res[str(count)]["by"] = 0
            res[str(count)]["desc"] = ""
            if (res[str(count)]["cdntTy"] - res[str(count)]["cdntSy"] > 0):
                res[str(count)]["desc"] += "head to south road with " + \
                    str(res[str(count)]["cdntTy"] - res[str(count)]["cdntSy"]) + "m" 
            else:
                res[str(count)]["desc"] += "head to north road with " + \
                    str(-res[str(count)]["cdntTy"] + res[str(count)]["cdntSy"]) + "m" 
            if (res[str(count)]["cdntTx"] - res[str(count)]["cdntSx"] > 0):
                res[str(count)]["desc"] += " and head to east with " + \
                str(res[str(count)]["cdntTx"] - res[str(count)]["cdntSx"]) + "m"
            else:
                res[str(count)]["desc"] += " and head to west with "  + \
                str(-res[str(count)]["cdntTx"] + res[str(count)]["cdntSx"]) + "m"

        return res


def plan(a,b,pr):
    a=str(a);b=str(b)
    graph1 = Graph()
    if pr ==1: route = graph1.a_star_algorithm(a,b)
    if pr ==2: route = graph1.a_star_algorithm_time(a,b)
    if pr ==3: route = graph1.a_star_algorithm_auto(a,b)
    return graph1.wrapper(route)

if __name__ == '__main__':
    plan("13","3",1)
