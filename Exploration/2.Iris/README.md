### File description

1. Iris.ipynb   
    iris_2.ipynb

    - This is study code for scikit-learn and machine learning
    
2.
    project_digits.ipynb   
    project_breast.ipynb   
    project_wine.ipynb

    - This is classification code for scikit-learn dataset using 5 models
        - decision tree
        - random forest
        - Support vector machine
        - Stochatic Gradient Descent
        - Logisitic regression

3. Conclusion
    - decision tree
        - pros
            - 어떠한 경우의 데이터셋 상태여도 나쁘지 않은 성능을 보임
        - cons
            - 데이터셋의 질과 양이 좋을 때는 가장 낮은 성능을 보임
    - random forest
        - pros
            - 어떠한 경우의 데이터셋 상태여도 좋은 성능을 보임
        - cons
            - 단, 데이터셋의 질과 양이 좋으면 SVM보다 성능은 소폭 낮음
    - Support vector machine
        - pros
            - 데이터셋이 크고 균형있을 때, 성능이 최고를 보여줌
            - 데이터셋이 불균형이어도 크기가 크면 준수한 성능 보임
        - cons
            - 단, 데이터셋 크기도 작으면 학습이 잘 되지 않음
    - Stochatic Gradient Descent
        - pros
            - 데이터셋이 크면 정확도는 올라감
        - cons
            - 데이터셋이 불균형이면, 학습이 잘 진행되지 않음
    - Logisitic regression
        - pros
            - 데이터셋이 불균형해도 좋은 성능을 보임
        - cons
            - 단, 데이터셋이 균형있고 크면, SVM이나 Random forest 보다 성능이 낮음
    - 종합
    
        |데이터셋 크기|데이터셋 균형여부|특성 수|
        |:---:|:---:|:---:|
        ||ajewiof|보통