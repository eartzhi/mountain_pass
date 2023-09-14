<!DOCTYPE html>
<html>
 <head>
   <title>Swagger</title>
   <meta
charset="utf-8"/>
   <meta name="viewport" content="width=device-width, initial-scale=1">
   <link rel="stylesheet" type="text/css" href="//unpkg.com/swagger-ui-dist@3/swagger-ui.css" />
 </head>
 <body>
   <div id="swagger-ui"></div>
   <script src="//unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js"></script>
   <script>
   const ui = SwaggerUIBundle({
       url: "/static/openapi-schema.yml",
       dom_id: '#swagger-ui',
       presets: [
         SwaggerUIBundle.presets.apis,
         SwaggerUIBundle.SwaggerUIStandalonePreset
       ],
       layout: "BaseLayout",
       requestInterceptor: (request) => {
         request.headers['X-CSRFToken'] = "Kgt8S9Bg8mqXdOv6Ke0l3irDFJY9Dt9Jbyx7cwbd015Oo9a5xSZiQplKS21k8qmL"
         return request;
       }
     })
   </script>
 </body>
</html>