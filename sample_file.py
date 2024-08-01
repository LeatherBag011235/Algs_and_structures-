def summaryRanges(nums):
    if not nums:
        return []
    elif len(nums) == 1:
        return [f"{nums[0]}"]
    else:

        ints = []

        int_start = nums[0]
        prev_num = nums[0]

        for x in nums[1:]:

            if x - 1 != prev_num:

                int_end = prev_num

                if int_start == int_end:
                    ints.append(f"{int_start}")
                else:
                    ints.append(f"{int_start}->{int_end}")

                int_start = x

            prev_num = x

        if int_start == x:
            ints.append(f"{int_start}")
        else:
            ints.append(f"{int_start}->{x}")

        return ints
