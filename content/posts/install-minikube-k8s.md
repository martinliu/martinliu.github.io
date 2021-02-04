---
title: 用Minikube体验单节点K8S
subtitle: minikube上手指南
date: 2017-09-21
bigimg: [{src: "/images/abstract-1.jpg"}]
tags:
- DevOps
- Docker
---

<p>Minikube为各种操作系统的开发者，提供了运行K8S最简洁的方式。它最小化了安装k8s的需求和工作量。而且在各种操作系统上可以实现相同的体验。本文用精简的语言，描述了从安装minikube到运行容器化应用的过程。主要命令和输出来自macOS。</p>

![year-map](/images/minikube-logo.png)

<h2 id="hypervisor">安装Hypervisor</h2>
<p>需要在任何笔记本或者工作上安装一个Hypervisor，因此首先你需要坚持电脑的CPU是否开启了虚拟化的支持，检查BIOS的VT-X或者AMD-v的配置。</p>
<ul>
<li>OS X，安装  xhyve driver, <a href="https://www.virtualbox.org/wiki/Downloads">VirtualBox</a> 或 VMware Fusion</li>
<li>Linux， 安装 VirtualBox 或 KVM</li>
<li>Windows， 安装 VirtualBox or Hyper-V</li>
</ul>
<p>Minikube会生成一个虚拟机，用于运行一个安装和部署好的k8s单节点系统。</p>

<h2 id="kubectl">安装kubectl</h2>
<p>kubectl是k8s系统的管理工具，是一个命令行工具，它用于和master交互，完成群集和服务的管理等工作。</p>
<p>kubectl的安装文档： <a href="https://kubernetes.io/docs/tasks/tools/install-kubectl/">https://kubernetes.io/docs/tasks/tools/install-kubectl/</a></p>
<p>在macOS上最简单的安装方法是下面这条命令：</p>
<pre><code>brew install kubectl
</code></pre>
<p>brew的好处是后续可以帮忙持续的升级。</p>
<p>其它非brew安装方法，见以上安装文档的 <code>Install kubectl binary via curl</code> 部分。</p>

<h2 id="minikube">安装 minikube</h2>
<p>在macOS上使用的默认的Hypervisor是VirtualBox，如果想要用xhyve需要在启动的时候加上参数 <code>--vm-driver=xhyve</code></p>
<p>安装最新版本的 minikube 需要参考这个网页 <a href="https://github.com/kubernetes/minikube/releases">https://github.com/kubernetes/minikube/releases</a></p>
<p><code>minikube</code> 是一个命令行工具，它的命令行参数如下：</p>
<pre><code>Minikube is a CLI tool that provisions and manages single-node Kubernetes clusters optimized for development workflows.

Usage:
  minikube [command]

Available Commands:
  addons           Modify minikube's kubernetes addons
  completion       Outputs minikube shell completion for the given shell (bash)
  config           Modify minikube config
  dashboard        Opens/displays the kubernetes dashboard URL for your local cluster
  delete           Deletes a local kubernetes cluster
  docker-env       Sets up docker env variables; similar to '$(docker-machine env)'
  get-k8s-versions Gets the list of available kubernetes versions available for minikube
  ip               Retrieves the IP address of the running cluster
  logs             Gets the logs of the running localkube instance, used for debugging minikube, not user code
  mount            Mounts the specified directory into minikube
  profile          Profile sets the current minikube profile
  service          Gets the kubernetes URL(s) for the specified service in your local cluster
  ssh              Log into or run a command on a machine with SSH; similar to 'docker-machine ssh'
  ssh-key          Retrieve the ssh identity key path of the specified cluster
  start            Starts a local kubernetes cluster
  status           Gets the status of a local kubernetes cluster
  stop             Stops a running local kubernetes cluster
  update-context   Verify the IP address of the running cluster in kubeconfig.
  version          Print the version of minikube

