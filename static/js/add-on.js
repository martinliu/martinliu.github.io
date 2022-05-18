/*
  This js file is for individual users to modify the scripts for their personal site,
  or for the implementation of features specifically for their site. Anything that
  is an official part of the theme (ex. Pull Requests) should be included in main.js
  and follow the formatting and style given.
*/
<script src="/js/elastic-apm-rum.umd.min.js"></script>
<script>
  elasticApm.init({
    serviceName: 'Martin-Blog-Cloudflare',
    environment: 'production',
    serviceVersion: '1.6.4',
    breakdownMetrics: 'true',
    serverUrl: 'https://b1c7fb0e25894d4db3cabb678546c24f.apm.ap-east-1.aws.elastic-cloud.com:443',
  })
</script>