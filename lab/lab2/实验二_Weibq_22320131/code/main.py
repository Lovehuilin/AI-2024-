from __Resolution import ResolutionFOL
import time

def main():
    print("首先，请输入子句数量：")
    num_of_clause = input()
    print(f"请输入",num_of_clause, "条子句：")
    start = time.time()
    ResolutionFOL(num_of_clause)
    end = time.time()
    print('\nRunning time %.6f sec' % (end - start))
if __name__ == "__main__":
    main()