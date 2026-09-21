"""接雨水程序入口。"""

from rain_water import trap


def parse_heights(text: str) -> list[int]:
    """将用户输入转换为高度列表。"""
    normalized = text.replace(",", " ").replace("，", " ")
    return [int(value) for value in normalized.split()]


def main() -> None:
    print("=== 接雨水计算器 ===")
    print("请输入柱子高度，用空格或逗号分隔。")
    print("例如：3 0 2 0 4")
    print("直接回车使用示例数据。")

    text = input("柱子高度：").strip()

    try:
        heights = parse_heights(text) if text else [3, 0, 2, 0, 4]
        water = trap(heights)
    except ValueError as error:
        print(f"输入错误：{error}")
        print("请输入非负整数，例如：3 0 2 0 4")
        return

    print(f"\n柱子高度：{heights}")
    print(f"可接雨水：{water} 单位")


if __name__ == "__main__":
    main()