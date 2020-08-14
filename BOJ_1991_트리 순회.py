import sys

n=int(sys.stdin.readline()) #노드의 개수
tree={} #트리를 딕셔너리로 구현, 부모는 키:자식은 값
        #배열로 구현 시 2^노드 개수-1 만큼의 크기가 필요하므로 메모리 초과

#데이터 입력
for i in range(n):
    parent,left,right=sys.stdin.readline().split()
    tree[parent]=[left,right]

#전위순회
def preorder(n):  #부모->왼쪽 자식->오른쪽 자식
    print(n,end='')
    if tree[n][0]!='.': #왼쪽 자식이 비어있지 않다면 접근
        preorder(tree[n][0])
    if tree[n][1]!='.': #오른쪽 자식이 비어있지 않다면 접근
        preorder(tree[n][1])

#중위순회
def inorder(n):  #왼쪽자식->부모->오른쪽 자식
    if tree[n][0]!='.':  #왼쪽 자식이 비어있지 않다면 접근
        inorder(tree[n][0])
    print(n,end='')
    if tree[n][1]!='.':  #오른쪽 자식이 비어있지 않다면 접근  
        inorder(tree[n][1])

#후위순회
def postorder(n):  #왼쪽 자식->오른쪽 자식->부모
    if tree[n][0]!='.':
        postorder(tree[n][0])  #왼쪽 자식이 비어있지 않다면 접근
    if tree[n][1]!='.':    
        postorder(tree[n][1])  #오른쪽 자식이 비어있지 않다면 접근
    print(n,end='')

#항상 A가 루트 노드
preorder('A') 
print()
inorder('A')
print()
postorder('A')
