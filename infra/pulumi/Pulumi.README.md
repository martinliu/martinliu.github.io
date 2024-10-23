# Pulumi Cloud README

​
[Sign in to Azure to view stack resources!](https://portal.azure.com)
​
[Take me to the project home page!](${outputs.staticEndpoint})

## On Call Operations

* **Primary**: Tom
* **Secondary**: Martin
​

## Monitoring

1. [Azure Monitor Metrics](https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2#dashboards:name=${outputs.dashboardName}): Monitor holistic metrics tracking overall service health
2. [RDS Performance Metrics](https://us-west-2.console.aws.amazon.com/rds/home?region=us-west-2#performance-insights-v20206:/resourceId/${database.databaseCluster.id}/resourceName/${outputs.rdsClusterWriterInstance}): Monitor RDS performance (wait times, top queries)
3. [Azure Monitor Logs](https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2#logStream:group=${outputs.cloudwatchLogGroup}): Search across service logs
