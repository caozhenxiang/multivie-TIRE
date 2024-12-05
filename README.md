# Multiview TIRE model
Repository for developing the multiview extension for time-invariant representation autoencoder approach (TIRE) for change point detection (CPD) task. More information can be found in the paper **A Multiview Extension for Change Point Detection via Time-invariant representations**.


The authors of this paper are:

- [Zhenxiang Cao](https://www.esat.kuleuven.be/stadius/person.php?id=2380) ([STADIUS](https://www.esat.kuleuven.be/stadius/), Dept. Electrical Engineering, KU Leuven)
- [Nick Seeuws](https://www.esat.kuleuven.be/stadius/person.php?id=2318) ([STADIUS](https://www.esat.kuleuven.be/stadius/), Dept. Electrical Engineering, KU Leuven)
- [Maarten De Vos](https://www.esat.kuleuven.be/stadius/person.php?id=203) ([STADIUS](https://www.esat.kuleuven.be/stadius/), Dept. Electrical Engineering, KU Leuven and Dept. Development and Regeneration, KU Leuven)
- [Alexander Bertrand](https://www.esat.kuleuven.be/stadius/person.php?id=331) ([STADIUS](https://www.esat.kuleuven.be/stadius/), Dept. Electrical Engineering, KU Leuven)
All authors are affiliated to [LEUVEN.AI - KU Leuven institute for AI](https://ai.kuleuven.be).

## Abstract
*In the realm of change point detection in time series, distribution-free models have replaced traditional statistical tests and come to dominate the field. They offer superior detection performance and exhibit better generalization capabilities across a spectrum of simulated and real-life datasets. However, many existing approaches for change point detection either rely solely on information from time domain or frequency domain or balance contributions from different domains through intricate post-processing procedures. Both of these scenarios overlook important realities: 1) Different types of change points can occur simultaneously within one single recording. 2) Different types of change points often manifest themselves differently in different domains. In response to these challenges, we introduce a multiview model. This model possesses the ability to adaptively select change point-relevant information from both the time and frequency domains. When compared to existing baselines, the new model consistently achieves superior or, at the very least, comparable performance across a diverse set of benchmark datasets, including both simulated and real-life scenarios.*

## Requirements
This code requires:
**tensorflow**,
**tensorflow-addons**,
**numpy**,
**pandas**,
**scipy**,
**matplotlib**,
**seaborn**,
**scikit-learn**.

To install the required packages, run:

```
cd functions
pip install -e .
```

## Contact
In case of comments or questions, please contact me at <zhenxiang.cao@esat.kuleuven.be>. 


**PS. This repository has been included in the tire-cpd toolbox on Pypi.org. Please refer to the new repository [tire-cpd_toolbox_examples](https://github.com/caozhenxiang/tire-cpd_toolbox_examples) for more details.**
