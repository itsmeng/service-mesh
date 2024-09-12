# service-mesh

local testing using curl 
```
curl -X POST http://localhost:8080/mesh/function1 \
  -H "Content-Type: application/json" \
  -d '{"userId": "12345"}'
```