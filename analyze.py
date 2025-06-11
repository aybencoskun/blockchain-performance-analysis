{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "d58915ab-7974-498f-b4be-c34469bc810b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "import os\n",
    "\n",
    "with open(\"d82cf01e-0fc7-4be1-9b1a-b9fecc94ff8d.json.json\", \"r\") as f:\n",
    "    data = json.load(f)\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "diff_bins = np.arange(-0.6, 0.7, 0.1)\n",
    "\n",
    "seconds_bins = np.arange(df['seconds'].min(), df['seconds'].max() + 1, 1)\n",
    "\n",
    "df['diff_bin'] = pd.cut(df['diff'], bins=diff_bins, include_lowest=True)\n",
    "df['seconds_bin'] = pd.cut(df['seconds'], bins=seconds_bins, include_lowest=True)\n",
    "\n",
    "pivot = (\n",
    "    df.groupby(['seconds_bin', 'diff_bin'], observed=True)['result']\n",
    "    .agg(['count', 'sum'])\n",
    "    .rename(columns={'count': 'total', 'sum': 'success'})\n",
    "    .reset_index()\n",
    ")\n",
    "pivot['success_rate'] = pivot['success'] / pivot['total']\n",
    "\n",
    "pivot['label'] = pivot['success_rate'].apply(lambda x: f\"{x:.0%}\") + \"\\n(\" + pivot['total'].astype(str) + \")\"\n",
    "\n",
    "heatmap_data = pivot.pivot(index='seconds_bin', columns='diff_bin', values='success_rate')\n",
    "heatmap_labels = pivot.pivot(index='seconds_bin', columns='diff_bin', values='label')\n",
    "\n",
    "os.makedirs(\"output\", exist_ok=True)\n",
    "\n",
    "plt.figure(figsize=(12, 6))\n",
    "sns.heatmap(heatmap_data, annot=heatmap_labels, fmt=\"\", cmap='YlGnBu', cbar_kws={'label': 'Success Rate'})\n",
    "plt.title('Success Rate (result == 1) by diff and seconds bins')\n",
    "plt.xlabel('diff bins')\n",
    "plt.ylabel('seconds bins')\n",
    "plt.xticks(rotation=45)\n",
    "plt.tight_layout()\n",
    "plt.savefig(\"output/heatmap_success_rate.png\")\n",
    "plt.close()\n",
    "\n",
    "plt.figure(figsize=(8, 4))\n",
    "sns.histplot(df['diff'], bins=30, kde=True)\n",
    "plt.title(\"Diff Değerlerinin Dağılımı\")\n",
    "plt.xlabel(\"diff\")\n",
    "plt.tight_layout()\n",
    "plt.savefig(\"output/diff_distribution.png\")\n",
    "plt.close()\n",
    "\n",
    "pivot.to_csv(\"output/summary_table.csv\", index=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "afa7fe31-d2d5-4856-ae51-d3bb93eec735",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['diff_distribution.png', 'heatmap_success_rate.png', 'summary_table.csv']"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "os.listdir(\"output\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "99c82129-7262-4c5d-9d18-9dcd92a6077f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
