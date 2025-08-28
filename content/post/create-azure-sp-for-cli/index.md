---
title: "创建用于命令行登录认证 Azure 的 Service Principal 必读"
date: 2023-11-14T11:03:55+08:00
description:  包括 Azure CLI 在内的 Azure 命令行工具，都可以使用 Service Principal 的方式，来完成 Azure 账号的登录认证。本文介绍如何创建一个用于在命令行登录认证 Azure 的 Service Principal。
slug: create-azure-sp-for-cli
image: pexels-miguel-2882566.webp
categories:
    - DevOps
tags:
    - azure
comments: true
toc: true

---

DevOps的工作流程中所需要到各种各样的命令行工具，在 Azure 的环境中，不同的 DevOps 工具在运行之前，都必须先完成 Azuore 账号的登录认证。而且，最好是在非用户干预和交互的方式下，完成登录认证。在这种情况下就可以使用 Service Principal 的方式，来完成 Azure 账号的登录认证。本文介绍如何创建一个用于在命令行登录认证 Azure 的 Service Principal。

## 创建 Service Principal

首先你需要安装或者准备好 Azure CLI，然后使用 Azure CLI 命令行工具，创建一个 Service Principal 的命令如下：

```bash
az ad sp create-for-rbac --name azure-sp-4-devops \
--role Contributor \
--scopes /subscriptions/${SUBSCRIPTION}/resourceGroups/${RESOURCE_GROUP}
```

参数说明：

- `--name`：Service Principal 的名称，这个名称可以随意指定，但是最好是有意义的名称，方便后续的管理。
- `--role`：Service Principal 的角色，这里指定为 `Contributor`，表示这个 Service Principal 在 Azure 中的权限是 `Contributor`。
- `--scopes`：Service Principal 的作用域，这里指定为 `/subscriptions/${SUBSCRIPTION}/resourceGroups/${RESOURCE_GROUP}`，表示这个 Service Principal 的作用域是 `${RESOURCE_GROUP}` 资源组。
  - `${SUBSCRIPTION}`：是一个环境变量，用于指定 Azure 订阅 ID。
  - `${RESOURCE_GROUP}`：是一个环境变量，用于指定 Azure 资源组名称。

在上面的命令中，应该注意的是 `--role` 需要是权限合理的值。应该保持最小可用权限的原则，不要使用 `Owner` 这样的权限。如果你不知道应该使用什么权限，可以先使用 `Contributor` 权限，然后在后续的使用中，逐步降低权限。

在我最近的测试中，由于我需要在多个教程项目间切换不同的资源组，而且资源组都是短期的，用完了就用删除的资源组，删除整个资源组是彻底清除已用资源的一个好方法。因此我在 `--scopes` 这个参数中，最经常使用的 SP 作用范围是 --scopes /subscriptions/${SUBSCRIPTION} ，这样就可以在任何一个资源组中使用这个 SP 了。假如你需要在多个不同订阅之间工作，可以灵活的使用 ${SUBSCRIPTION} 这个环境变量，来指定不同的订阅 ID。

以上命令行的输出结果类似如下：

```json
{
"appId": "3930xxxx-xxxx-xxxx-xxxx-xxxxd0e2xxxx",
"displayName": "azure-sp-4-devops",
"password": "eKxxxxxxxxxxxxxxxxxxxxxxxxxxxxX",
"tenant": "21d7xx-xxxxxx-xxxxxxx-xxxxxxx-xxxxxx55"
}
```

## 将 SP 的细节信息用于命令行变量

以上输出结果默认是 JSON 格式的，如果你需要将它直接用于命令行变量，可以使用 `--query` 参数，来指定输出的格式。例如，如果你需要将 `appId` 等的值，用于命令行变量，参考使用如下的命令：

```bash
SERVICE_PRINCIPAL_JSON=$(az ad sp create-for-rbac --name aks-getting-started-sp --role Contributor --scopes /subscriptions/${SUBSCRIPTION} -o json)
SERVICE_PRINCIPAL=$(echo $SERVICE_PRINCIPAL_JSON | jq -r '.appId')
SERVICE_PRINCIPAL_SECRET=$(echo $SERVICE_PRINCIPAL_JSON | jq -r '.password')
TENANT_ID=$(echo $SERVICE_PRINCIPAL_JSON | jq -r '.tenant')
```

以上命令中，使用了 `jq` 命令，来从 JSON 格式的输出中，提取出 `appId` 和 `password` 的值，并且分别用于命令行变量 `SERVICE_PRINCIPAL` 和 `SERVICE_PRINCIPAL_SECRET`。这样的好处是，避免了手工的复制和粘贴，也避免了数据在命令行的泄露。但是，如果是用于测试目的的 SP，也可以将这三个变量的值，直接复制保持到一个安全的地方，方便后续的反复使用。

## 登录 Azure

使用以上准备好的 Service Principal 登录 Azure 的命令如下：

```bash
az login \
--service-principal \
--tenant $TENANT_ID \
--username $SERVICE_PRINCIPAL \
--password $SERVICE_PRINCIPAL_SECRET \
--output table
```

在以上三个变量都正确的情况下，运行完以上命令后，会输出当前登录的 Azure 账号的相关信息，类似如下：

```bash
Environment    Name                 Tenant Id                             Subscription Id                        State    Is Default
-------------  -------------------  ------------------------------------  ------------------------------------  -------  -----------
AzureCloud     azure-sp-4-devops    21d7xx-xxxxxx-xxxxxxx-xxxxxxx-xxxxxx55  3930xxxx-xxxx-xxxx-xxxx-xxxxd0e2xxxx  Enabled  True
```

这样，就完成了 Azure 账号的登录认证。

## 查看当前登录的 Azure 账号

如果不确定，当前是否已经登录，或者不确定在什么 Azure 的账号下，可使用以下命令，可以查看当前登录的 Azure 账号：

```bash
az account show
```

## 参考

- [az ad sp create-for-rbac](https://docs.microsoft.com/en-us/cli/azure/ad/sp?view=azure-cli-latest#az-ad-sp-create-for-rbac)
- [az login](https://docs.microsoft.com/en-us/cli/azure/reference-index?view=azure-cli-latest#az-login)
- [az account show](https://docs.microsoft.com/en-us/cli/azure/reference-index?view=azure-cli-latest#az-account-show)


❤️ Feature Photo by Miguel Á. Padriñán: <https://www.pexels.com/photo/close-up-shot-of-keyboard-buttons-2882566/>
