class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 문제의 경우 nums 리스트의 길이 또는 새로운 리스트로 풀면 안되기 때문에
        # 기존 리스트 내부에서 다시 정렬을 진행
        output = 0                          # 내부에 정렬할 인덱스 번호이자 정렬된 개수

        for i in range(len(nums)) :         # 값 전체를 비교
            if(nums[i] != nums[output]) :   # 최소값 찾기
                output += 1                 # 다음 번째 위치에서
                nums[output] = nums[i]      # 최소값을 저장
                
        return output + 1