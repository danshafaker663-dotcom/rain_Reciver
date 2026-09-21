"""接雨水算法模块。"""


def trap(height: list[int]) -> int:
    """计算柱子之间能够接住的雨水总量。

    参数:
        height: 非负整数列表，每个数字代表一根柱子的高度。

    返回:
        雨水总量，每根柱子的宽度为 1。

    示例:
        trap([3, 0, 2, 0, 4]) == 7
    """
    if any(type(value) is not int or value < 0 for value in height):
        raise ValueError("柱子高度必须是非负整数")

    left = 0
    right = len(height) - 1
    left_max = 0
    right_max = 0
    total = 0

    while left < right:
        if height[left] <= height[right]:
            left_max = max(left_max, height[left])
            total += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            total += right_max - height[right]
            right -= 1

    return total