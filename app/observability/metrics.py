from collections import Counter
_metrics=Counter()
def increment(name,amount=1):_metrics[name]+=amount
def snapshot():return dict(_metrics)
def reset():_metrics.clear()