Flags:
      --alsologtostderr                  log to standard error as well as files
  -b, --bootstrapper string              The name of the cluster bootstrapper that will set up the kubernetes cluster. (default "localkube")
  -h, --help                             help for minikube
      --log_backtrace_at traceLocation   when logging hits line file:N, emit a stack trace (default :0)
      --log_dir string                   If non-empty, write log files in this directory
      --loglevel int                     Log level (0 = DEBUG, 5 = FATAL) (default 1)
      --logtostderr                      log to standard error instead of files
  -p, --profile string                   The name of the minikube VM being used.
	This can be modified to allow for multiple minikube instances to be run independently (default "minikube")
      --stderrthreshold severity         logs at or above this threshold go to stderr (default 2)
  -v, --v Level                          log level for V logs
      --vmodule moduleSpec               comma-separated list of pattern=N settings for file-filtered logging

Use "minikube [command] --help" for more information about a command.
</code></pre>
<p>minikube 就是一个命令行工具，就是一个可执行文件。在macOS上也可以用brew安装，安装命令如下：</p>
<pre><code>brew cask install minikube
</code></pre>
<p>minikube 的快速参考文档在这里： <a href="https://github.com/kubernetes/minikube/blob/v0.22.2/README.md">https://github.com/kubernetes/minikube/blob/v0.22.2/README.md</a></p>

<h2 id="minikube">启动minikube</h2>
<p>虚拟化的Hypervisor和kubctl就绪了以后，就可以启动minikube了，命令如下：</p>
<pre><code>minikube start

