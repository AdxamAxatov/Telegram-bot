def mergeTwo_sorts(list1, list2):
    new = []
    new.append(list1)
    new.append(list2)
    merged_list = sorted(new)
    return merged_list

list1 = [1, 2, 3, 4]
list2 = [1, 3, 5]

hi = mergeTwo_sorts(list1=[1, 2, 3, 4], list2=[1,3,5])
# print(hi)

def merge_and_sort(list1, list2):
    merged_list = list1 + list2  # Merge the two lists
    merged_list.sort(reverse=True)  # Sort the merged list in descending order
    return merged_list

# Example usage
list1 = [1, 2, 3, 4]
list2 = [1, 3, 5]
merged_sorted_list = merge_and_sort(list1, list2)
# print(merged_sorted_list)
hi = 'hi'



class Solution:
    def removeElement(self, nums: int, val: int) -> int:
        a = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[a] = nums[i]
                a += 1
        return a
    
# hi = Solution()
# print(hi.removeElement([3,2,2,3], 3))

class Solution:
    def removeDuplicates(self, nums: int) -> int:
        if not nums:
            return 0

        j = 0  
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j + 1  


# hi = Solution()
# print(hi.removeDuplicates([1,1,2]))

class Solution:
    def searchInsert(self, nums: int, target: int) -> int:
        # j = 0
        # for i in range(len(nums)):
        #     if nums[i] != target:
        #         j += 1
        #     else:
        #         return j
        
        length = len(nums)
        l = 0
        r = length - 1    
        while l <= r: 
            mid = (l+r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return mid + 1
            else:
                r = mid - 1

        return -1 
        

hi = Solution()
print(hi.searchInsert([1,3,5,6], 5))

































































