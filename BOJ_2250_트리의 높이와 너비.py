import sys
sys.setrecursionlimit(100000) #재귀 깊이 제한을 100000까지 허용
n=int(sys.stdin.readline())

root=int(n*(n+1)/2) #노드 번호는 1부터 N까지 이므로 등차수열의 합 공식 사용
                    #-> 모든 노드의 합을 구한 뒤 자식들 값을 빼주면 노드 값이 됨
tree={}  #트리를 구현할 딕셔너리 

for i in range(n):
    parent,left,right=sys.stdin.readline().split()
    tree[parent]=[left,right,'','']   #[왼쪽 자식, 오른쪽 자식, 트리의 레벨, 열 번호]
    if left!='-1':
        root-=int(left)
    if right!='-1':
        root-=int(right)

tree[str(root)][2]=1    #루트 노드의 트리 레벨을 1로 설정

column=1  #열 번호
level=1  #트리의 레벨

#트리를 중위순회하여 각 노드의 레벨과 열 번호를 구함
def inorder(root):
    global column, level
    if tree[root][0]!='-1':
        level+=1
        inorder(tree[root][0])
    tree[root][2]=level
    tree[root][3]=column
    column+=1
    if tree[root][1]!='-1':
        level+=1
        inorder(tree[root][1])
    level-=1

inorder(str(root))

same_row_node_list=[[] for i in range(10001)]  #같은 레벨에 있는 노드들의 열 번호를 담은 리스트 여러개로 구성된 2차원 리스트
                                               #리스트 인덱스 = 레벨

for i in tree.values():
    same_row_node_list[i[2]].append(i[3])  #리스트에 열 번호를 추가

max_len=0  #최대 간격
max_level=0 #최대 간격을 가지는 레벨

#같은 레벨에 있는 노드들 중 열 번호가 최소인 것과 최대인 것을 구하여 간격을 구함
for i,v in enumerate(same_row_node_list):
    if len(v)>0:
        length=max(v)-min(v)+1
        if  length>max_len:
            max_len=length
            max_level=i

print(max_level,max_len)
