### List resources
QUERY="select * {?s ?p ?o}"
curl \
  --request POST \
  --data "query=$QUERY" \
  http://localhost:3030/ds/query

### Add resources
UPDATE_QUERY=$(cat <<EOF
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    INSERT DATA
    { 
    <http://example/book1> dc:title "A new book" ;
                            dc:creator "A.N.Other" .
    }
EOF
)

curl \
  --request POST \
  --data "update=$UPDATE_QUERY" \
  http://localhost:3030/ds/update









<!-- DATASET=example2
curl \
  --request POST \
  --data 'query=select * {?s ?p ?o}' \
  http://localhost:3030/ds/query
s-put http://localhost:3030/ds/data $DATASET jena-fuseki-docker-4.1.0 example2.ttl -->


