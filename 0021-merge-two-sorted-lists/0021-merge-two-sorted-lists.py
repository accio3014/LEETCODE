# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 문제의 리스트를 확인하면 2개의 리스트 내용이 이미 정렬되어 있음
        # 그렇기 때문에 두 리스트의 값을 비교하여 연결하면 됨
        
        if((not(list1)) and (not(list2))):  # 둘다 빈 리스트인 경우
            return None
        elif((not(list1)) or (not(list2))): # 둘 중 하나만 빈 리스트인 경우
            return list1 or list2           # 값이 있는 리스트를 리턴
        else:
            tail = head = ListNode()        # tail, head는 같은 주소를 가리킴
            
            while(list1 and list2):         # list1, list2의 값을 전부 반복함
                                            # 내부에서 list1, list2의 내용이 변경되기 때문에
                                            # 내부에 따로 증감식 등이 필요 없음
                if(list1.val < list2.val): 
                    tail.next = list1       # ListNode의 다음값으로 list1의 현재 값을 넣음
                    list1 = list1.next      # 다음 값으로 교체
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next
            
            tail.next = list1 or list2      # 만약 하나의 리스트의 내용을 전부 반복했을 때
                                            # 다른 리스트의 내용을 뒤에 붙임
            
        return head.next                    # ListNode의 시작 주소 값을 리턴
                    