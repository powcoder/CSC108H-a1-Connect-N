https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
"""Python >= 3 tests for redefining an outer loop's variable."""

for i, *j in [(1, 2, 3, 4)]:
    for j in range(i): #[redefined-outer-name]
        print(j)