Starting local Kubernetes v1.7.5 cluster...
Starting VM...
Getting VM IP address...
Moving files into cluster...
Setting up certs...
Connecting to cluster...
Setting up kubeconfig...
Starting cluster components...
Kubectl is now configured to use the cluster.
</code></pre>
<p>启动以后随时都可以用下面这个命令检查minikube的状态。</p>
<pre><code>minikube status
</code></pre>
<p>停止minikube服务，也就是关机那个start命令创建的虚拟机。</p>
<pre><code>minikube stop
</code></pre>
<h2 id="minikube">访问和使用minikube</h2>
<h3 id="minikubessh">minikube ssh</h3>
<p>登录到minikube的虚拟机里的命令就是ssh，进去之后，查看一下docker镜像。</p>
<pre><code>minikube ssh
                        ##         .
                  ## ## ##        ==
               ## ## ## ## ##    ===
           /"""""""""""""""""\___/ ===
      ~~~ {~~ ~~~~ ~~~ ~~~~ ~~~ ~ /  ===- ~~~
           \______ o           __/
             \    \         __/
              \____\_______/
 _                 _   ____     _            _
| |__   ___   ___ | |_|___ \ __| | ___   ___| | _____ _ __
| '_ \ / _ \ / _ \| __| __) / _` |/ _ \ / __| |/ / _ \ '__|
| |_) | (_) | (_) | |_ / __/ (_| | (_) | (__|   &lt;  __/ |
|_.__/ \___/ \___/ \__|_____\__,_|\___/ \___|_|\_\___|_|
Boot2Docker version 1.11.1, build master : 901340f - Fri Jul  1 22:52:19 UTC 2016
Docker version 1.11.1, build 5604cbe
docker@minikube:~$ docker images
REPOSITORY                                             TAG                 IMAGE ID            CREATED             SIZE
nginx                                                  latest              da5939581ac8        9 days ago          108.3 MB
gcr.io/google_containers/kubernetes-dashboard-amd64    v1.6.3              691a82db1ecd        8 weeks ago         139 MB
&lt;none&gt;                                                 &lt;none&gt;              2f7f7bce8929        11 weeks ago        107.5 MB
gcr.io/google_containers/k8s-dns-sidecar-amd64         1.14.4              38bac66034a6        12 weeks ago        41.82 MB
gcr.io/google_containers/k8s-dns-kube-dns-amd64        1.14.4              a8e00546bcf3        12 weeks ago        49.39 MB
gcr.io/google_containers/k8s-dns-dnsmasq-nanny-amd64   1.14.4              f7f45b9cb733        12 weeks ago        41.42 MB
gcr.io/google-containers/kube-addon-manager            v6.4-beta.2         0a951668696f        3 months ago        79.24 MB
gcr.io/google_containers/kubernetes-dashboard-amd64    v1.5.0              e5133bac8024        9 months ago        88.9 MB
gcr.io/google-containers/kube-addon-manager            v6.1                59e1315aa5ff        9 months ago        59.37 MB
gcr.io/google_containers/kubedns-amd64                 1.8                 597a45ef55ec        11 months ago       57.89 MB
gcr.io/google_containers/kube-dnsmasq-amd64            1.4                 3ec65756a89b        11 months ago       5.13 MB
gcr.io/google_containers/exechealthz-amd64             1.2                 93a43bfb39bf        12 months ago       8.375 MB
gcr.io/google_containers/echoserver                    1.4                 a90209bb39e3        16 months ago       140.4 MB
gcr.io/google_containers/pause-amd64                   3.0                 99e59f495ffa        16 months ago       746.9 kB
docker@minikube:~$ docker ps
</code></pre>
<p>以上的命令输出中，镜像的名称是以 <code>gcr.io/google_containers/</code> 就都是属于k8s的系统容器，k8s的系统服务就都是这些docker容器提供的服务。</p>
<p>用<code>docker ps</code>命令可以看到当前这个虚拟机正在运行的容器。</p>

<h3 id="kubectlrun">kubectl run</h3>
<p>kubectl run 命令是用来运行一个docker镜像的，还可以制定在k8s群集中运行几个某镜像的容器。可以创建一个部署或者作业，用它们来管理容器的创建。包括在一个部署或者作业中，运行某个docker镜像的，容器数量，环境变量参数，开放的端口，启动的参数等等。看下面的这个实例。</p>
<pre><code>$ kubectl run hello-minikube --image=gcr.io/google_containers/echoserver:1.4 --port=8080
deployment "hello-minikube" created
$ kubectl expose deployment hello-minikube --type=NodePort
service "hello-minikube" exposed

# We have now launched an echoserver pod but we have to wait until the pod is up before curling/accessing it
# via the exposed service.
# To check whether the pod is up and running we can use the following:
$ kubectl get pod
NAME                              READY     STATUS              RESTARTS   AGE
hello-minikube-3383150820-vctvh   1/1       ContainerCreating   0          3s
# We can see that the pod is still being created from the ContainerCreating status
$ kubectl get pod
NAME                              READY     STATUS    RESTARTS   AGE
hello-minikube-3383150820-vctvh   1/1       Running   0          13s
# We can see that the pod is now Running and we will now be able to curl it:
$ curl $(minikube service hello-minikube --url)
CLIENT VALUES:
client_address=172.17.0.2
command=GET
real path=/
query=nil
request_version=1.1
request_uri=http://192.168.99.100:8080/

SERVER VALUES:
server_version=nginx: 1.10.0 - lua: 10001

HEADERS RECEIVED:
accept=*/*
host=192.168.99.100:31721
user-agent=curl/7.54.0
BODY:
-no body in request-%
</code></pre>
<p>命令含义简介：</p>
<ul>
<li><code>kubectl expose</code> 在一个特定的端口上，把一个资源暴露为k8s的一个服务，这个资源可以是一个部署、副本集。可能的资源包括：pod (po), service (svc), replicationcontroller (rc), deployment (deploy), replicaset (rs)</li>
<li><code>kubectl get</code> 显示/查看一个或者多个资源的信息。</li>
<li><code>minikube service</code> 获取本地k8s群集里某个特定服务的服务地址URL</li>
</ul>

<h3 id="api">访问API服务器</h3>
<p>访问k8s的重要组件API服务器，访问的方法是：用kubectl先得到一个 Bearer Token 的访问令牌，用这个令牌访问API服务器的服务网址，下面的例子使用curl当api访问的客户端。</p>
<pre><code>$ TOKEN=$(kubectl describe secret $(kubectl get secrets | grep default | cut -f1 -d ' ') | grep -E '^token' | cut -f2 -d':' | tr -d '\t')

$ APISERVER=$(kubectl config view | grep https | cut -f 2- -d ":" | tr -d " ")

$  curl $APISERVER --header "Authorization: Bearer $TOKEN" --insecure
{
  "paths": [
    "/api",
    "/api/v1",
    "/apis",
    "/apis/",
    "/apis/admissionregistration.k8s.io",
    "/apis/admissionregistration.k8s.io/v1alpha1",
    "/apis/apiextensions.k8s.io",
    "/apis/apiextensions.k8s.io/v1beta1",
    "/apis/apiregistration.k8s.io",
    "/apis/apiregistration.k8s.io/v1beta1",
    "/apis/apps",
    "/apis/apps/v1beta1",
    "/apis/authentication.k8s.io",
    "/apis/authentication.k8s.io/v1",
    "/apis/authentication.k8s.io/v1beta1",
    "/apis/authorization.k8s.io",
    "/apis/authorization.k8s.io/v1",
    "/apis/authorization.k8s.io/v1beta1",
    "/apis/autoscaling",
    "/apis/autoscaling/v1",
    "/apis/autoscaling/v2alpha1",
    "/apis/batch",
    "/apis/batch/v1",
    "/apis/batch/v2alpha1",
    "/apis/certificates.k8s.io",
    "/apis/certificates.k8s.io/v1beta1",
    "/apis/extensions",
    "/apis/extensions/v1beta1",
    "/apis/networking.k8s.io",
    "/apis/networking.k8s.io/v1",
    "/apis/policy",
    "/apis/policy/v1beta1",
    "/apis/rbac.authorization.k8s.io",
    "/apis/rbac.authorization.k8s.io/v1alpha1",
    "/apis/rbac.authorization.k8s.io/v1beta1",
    "/apis/settings.k8s.io",
    "/apis/settings.k8s.io/v1alpha1",
    "/apis/storage.k8s.io",
    "/apis/storage.k8s.io/v1",
    "/apis/storage.k8s.io/v1beta1",
    "/healthz",
    "/healthz/autoregister-completion",
    "/healthz/ping",
    "/healthz/poststarthook/apiservice-registration-controller",
    "/healthz/poststarthook/apiservice-status-available-controller",
    "/healthz/poststarthook/bootstrap-controller",
    "/healthz/poststarthook/ca-registration",
    "/healthz/poststarthook/extensions/third-party-resources",
    "/healthz/poststarthook/generic-apiserver-start-informers",
    "/healthz/poststarthook/kube-apiserver-autoregistration",
    "/healthz/poststarthook/start-apiextensions-controllers",
    "/healthz/poststarthook/start-apiextensions-informers",
    "/healthz/poststarthook/start-kube-aggregator-informers",
    "/healthz/poststarthook/start-kube-apiserver-informers",
    "/logs",
    "/metrics",
    "/swagger-2.0.0.json",
    "/swagger-2.0.0.pb-v1",
    "/swagger-2.0.0.pb-v1.gz",
    "/swagger.json",
    "/swaggerapi",
    "/ui",
    "/ui/",
    "/version"
  ]
}%


</code></pre>
<h3 id="webuidashboard">访问Web UI (Dashboard)</h3>
<p>Dashboad是k8s的一个图形界面，可以用它部署容器化的应用，排错和管理k8s群集。在minikube上启动这个界面的命令是 <code>minikube dashboard</code> ，你系统的默认浏览器会自动弹出如下界面。</p>


![year-map](/images/Overview---Kubernetes-Dashboard.jpg)
<p>关于Dashbaord的文档在： <a href="https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/">https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/</a></p>

<h2 id="minikube">用minikube运行应用</h2>
<p>minikube正常运行起来以后，就可以参考文档 <a href="https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/">https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/</a> 在这个k8s系统上运行一些demo的应用，对应用做启停、扩缩容等体验。</p>

