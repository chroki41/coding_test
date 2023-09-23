def solution(cacheSize, cities):
    cache_dict = {}
    answer = 0
    queue = []
    if cacheSize == 0:
        return 5*len(cities)
    
    for item in cities:
        item = item.lower()
        remove_list = []
        print(item)
        if item in list(cache_dict.keys()):
            answer += 1
            cache_dict[item] = cache_dict[item] + 1
            queue.remove(item)
            queue = [item] + queue
            # queue.append(item)
            # print("case1", cache_dict, queue)
        else:
            answer += 5
            if len(cache_dict) < cacheSize:
                cache_dict[item] = 1
                queue = [item] + queue
                # queue.append(item)
                # print("case2", cache_dict, queue)
            elif len(cache_dict) == cacheSize:
                minimum = min(list(cache_dict.values()))
                for element in list(cache_dict.keys()):
                    if cache_dict[element] == minimum:
                        remove_list.append(element)
                if len(remove_list) == 1:
                    queue.remove(element)
                    queue = [item] + queue
                    # queue.append(item)
                    del cache_dict[element]
                    cache_dict[item] = 1
                    # answer += 5
                    # print("case3", cache_dict, queue)
                else:
                    for i in range(len(queue)):
                        if queue[i] in remove_list:
                            item_to_remove = queue[i]
                    queue.remove(item_to_remove)
                    queue = [item] + queue
                    # queue.append(item)
                    del cache_dict[item_to_remove]
                    cache_dict[item] = 1
                    # answer += 5 
                    # print("case4", cache_dict, queue)
                
    return answer
