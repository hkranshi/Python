list=[
    ["What is k8s?","similar like docker","images registry","container orchestration framework","none of the above","c"],
    ["What is the default port for the Kubernetes API server?","6443","8080","80","443","a"],
    ["Which of the following is a Kubernetes object?","Pod","Service","Deployment","All of the above","d"],
    ["What is the purpose of a Kubernetes Service?","To expose an application running on a set of Pods","To manage the lifecycle of Pods","To store configuration data","To monitor the health of Pods","a"],
    ["What is a Kubernetes Namespace?","A way to organize resources within a cluster","A way to isolate resources between clusters","A way to manage network policies","A way to scale applications","a"],
    ["What is the purpose of a Kubernetes ConfigMap?","To store configuration data for applications","To manage secrets","To define network policies","To monitor resource usage","a"]
]
prizes=[
    100, 200, 300, 500, 1000, 2000]
i=0
for q in list:
    print(f"Question {i+1}: {q[0]}")
    print("Options:")
    for j in range(1, 5):
        print(f"{j}. {q[j]}")
    
    answer = input("Enter your answer (a/b/c/d): ").strip().lower()
    
    if answer == q[5]:
        print(f"Correct! You've won ${prizes[i]}!\n")
    else:
        print(f"Wrong answer! The correct answer was {q[5]}. \n")
        print("Better luck next time!")
        break
    
    i += 1
