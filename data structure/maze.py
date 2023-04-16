from collections import deque
maze=[
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0 ,1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1 ,1 ,0 ,1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dir = [
        lambda x, y: (x + 1, y),
        lambda x, y: (x, y + 1),
        lambda x, y: (x - 1, y),
        lambda x, y: (x, y - 1)
]

def maze_path_byStack(x1,y1,x2,y2):         #DFS
    stack=[]
    stack.append((x1,y1))
    while len(stack)>0:
        cur=stack[-1]   #当前节点为栈顶元素
        if cur[0]==x2 and cur[1]==y2:  #[0][1]为元组的下标
            for p in stack:
                print(p)
            return True
        for d in dir:
            new=d(cur[0],cur[1])    #下个节点
            if maze[new[0]][new[1]]==0:
                stack.append(new)
                maze[new[0]][new[1]]=2
                break
        else:
            maze[new[0]][new[1]]=2
            stack.pop()
    print("No Way")
    return False

def print_road(path):
    cur=path[-1]
    res=[]
    while cur[2]!=-1:
        res.append(cur[0:2])
        cur=path[cur[2]]

    res.append(cur[0:2])
    res.reverse()
    for road in res:
        print(road)



def maze_path_byQueue(x1,y1,x2,y2):         #BFS
    queue=deque()
    queue.append((x1,y1,-1))   #同时放入多位平行的数要用元组
    path=[]             #path也为三维数组 存当前x,y坐标，和父坐标的下标
    while len(queue)>0:
        cur=queue.popleft()
        path.append(cur)
        if cur[0]==x2 and cur[1]==y2:       #此时cur为终点，也为search_index的最后一个元素
            print_road(path)
            return True
        for d in dir:
           new=d(cur[0],cur[1])
           if maze[new[0]][new[1]]==0:
               queue.append((new[0],new[1],len(path)-1))     #元组
               maze[new[0]][new[1]]=2   #已走过 不用break
    else:
        print("No Way")
        return False






maze_path_byQueue(1,1,8,8)