from matplotlib import pyplot as plt
from matplotlib_venn import venn2, venn3

venn3(subsets=(10, 15, 12, 5, 8, 3, 2), set_labels=('A', 'B', 'C'))
plt.title("Three-set Venn diagram")
plt.show()